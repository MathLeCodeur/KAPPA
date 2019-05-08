import face_recognition
from kappa.face_recognition.face_recognition import recognizePeople

if __name__ == "__main__":
    known_image1 = face_recognition.load_image_file("/home/kappa/Bureau/Daniel Jouanin.jpg")
    known_name1 = "Daniel Jouanin"
    known_image2 = face_recognition.load_image_file("/home/kappa/Bureau/Clery Plassat.jpg")
    known_name3 = "Lucie Gartiser"
    known_image3 = face_recognition.load_image_file("/home/kappa/Bureau/Lucie Gartiser.jpg")
    known_name2 = "Clery Plassat"

    imagePath = "/home/kappa/Bureau/unknown13.jpg"

    known_encoding1 = face_recognition.face_encodings(known_image1)[0]
    known_encoding2 = face_recognition.face_encodings(known_image2)[0]
    known_encoding3 = face_recognition.face_encodings(known_image3)[0]
    knownPeople1 = [known_name1, known_encoding1]
    knownPeople2 = [known_name2, known_encoding2]
    knownPeople3 = [known_name3, known_encoding3]

    peopleInformation = [knownPeople1, knownPeople2, knownPeople3]
    facePositions = [[366,600,260,600]]

    print(recognizePeople(peopleInformation,facePositions,imagePath))
