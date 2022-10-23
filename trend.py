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
from VF1 import VF1

files = ["mpInfo_bin_log\\MPInfoBuf.bin"]


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

# def main():
#     return [path,level,serialNo,driveCap,firmwareRev,modelNo]


filename = files[0]
with open(filename, 'rb') as f:
    content = f.read()


Hexify_String = binascii.hexlify(content)
print(len(Hexify_String))

HexList = [Hexify_String[i:i+32] for i in range(0, len(Hexify_String), 32)]


HexLineList = [120, 122, 123, 127, 180]
DecimalLineList = [int(str(i), base=16)
                   for i in HexLineList]  # [288, 290, 291, 295, 384]


serial_x = serialUpdate(str=serialNo, level=level)
drivecap_x = updateDriveCap(cap=driveCap, level=level)
firmware_x = updateFirmware(firmware=firmwareRev, date=todaysDate())
model_x = updateModel(model=modelNo, level=level)

# convert each updated value to hex
serial_x_hex = stringToHex(serial_x)
drivecap_x_hex = stringToHex(drivecap_x)
firmware_x_hex = stringToHex(firmware_x)
model_x_hex = stringToHex(model_x)

# handling extra bits
extra_byte = "\x00"*32
extra_x_hex = stringToHex(extra_byte)

if len(drivecap_x_hex) > 32:
    left = len(drivecap_x_hex) - 32
    r = drivecap_x_hex
    drivecap_x_hex = r[:32]
    extra_x_hex = r[32:] + extra_x_hex[left:]


temp = [serial_x_hex, drivecap_x_hex, extra_x_hex, firmware_x_hex, model_x_hex]
final = []  # help to update directly to hexLIst.
for i in range(0, len(temp)):
    ln = len(temp[i])
    print(ln)
    if ln < 32:
        z = 32 - ln
        final.append(temp[i] + "0"*z)
    else:
        final.append(temp[i])

print(final)  # hex not converted to bytes...
byteFinal = [hexToBytes(i) for i in final]
print(byteFinal)  # hex converted to bytes...


# updating HexList with the help of byteFinal...
j = 0
for i in DecimalLineList:
    HexList[i] = byteFinal[j]
    j = j + 1

# converting HexList to bytes String...
updatedString = b''.join(HexList)

# UnHexlify the bytesString to hexString...
unHexify_String = binascii.unhexlify(updatedString)


# creating new MPinfo.bin file with user inputed updated information
with open('MPinfo.bin', 'wb') as f:
    f.write(unHexify_String)
    

current_path = os.getcwd()+"\\MPinfo.bin"
current_path = pathConvertion(current_path)

VF1(current_path = current_path, level = "VF1", serialNo = serialNo, driveCap = driveCap, firmwareRev = firmwareRev, modelNo = modelNo)



# user input PATH :-
# >>> from path import path
# >>> path('mydir/myfile.txt').abspath()
# 'C:\\example\\cwd\\mydir\\myfile.txt'
