class word_details:
    def __init__(self, word, pos, prounciation, defi):
        self.word = word
        self.pos = pos
        self.prounciation = prounciation
        self.defi = defi

    def disp(self):
        print(self.word, self.pos, self.sylla, self.prounciation, self.defi)


