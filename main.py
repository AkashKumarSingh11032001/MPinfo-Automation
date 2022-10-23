import os
from datetime import date
import binascii
from supportFunction import stringRepToZero
from supportFunction import todaysDate
from supportFunction import stringToHex
from supportFunction import HexToAscii
from supportFunction import serialUpdate
from supportFunction import updateDriveCap
from supportFunction import updateFirmware
from supportFunction import updateModel
from supportFunction import hexToBytes
from supportFunction import pathConvertion
from f1_PF0 import PF0
from f2_VF1 import VF1


file_path = "mpInfo_bin_log\\MPInfoBuf.bin"

# level = input("Enter the Physical Function name. : \n")
# serialNo = input("Enter the Serial Number. : \n")
# driveCap = input("Enter the Drive Capacity. : \n")
# firmwareRev = input("Enter the Firmware Revision. : \n")
# modelNo = input("Enter the Model Number. : \n")

# # user input:
level = "PF1"
serialNo = "0000001"
driveCap = "256G"
firmwareRev = "WS20"
modelNo = "SUBNQN1"


# getting current Path
current_path = os.getcwd()+"\\MPinfo.bin"
current_path = pathConvertion(current_path)

PF0([file_path, level, serialNo, driveCap, firmwareRev, modelNo, [120, 122, 123, 127, 180]])
VF1([current_path, "VF1", serialNo, driveCap, firmwareRev, modelNo, [300, 302, 303, 304, 306]])
VF1([current_path, "VF2", serialNo, driveCap, firmwareRev, modelNo, [320, 322, 323, 324, 326]])
VF1([current_path, "VF3", serialNo, driveCap, firmwareRev, modelNo, [340, 342, 343, 344, 346]])
VF1([current_path, "VF4", serialNo, driveCap, firmwareRev, modelNo, [360, 362, 363, 364, 366]])
VF1([current_path, "VF5", serialNo, driveCap, firmwareRev, modelNo, [380, 382, 383, 384, 386]])
VF1([current_path, "VF6", serialNo, driveCap, firmwareRev, modelNo, ["3a0", "3a2", "3a3", "3a4", "3a6"]])
VF1([current_path, "VF7", serialNo, driveCap, firmwareRev, modelNo, ["3c0", "3c2", "3c3", "3c4", "3c6"]])
VF1([current_path, "VF8", serialNo, driveCap, firmwareRev, modelNo, ["3e0", "3e2", "3e3", "3e4", "3e6"]])




# 3200  S0000001VF1
# 3220  WDSSDATPOCM256GVF1
# 3240  WS211310(day/month) --> (edit : from 9th bit which will be default CFW)
# 3260  SUBNQN1VF1

# 3400 / 3420 / 3440 / 3460
# 3600 / 
# 3800 / 
# 3a00 / 
# 3c00 / 
# 3e00 / 



