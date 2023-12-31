## upload_run.py

First, it is useful to test whether SSH connection to the Raspberry Pi works. To do this, please follow the instructions in uploader/SSHSetup/README.md

The first of three basic utility functions. This one is used on the home PC. *upload_run.py* contains all the code needed to: 
- Establish an SSH connection with the Raspberry Pi
- Send runscript.py and any other files to the Raspberry Pi
- Automatically execute runscript.py on the Raspberry Pi
- Display the output of runscript.py on the home PC

# How to use: 

First, make sure that paramiko is installed by running ```pip install paramiko``` on the home PC.

```python
from upload_run import * 

pi_host = '192.168.1.111'
pi_port = 22
pi_username = 'username'
pi_password = 'password'
pi_path = 'path/folder/'

pi_list = [pi_host, pi_port, pi_username, pi_password, pi_path]
file_list = ['dance.py', 'ardSerial.py', 'SerialCommunication.py']
debug = 1 #optional debugging mode

upload_run(pi_list, file_list, debug)
# filename is usually instructions.py. runscript.py is always automatically uploaded. 
```

The upload_run function will grant write permissions to the folder path you have specified and then revert them after the program is complete. 
See /examples for a short code examples. 