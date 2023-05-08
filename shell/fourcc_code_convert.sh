#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 [<fourcc dec/hex code>|<format>]"
    exit 1
fi

fourcc_arr=(
    [0x20203843]=C8
    [0x20203852]=R8
    [0x20363152]=R16
    [0x38384752]=RG88
    [0x38385247]=GR88
    [0x32334752]=RG32
    [0x32335247]=GR32
    [0x38424752]=RGB8
    [0x38524742]=BGR8
    [0x32315258]=XR12
    [0x32314258]=XB12
    [0x32315852]=RX12
    [0x32315842]=BX12
    [0x32315241]=AR12
    [0x32314241]=AB12
    [0x32314152]=RA12
    [0x32314142]=BA12
    [0x35315258]=XR15
    [0x35314258]=XB15
    [0x35315852]=RX15
    [0x35315842]=BX15
    [0x35315241]=AR15
    [0x35314241]=AB15
    [0x35314152]=RA15
    [0x35314142]=BA15
    [0x36314752]=RG16
    [0x36314742]=BG16
    [0x34324752]=RG24
    [0x34324742]=BG24
    [0x34325258]=XR24
    [0x34324258]=XB24
    [0x34325852]=RX24
    [0x34325842]=BX24
    [0x34325241]=AR24
    [0x34324241]=AB24
    [0x34324152]=RA24
    [0x34324142]=BA24
    [0x30335258]=XR30
    [0x30334258]=XB30
    [0x30335852]=RX30
    [0x30335842]=BX30
    [0x30335241]=AR30
    [0x30334241]=AB30
    [0x30334152]=RA30
    [0x30334142]=BA30
    [0x38345258]=XR48
    [0x38344258]=XB48
    [0x38345241]=AR48
    [0x38344241]=AB48
    [0x48345258]=XR4H
    [0x48344258]=XB4H
    [0x48345241]=AR4H
    [0x48344241]=AB4H
    [0x30314241]=AB10
    [0x56595559]=YUYV
    [0x55595659]=YVYU
    [0x59565955]=UYVY
    [0x59555956]=VYUY
    [0x56555941]=AYUV
    [0x56555958]=XYUV
    [0x34325556]=VU24
    [0x30335556]=VU30
    [0x30313259]=Y210
    [0x32313259]=Y212
    [0x36313259]=Y216
    [0x30313459]=Y410
    [0x32313459]=Y412
    [0x36313459]=Y416
    [0x30335658]=XV30
    [0x36335658]=XV36
    [0x38345658]=XV48
    [0x304c3059]=Y0L0
    [0x304c3058]=X0L0
    [0x324c3059]=Y0L2
    [0x324c3058]=X0L2
    [0x38305559]=YU08
    [0x30315559]=YU10
    [0x38415258]=XRA8
    [0x38414258]=XBA8
    [0x38415852]=RXA8
    [0x38415842]=BXA8
    [0x38413852]=R8A8
    [0x38413842]=B8A8
    [0x38413552]=R5A8
    [0x38413542]=B5A8
    [0x3231564e]=NV12
    [0x3132564e]=NV21
    [0x3631564e]=NV16
    [0x3136564e]=NV61
    [0x3432564e]=NV24
    [0x3234564e]=NV42
    [0x3531564e]=NV15
    [0x30313250]=P210
    [0x30313050]=P010
    [0x32313050]=P012
    [0x36313050]=P016
    [0x30333050]=P030
    [0x30313451]=Q410
    [0x31303451]=Q401
    [0x39565559]=YUV9
    [0x39555659]=YVU9
    [0x31315559]=YU11
    [0x31315659]=YV11
    [0x32315559]=YU12
    [0x32315659]=YV12
    [0x36315559]=YU16
    [0x36315659]=YV16
    [0x34325559]=YU24
    [0x34325659]=YV24
)


#   for ((j=0; j<3; j++)); do
#     echo -n "${fourcc_arr[0x34325659]} "
#   done

code=$1

if [[ $code =~ ^0x[0-9a-fA-F]+$ ]]; then
    echo "Enter as a hexadecimal number!"

    echo "Format      : ${fourcc_arr[$code]} "
    echo "Fourcc Code : 0x$code"
elif  echo "$code" | grep -qE '^[a-zA-Z]'; then
    echo "Input is string!"
    # Extract individual characters and convert to ASCII
    char1=$(printf "%d" "'${code:0:1}")
    char2=$(printf "%d" "'${code:1:1}")
    char3=$(printf "%d" "'${code:2:1}")
    char4=$(printf "%d" "'${code:3:1}")
    hex1=$(printf "%x" $char4)
    hex2=$(printf "%x" $char3)
    hex3=$(printf "%x" $char2)
    hex4=$(printf "%x" $char1)
    hex=$hex1$hex2$hex3$hex4
    dec=`echo "ibase=16; $hex" | bc`
    # dec=$(printf "%d" "$hex")
    echo "Format      : $code"
    echo "Fourcc Code : 0x$hex($dec)"
else
    echo "Enter as a decimal number!"
    hex=`echo "obase=16; $code" | bc`
    echo "hex:$hex"
    echo "Format      : ${fourcc_arr[0x$hex]} "
    echo "Fourcc Code : 0x$hex($code)"
fi


echo ""
exit 0