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
		imageHeight, imageWidth, _ = unknownImage.shape

		currentPersonPicture = unknownImage[int(round(facePositions[i][2] * imageHeight)) : int(round(facePositions[i][3] * imageWidth)),
							int(round(facePositions[i][0]) * imageHeight) : int(round(facePositions[i][1] * imageWidth))]
		# currentPersonPicture = unknownImage[int(round(facePositions[i][0] * imageHeight)) : int(round(facePositions[i][2] * imageHeight)),
        #                 int(round(facePositions[i][1] * imageWidth)) : int(round(facePositions[i][3] * imageWidth))]

		unknownEncoding = face_recognition.face_encodings(currentPersonPicture)
		peopleName = "Unknown"
		for j in range(len(peopleInformation)):
			if face_recognition.compare_faces(peopleInformation[j][1], unknownEncoding)[0] == True:
				peopleName = peopleInformation[j][0]
		outputList.append(peopleName)
	return outputList
