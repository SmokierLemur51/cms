from datetime import datetime
import gui
import logic

# CONSTANTS
DB_FILE = "test.db"


riviera = logic.Project("La Riviera Maya Restaurant", True, 2.00, datetime.now().strftime("%Y-%m-%d"), 40.00, datetime.now().strftime("%Y-%m-%d"), None, False, None, None)

# logic.insert_project(DB_FILE, riviera)


app = gui.create_app(riviera)

app.mainloop()

