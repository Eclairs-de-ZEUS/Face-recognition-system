import cv2
import face_recognition
import os
import numpy as np
from print_data import *
from handle_attendance import *
from voice_handler.voice_assistant import *
from horoscope.horoscope import *

def get_data(database_path: str) -> list and list:
    """ Function that takes data and labelise it """
    path = database_path
    images = []
    class_names = []
    horos = []
    mylist = os.listdir(path)

    for cl in mylist:
        img_path = path + cl
        cur_img = cv2.imread(img_path)
        images.append(cur_img)

        interm = cl.split('.')
        interm2 = interm[0].split('_')
        class_names.append(interm2[0])
        sign = detect_sign(int(interm2[1]), int(interm2[2]))
        horos.append(horoscope(sign))

        class_names.append((cl.split('.'))[0])


    return images, class_names, horos

def find_encodings(images: list) -> list:
    """ Function that runs training on data """
    encode_list = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoded_face = face_recognition.face_encodings(img)[0]
        encode_list.append(encoded_face)
    return (encode_list)

def face_rec(database_path: str) -> None:
    """ Main function for facial recognition app"""
    images, class_names, horos = get_data(database_path)
    encoded_face_train = find_encodings(images)

    print_info("Facial recognition system started")

    # start camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print_error("Can't open camera")
    while True:
        success, img = cap.read()
        if not success:
            print_error("Can't receive frame (stream end?). Existing ...")

        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        faces_in_frame = face_recognition.face_locations(imgS)
        encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)

        # Loop through image
        for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
            matches = face_recognition.compare_faces(encoded_face_train, encode_face)
            face_dist = face_recognition.face_distance(encoded_face_train, encode_face)
            match_index = np.argmin(face_dist)

            # Find the appropriate label for the image
            if matches[match_index]:
                name = class_names[match_index].upper().lower()
                scop = horos[match_index].upper().lower()

                y1,x2,y2,x1 = faceloc
                y1, x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img, (x1,y2-35),(x2,y2), (0,255,0), cv2.FILLED)
                cv2.putText(img,name, (x1+6,y2-5), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                mark_attendance(name)
                voice_assistant(name, scop)


        cv2.imshow('webcam', img)
        if cv2.waitKey(1) == ord('q'):
            break

    # Close camera
    cap.release()
    cv2.destroyAllWindows()
    print_info("Facial recognition system ended")


if __name__ == "__main__":
    face_rec('./images_db/')
