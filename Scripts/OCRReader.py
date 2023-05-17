import pytesseract
from PIL import Image

def ocr_reader(img_path):
    # Görüntüyü aç
    img = Image.open(img_path)

    # OCR işlemi yap
    text = pytesseract.image_to_string(img)

    # Metni döndür
    return text
