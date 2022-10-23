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

def VF1():

    files = ["C:\\Users\\1000300665\\Desktop\\FVT\\MPinfo-Automation\\MPinfo.bin"]


    filename = files[0]
    with open(filename, 'rb') as f:
        content = f.read()


    Hexify_String = binascii.hexlify(content)
    print(len(Hexify_String))

    HexList = [Hexify_String[i:i+32] for i in range(0, len(Hexify_String), 32)]


    HexLineList = [300, 302, 303, 304, 306]
    DecimalLineList = [int(str(i), base=16) for i in HexLineList]


    # user input:
    level = "VF1"
    serialNo = "0000001"
    driveCap = "256G"
    firmwareRev = "WS20"
    modelNo = "SUBNQN1"

    serial_x = serialUpdate(str=serialNo, level=level)
    drivecap_x = updateDriveCap(cap=driveCap, level=level)
    firmware_x = updateFirmware(firmware=firmwareRev, date=todaysDate())
    model_x = updateModel(model=modelNo, level=level)
    print("updated Serial : ({0})".format(serialUpdate(str=serialNo, level=level)))
    print("upadted driveCap : ({0})".format(
        updateDriveCap(cap=driveCap, level=level)))
    print("update FirmwareRev : ({0})".format(
        updateFirmware(firmware=firmwareRev, date=todaysDate())))
    print("update Model : ({0})".format(updateModel(model=modelNo, level=level)))

    # convert each updated value to hex
    serial_x_hex = stringToHex(serial_x)
    drivecap_x_hex = stringToHex(drivecap_x)
    firmware_x_hex = stringToHex(firmware_x)
    print(firmware_x_hex)
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
        if i == 3 and ln < 32:
            z = 32 - ln
            final.append("0"*z + temp[i])
        
        if i != 3:    
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
