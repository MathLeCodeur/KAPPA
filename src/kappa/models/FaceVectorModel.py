from kappa.models.VectorModel import VectorModel


class FaceVectorModel(VectorModel):
	def __init__(self, id, value, tagName, isKnown):
		super().__init__( id, value, tagName)
		self.isKnown = isKnown
