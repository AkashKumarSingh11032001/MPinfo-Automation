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


filename = files[0]
with open(filename, 'rb') as f:
    content = f.read()

# print(content)
HexString = str(binascii.hexlify(content))
# print(HexString)
HexString = HexString[2:]
HexList = [HexString[i:i+32] for i in range(0, len(HexString), 32)]
s = HexList[288]
s = s.replace(s, "0"*32)

# ********************************************* PF info Modification *********************************************
# lines : 120 / 122 / 127 / 180


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


lineList = [120, 122, 123, 127, 180]
updateLIst = []
for i in range(0, len(lineList)):
    updateLIst.append(stringRepToZero(HexList[i]))

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
model_x_hex = stringToHex(model_x)
print("Hex updated Serial : ({0})".format(serial_x_hex))
print("Hex upadted driveCap : ({0})".format(drivecap_x_hex))
print("Hex update FirmwareRev : ({0})".format(firmware_x_hex))
print("Hex update Model : ({0})".format(model_x_hex))
print("length of updated Serial : ({0})".format(len(serial_x_hex)))
print("length of upadted driveCap : ({0})".format(len(drivecap_x_hex)))
print("length of update FirmwareRev : ({0})".format(len(firmware_x_hex)))
print("length of update Model : ({0})".format(len(model_x_hex)))

extra_x_hex = ""
if len(drivecap_x_hex) > 32:
    extra_x_hex = drivecap_x_hex[32:]
    drivecap_x_hex = drivecap_x_hex[0:32]


# print(drivecap_x_hex)
# print(extra_x_hex)
# replace each value to its respective updateLIst indexs
updated_Hex_list = [serial_x_hex, drivecap_x_hex,
                    "30"*16, firmware_x_hex, model_x_hex]

for i in range(0, len(updated_Hex_list)):
    if i == 2 and extra_x_hex != "":
        updated_Hex_list[i] = extra_x_hex + updated_Hex_list[i][4:]
    else:
        part_hex_length = len(updated_Hex_list[i])
        updateLIst[i][:part_hex_length] = updated_Hex_list[i]
        updated_Hex_list[i] = updateLIst[i]

print("Before HexLIst Update : ({0}) --- ({1})".format(
    HexList[lineList[0]], len(HexList[lineList[0]])))
j = 0
for i in lineList:
    HexList[i] = HexList[i].replace(HexList[i], updated_Hex_list[j])
    j = j + 1

print("After HexLIst Update : ({0})--- ({1})".format(
    HexList[lineList[0]], len(HexList[lineList[0]])))
# ********************************************* PF info Modification *********************************************


# ********************************************* New MPinfo File Creation *********************************************
print("Hex to ASCII : ({0})".format(HexList[0]))
val = bytearray.fromhex(HexList[0]).decode()
print(type(val))
s1 = bytes(val, "utf-8")
print(s1)
print("Hex to ASCII func : ({0})".format(
    bytearray.fromhex(HexList[0]).decode()))
# for i in HexList[0]:
#     Binary = binascii.a2b_uu(i)
# print("Binary ASCII to BIN : ({0})".format(Binary))
# with open('MPinfo.bin', 'wb') as f:
#     if os.path.exists("MPinfox.bin"):
#         # os.remove("MPinfo.bin")
#         # print("The file has been deleted successfully")
#         pass
#     else:
#         print("The file does not exist! so creating new MPinfo.bin file...")
#         i = 0
#         while i < len(HexList):
#             val = bytearray.fromhex(HexList[i]).decode()
#             s1 = bytes(val, "utf-8")
#             f.write(s1)
#             i = i + 1
#         # for i in range(0,len(HexList)):
#         #     # res = bytes(test_string, 'utf-8')
#         #     print(i)
#         #     # HexList[i] = bytes(HexList[i], 'utf-8')
#         #     val = bytearray.fromhex(HexList[i]).decode()
#         #     print(type(val))
#         #     # print(type(HexList[i]))
#         #     f.write(val)


print("UPdated with zero List : ({0})".format(updateLIst))
print("UPdated with Hex List : ({0})".format(updated_Hex_list))
print("UPdated with Hex List val 1: ({0})".format(
    bytearray.fromhex(updated_Hex_list[0]).decode()))
print(type(bytearray.fromhex(updated_Hex_list[0]).decode()))
print("UPdated with Hex List val 2: ({0})".format(
    bytearray.fromhex(updated_Hex_list[1]).decode()))
print("UPdated with Hex List val 3: ({0})".format(
    bytearray.fromhex(updated_Hex_list[2]).decode()))
print("UPdated with Hex List val 4: ({0})".format(
    bytearray.fromhex(updated_Hex_list[3]).decode()))
print("UPdated with Hex List val 5: ({0})".format(
    bytearray.fromhex(updated_Hex_list[4]).decode()))
print("Hex Length : ({0})".format(len(HexList)))
print(HexList[288])
print(type(str(HexString)))
