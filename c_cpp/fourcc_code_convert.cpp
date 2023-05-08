#include <getopt.h>

#include <iomanip>
#include <iostream>
#include <sstream>

#include "drm_fourcc.h"

using namespace std;

void help(const char *name) {
    cout << name << " [opt] [val|str]:" << endl;
    cout << "                -i - Fourcc code convert to str.\n";
    cout << "                -s - Str convert to fourcc code.\n";
    cout << "                -l - List all Drm fourcc code & string.\n";
    cout << "                -v - Verbose Log.\n";
}

string fourcc_code_to_str(uint32_t code) {
    uint8_t bytes[4];

    // 将32位的十六进制数分为4个8位的字节
    bytes[0] = (code >> 24) & 0xFF;
    bytes[1] = (code >> 16) & 0xFF;
    bytes[2] = (code >> 8) & 0xFF;
    bytes[3] = code & 0xFF;

    // 将每个字节转换为对应的ASCII字符，并连接在一起
    std::stringstream ss;
    for (int i = 0; i < 4; i++) {
        ss << static_cast<char>(bytes[4 - i - 1]);
    }
    std::string str = ss.str();

    // 输出ASCII字符
    // std::cout << str << std::endl;
    return str;
}

int main(int argc, char *argv[]) {
    int  option;
    bool verbose = false;
    bool code_to_str = false;
    bool str_to_code = false;
    bool list_all = false;

    uint32_t code;

    while ((option = getopt(argc, argv, "vhi:s:l")) != -1) {
        switch (option) {
            case 'v':
                verbose = true;
                break;
            case 'i':
                code_to_str = true;
                code = std::stoul(optarg, nullptr, 16);
                if (str_to_code) str_to_code = false;
                break;
            case 's':
                str_to_code = true;
                code = fourcc_code(optarg[0], optarg[1], optarg[2], optarg[3]);
                // cout << optarg << endl;
                if (code_to_str) code_to_str = false;
                break;
            case 'l':
                list_all = true;
                if (str_to_code) str_to_code = false;
                if (code_to_str) code_to_str = false;
                break;
            case 'h':
            default:
                help(argv[0]);
                return 0;
        }
    }
    if (argc < 2) {
        help(argv[0]);
        return 0;
    }
    if (verbose) {
        cout << "code_to_str: " << code_to_str << endl;
        if (code_to_str || str_to_code) cout << hex << "       code: 0x" << code << endl << dec;
        cout << "str_to_code: " << str_to_code << endl;
        cout << "    verbose: " << verbose << endl;
        cout << "   list_all: " << list_all << endl;
    }
    if (list_all) {
        for (int i = 0; i < sizeof(fourcc_code) / sizeof(uint32_t); ++i) {
            // cout << std::dec << "id:" << i << endl;
            // cout << "   Format     :\"" << fourcc_code_to_str(fourcc_code[i]) << "\"\n";
            // cout << "   Fourcc Code:\"" << hex << setfill('0') << setw(8) << std::showbase << fourcc_code[i] << "\""
            //      << endl;
            cout << "[" << hex << setfill('0') << setw(8) << std::showbase << fourcc_code[i] << "]"
                 << "=" << fourcc_code_to_str(fourcc_code[i]) << endl;
        }
    }

    if (str_to_code || code_to_str) {
        for (int i = 0; i < sizeof(fourcc_code) / sizeof(uint32_t); ++i) {
            if (fourcc_code[i] == code) {
                cout << std::dec << "id:" << i << endl;
                cout << "   Format     :\"" << fourcc_code_to_str(fourcc_code[i]) << "\"\n";
                cout << "   Fourcc Code:\"" << hex << setfill('0') << setw(8) << std::showbase << fourcc_code[i] << "\""
                     << endl;
            }
        }
    }

    return 0;
}