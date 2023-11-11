#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import sys
sys.path.append("..")
from ardSerial import *

if __name__ == '__main__':
    try:
        print("Hello World!")

    except Exception as e:
        logger.info("Exception")
        closeAllSerial(goodPorts)
        os._exit(0)
        raise e
