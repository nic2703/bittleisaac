import os
import time
import subprocess
import argparse

def runscript(pi_path, filename, debug=0):
    """
    File that runs on the Raspberry Pi automatically and monitors current program execution. Called automatically by upload_run.

    Args:
        pi_path: Path on Raspberry Pi to the working directory
        filename: Name of the file to be executed
        debug: Set to 1 to output debug messages in the terminal
    """

    try: 
        print(debug)
        debug == 1 and print("RUNSCRIPT: STARTED")
        # Navigate to the working directory
        os.chdir(pi_path)
        debug == 1 and print("RUNSCRIPT: Opening " + filename + " in folder " + pi_path)

        # Perform dos2unix for conversion. 
        # check_dos2unix_installed(debug)
        dos2unix_command = ["dos2unix", filename]
        subprocess.run(dos2unix_command)
        # Make the file an executable
        chmod_command = ["chmod", "+x", filename]
        subprocess.run(chmod_command)

        # Run filename
        process = subprocess.Popen(['./' + filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        debug == 1 and print("RUNSCRIPT: Subprocess opened")

        stdout, stderr = process.communicate()
        debug == 1 and print("RUNSCRIPT | STANDARD OUTPUT:")
        debug == 1 and print("\t INSTRUCTION START\n")
        debug == 1 and print(stdout.decode())
        debug == 1 and print(stderr.decode())
        debug == 1 and print("\t \n INSTRUCTION END")
        # Wait for the process to complete and capture the exit status
        process.wait()
        exit_status = process.returncode

        if exit_status == 0:
            debug == 1 and print("RUNSCRIPT: Execution completed successfully, returning to UPLOADER")
        else:
            print(f"RUNSCRIPT: Execution failed with exit status {exit_status}, returning to UPLOADER")

    except Exception as e:
        print(f"RUNSCRIPT: An error occured: {str(e)}")


def check_dos2unix_installed(debug=0):
    """
    Function that checks whether dos2unix is installed on the Raspberry Pi. If not, it installs it.

    Args:
        debug: Set to 1 to output debug messages in the terminal
    """
    try: 
        subprocess.run(['dos2unix', '--version'], check=True)

    except subprocess.CalledProcessError:
        print("RUNSCRIPT: dos2unix is not installed. Installing...")

        try: 
            # Install dos2unix
            update_process = subprocess.Popen(['sudo', 'apt-get', 'update'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            update_process.communicate()
            if update_process.returncode != 0:
                raise subprocess.CalledProcessError(update_process.returncode, update_process.args)

            install_process = subprocess.Popen(['sudo', 'apt-get', 'install', '-y', 'dos2unix'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            install_process.communicate()
            if install_process.returncode != 0:
                raise subprocess.CalledProcessError(install_process.returncode, install_process.args)

            print("dos2unix installed successfully.")

        except subprocess.CalledProcessError as install_error:
            print(f"Error installing dos2unix: {install_error}")
            raise  # Re-raise the exception if installation fails

        finally:
            # Close subprocesses to avoid resource leaks
            if update_process:
                update_process.stdout.close()
                update_process.stderr.close()

            if install_process:
                install_process.stdout.close()
                install_process.stderr.close()

    else: 
        debug == 1 and print("dos2unix is already installed")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a Python script with cancellation support.")
    parser.add_argument("--pi_path", help="Path to the Python script to execute.")
    parser.add_argument("--filename", help="Name of the user Python file.")
    parser.add_argument("--debug", help="Debugging mode toggle")

    args = parser.parse_args()
    print("    PI_PATH: " + args.pi_path)
    print("    FILENAME: " + args.filename)
    print("    DEBUG MODE: " + args.debug)
    runscript(args.pi_path, args.filename, args.debug)