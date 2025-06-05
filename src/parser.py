''' Script for handling the parsing of a web page '''

import requests

from bs4 import BeautifulSoup
from typing import List

class ImageGrab:
    def __init__(self,) -> None:
        """ Init class attributes"""
        pass  # TBD
    
    def grab_image_elements(self, page: str) -> List[str]: 
        """ Pulls images from web page html.
        
        Args: 
            page: the web page url
        
        Returns:
            List of image urls
        
        
        """
        response = requests.get(page)
        html_content = BeautifulSoup(response.text, "html.parser")
        all_imgs = html_content.find_all("img")
        img_storage = []
        nono_words = ["logo", "icon", "social", "instagram", "linkedin", "collage", "mobile"]
        for img_tag in all_imgs: 
            media_link = img_tag['src']
            if not any(word in media_link.lower() for word in nono_words):
                img_storage.append(media_link)
        
        return img_storage
    
    
        
        