import struct

# 定义支持的fourcc code对应的格式信息
formats = {
    "Y8": "Grayscale 8-bit",
    "Y10": "Grayscale 10-bit",
    "Y12": "Grayscale 12-bit",
    "Y16": "Grayscale 16-bit",
    "RGB8": "RGB 8:8:8",
    "BGR24": "BGR 8:8:8",
    "RGB565": "RGB 5:6:5",
    "RGB555": "RGB 5:5:5",
    "RG1616": "RG 16:16:16",
    "XR24": "x:R:G:B 8:8:8:8 little endian",
    "ARGB": "ARGB 8:8:8:8",
    "BGRA": "BGRA 8:8:8:8",
    "RGBA": "RGBA 8:8:8:8",
    "ABGR": "ABGR 8:8:8:8",
    "AYUV": "AYUV 8:8:8:8",
    "NV12": "NV12",
    "NV21": "NV21",
    "NV16": "NV16",
    "NV61": "NV61",
    "YUYV": "YUYV 4:2:2",
    "YVYU": "YVYU 4:2:2",
    "UYVY": "UYVY 4:2:2",
    "VYUY": "VYUY 4:2:2",
    "I420": "I420",
    "YV12": "YV12",
    "422P": "422P",
    "444P": "444P",
    "JPEG": "JPEG"
}

def fourcc_to_str(code):
    # 根据输入的code，计算对应的bytes并转换为字符串
    if isinstance(code, str):
        code = int(code, 16) if code.startswith('0x') else int(code)
    str_code = struct.pack("<I", code).decode("ascii")
    # 如果存在对应的格式信息，则输出格式信息，否则输出"Unknown"
    if str_code in formats:
        return str_code + " - " + formats[str_code]
    else:
        return "Unknown"

if __name__ == '__main__':
    # 等待用户输入，并输出对应的格式信息
    while True:
        code = input("Please enter fourcc code: ")
        if not code:
            break
        try:
            print(fourcc_to_str(code))
        except Exception as e:
            print("Error: ", e)
