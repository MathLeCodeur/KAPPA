import face_recognition
import numpy as np

# Inputs :
# peopleInformations : List including name and vectorial information about a picture of a person ["Name",[vector]]
# facePositions : List of positions where faces were recognized [[x1,x2,y1,y2],[x1,x2,y1,y2],...]
# imagePath : Path of the image "/image/picture.jpg

# Outputs :
# List including :
# - name of the different recognized persons in the same order as the input positions list ['Bob','Unknown','Carl']
# Output will be unknown if a person isn't recognized
# The output have to be linked with the facePositions to understand who was recognized

def recognizePeople(peopleInformation, facePositions, imagePath):
	outputList = []
	unknownImage = face_recognition.load_image_file(imagePath)
	for i in range(len(facePositions)):
		#Crop in the big picture to face of every person and compute if they can be recognized
		currentPersonPicture = unknownImage[facePositions[i][2]:facePositions[i][3],
							facePositions[i][0]:facePositions[i][1]]
		print(type(currentPersonPicture))
		unknownEncoding = face_recognition.face_encodings(currentPersonPicture)
		peopleName = "Unknown"
		for j in range(len(peopleInformation)):
			if face_recognition.compare_faces(peopleInformation[j][1], unknownEncoding)[0] == True:
				peopleName = peopleInformation[j][0]
		outputList.append(peopleName)
	return outputList
