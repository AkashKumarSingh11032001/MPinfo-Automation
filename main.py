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
from supportFunction import printing
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

serialNo = input("Enter the Serial Number. : \n")
driveCap = input("Enter the Drive Capacity. : \n")
firmwareRev = input("Enter the Firmware Revision. : \n")
modelNo = input("Enter the Model Number. : \n")

# serialNo = "0000001"
# driveCap = "256G"
# firmwareRev = "WS20"
# modelNo = "SUBNQN1"


# getting current Path
current_path = os.getcwd()+"\\MPinfo.bin"
current_path = pathConvertion(current_path)

print("")
print("Updating... ")
print("")

PF0([mp_file_path, "PF1", serialNo, driveCap, firmwareRev, modelNo, [120, 122, 123, 127, 180]])
printing("... Physical Function [ PF-0 ] Updated!", 1)

VF1([current_path, "VF1", serialNo, driveCap, firmwareRev, modelNo, [300, 302, 303, 304, 306]])
printing("... Virtual Function [ VF-1 ] Updated! ", 1)

VF2([current_path, "VF2", serialNo, driveCap, firmwareRev, modelNo, [320, 322, 323, 324, 326]])
printing("... Virtual Function [ VF-2 ] Updated! ", 1)

VF3([current_path, "VF3", serialNo, driveCap, firmwareRev, modelNo, [340, 342, 343, 344, 346]])
printing("... Virtual Function [ VF-3 ] Updated! ", 1)

VF4([current_path, "VF4", serialNo, driveCap, firmwareRev, modelNo, [360, 362, 363, 364, 366]])
printing("... Virtual Function [ VF-4 ] Updated! ", 1)

VF5([current_path, "VF5", serialNo, driveCap, firmwareRev, modelNo, [380, 382, 383, 384, 386]])
printing("... Virtual Function [ VF-5 ] Updated! ", 1)

VF6([current_path, "VF6", serialNo, driveCap, firmwareRev, modelNo, ["3a0", "3a2", "3a3", "3a4", "3a6"]])
printing("... Virtual Function [ VF-6 ] Updated! ", 1)

VF7([current_path, "VF7", serialNo, driveCap, firmwareRev, modelNo, ["3c0", "3c2", "3c3", "3c4", "3c6"]])
printing("... Virtual Function [ VF-7 ] Updated! ", 1)

VF8([current_path, "VF8", serialNo, driveCap, firmwareRev, modelNo, ["3e0", "3e2", "3e3", "3e4", "3e6"]])
printing("... Virtual Function [ VF-8 ] Updated! ", 1)


print("")
print("*** New MPinfo.bin Created and Updated Successfully!!! *** ")
