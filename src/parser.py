''' Script for handling the parsing of a web page '''
import io
import requests
import PIL.Image
import matplotlib.pyplot as plt

from typing import List
from bs4 import BeautifulSoup
from sqlite3 import Cursor, Connection

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

    def imgs_to_db(self, sql_connection: Connection, sql_cursor: Cursor, img_urls: List[str]) -> None:
        """ Pulls image pixel data & saves to db.
        Args:
            sql_connection: Maintain connection to db
            sql_cursor: Used to execute sql.
            img_urls: List of image urls .

        Returns:

        """
        sql_cursor.execute("""
                CREATE TABLE IF NOT EXISTS images (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                page_url TEXT NOT NULL,
                image BLOB NOT NULL
                )
            """)
        for img in img_urls:
            try:
                img_data = requests.get(img).content
                sql_cursor.execute("INSERT INTO images (page_url, image) VALUES (?, ?)", (img, img_data))
            except Exception as e:
                print(f"Failed to download image {img}: {e}")

        sql_connection.commit()

    def read_img_from_db(self,sql_cursor: Cursor, img_id: int) -> None:
        sql_cursor.execute("SELECT image FROM images WHERE id=?", (img_id,))
        row = sql_cursor.fetchone()
        if row:
            img_bytes = row[0]
            img = PIL.Image.open(io.BytesIO(img_bytes))
            plt.imshow(img)
            plt.axis("off")
            plt.show()