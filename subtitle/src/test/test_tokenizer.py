from collections import Counter

from src.data import DATA_DIR
from src.parse_subtitle import Subtitle


def test_tokenizer():
    
    sub_file_path = DATA_DIR / "Subtitle" / 'Game of Thrones - 1x01 - Winter is Coming.720p HDTV.en.srt'
    sub = Subtitle(sub_file_path)
    sub.tokenize()
    assert "." == Counter(sub.words).most_common()[0][0]