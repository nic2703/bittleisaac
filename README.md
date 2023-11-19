# bitrobotics
(WIP) Library for various Bittle, Python and ROS integrations. My intention is to build a library of functions to easily upload to and control Petoi Bittle using a Raspberry Pi 3A+. This probably is going to expand to ROS/Isaac Sim integration. 

## What currently works
I am very pleased to announce that /isaacgym now works. Please follow the instructions in the associated README.md.

/uploader contains prototype upload_run.py and runscript.py which both work. Please refer to SerialConnection/README.md on how to properly set up the Raspberry Pi.

## Added in last merge
- Added and cleaned /isaacgym from [IsaacGymEnvs](https://github.com/NVIDIA-Omniverse/IsaacGymEnvs)
- Added Bittle integrations including from [Fork: IsaacGymEnvs](https://github.com/AIWintermuteAI/IsaacGymEnvs/tree/main)
- Added documentation/debugging

## Roadmap
- Upgrade Bittle servo board to ESP32 in anticipation of ROS integration
- Get real-time output working on runscript.py
- Make and runs tests for library (including movement tests)
- Add remote shutdown command
- Make simple library out of sbituploader.py
- Add proper documentation
- Check resource consumption

## Future
- Train list of different Bittle movements into library
- Modify ardSerial.py as a debug function
- ROS Implementation