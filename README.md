# bitrobotics
(WIP) Library for various Bittle, Python and ROS integrations. My intention is to build a library of functions to easily upload to and control Petoi Bittle using a Raspberry Pi 3A+. This probably is going to expand to ROS/Isaac Sim integration. 

# What currently works
/uploader contains prototype upload_run.py and runscript.py which both work. Please refer to SerialConnection/README.md on how to properly set up the Raspberry Pi.
upload_run.py defines a function which makes it easy to upload and execute scripts to the Raspberry Pi from the PC. 
runscript.py is a helper function which is triggered by upload_run.py and runs on the Raspberry Pi in addition to the user file. 

# Added in last merge
- Updated runscript.py to work with ardSerial.py and SerialCommunications.py, allowing Bittle to dance now :D
- Configured dos2unix for running files in runscript.py
- Input argument conditions for all upload_run.py and runscript.py
- Better error handling
- Added function descriptions
- Reorganized functions and ensured cleanup
- Got real-time output working on upload_run.py, currently working on runscript.py

# Roadmap
- Get real-time output working on runscript.py
- Make and runs tests for library (including movement tests)
- Add remote shutdown command
- Make simple library out of sbituploader.py
- Add proper documentation
- Check resource consumption

# Future
- Add list of different Bittle movements into library
- Modify ardSerial.py as a debug function
- ROS Implementation