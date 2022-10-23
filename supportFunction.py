import os
from datetime import date
import binascii

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
    x = x.replace("\\x", '')
    x = str.encode(x[0:len(x)])
    return x

def pathConvertion(path):
    supportedPath = path.replace("\\","\\\\")
    return supportedPath