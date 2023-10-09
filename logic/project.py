import sqlite3

def load_projects(db_file):
	"""
		Parameters:
		- db_file: database file
		- status:  you want to load projects of this status
	"""
	connection = sqlite3.connect(db_file)
	cursor = connection.cursor()
	projects = {"active": [], "inactive": []}
	try:
		cursor.execute("""SELECT * FROM projects""")
		rows = cursor.fetchall()

		for row in rows:
			print(f"Row 1: {row[1]}\nRow 2: {row[2]}\nRow 3: {row[3]}\nRow 4: {row[4]}")
			print(f"Row 5: {row[5]}\nRow 6: {row[6]}\nRow 7: {row[7]}\nRow 8: {row[8]}")
			print(f"Row 9: {row[9]}")
			_ = Project(
				row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], None, row[9]
			)
			print(f"_ Rate: {_.hourly_rate}")
	except sqlite3.Error as e:
		print(e)
	finally:
		connection.close()
	return projects

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

class Project:

	def __init__(self, project, hourly_rate, status, hours,current_project, created_at, finished_at, notes, customer_id):
		self.name = name
		self.hourly_rate = hourly_rate
		self.status = status
		self.total_hours = hours
		self.current_project = current_project
		self.create_date = create_date
		self.finish_date = finish_date
		self.notes = notes
		self.customer = customer

	def set_current(self):
		pass


	def load_notes(db_file):

		pass


