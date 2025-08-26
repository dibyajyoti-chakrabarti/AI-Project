import os
import cv2
import time
import uuid

IMAGE_PATH = r"C:\Disc D\[VIT Uni]\Projects\AI\AI-Project\CollectedImages"

labels = [
    'HELLO', 'GOOD', 'MORNING', 'AFTERNOON', 'EVENING', 'GOODBYE',
    'WHAT', 'NAME', 'MY', 'ME', 'NICE', 'MEET', 'WHERE', 'FROM',
    'HOW', 'YOU', 'FINE', 'PLEASE', 'THANK', 'SORRY',
    'UNDERSTAND', 'NOT', 'DONT', 'REPEAT', 'AGAIN', 'SLOW', 'SHOW',
    'YES', 'NO', 'HELP', 'ASK', 'QUESTION', 'WANT', 'WATER', 'HUNGRY',
    'THIRSTY', 'LIKE', 'DONT_LIKE'
]

number_of_images = 25

for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path, exist_ok=True)
    cap = cv2.VideoCapture(0)
    print(f'Collecting images for {label}')
    time.sleep(5)
    for imgnum in range(number_of_images):
        ret, frame = cap.read()
        imagename = os.path.join(img_path, f'{label}.{str(uuid.uuid1())}.jpg')
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(3)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
