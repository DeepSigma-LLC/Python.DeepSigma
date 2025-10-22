from PIL import Image, ImageOps, ImageEnhance
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Users\brend\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


class ImageToText:

    @staticmethod
    def image_to_text(image_path: str) -> str:
        """
        Extracts text from an image file.
        :param image_path:
        :return: text
        """

        image = Image.open(image_path)
        image = ImageToText.__convert_image(image)
        text = pytesseract.image_to_string(image)
        return text

    @staticmethod
    def __convert_image(image: Image) -> Image:
        """
        Converts image to preferred formate for text extraction.
        :param image:
        :return: Re-formatted Image.
        """
        image = image.convert('L')  # monochromatic
        contrast = ImageEnhance.Contrast(image)
        image = contrast.enhance(2)
        image = image.rotate(-90, expand=True)
        return image

