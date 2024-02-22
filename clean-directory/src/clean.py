import shutil
from pathlib import Path
from collections import Counter

class Organizer:

    def __init__(self,directory):
        self.directory = Path(directory)
        if not self.directory.exists():
            raise FileNotFoundError(f'{self.directory} does not exist' )
        self.ext_destination = {
            '.png':'image',
            '.jpg':'image',
            '.csv':'data',
            'mp4':'video',
            '.zip':'compressed',
            '.ipynb':'notebook',
                }



    def __col__(self):
        file_extensions = []
        for file_path in self.directory.iterdir():
            # ignore directory
            if file_path.is_dir():
                continue

            # ignore hidden files
            if file_path.name.startswith('.'):
                continue

            # move file
            file_extensions.append(file_path.suffix)

            if file_path.suffix not in self.ext_destination:
                DEST_DIR = DIR_PATH / 'other'

            else:
                DEST_DIR = DIR_PATH / self.ext_destination[file_path.suffix]

            DEST_DIR.mkdir(exist_ok=True)
            shutil.move(file_path,DEST_DIR)
            print(f'{file_path.suffix} {DEST_DIR}')


if __name__ == '__main__':
    download = Organizer('Downloads')
    download()