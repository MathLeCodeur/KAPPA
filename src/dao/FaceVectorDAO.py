import VectorModel as vm


class FaceVectorDAO(vm.VectorDAO):
	def __init__(self, id, value, tagName, parent, isKnown):        
		super().__init__(self, id, value, tagName, parent)
		self.isKnown = isKnown