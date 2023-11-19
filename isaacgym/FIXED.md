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

# cuDNN Error
undefined symbol: cublasLtGetStatusString, version libcublasLt.so.11

In this case, I uninstalled cuDNN CU 11 and installed cuDNN CU 12. 
Inside bitrobotics/isaacgym:
```
   $ pip uninstall nvidia-cublas-cu11
   $ pip install nvidia-cublas-cu12 
```