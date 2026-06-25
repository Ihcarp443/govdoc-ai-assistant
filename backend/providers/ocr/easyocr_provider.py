import easyocr

class EasyOCRProvider:

    def __init__(self):
        self.reader = easyocr.Reader(
            ['en', 'hi'],
            gpu=False
        )

    def extract_text(self, image_path):

        result = self.reader.readtext(
            image_path,
            detail=0
        )

        return "\n".join(result)