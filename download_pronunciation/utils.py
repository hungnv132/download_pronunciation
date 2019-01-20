from pathlib import Path
from download_pronunciation.settings import (
    HOME_DIRECTORY, DOWNLOADED_AUDIO_FOLDER_NAME
)


def get_file_name_from_url(url):
    return url.split('/')[-1]


def get_downloaded_folder_path():
    return "{}/{}".format(HOME_DIRECTORY, DOWNLOADED_AUDIO_FOLDER_NAME)


def create_folder_for_downloading(path):
    p = Path(path)
    if not p.exists():
        p.mkdir()