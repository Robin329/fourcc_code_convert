#!/bin/env python3
import struct
import binascii

# 定义支持的fourcc code对应的格式信息
formats = {
    "C8": " ",
    "R8": " ",
    "R16": " ",
    "RG88": " ",
    "GR88": " ",
    "RG32": " ",
    "GR32": " ",
    "RGB8": " ",
    "BGR8": " ",
    "XR12": " ",
    "XB12": " ",
    "RX12": " ",
    "BX12": " ",
    "AR12": " ",
    "AB12": " ",
    "RA12": " ",
    "BA12": " ",
    "XR15": " ",
    "XB15": " ",
    "RX15": " ",
    "BX15": " ",
    "AR15": " ",
    "AB15": " ",
    "RA15": " ",
    "BA15": " ",
    "RG16": " ",
    "BG16": " ",
    "RG24": " ",
    "BG24": " ",
    "XR24": " ",
    "XB24": " ",
    "RX24": " ",
    "BX24": " ",
    "AR24": " ",
    "AB24": " ",
    "RA24": " ",
    "BA24": " ",
    "XR30": " ",
    "XB30": " ",
    "RX30": " ",
    "BX30": " ",
    "AR30": " ",
    "AB30": " ",
    "RA30": " ",
    "BA30": " ",
    "XR48": " ",
    "XB48": " ",
    "AR48": " ",
    "AB48": " ",
    "XR4H": " ",
    "XB4H": " ",
    "AR4H": " ",
    "AB4H": " ",
    "AB10": " ",
    "YUYV": " ",
    "YVYU": " ",
    "UYVY": " ",
    "VYUY": " ",
    "AYUV": " ",
    "XYUV": " ",
    "VU24": " ",
    "VU30": " ",
    "Y210": " ",
    "Y212": " ",
    "Y216": " ",
    "Y410": " ",
    "Y412": " ",
    "Y416": " ",
    "XV30": " ",
    "XV36": " ",
    "XV48": " ",
    "Y0L0": " ",
    "X0L0": " ",
    "Y0L2": " ",
    "X0L2": " ",
    "YU08": " ",
    "YU10": " ",
    "XRA8": " ",
    "XBA8": " ",
    "RXA8": " ",
    "BXA8": " ",
    "R8A8": " ",
    "B8A8": " ",
    "R5A8": " ",
    "B5A8": " ",
    "NV12": " ",
    "NV21": " ",
    "NV16": " ",
    "NV61": " ",
    "NV24": " ",
    "NV42": " ",
    "NV15": " ",
    "P210": " ",
    "P010": " ",
    "P012": " ",
    "P016": " ",
    "P030": " ",
    "Q410": " ",
    "Q401": " ",
    "YUV9": " ",
    "YVU9": " ",
    "YU11": " ",
    "YV11": " ",
    "YU12": " ",
    "YV12": " ",
    "YU16": " ",
    "YV16": " ",
    "YU24": " ",
    "YV24": " ",
}

def is_hex(s):
    if s.startswith('0x'):
        return True

def is_decimal(s):
    if s.isdigit():
        return True
    elif s.isalpha():
        return False
    else:
        try:
            int(s, 10)
            return True
        except ValueError:
            return False

def is_string(s):
    return not s.isdigit() and s.isalpha()

def str_to_fourcc(s):
    hex_string = binascii.hexlify(s.encode()).decode()
    fourcc = ""
    for i in range(0, len(hex_string), 2):
        fourcc = hex_string[i:i+2] + fourcc
    return "0x" + fourcc.upper()

def fourcc_to_str_dec(code):
    fourcc_str = ""
    for i in range(4):
        fourcc_str += chr((code >> 8 * i) & 0xFF)
    return fourcc_str

def fourcc_to_str(code):
    # 根据输入的code，计算对应的bytes并转换为字符串
    if isinstance(code, str):
        code = int(code, 16) if code.startswith('0x') else int(code)
    str_code = struct.pack("<I", code).decode("ascii")
    # 如果存在对应的格式信息，则输出格式信息，否则输出"Unknown"
    if str_code in formats:
        return "\tFormat     : \"" + str_code + " - " + formats[str_code] + "\""
    else:
        return "Unknown"

if __name__ == '__main__':
    # 等待用户输入，并输出对应的格式信息
    while True:
        code = input("Please Input: ")
        if not code:
            break
        try:
            if is_hex(code):
                print("is hex " + code)
                print(fourcc_to_str(code))
                print("\tFourcc Code:\"" + code + "(" + str(int(code, 16)) + ")" + "\"")
            elif is_decimal(code):
                print("is dec " + code)
                print("\tFormat     :\"" + fourcc_to_str_dec(int(code)) + "\"")
                print("\tFourcc Code:\"" + hex(int(code)) + "(" + code + ")\"")
            else:
                print("is string " + code)
                hex_val = str_to_fourcc(code)
                print(fourcc_to_str(str_to_fourcc(code)))
                print("\tFourcc Code:\"" + str_to_fourcc(code) + "(" + str(int(hex_val, 16)) + ")\"")
        except Exception as e:
            print("Error: ", e)
