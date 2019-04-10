import kappa.models.Model as m


class VectorModel(m.Model):
	def __init__(self, id, value, tagName, parent):
		self.id = id
		self.value = value
		self.tagName = tagName
		self.parent = parent
