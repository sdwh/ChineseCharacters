import chars
import readCNS
import readPinyin
import readStroke

class CharacterInfo:
    def __init__(self, unicode_number, cns, word):
        self.unicode_number = unicode_number
        self.cns = cns
        self.zhuyin = None
        self.han = None
        self.zuin2 = None
        self.yale = None
        self.wei = None
        self.general = None
        self.stroke_count = None
        self.word = word

    def __str__(self):
        return f"Unicode Number: {self.unicode_number}\nCNS: {self.cns}\n注音: {self.zhuyin}\n漢語: {self.han}\n注音第二式: {self.zuin2}\n耶魯: {self.yale}\n韋式: {self.wei}\n通用: {self.general}\n筆畫數: {self.stroke_count}"

res = []

with open('output.txt', 'w', encoding = 'utf8') as file:
    for c in chars.chars2:
        try:
            unicode = str(c[0]).upper()
            unicode_hex = int('0x' + c[0], 16)
            word = chr(unicode_hex)
            cns = readCNS.cns_mapping[unicode]
            pinyin = readPinyin.phoneticsMapping[cns]
            stroke = readStroke.strokes[cns]
            #print(f'{cns}, {chr(unicode_hex)}, {hex(unicode_hex)}, {pinyin.han}')
            character = CharacterInfo(
                unicode_number=unicode,
                cns = cns,
                word = word
            )
            character.zhuyin = pinyin.zhuyin
            character.han = pinyin.han
            character.zuin2 = pinyin.zuin2
            character.yale = pinyin.yale
            character.wei = pinyin.wei
            character.general = pinyin.general
            character.stroke = stroke
            res.append(character)

            line = f'|{word}|{cns}|{unicode}|{pinyin.han}|{pinyin.wei}|{stroke}|\n'
            print(line)

            file.writelines(line)
        except:
            print(c)

    

