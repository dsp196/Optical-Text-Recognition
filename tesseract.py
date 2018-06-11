import pytesseract
from PIL import Image
img=Image.open('Capture.PNG')

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

result =  pytesseract.image_to_string(img)
with open('result.txt',mode='w') as file:
    file.write(result)
    print("See the text file ")
