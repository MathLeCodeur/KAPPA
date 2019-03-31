import VectorModel as vm


class ObjectVectorDAO(vm.VectorDAO):
	def __init__(self, id, value, tagName="", parent=""):        
		super().__init__(self, id, value, tagName, parent)