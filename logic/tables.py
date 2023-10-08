import sqlite3

"""

"""


def create_setup_tables(db_file):
	"""
		Parameters:
		- db_file: database file
		Example Usage:
		- create_projects_table("test.db") This is not necessary
	"""
	connection = sqlite3.connect(db_file)
	cursor = connection.cursor()
	try:
		# projects table
		cursor.execute("""CREATE TABLE IF NOT EXISTS projects (
			id INTEGER PRIMARY KEY,
			project TEXT NOT NULL,
			current_project BOOL,
			hours REAL,
			hourly_rate REAL,
			last_worked_on DATE,
			created_at DATE,
			finished_at DATE,
			status TEXT,
			notes INTEGER,
			customer_id INTEGER,
			FOREIGN KEY (notes) REFERENCES notes(id),
			FOREIGN KEY (customer_id) REFERENCES customers(id)
		);""")
		# notes table 
		cursor.execute("""CREATE TABLE IF NOT EXISTS notes (
			id INTEGER PRIMARY KEY,
			project_id INTEGER,
			title TEXT,
			content TEXT,
			FOREIGN KEY (project_id) REFERENCES projects(id),
		);""")
		# customer table
		cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
			id INTEGER PRIMARY KEY,
			name TEXT,
			project_ids INTEGER,
			contact_info INTEGER,
			FOREIGN KEY (project_ids) REFERENCES projects(id),
			FOREIGN KEY (contact_info) REFERENCES contacts(id)
		);""")
		cursor.execute("""CREATE TABLE IF NOT EXISTS contacts (
			id INTEGER PRIMARY KEY,
			name TEXT,
			phone_number TEXT,
			email TEXT
		);""")
		print("Created tables successfully.")
		connection.commit()
	except sqlite3.Error as e:
		print(e)
	finally:
		connection.close()

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

def insert_project(db_file, project):
	connection = sqlite3.connect(db_file)
	cursor = connection.cursor()
	try:
		cursor.execute("""INSERT INTO projects (
	    project, current_project, hours, hourly_rate,
	    last_worked_on, created_at, finished_at, status,
	    notes, customer_id)
	    VALUES (?, ?, ?, ?, ?, ?, NULL, ?, NULL, ?)
		""", (
		project.name, project.current_project, project.total_hours,
		project.hourly_rate, project.last_worked_on, project.create_date,
		project.status, project.customer
		))
		print("successfully inserted project")
		connection.commit()
	except sqlite3.Error as e:
		print(e)
	finally:
		connection.close()

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

def load_projects(db_file, status):
	"""
		Parameters:
		- db_file: database file
		- status:  you want to load projects of this status
	"""
	projects = []

	return projects


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
def create_table(db_file, table_name, columns):
    """
        Paramters:
        - db_file: The database file to connect to.
        - table_name: The name of the table to be created.
        - columns:  List of column definitions, where each column definition is a tuple
                    containing (column_name, data_type)

        Example Usage:
        - create_table("countyfair.db", "prize_hog", [("id", "INTEGER PRIMARY KEY AUTOINCREMENT"), ("name", "TEXT"), ("age", "INTEGER")])
    """
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    createTableSQL = f"CREATE TABLE IF NOT EXISTS {table_name} ("

    for column in columns:
        column_name, data_type = column
        createTableSQL += f"{column_name} {data_type}, "

    createTableSQL = createTableSQL.rstrip(", ")
    createTableSQL += ");"

    try:
        cursor.execute(createTableSQL)
        print(f"\t*\tTable {table_name} created successfully.")
        connection.commit()

    except sqlite3.Error as e:
        print(f"Error creating table {table_name}: {e}")

    finally:
        connection.close()