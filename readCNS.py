import glob

# 用于存储数据的列表
cns_mapping = {}

# 获取所有以"CNS2UNICODE_Unicode"开头的文件
file_pattern = "CNS2UNICODE_Unicode*.txt"
file_list = glob.glob(file_pattern)

# 遍历文件并追加数据
for filename in file_list:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            # 去除换行符并按制表符分隔数据
            line = line.strip()
            parts = line.split('\t')

            # 确保数据包含两个部分，否则跳过
            if len(parts) == 2:
                cns = parts[0]
                unicode_number = parts[1]
                # 将数据作为元组添加到列表中
                cns_mapping[unicode_number] = cns