# 设置编译器
CXX = g++

# 设置编译选项
CXXFLAGS = -Wall -std=c++11

# 设置目标文件名
TARGET = fourcc_code_convert

# 设置依赖项和对应的源文件
SRCS = fourcc_code_convert.cpp

# 生成目标文件
$(TARGET): $(SRCS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRCS)

# 清理中间文件和目标文件
clean:
	rm -f $(TARGET)