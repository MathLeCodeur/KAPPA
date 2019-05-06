import kappa.models.Model as m


class ImageModel(m.Model):
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
