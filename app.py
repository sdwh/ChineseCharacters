import chars
import readCNS
import readPinyin
import readStroke

class CharacterInfo:
    def __init__(self, unicode_number, cns, word, zhuyin, han, zuin2, yale, wei, general, stroke_count):
        self.unicode_number = unicode_number
        self.cns = cns
        self.zhuyin = zhuyin
        self.han = han
        self.zuin2 = zuin2
        self.yale = yale
        self.wei = wei
        self.general = general
        self.stroke_count = stroke_count
        self.word = word

    def __str__(self):
        return (f"Unicode Number: {self.unicode_number}\nCNS: {self.cns}\n注音: {self.zhuyin}\n漢語: {self.han}\n注音第二式: {self.zuin2}"
                f"\n耶魯: {self.yale}\n韋式: {self.wei}\n通用: {self.general}\n筆畫數: {self.stroke_count}")

def create_character_info(char):
    try:
        unicode_hex = int('0x' + char[0], 16)
        word = chr(unicode_hex)
        cns = cns_mapping[char[0].upper()]
        pinyin = phoneticsMapping[cns]
        stroke = strokes[cns]

        return CharacterInfo(
            unicode_number=char[0].upper(),
            cns=cns,
            word=word,
            zhuyin=pinyin.zhuyin,
            han=pinyin.han,
            zuin2=pinyin.zuin2,
            yale=pinyin.yale,
            wei=pinyin.wei,
            general=pinyin.general,
            stroke_count=stroke
        )
    except KeyError as e:
        print(f"Key error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

res = []
cns_mapping = readCNS.load_cns_mapping('CNS2UNICODE_Unicode*.txt')
phoneticsMapping = readPinyin.get_mapping("CNS_pinyin_1.txt", 'CNS_phonetic.txt')
strokes = readStroke.read_stroke('CNS_stroke.txt')

with open('output.txt', 'w', encoding='utf8') as file:
    for char in chars.chars2:
        character = create_character_info(char)
        if character:
            res.append(character)
            line = f'|{character.word}|{character.cns}|{character.unicode_number}|{character.han}|{character.wei}|{character.stroke_count}|\n'
            print(line)
            file.write(line)
