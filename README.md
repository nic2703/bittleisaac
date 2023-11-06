# bitrobotics
(WIP) Library for various Bittle, Python and ROS integrations. My intention is to build a library of functions to easily upload to and control Petoi Bittle using a Raspberry Pi 3A+. This probably is going to expand to ROS/Isaac Sim integration. 

# What currently works
/uploader contains prototype sbituploader.py and runscript.py which both work. Please refer to SerialConnection/README.md on how to properly set up the Raspberry Pi.
sbituploader.py defines a function which makes it easy to upload and execute scripts to the Raspberry Pi from the PC. 
runscript.py is a helper function which is triggered by sbituploader.py and runs on the Raspberry Pi in addition to the user file. 

# Roadmap
- Add and test cancel condition for sbituploader.py/runscript.py
- Add remote shutdown command
- Make simple library out of sbituploader.py
- Make and runs tests for library (including movement tests)
- Add proper documentation
- Check resource consumption

# Future
- Add list of different Bittle movements into library
- Modify ardSerial.py as a debug function
- ROS Implementation