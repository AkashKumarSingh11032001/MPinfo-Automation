import os
from datetime import date
import binascii

files = ["mpInfo_bin_log\\MPInfoBuf.bin"]


def stringRepToZero(str):
    return str.replace(str, "0"*32)


def todaysDate():
    today = date.today()
    return "{0}{1}".format(today.day, today.month)


def stringToHex(str):
    s = ''
    for c in str:
        s += hex(ord(c)).replace('0x', '')
    return s


def HexToAscii(str):
    return bytearray.fromhex(str).decode()


def serialUpdate(str, level):
    newSerial = "S{0}{1}".format(str, level)
    return newSerial[:]


def updateDriveCap(cap, level):
    str = "WDSSDATPOCM"
    newDriveCap = "{0}{1}{2}".format(str, cap, level)
    return newDriveCap[:]


def updateFirmware(firmware, date):
    newFirmware = "{0}{1}".format(firmware, date)
    return newFirmware[:]


def updateModel(model, level):
    newModel = "{0}{1}".format(model, level)
    return newModel[:]


def hexToBytes(hex):
    x = str(hex)
    x = x.replace("\\x",'')
    x = str.encode(x[0:len(x)])   
    return x


filename = files[0]
with open(filename, 'rb') as f:
    content = f.read()

# print(len(content)) # byt es content -b'ISP Rev:S0222BRD1.2.4\x00\x00\x00SMI-0000\\\xc9\

Hexify_String = binascii.hexlify(content)
print(len(Hexify_String))
# unHexify_String = binascii.unhexlify(Hexify_String)
# print(len(unHexify_String))
HexList = [Hexify_String[i:i+32] for i in range(0, len(Hexify_String), 32)]
print(HexList[288])  # b'32303232303830330000000000000000'

HexLineList = [120, 122, 123, 127, 180]
DecimalLineList = [int(str(i), base=16)
                   for i in HexLineList]  # [288, 290, 291, 295, 384]
# for i in DecimalLineList:
#     print((HexList[i]))

# user input:
level = "PF0"
serialNo = "0000001"
driveCap = "256G"
firmwareRev = "WS2"
modelNo = "SUBNQN1"

serial_x = serialUpdate(str=serialNo, level=level)
drivecap_x = updateDriveCap(cap=driveCap, level=level)
firmware_x = updateFirmware(firmware=firmwareRev, date=todaysDate())
model_x = updateModel(model=modelNo, level=level)
# print("updated Serial : ({0})".format(serialUpdate(str=serialNo, level=level)))
# print("upadted driveCap : ({0})".format(
#     updateDriveCap(cap=driveCap, level=level)))
# print("update FirmwareRev : ({0})".format(
#     updateFirmware(firmware=firmwareRev, date=todaysDate())))
# print("update Model : ({0})".format(updateModel(model=modelNo, level=level)))

# convert each updated value to hex
serial_x_hex = stringToHex(serial_x)
drivecap_x_hex = stringToHex(drivecap_x)
firmware_x_hex = stringToHex(firmware_x)
model_x_hex = stringToHex(model_x)
print("Hex updated Serial : ({0})".format(serial_x_hex))
print("Hex upadted driveCap : ({0})".format(drivecap_x_hex))
print("Hex update FirmwareRev : ({0})".format(firmware_x_hex))
print("Hex update Model : ({0})".format(model_x_hex))
print("length of updated Serial : ({0})".format(len(serial_x_hex)))
print("length of upadted driveCap : ({0})".format(len(drivecap_x_hex)))
print("length of update FirmwareRev : ({0})".format(len(firmware_x_hex)))
print("length of update Model : ({0})".format(len(model_x_hex)))

extra_byte = "\x00"*32
extra_x_hex = stringToHex(extra_byte)

if len(drivecap_x_hex) > 32:
    left = len(drivecap_x_hex) - 32
    r = drivecap_x_hex
    drivecap_x_hex = r[:32]
    extra_x_hex = r[32:] + extra_x_hex[left:]
    
# bytechnage_extra = bytes.fromhex(extra_x_hex)
# bytechnage_drive = bytes.fromhex(drivecap_x_hex)
# print(bytechnage_extra)
# print(bytechnage_drive)

temp = [serial_x_hex, drivecap_x_hex, extra_x_hex, model_x_hex, firmware_x_hex]
final = [] # help to update directly to hexLIst.
for i in range(0, len(temp)):
    ln = len(temp[i])
    print(ln)
    if ln < 32:
        z = 32 - ln
        final.append(temp[i] + "0"*z)
    else:
         final.append(temp[i])
    
print(final) # hex not converted to bytes...

byteFinal = [hexToBytes(i) for i in final]
print(byteFinal) # hex converted to bytes...

# x = str(byteFinal[0])
# x = x.replace("\\x",'')
# x = str.encode(x[2:len(x)-1])
# print(type(x))
# unHexify_String = binascii.unhexlify(byteFinal[0])
# print(len(unHexify_String))

# print(HexList)
j = 0
for i in DecimalLineList:
    HexList[i] = byteFinal[j]
    j = j + 1
    
# print(HexList)
for i in DecimalLineList:
    print(len(HexList[i]))

updatedString = b''.join(HexList)

unHexify_String = binascii.unhexlify(updatedString)
    
print(len(updatedString))
print(unHexify_String)

# print(HexList[288])
# HexList[288] = byteFinal[0]
# print(HexList[288])

with open('MPinfo.bin', 'wb') as f:
    f.write(unHexify_String)