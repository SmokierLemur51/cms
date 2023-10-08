
class Project:

	def __init__(self, name, current_project, total_hours, last_worked_on, hourly_rate, create_date, finish_date, status, notes, customer):
		self.name = name
		self.current_project = current_project
		self.total_hours = total_hours
		self.hourly_rate = hourly_rate
		self.last_worked_on = last_worked_on
		self.create_date = create_date
		self.finish_date = finish_date
		self.status = status
		self.notes = notes
		self.customer = customer

	def set_current(self):
		pass


