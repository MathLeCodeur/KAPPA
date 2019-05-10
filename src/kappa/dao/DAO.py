from kappa.dao.ConnectionManager import ConnectionManager

class DAO:
	def __init__(self):
		self.connectionManager = ConnectionManager("KappaBase")
