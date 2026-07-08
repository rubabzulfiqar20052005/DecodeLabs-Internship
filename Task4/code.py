import cv2
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_path = "test.png"

image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)

thresh = cv2.adaptiveThreshold(
    blurred, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    31, 10
)

custom_config = r'--oem 3 --psm 6'
data = pytesseract.image_to_data(thresh, config=custom_config, output_type=Output.DICT)

extracted_words = []
confidence_threshold = 80

for i in range(len(data['text'])):
    word = data['text'][i].strip()
    conf = int(data['conf'][i])

    if word != "" and conf >= confidence_threshold:
        extracted_words.append((word, conf))

final_text = " ".join([w[0] for w in extracted_words])

print("Recognized Text (confidence >= 80%):")
print(final_text)
print()
print("Word-by-word breakdown:")
for word, conf in extracted_words:
    print(f"{word} — {conf}%")

cv2.imwrite("processed_output.png", thresh)