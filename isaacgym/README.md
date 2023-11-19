## IsaacGym Training Environment for Bittle
This folder includes the IsaacGym training environment for bittle. 

This folder is forked from [IsaacGymEnvs](https://github.com/NVIDIA-Omniverse/IsaacGymEnvs) and uses files from [Fork: IsaacGymEnvs](https://github.com/AIWintermuteAI/IsaacGymEnvs/tree/main). This folder is a very slimmed-down version of the original repository. Please refer to 'READMENVIDIA.md' for detailed information on IsaacGym. Please refer to licenses from [IsaacGymEnvs](https://github.com/NVIDIA-Omniverse/IsaacGymEnvs) for using these repository. 

Trained checkpoints for bittle can be found in isaacgymenvs/runs. 

# Prerequisites
- Linux machine (e.g. Ubuntu 22.04)
- Nvidia GPU running CUDA 11.0+

# Setup: Python Environment
- Download IsaacGym (Prerelease) from the Nvidia website
- In '/IsaacGym_Preview_.../isaacgym/docs/index.html there is a quick tutorial on how to set up a conda environment named 'rlgpu' to run Python. IsaacGym uses it's own version of Python. 
- Navigate to bitrobotics/isaacgym and type '$ conda activate rlgpu'

# Setup: Packages
- In bitrobotics/isaacgym, enter '$ pip install -e .'
- '$ export LD_LIBRARY_PATH=/home/./miniconda3/envs/rlgpu/lib:$LD_LIBRARY_PATH'
- Navigate to bitrobotics/isaacgym/isaacgymenvs and run 'python train.py task=Cartpole'

A window should now open with a Cartpole task training itself. Use the key 'v' to pause/unpause the renderer. This can greatly speed up training. 

# Navigation
These are the essential files for training Bittle: 
    assets/urdf:                            Folder containing bittle.urdf as well as .obj files and textures
    isaacgymenvs/cfg/task/Bittle.yaml:      Configuration file for Bittle and environment
    isaacgymenvs/cfg/train/BittlePPO.yaml:  Configuration file for the Proximal Policy Optimization
    isaacgymenvs/cfg/config.yaml:           Configuration file for task selection
    isaacgymenvs/tasks/bittle.py:           Bittle training file, including setup and reward functions

# Quick Start
Once you have set up the necessary rlgpu environment and the packages, the following will allow you to quickly restart training when reloading: 
```
    $ conda activate rlgpu
    $ export LD_LIBRARY_PATH=/home/./miniconda3/envs/rlgpu/lib:$LD_LIBRARY_PATH
    $ cd isaacgymenvs
    $ python train.py task=Bittle checkpoint=runs/Bittle_.../nn/Bittle.pth
``` 
Run files with flag 'headless=True' for absolute fastest training speed. 

# Common Issues
Please refer to FIXES.md for some issues I encountered and fixed. 