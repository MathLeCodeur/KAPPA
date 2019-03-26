import ConnectionManager

def main():
	y = ConnectionManager.ConnectionManager('../KappaBase.db')
	print(y.instance.connection)

	#Select
	rows = y.executeSQL('select * from Image');
	for row in rows:
		print(row)
	#y.executeAndCommitSQL("Insert into Image (id_image) values (3)")

if __name__ == "__main__":
    main()
