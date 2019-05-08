import kappa.models.Model as m


class VectorModel(m.Model):
	def __init__(self, id, value, tagName):
		self.id = id
		self.value = value
		self.tagName = tagName
