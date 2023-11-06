import paramiko
import os

# Uploads and executes Python files on the Raspberry Pi. Will always upload and execute 'runscript.py'. 

def sbitupload(pi_host, pi_port, pi_username, pi_password, pi_path, filename=None):
    try:
        print("UPLOADER: STARTED")
        local_files = ['runscript.py']
        if filename is not None:
            local_files.append(filename)
        
        # Start SSH Client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(pi_host, port=pi_port, username=pi_username, password=pi_password)

        # Secure Copy Protocol File Transfer
        sftp = ssh_client.open_sftp()
        print("UPLOADER: SSH Client accessed")

        # Enable permissions in the remote path
        sftp.chmod(pi_path, 0o777)
        for file in local_files:
            local_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
            remote_path = os.path.join(pi_path, file)
            print("UPLOADER: Copying " + local_path + " to " + remote_path)
            sftp.put(local_path, remote_path)
        sftp.close()

        print("UPLOADER: Files uploaded")

        # Run the script on the Raspberry Pi automatically
        command = f'python {pi_path}runscript.py'
        command += f' --pi_path {pi_path} --filename {filename}'

        stdin, stdout, stderr = ssh_client.exec_command(command)
        print("UPLOADER: Executing runscript.py")
 
        # Print the captured output and error
        print("UPLOADER | Passing arguments to runscript.py:")
        print(stdout.read().decode())
        print(stderr.read().decode())

        # Verify whether the script executed correctly on the Raspberry Pi
        exit_status = stdout.channel.recv_exit_status()
        if exit_status == 0:
            print("UPLOADER: Script executed successfully")
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
