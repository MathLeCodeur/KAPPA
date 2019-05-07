from kappa.models.VectorModel import VectorModel


class ObjectVectorModel(VectorModel):
	def __init__(self, id, value, tagName, parent):        
		super().__init__(id, value, tagName)
		self.parent = parent