from kappa.models.VectorModel import VectorModel


class ObjectVectorModel(VectorModel):
	def __init__(self, id, value, tagName, parent):        
		super().__init__(id, value, tagName)
		self.parent = parent

	
	def getObjectVectorWithItsMommiesAndDaddies(self):
		if (self.parent == None):
			return (self.tagName.split(","))[0]
		else :
			return self.parent.getObjectVectorWithItsMommiesAndDaddies() + "/" + (self.tagName.split(","))[0]