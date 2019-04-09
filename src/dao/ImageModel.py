import Model as m


class ImageModel(m.Model):
	def __init__(self, id, comment, lastUpdate, length, width, size,path, faceVectors, objectVectors):
		self.id = id
		self.comment = comment
		self.lastUpdate = lastUpdate
		self.path = path
		self.length = length
		self.width = width		
		self.size = size
		self.faceVectors = faceVectors
		self.objectVectors = objectVectors
