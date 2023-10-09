from datetime import datetime
# import gui
import logic

# CONSTANTS
DB_FILE = "test.db"


riviera = logic.Project("La Riviera Maya Restaurant", True, 2.00, datetime.now().strftime("%Y-%m-%d"), 40.00, datetime.now().strftime("%Y-%m-%d"), None, False, None, None)
print(f"Riviera Rate: {riviera.customer}")
logic.create_setup_tables(DB_FILE)
hpaint = logic.Project("Higganbotham Paint", True, 10.00, datetime.now().strftime("%Y-%m-%d"), 30, datetime.now().strftime("%Y-%m-%d"), None, False, None, None)
print(f"Higganbotham Rate: {hpaint.hourly_rate}")
logic.insert_project(riviera)
logic.insert_project(hpaint)

test = logic.load_projects(DB_FILE)

test[""]

# app = gui.create_app(riviera)

# app.mainloop()




# "La Riviera Maya Restaurant", True, 2.00, datetime.now().strftime("%Y-%m-%d"), 40.00, datetime.now().strftime("%Y-%m-%d"), None, False, None, None)
# row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], None, row[9]