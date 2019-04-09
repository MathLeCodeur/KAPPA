import sqlite3

class ConnectionManager:
	class ConnectionDB:
		def __init__(self,severName):
			self.connection = sqlite3.connect("KappaBase.db")


		def __str__(self):
			return 'coucou'

		def executeSQL(self,sql):
			print('sql execute')
			cur = self.connection.cursor()
			cur.execute(sql)
			rows = cur.fetchall()
			return rows

		def executeAndCommitSQL(self,sql):
			print('sql excute and commit')
			cur = self.connection.cursor()
			cur.execute(sql)
			self.connection.commit()
	
		def closeConnection(self):

			print('sql close')
			self.connection.close()

	instance = None
	def __new__(self, serverName):
		if not ConnectionManager.instance:
			ConnectionManager.instance = ConnectionManager.ConnectionDB(serverName)
			print("new instance")
		return ConnectionManager

	def executeSQL(sql):
		return ConnectionManager.instance.executeSQL(sql)
	
	def executeAndCommitSQL(sql):
		ConnectionManager.instance.executeAndCommitSQL(sql)
	
	def closeConnection():
		ConnectionManager.instance.closeConnection()
		ConnectionManager.instance = None
		






