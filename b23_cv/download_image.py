# simply download image
import os
from urllib.parse import urlparse

import requests


def download_image(img_link, folder):
    try:
        response = requests.get(img_link)
        if response.status_code == 200:
            img_name = os.path.basename(urlparse(img_link).path)
            img_path = os.path.join(folder, img_name)
            with open(img_path, 'wb') as f:
                f.write(response.content)
            return img_path
        return None
    except requests.exceptions.RequestException as e:
        print("Image download failed, due to: \n", e)
