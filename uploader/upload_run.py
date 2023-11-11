import paramiko
import os

def upload_run(pi_list, file_list, debug=0):
    """
    Uploads file(s) to the Raspberry Pi via SCP and executes the first passed file in filename_list automatically. 

    Args:
        pi_list: A list containing connection information to the Raspberry Pi. Should be of form [pi_host, pi_port, pi_username, pi_password, pi_path]
        file_lsit: File(s) that should be uploaded, found in the same folder. The first file is the file that is to be executed on the Raspberry Pi
        debug: Set to 1 to output debug messages in the terminal

    Raises: 
        TypeError: If the input is not in list format
        ValueError: If any element in the list is not a string

    Example: 
        pi_host = '192.168.1.111'
        pi_port = 22
        pi_username = 'username'
        pi_password = 'password'
        pi_path = 'Documents/autorun/'

        pi_list = [pi_host, pi_port, pi_username, pi_password, pi_path]
        filename_list = ['dance.py', 'ardSerial.py', 'SerialCommunication.py']
        upload_run(pi_list, filename_list)
    """

    # Check if input arguments are valid
    check_pi_list(pi_list)
    check_file_list(file_list)
    [pi_host, pi_port, pi_username, pi_password, pi_path] = pi_list
    debug == 1 and print("UPLOADER: All input arguments valid")

    # Make a local_files list including runscript.py
    local_files = ['runscript.py']
    if isinstance(file_list, str):
        file_list = [file_list]
    local_files = local_files + file_list

    try: 
        # Start SSH Client
        with paramiko.SSHClient() as ssh_client:
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(pi_host, port=pi_port, username=pi_username, password=pi_password)

            with ssh_client.open_sftp() as sftp:
                debug == 1 and print("UPLOADER: SSH Client accessed")

                # Enable permissions in the remote path
                sftp.chmod(pi_path, 0o777)

                # Upload files to the remote path
                for file in local_files:
                    local_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
                    remote_path = os.path.join(pi_path, file)
                    debug == 1 and print("UPLOADER: Copying " + local_path + " to " + remote_path)
                    sftp.put(local_path, remote_path)

                debug == 1 and print("UPLOADER: Files uploaded")

            # Execute runscript.py on the Raspberry Pi automatically, with input argument the name of the first file in file_list
            command = f'python -u {pi_path}runscript.py'
            command += f' --pi_path {pi_path} --filename {file_list[0]} --debug {debug}'

            stdin, stdout, stderr = ssh_client.exec_command(command)
            debug == 1 and print("UPLOADER: Executing runscript.py")

            # Print the captured output and error
            debug == 1 and print("UPLOADER | Passing arguments to runscript.py:")
            print(stdout.read().decode())
            print(stderr.read().decode())

            # Verify whether the script executed correctly on the Raspberry Pi
            exit_status = stdout.channel.recv_exit_status()
            if exit_status == 0:
                debug == 1 and print("UPLOADER: Script executed successfully")
            else:
                print(f"UPLOADER: Script execution failed with exit status {exit_status}")

            # Print the output of the command
            print(stdout.read().decode())

    except Exception as e:
        print(f"UPLOADER: An error occured: {str(e)}")

    finally:
        # Cleanup
        try:
            sftp.chmod(pi_path, 0o755)  # Set directory permissions back to 755
        except:
            pass  # Handle any exceptions that may occur during cleanup
        try:
            sftp.close()
        except:
            pass
        try:
            ssh_client.close()
        except:
            pass 
    

def check_pi_list(pi_list):
    """
    Check if all elements of pi_list are correct
    
    Args:
        pi_list: A list containing [pi_host, pi_port, pi_username, pi_password, pi_path]

    Raises: 
        TypeError: If the input is not in list format
        ValueError: If any element in the list is not a string    
    """
    # Check if pi_list is a list
    if not isinstance(pi_list, list):
        raise TypeError("pi_list must be a list")
    if len(pi_list) != 5:
        raise ValueError("pi_list must contain 5 elements. Please check function description")
    if not isinstance(pi_list[0], str):
        raise TypeError("pi_host must be a string. Example: '192.168.1.111'")
    if not (isinstance(pi_list[1], int) and pi_list[1]>0):
        raise TypeError("pi_port must be an integer. Example: 22")
    if not isinstance(pi_list[2], str):
        raise TypeError("pi_username must be a string. Example: 'username'")
    if not isinstance(pi_list[3], str):
        raise TypeError("pi_password must be a string. Example: 'password'")
    if not isinstance(pi_list[4], str):
        raise TypeError("pi_path must be a string. Example: 'Documents/autorun/'")

def check_file_list(file_list):
    """
    Check if all files in file_list are correct and in the same folder
    
    Args:
        file_list: A string or a list of strings with filenames

    Raises: 
        TypeError: If file_list is neither a string nor a list of strings    
        FileNotFoundError: If any file in file_list cannot be found in the current folder
    """
    # If the filename is a string (single), make it into a list
    if not isinstance(file_list, (str, list)):
        raise TypeError("file_list must be either a string or a list of strings")
    if isinstance(file_list, str):
        file_list = [file_list]
    if not all(isinstance(file, str) for file in file_list):
        raise TypeError("file_list must contain only strings")

    current_directory = os.path.dirname(os.path.abspath(__file__))

    for file in file_list:
        file_path = os.path.join(current_directory, file)
        if not os.path.exists(file_path):
            raise FileNotFoundError(file + " was not found in " + current_directory)