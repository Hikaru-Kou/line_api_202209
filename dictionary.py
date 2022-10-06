import csv
class Dictionary():
    def judge(self,word):
        np_dic = {}
        counter = {"p":0, "n":0, "e":0}
        fp = open("pn.csv", "rt", encoding="utf-8")
        reader = csv.reader(fp, delimiter='\t')
        for i, row in enumerate(reader):
            name = row[0]
            result = row[1]
            np_dic[name] = result
        word_sentence = word.split()
        for t in word_sentence:
            # 辞書にあるか確認
            if t in np_dic:
                r = np_dic[t]
                if r in counter:
                    counter[r] += 1

        return counter

    def select(self, word, **kwargs):
        np_dic = {}
        select = "green"
        fp = open("pn.csv", "rt", encoding="utf-8")
        reader = csv.reader(fp, delimiter='\t')
        for i, row in enumerate(reader):
            name = row[0]
            result = row[1]
            np_dic[name] = result
        word_sentence = word.split()
        for t in word_sentence:
            # 辞書にあるか確認
            if t in np_dic:
                #ポジティブ、ネガティブ、それ以外はそのまま
                if np_dic[t] == "p":
                    select = "orange"
                elif np_dic[t] == "n":
                    select = "red"
        
        return select
