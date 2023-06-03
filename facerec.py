# import face_recognition
# import cv2
# import os
# import numpy as np
# import datetime
# import pandas as pd

# def mark_attendance(name):
#     # Create new Excel file if one does not exist
#     if not os.path.isfile('attendance.xlsx'):
#         df = pd.DataFrame(columns=['Name', 'Time'])
#     else:
#         # Otherwise, load existing Excel file
#         df = pd.read_excel('attendance.xlsx')

#     # Add new row to the DataFrame
#     now = datetime.datetime.now()
#     new_row = pd.DataFrame({'Name': [name], 'Time': [now]})
#     df = pd.concat([df, new_row], ignore_index=True)

#     # Save Excel file
#     df.to_excel('attendance.xlsx', index=False)
#     print(f"Attendance created for {name}")

# # Load known faces and names from "known_faces" directory
# known_face_encodings = []
# known_face_names = []
# for filename in os.listdir("/Users/vaiebhavchettri/Documents/gui/known_faces"):
#     if filename.endswith(".jpg") or filename.endswith(".png"):
#         image = face_recognition.load_image_file("known_faces/" + filename)
#         face_encoding = face_recognition.face_encodings(image)[0]
#         known_face_encodings.append(face_encoding)
#         known_face_names.append(os.path.splitext(filename)[0])

# # Initialize webcam
# video_capture = cv2.VideoCapture(0)
# print("Capturing..")

# # Loop over frames from webcam
# while True:
#     # Capture frame
#     ret, frame = video_capture.read()

#     # Resize frame to 1/4 size for faster face detection
#     small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

#     # Detect faces in the frame
#     face_locations = face_recognition.face_locations(small_frame)
#     face_encodings = face_recognition.face_encodings(small_frame, face_locations)

#     # Recognize faces
#     face_names = []
#     for face_encoding in face_encodings:
#         # Compare face encoding with known faces
#         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#         name = "Unknown"

#         # Find best match
#         face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
#         best_match_index = np.argmin(face_distances)
#         if matches[best_match_index]:
#             name = known_face_names[best_match_index]

#         face_names.append(name)

#     # Draw rectangle and label for each detected face
#     for (top, right, bottom, left), name in zip(face_locations, face_names):
#         # Scale up face locations since we resized frame to 1/4 size
#         top *= 4
#         right *= 4
#         bottom *= 4
#         left *= 4

#         # Draw rectangle around face
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

#         # Draw label below face
#         cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
#         font = cv2.FONT_HERSHEY_DUPLEX
#         cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

#         # Mark attendance if face is recognized
#         if name != "Unknown":
#             print("Captured")
#             print(name)
#             # Release webcam and close window
#             video_capture.release()
#             cv2.destroyAllWindows()
#             quit()

#     # Display resulting frame
#     cv2.imshow('Video', frame)

#     # Exit loop if 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# #Release webcam and close window
# video_capture.release()
# cv2.destroyAllWindows()






import face_recognition
import cv2
import os
import numpy as np

def recognize_faces():
    # Load known faces and names from "known_faces" directory
    known_face_encodings = []
    known_face_names = []
    for filename in os.listdir("/Users/vaiebhavchettri/Documents/gui/known_faces"):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image = face_recognition.load_image_file("known_faces/" + filename)
            face_encoding = face_recognition.face_encodings(image)[0]
            known_face_encodings.append(face_encoding)
            known_face_names.append(os.path.splitext(filename)[0])

    # Initialize webcam
    video_capture = cv2.VideoCapture(0)
    print("Capturing..")

    # Loop over frames from webcam
    while True:
        # Capture frame
        ret, frame = video_capture.read()

        # Resize frame to 1/4 size for faster face detection
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Detect faces in the frame
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)

        # Recognize faces
        face_names = []
        for face_encoding in face_encodings:
            # Compare face encoding with known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # Find best match
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

        # Draw rectangle and label for each detected face
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale up face locations since we resized frame to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw rectangle around face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw label below face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # Mark attendance if face is recognized
            if name != "Unknown":
                print("Captured")
                # Release webcam and close window
                video_capture.release()
                cv2.destroyAllWindows()
                return name
                # print(name)

        # Display resulting frame
        cv2.imshow('Video', frame)

        # Exit loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    #Release webcam and close window
    video_capture.release()
    cv2.destroyAllWindows()
