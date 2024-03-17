import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'<path_to_tesseract_executable>'

def ocr(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray_image)
    return text
  
image_path = '<path_to_image>'
result = ocr(image_path)
print(result)
