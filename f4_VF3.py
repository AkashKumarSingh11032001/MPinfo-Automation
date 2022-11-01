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


def VF3(parameter):

    current_path, level, serialNo, driveCap, firmwareRev, HexLine = parameter

    files = [current_path]

    filename = files[0]
    with open(filename, 'rb') as f:
        content = f.read()

    Hexify_String = binascii.hexlify(content)
    # print(len(Hexify_String))

    HexList = [Hexify_String[i:i+32] for i in range(0, len(Hexify_String), 32)]

    HexLineList = HexLine
    DecimalLineList = [int(str(i), base=16) for i in HexLineList]

    # # user input:
    # level = "VF1"
    # serialNo = "0000001"
    # driveCap = "256G"
    # firmwareRev = "WS20"
    # modelNo = "SUBNQN1"

    serial_x = serialUpdate(str=serialNo, level=level)
    drivecap_x = updateDriveCap(cap=driveCap)
    firmware_x = updateFirmware(firmware=firmwareRev, date=todaysDate())
    model_x = updateModel(serial=serialNo)
    
    # convert each updated value to hex
    serial_x_hex = stringToHex(serial_x)
    drivecap_x_hex = stringToHex(drivecap_x)
    firmware_x_hex = stringToHex(firmware_x)
    # print(firmware_x_hex)
    model_x_hex = stringToHex(model_x)

    # handling extra bits
    extra_byte = "\x00"*32
    extra_x_hex = stringToHex(extra_byte)

    if len(drivecap_x_hex) > 32:
        left = len(drivecap_x_hex) - 32
        r = drivecap_x_hex
        drivecap_x_hex = r[:32]
        extra_x_hex = r[32:] + extra_x_hex[left:]
        
    # handling extra bits --> modelHex
    model_x_hex_2 = stringToHex("\00"*32)
    model_x_hex_3 = stringToHex("\00"*32)
    model_x_hex_4 = stringToHex("\00"*32)

    if len(model_x_hex) > 32:  # LEN(modelHex) = 112
        temp = model_x_hex
        model_x_hex = temp[:32]
        model_x_hex_2 = temp[32:64]
        model_x_hex_3 = temp[64:96]
        left = len(model_x_hex) - 96 - 16
        model_x_hex_4 = temp[96:]

    temp = [serial_x_hex, drivecap_x_hex, extra_x_hex, firmware_x_hex,
            model_x_hex, model_x_hex_2, model_x_hex_3, model_x_hex_4]
    final = []  # help to update directly to hexLIst.
    for i in range(0, len(temp)):
        ln = len(temp[i])
        # print(ln)
        if i == 3 and ln < 32:
            z = 32 - ln
            final.append("0"*z + temp[i])

        if i != 3:
            if ln < 32:
                z = 32 - ln
                final.append(temp[i] + "0"*z)
            else:
                final.append(temp[i])

    # print(final)  # hex not converted to bytes...
    byteFinal = [hexToBytes(i) for i in final]
    # print(byteFinal)  # hex converted to bytes...

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
    with open('MPxinfo.bin', 'wb') as f:
        f.write(unHexify_String)

