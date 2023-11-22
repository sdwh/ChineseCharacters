# cns_unicode_mapping.py

import glob

def load_cns_mapping(file_pattern):
    """加载CNS到Unicode的映射数据。"""
    cns_mapping = {}
    file_list = glob.glob(file_pattern)
    for filename in file_list:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                parts = line.split('\t')
                if len(parts) == 2:
                    cns, unicode_number = parts
                    cns_mapping[unicode_number] = cns
    return cns_mapping                