import MeCab

class CoeffieientBodyAnalyser:
    def exe_mecab(self, data):
        self.data = data
        tagger = MeCab.Tagger()  # 「tagger = MeCab.Tagger('-d ' + unidic.DICDIR)」
        node = tagger.parseToNode(self.data)
        elements = ["", ""]
        while(node):
            if node.surface != "":  # ヘッダとフッタを除外
                word_type = node.feature.split(",")[0]
                #全ての単語を追加
                elements[0] += node.surface + " "
                # 名詞だけに追加する
                if word_type in ["名詞"]:
                        elements[1] += node.surface + " " 

            node = node.next
            
            if node is None:
                break

        return elements
