import os
from datetime import date
import binascii
import time
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
from supportFunction import status
from f1_PF0 import PF0
from f2_VF1 import VF1
from f3_VF2 import VF2
from f4_VF3 import VF3
from f5_VF4 import VF4
from f6_VF5 import VF5
from f7_VF6 import VF6
from f8_VF7 import VF7
from f9_VF8 import VF8


mp_file_path = "mpInfo_bin_log\\MPInfoBuf.bin"


print(":-> Please enter required information below <-:")
print("")
# serialNo = input("Enter the Serial Number. : ")
# driveCap = input("Enter the Drive Capacity. : ")
# firmwareRev = input("Enter the Firmware Revision. : ")
# modelNo = input("Enter the Model Number. : ")

serialNo = "0000001"
driveCap = "256G"
firmwareRev = "WS21"
# modelNo = "SUBNQN1"

new_mp_file_name = "MPinfo.bin"


# getting current Path
current_path = os.getcwd()+"\\"+new_mp_file_name
current_path = pathConvertion(current_path)

# print("")
# status("Creating new MPInfo.bin file... ", 1)
# status("MPInfo.bin file Created!", 1)
# status("Updating MPInfo.bin... ", 1)
# print("")

PF0([mp_file_path, "PF0", serialNo, driveCap, firmwareRev, [120, 122, 123, 127, 180, 181, 182, 183], new_mp_file_name])
status("<> Physical Function [ PF-0 ] Updated!", 1)

VF1([current_path, "VF1", serialNo, driveCap, firmwareRev, [300, 302, 303, 304, 306, 307, 308, 309], new_mp_file_name])
status("<> Virtual Function  [ VF-1 ] Updated! ", 1)

VF2([current_path, "VF2", serialNo, driveCap, firmwareRev, [320, 322, 323, 324, 326, 327, 328, 329], new_mp_file_name])
status("<> Virtual Function  [ VF-2 ] Updated! ", 1)

VF3([current_path, "VF3", serialNo, driveCap, firmwareRev, [340, 342, 343, 344, 346, 347, 348, 349], new_mp_file_name])
status("<> Virtual Function  [ VF-3 ] Updated! ", 1)

VF4([current_path, "VF4", serialNo, driveCap, firmwareRev, [360, 362, 363, 364, 366, 367, 368, 369], new_mp_file_name])
status("<> Virtual Function  [ VF-4 ] Updated! ", 1)

VF5([current_path, "VF5", serialNo, driveCap, firmwareRev, [380, 382, 383, 384, 386, 387, 388, 389], new_mp_file_name])
status("<> Virtual Function  [ VF-5 ] Updated! ", 1)

VF6([current_path, "VF6", serialNo, driveCap, firmwareRev, ["3a0", "3a2", "3a3", "3a4", "3a6", "3a7", "3a8", "3a9"], new_mp_file_name])
status("<> Virtual Function  [ VF-6 ] Updated! ", 1)

VF7([current_path, "VF7", serialNo, driveCap, firmwareRev, ["3c0", "3c2", "3c3", "3c4", "3c6", "3c7", "3c8", "3c9"], new_mp_file_name])
status("<> Virtual Function  [ VF-7 ] Updated! ", 1)

VF8([current_path, "VF8", serialNo, driveCap, firmwareRev, ["3e0", "3e2", "3e3", "3e4", "3e6", "3e7", "3e8", "3e9"], new_mp_file_name])
status("<> Virtual Function  [ VF-8 ] Updated! ", 1)


print("")
print("*** New MPInfo.bin Created and Updated Successfully!!! *** ")
