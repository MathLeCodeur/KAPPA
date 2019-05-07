import sqlite3
import context
class ConnectionManager:
	class ConnectionDB:
		def __init__(self,severName):
			self.connection = sqlite3.connect("./res/database/KappaBase.db")

		def __str__(self):
			return 'ConnectionManager'

		def executeSQL(self,sql):
			cur = self.connection.cursor()
			cur.execute(sql)
			rows = cur.fetchall()
			return rows

		def executeAndCommitSQL(self,sql):
			cur = self.connection.cursor()
			cur.execute(sql)
			self.connection.commit()

		def closeConnection(self):
			self.connection.close()

	instance = None
	def __new__(self, serverName):
		if not ConnectionManager.instance:
			ConnectionManager.instance = ConnectionManager.ConnectionDB(serverName)
		return ConnectionManager

	def executeSQL(sql):
		return ConnectionManager.instance.executeSQL(sql)

	def executeAndCommitSQL(sql):
		ConnectionManager.instance.executeAndCommitSQL(sql)

	def closeConnection():
		ConnectionManager.instance.closeConnection()
		ConnectionManager.instance = None
