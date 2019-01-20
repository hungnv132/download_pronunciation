# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from download_pronunciation.utils import (
    create_folder_for_downloading, get_downloaded_folder_path
)
create_folder_for_downloading(get_downloaded_folder_path())