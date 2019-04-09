import ConnectionManager as cm

class DAO:
	def __init__(self):
		self.connectionManager = cm.ConnectionManager("KappaBase")
