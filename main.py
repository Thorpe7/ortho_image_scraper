''' Main function for container '''
from src.parser import ImageGrab
from src.sql_setup import setup_db


def main() -> None:
    """ Main function"""
    connection, cursor = setup_db()
    ImageCollector = ImageGrab()
    img_urls = ImageCollector.grab_image_elements(page="https://www.stryker.com/us/en/orthopaedic-instruments.html")
    ImageCollector.imgs_to_db(sql_connection=connection, sql_cursor=cursor, img_urls=img_urls)
    ImageCollector.read_img_from_db(sql_cursor=cursor, img_id=5)




if __name__ == "__main__":
    main()