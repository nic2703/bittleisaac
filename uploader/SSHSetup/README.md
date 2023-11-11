## ardSerial.py
These files are forked from the OpenCat repository. 
ardSerial.py allows you to send commands to bittle remotely. SerialCommunication.py is a dependency.


## SSH Setup

On your Rasperry Pi (with Raspbian installed), make sure to permit SSH connections: 

1. Run *raspi-config* with *sudo*: ```sudo raspi-config```
2. Find Interfacing Options -> SSH
3. Enable SSH
4. Find Interfacing Options -> Serial
5. At *Would you like a login shell to be accessible over serial?* select 'No'
6. At *Would you like the serial port hardware to be enabled?* slect 'Yes'
7. Exit raspi-config and reboot

**Connecting to the Raspberry Pi in headless mode**

This allows you access to the Terminal of the Raspberry Pi using your home PC. 

1. Make sure the Raspberry Pi is connected to the same WiFi network as the home PC
2. On the home PC, enter in Powershell: ```ssh [username]@[ip-address]```. The *username* is the name of your account on the Raspberry Pi. You can find the *ip-address* of the Raspberry by running 'hostname -I' in the <u> Raspberry Pi Terminal </u>. It should be of form xxx.xxx.xxx.xx.
3. You will be prompted to enter your password for the Raspberry Pi. Sometimes you have to wait 15 seconds for the Raspberry Pi to fully boot up.

If this does not work, try turning off the bluetooth capabilities of the Raspberry Pi. 

**Transmitting files home PC -> Raspberry Pi**

How to send a Python file to the Raspberry Pi using Secure Copy Protocol (SCP).

1. Once the above steps have been completed, open a new Powershell terminal on the home PC. 
2. Navigate to the directory of the file you want to transmit. 
3. Use the command ```scp [filename] [username]@[ip-address]:[raspi-path]``` to copy the file. [raspi-path] specifies the destination location relative to the *home* directory. 
4. You will be prompted to enter your password for the Raspberry Pi. 
5. The file should be transmitted. You can check using the SSH Terminal you created earlier. 


**Running Python files on Raspberry Pi**

Before running Python files, check if Python is installed (````python --version``) and disconnect the 6-pin USB adapter from Bittle.

1. Return to the Raspberry Pi terminal you have created. 
2. Navigate to the location of your Python file. 
3. Run ```dos2unix [filename]```. If dos2unix is not installed, run ```sudo apt install dos2unix```. 
4. Run ```chmod +x [filename]``` to make the file executable. 
5. Run ```./[filename]``` and watch Bittle go!


## Future

UPDATE: This is being implemented in sbituploader.py and runscript.py

I intend to make most of this procedure run automatically if possible. Ideally, I would have three scripts: 

*uploader.py*: Automatically uploads the next two files to the Raspberry Pi using SCP, without me having to enter any passwords, and autoruns runscript.py with arg *instruction.py*. 

*runscript.py*: File on the Raspberry Pi that will runs automatically after upload and
- Finds instruction.py in the folder or subfolder
- Checks if there are duplicates
- Prints the time that *instruction.py* was last modified (uploaded)
- Completes the dos2unix and chmod command on *instruction.py*
- Runs the file
- Checks for keyboard interrupts during *instruction.py* execution.
- Ends execution and outputs error messages in case the Raspberry Pi shuts down (Battery empty)

*instruction.py*: Python file that contains the servo instructions for Bittle. Ideally complemented by a separate library of various Bittle instructions. This may or may not include a terminal logger for external inputs (ROS?).

