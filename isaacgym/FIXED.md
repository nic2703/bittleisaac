# Packages not found
Make sure that you are in your rlgpu environment. 
Make sure that you have run in bitrobotics/isaacgym
```
    $ pip install -e .
```

If isaacgymenvs is missing, make sure you have run 
```
    $ export LD_LIBRARY_PATH=/home/./miniconda3/envs/rlgpu/lib:$LD_LIBRARY_PATH
```

# TorchScript Incompatibility
RuntimeError: nvrtc: error: invalid value for --gpu-architecture (-arch)

Fix by upgrading CUDA framework. 

```
    $ nvcc --version
```

If nvcc version is not 11.0+, refer to the following: 
Check if a newer CUDA installation is available under usr/local/cuda-xx.x. If not, download a new version. 

In my case, I had CUDA 12.1 installed but nvcc used 10.1. I made nvcc use CUDA 12.1 using the following: 
```
    $ export PATH=/usr/lib/cuda-12.1/bin:$PATH
    $ export LD_LIBRARY_PATH=/usr/lib/cuda-12.1/lib64:$LD_LIBRARY_PATH
    $ export CUDA_HOME=/usr/local/cuda-12.1
    $ export CUDA_PATH=/usr/local/cuda-12.1
    $ nvcc --version
```

UPDATE: I noticed that this sometimes resets after a while. A more permanent solution is to modify the ~/.bashrc file using nano. 
```
nano ~/.bashrc
```
Add to the bottom of the file the following two lines (dependent on your CUDA location and version of course):
```
export PATH=/usr/local/cuda-12.1/bin:$PATH
export CUDA_HOME=/usr/local/cuda-12.1
```

Back in the terminal, reload the configuration and check if the version has been updated. 
```
source ~/.bashrc
nvcc --version
```

# cuDNN Error
undefined symbol: cublasLtGetStatusString, version libcublasLt.so.11

In this case, I uninstalled cuDNN CU 11 and installed cuDNN CU 12. 
Inside bitrobotics/isaacgym:
```
   $ pip uninstall nvidia-cublas-cu11
   $ pip install nvidia-cublas-cu12 
```

# libpython3.7m.so.1.0 cannot be opened

```
Importing module 'gym_37' (/home/nic/Documents/IsaacGym_Preview_4_Package/isaacgym/python/isaacgym/_bindings/linux-x86_64/gym_37.so)
Error executing job with overrides: ['task=Cartpole']
Traceback (most recent call last):
  File "train.py", line 79, in launch_rlg_hydra
    import isaacgym
  File "/home/nic/Documents/IsaacGym_Preview_4_Package/isaacgym/python/isaacgym/__init__.py", line 5, in <module>
    from isaacgym import gymapi
  File "/home/nic/Documents/IsaacGym_Preview_4_Package/isaacgym/python/isaacgym/gymapi.py", line 104, in <module>
    _import_active_version()
  File "/home/nic/Documents/IsaacGym_Preview_4_Package/isaacgym/python/isaacgym/gymapi.py", line 63, in _import_active_version
    module = importlib.import_module(package_path)
  File "/home/nic/miniconda3/envs/rlgpu/lib/python3.7/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
ImportError: libpython3.7m.so.1.0: cannot open shared object file: No such file or directory
```

This error occurs if the conda environment has not been set up correctly. Please follow the exact steps below: 
When opening the folder, make sure that you are not in the conda environment yet. Then run: 
```
(base) ...:~/.../bitrobotics/isaacgym$ conda activate rlgpu
(rlgpu) ...:~/.../bitrobotics/isaacgym$ pip install -e .
(rlgpu) ...:~/.../bitrobotics/isaacgym$ pip uninstall nvidia-cublas-cu11
(rlgpu) ...:~/.../bitrobotics/isaacgym$ export LD_LIBRARY_PATH=/home/.../miniconda3/envs/rlgpu/lib
(rlgpu) ...:~/.../bitrobotics/isaacgym$ cd isaacgymenvs
(rlgpu) ...:~/.../bitrobotics/isaacgym/isaacgymenvs$ python train.py task=Cartpole
```

