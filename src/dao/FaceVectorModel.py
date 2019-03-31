import VectorModel as m


class FaceVectorModel(m.VectorModel):
	def __init__(self, id, value, tagName, parent, isKnown):        
		super().__init__(self, id, value, tagName, parent)
		self.isKnown = isKnown