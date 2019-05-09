from kappa.models.Model import Model

class VectorModel(Model):
	def __init__(self, id, value, tagName):
		self.id = id
		self.value = value
		self.tagName = tagName
