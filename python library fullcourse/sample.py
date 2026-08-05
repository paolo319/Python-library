import cv2
import re
import pytesseract
from pytesseract import Output

# --- UNCOMMENT & ADJUST FOR WINDOWS IF NEEDED ---
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open webcam
cap = cv2.VideoCapture(0)

# Exact pattern for Student ID: 2 digits - 4 digits - 6 digits
# (e.g., 12-3456-789012 or with spaces/dashes)
pattern = r'\b(\d{2})[\s\-]*(\d{4})[\s\-]*(\d{6})\b'

# Tesseract configuration: Whitelist digits and hyphens/spaces
tess_config = r'--psm 6 -c tessedit_char_whitelist=0123456789- '

print("Tesseract OCR active. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret: 
        break

    # Convert to grayscale for better Tesseract reading
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Get OCR detection data dictionary (includes text, confidence, and coordinates)
    data = pytesseract.image_to_data(gray, config=tess_config, output_type=Output.DICT)

    # Reconstruct text line to match regex pattern
    full_text = " ".join([text for text in data['text'] if text.strip()])
    matches = re.findall(pattern, full_text)

    if matches:
        p1, p2, p3 = matches[0]
        formatted_id = f"{p1}-{p2}-{p3}"

        # Loop through detected word blocks to find and draw the bounding box
        n_boxes = len(data['text'])
        for i in range(n_boxes):
            text_item = data['text'][i].strip()
            raw_conf = data['conf'][i]

            try:
                confidence = float(raw_conf)
            except (ValueError, TypeError):
                confidence = 0.0

            # Match bounding box corresponding to parts of the detected ID
            if confidence > 30 and (p1 in text_item or p2 in text_item or p3 in text_item):
                x = data['left'][i]
                y = data['top'][i]
                w = data['width'][i]
                h = data['height'][i]

                pt1 = (x, y)
                pt2 = (x + w, y + h)

                print(f"[Detected Student ID]: {formatted_id} (Confidence: {confidence/100:.2f})")

                # Draw green bounding box around detected text
                cv2.rectangle(frame, pt1, pt2, (0, 255, 0), 2)
                cv2.putText(
                    frame, 
                    formatted_id, 
                    (pt1[0], max(20, pt1[1] - 10)), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    0.8, 
                    (0, 255, 0), 
                    2
                )
                break  # Draw once per matched ID instance

    cv2.imshow("Student ID Detector (Tesseract)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()