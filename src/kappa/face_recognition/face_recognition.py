from face_recognition import compare_faces, face_encodings


# Inputs :
# peopleInformations : List including name and vectorial information about a picture of a person ["Name",[vector]]
# facePositions : List of positions where faces were recognized [[x1,x2,y1,y2],[x1,x2,y1,y2],...]
# imageMatrix : Numpy image array

# Outputs :
# List including :
# - name of the different recognized persons in the same order as the input positions list ['Bob','Unknown','Carl']
# Output will be unknown if a person isn't recognized
# The output have to be linked with the facePositions to understand who was recognized

def recognizePeople(peopleInformation, facePositions, imageMatrix):
	recognizedNames = []
	recognizedVectorIndices = []
	unknownEncodings = face_encodings(imageMatrix, known_face_locations=facePositions)
	print(peopleInformation)

	for i in range(len(unknownEncodings)):
		for j in range(len(peopleInformation)):
			comparisonResult = compare_faces([unknownEncodings[i]], peopleInformation[j][1])
			if comparisonResult and comparisonResult[0] == True:
				recognizedNames.append(peopleInformation[j][0])
				recognizedVectorIndices.append(j)
				break
		else:
			recognizedNames.append("Unknown")
			recognizedVectorIndices.append(None)
	return recognizedNames, recognizedVectorIndices
