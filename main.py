''' Main function for container '''
from src.parser import ImageGrab


def main() -> None:
    """ Main function"""
    ImageCollector = ImageGrab()
    ImageCollector.grab_image_elements(page="https://www.stryker.com/us/en/orthopaedic-instruments.html")




if __name__ == "__main__": 
    main()