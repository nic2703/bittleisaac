#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import sys
sys.path.append("..")
from ardSerial import *

hlw = [ # customized gait that takes smaller steps ajusted for the costume
14, 0, 0, 1,
  10,  29,  51,  46,  33,  30,   4,  15,
  10,  32,  43,  48,  40,  29,   3,  16,
  15,  35,  34,  49,  35,  30,  13,  18,
  19,  44,  36,  52,  33,  17,  14,  19,
  22,  38,  39,  53,  31,  16,  14,  22,
  25,  30,  42,  61,  30,  17,  14,  11,
  28,  21,  44,  56,  30,  21,  15,   6,
  31,   8,  47,  49,  29,  40,  16,   3,
  33,  13,  48,  41,  30,  37,  17,   3,
  38,  16,  51,  33,  28,  34,  18,  17,
  42,  20,  52,  37,  16,  32,  20,  14,
  35,  23,  59,  40,  16,  31,  16,  14,
  26,  26,  59,  42,  19,  30,   8,  14,
  15,  28,  52,  45,  27,  30,   5,  15]
jump = [ # customized behavior designed with the Petoi Skill Composer
-4,   0,   0,   1,
   1,   2,   2,
   0,   0,   0,   0,   0,   0,   0,   0,  30,  30,  30,  30,  30,  30,  30,  30,   8,   0,   0,   0,
   0,   0,   0,   0,   0,   0,   0,   0,  42,  42,  42,  42,   6,   6,   6,   6,  48,   0,   0,   0,
  37,   0,   0,   0,   0,   0,   0,   0, -10, -10, -10, -10, 110, 110, 110, 110,   0,   0,   0,   0,
  26,  11, -11,   0,  11,  11, -22, -22,   6,   6,   8,   8,   8,   8,  52,  52,   0,   0,   0,   0,]

model = 'Bittle'
postureTable = postureDict[model]

E_RGB_ALL = 0
E_RGB_RIGHT = 1
E_RGB_LEFT = 2
E_EFFECT_BREATHING = 0
E_EFFECT_ROTATE = 1
E_EFFECT_FLASH = 2
E_EFFECT_NONE = 3

if __name__ == '__main__':
    try:
        testSchedule = [# the storyline

            ['K',hlw,4],                # walk in the halloween gait for 4 seconds
            
        ]
        goodPorts = {}
        connectPort(goodPorts) # discover petoi robots connected to the computer's serial ports
        t=threading.Thread(target = keepCheckingPort, args = (goodPorts,))
        t.start()
        parallel = False # we are not controlling multiple robots in this demo
#        if len(goodPorts)>0:
        time.sleep(2)
        for task in testSchedule:  # execute the tasks in the testSchedule
            print(task)
            send(goodPorts, task)
        closeAllSerial(goodPorts)
        logger.info("finish!")
        os._exit(0)

    except Exception as e:
        logger.info("Exception")
        closeAllSerial(goodPorts)
        os._exit(0)
        raise e

