import pytesseract
from PIL import Image

# Path to the Tesseract executable (change it according to your installation)
pytesseract.pytesseract.tesseract_cmd = r"C:/Users/aksha/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"

# Path to your image file
image_path = "C:/Users/aksha/OneDrive/Desktop/IMG_4139_00236.jpg"

# Open the image using PIL (Python Imaging Library)
image = Image.open(image_path)

# Use Tesseract to recognize text from the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)

