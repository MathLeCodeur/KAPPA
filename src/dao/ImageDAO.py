import Model as m


class ImageDAO(m.Model):
	def __init__(self, id, comment, lastUpdate, path, length, width, size, faceVectors, objectVectors):
		self.id = id
		self.comment = comment
		self.lastUpdate = lastUpdate
		self.path = path
		self.length = length
		self.width = width		
		self.size = size
		self.faceVectors = faceVectors
		self.objectVectors = objectVectors