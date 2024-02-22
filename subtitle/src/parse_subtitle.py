import pysrt
from loguru import logger
from nltk.tokenize import word_tokenize
from tqdm import tqdm

# import nltk
# nltk.download('punkt')

class Subtitle:
    
    def __init__(self,file_path):
        self.subs = pysrt.open(file_path)
        self.words = []
    
    def tokenize(self):
        logger.info('Tokenizing subtitle...')
        for sub in tqdm(self.subs):
            self.words.extend(word_tokenize(sub.text))
        
        
if __name__ == '__main__':
    from collections import Counter

    from data import DATA_DIR
    
    sub_file_path = DATA_DIR / "Subtitle" / 'Game of Thrones - 1x01 - Winter is Coming.720p HDTV.en.srt'
    sub = Subtitle(sub_file_path)
    sub.tokenize()
    print(Counter(sub.words).most_common(10))




