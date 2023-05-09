- [1. fourcc\_code\_convert](#1-fourcc_code_convert)
  - [1.1. c\_cpp](#11-c_cpp)
  - [1.2. python](#12-python)
    - [1.2.1. Method 1](#121-method-1)
    - [1.2.2. Method 2](#122-method-2)
    - [1.2.3. Method 3](#123-method-3)
  - [1.3. shell](#13-shell)


# 1. fourcc_code_convert
If you need to convert fourcc code to human readable color format, or between the two, yes you can use this tool, it supports multiple languages


## 1.1. c_cpp

```shell
$ cd c_cpp/ && make
$ ./fourcc_code_convert -h
 ./fourcc_code_convert [opt] [val|str]:
                -i - Fourcc code convert to str.
                -s - Str convert to fourcc code.
                -l - List all Drm fourcc code & string.
                -v - Verbose Log.
```

## 1.2. python

### 1.2.1. Method 1
```shell
$ ./fourcc_code_convert.py
Please Input: AR24
is string AR24
        Format     : "AR24 -  "
        Fourcc Code:"0x34325241(875713089)"
```

### 1.2.2. Method 2
```shell
$ ./fourcc_code_convert.py
Please Input: 0x30335852
is hex 0x30335852
        Format     : "RX30 -  "
        Fourcc Code:"0x30335852(808671314)"
```

### 1.2.3. Method 3
```shell
$ ./fourcc_code_convert.py
Please Input: 875710290
is dec 875710290
        Format     :"RG24"
        Fourcc Code:"0x34324752(875710290)"
```


## 1.3. shell

```sh
$ ./fourcc_code_convert.sh
Usage: ./fourcc_code_convert.sh [<fourcc dec/hex code>|<format>]

$ ./fourcc_code_convert.sh 0x34324142
    Format      : BA24
    Fourcc Code : 0x0x34324142

$ ./fourcc_code_convert.sh 875710290
    hex:34324752
    Format      : RG24
    Fourcc Code : 0x34324752(875710290)

$ ./fourcc_code_convert.sh BA24
Format      : BA24
Fourcc Code : 0x34324142(875708738)

```

Enjoy Yourself!!