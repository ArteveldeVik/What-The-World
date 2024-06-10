import cv2
from ultralytics import YOLO
from helpers import predict_and_detect
from CommentatorAgent import generate_conversation
from creativeAgent import generate_art

# Load the model
model = YOLO('./datasets/runs/detect/train/weights/best.pt')

# Open the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Read the frame
    ret, frame = cap.read()
    if ret:
        # Predict and detect
        result_img, webcam_objects = predict_and_detect(model, frame, classes=[], conf=0.2)
        # Display the image
        cv2.imshow('Webcam', result_img)

        # Display the webcam objects (person, car, etc.)
        print(webcam_objects)

        #Process the frame
        def process_frame(objects):
            scene_description = generate_conversation(objects)
            print(scene_description)
            if scene_description:
                generate_art(scene_description)
        
        process_frame(webcam_objects)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
