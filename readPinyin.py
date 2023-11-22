class PinyinEntity:
    def __init__(self, zhuyin, han, zuin2, yale, wei, general):
        self.zhuyin = zhuyin
        self.han = han
        self.zuin2 = zuin2
        self.yale = yale
        self.wei = wei
        self.general = general

    def __str__(self):
        return f"注音: {self.zhuyin}\n漢語: {self.han}\n注音第二式: {self.zuin2}\n耶魯: {self.yale}\n韋式: {self.wei}\n通用: {self.general}"

def read_txt_file(filename):
    res = {}
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split('\t')
            if len(data) == 6:
                entry = PinyinEntity(data[0], data[1], data[2], data[3], data[4], data[5])
                res[data[0]] = entry
    return res

def read_phonetic(filename):
    phonetic = {}
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            data = line.strip().split('\t')
            if len(data) == 2:
                phonetic[data[0]] = data[1]
    return phonetic

def get_mapping(file1, file2):

    pinyinEntitys = read_txt_file(file1)
    phonetics = read_phonetic(file2)

    phoneticsMapping = {}

    for key, value in phonetics.items():
        phoneticsMapping[key] = pinyinEntitys[value]

    return phoneticsMapping