# This is a testing runscript.py file.
import os
import time
import subprocess
import argparse

def runscript(pi_path, filename=None):
    try: 
        if filename is None:
            print("RUNSCRIPT: No file specified!")
        print("RUNSCRIPT: STARTED")
        instruction_path = os.path.join(pi_path, filename)
        process = subprocess.Popen(['python', instruction_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("RUNSCRIPT: Subprocess opened")

        # Check cancel signal every 0.5 seconds
        while process.poll() is None:
            time.sleep(0.5)

        # Check if a 'cancel.txt' file exists
        cancel_file_path = os.path.join(os.path.dirname(pi_path), 'cancel.txt')
        if os.path.exists(cancel_file_path):
            print("Cancellation signal detected. Cleaning up and exiting...")
            os.remove(cancel_file_path)  # Remove the cancellation file
            process.terminate()  # Terminate the execution of the Python script
            print("Execution canceled.")
            return 1

        stdout, stderr = process.communicate()
        print("RUNSCRIPT | STANDARD OUTPUT:")
        print("\t INSTRUCTION START\n")
        print(stdout.decode())
        print(stderr.decode())
        print("\t \n INSTRUCTION END")
        # Wait for the process to complete and capture the exit status
        process.wait()
        exit_status = process.returncode

        if exit_status == 0:
            print("RUNSCRIPT: Execution completed successfully, returning to UPLOADER")
        else:
            print(f"RUNSCRIPT: Execution failed with exit status {exit_status}, returning to UPLOADER")

    except Exception as e:
        print(f"RUNSCRIPT: An error occured: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a Python script with cancellation support.")
    parser.add_argument("--pi_path", help="Path to the Python script to execute.")
    parser.add_argument("--filename", help="Name of the user Python file.")

    args = parser.parse_args()
    print("    PI_PATH: " + args.pi_path)
    print("    FILENAME: " + args.filename)
    runscript(args.pi_path, args.filename)