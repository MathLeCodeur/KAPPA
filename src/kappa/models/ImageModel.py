from kappa.models.Model import Model

class ImageModel(Model):
	def __init__(self, id, comment, creation_date, length, width, size,path, faceVectors, objectVectors):
		self.id = id
		self.comment = comment
		self.creation_date = creation_date
		self.path = path
		self.length = length
		self.width = width
		self.size = size
		self.faceVectors = faceVectors
		self.objectVectors = objectVectors

	def getObjectVectorsWithTheirMommiesAndDaddies(self) :
		tagList = []
		for v in self.objectVectors:
			tagList.append(v.getObjectVectorWithItsMommiesAndDaddies())
		return tagList
