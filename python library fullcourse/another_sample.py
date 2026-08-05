import cv2
import re
from rapidocr_onnxruntime import RapidOCR

# Initialize RapidOCR engine
engine = RapidOCR()

# Open webcam
cap = cv2.VideoCapture(0)

# Exact pattern for Student ID: 2 digits - 4 digits - 6 digits
# (e.g., 12-3456-789012 or with spaces/dashes)
pattern = r'\b(\d{2})[\s\-]*(\d{4})[\s\-]*(\d{6})\b'

print("RapidOCR active. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret: 
        break

    # RapidOCR handles raw color images directly
    result, _ = engine(frame)

    if result:
        for item in result:
            text = item[1]         # Detected text string
            raw_conf = item[2]     # Confidence score
            
            # Convert confidence to float safely
            try:
                confidence = float(raw_conf)
            except (ValueError, TypeError):
                confidence = 0.0

            # Search for the target ID format
            matches = re.findall(pattern, text)
            if matches and confidence > 0.4:
                p1, p2, p3 = matches[0]
                formatted_id = f"{p1}-{p2}-{p3}"
                
                print(f"[Detected Student ID]: {formatted_id} (Confidence: {confidence:.2f})")

                # Draw green bounding box around detected text
                box = item[0]
                pt1 = (int(box[0][0]), int(box[0][1]))
                pt2 = (int(box[2][0]), int(box[2][1]))
                
                cv2.rectangle(frame, pt1, pt2, (0, 255, 0), 2)
                cv2.putText(
                    frame, 
                    formatted_id, 
                    (pt1[0], pt1[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    0.8, 
                    (0, 255, 0), 
                    2
                )

    cv2.imshow("Student ID Detector (RapidOCR)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()