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