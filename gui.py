import tkinter as tk

def populate_projects(projects):
	"""
		Parameters:
		- projects: Dictionary, {"active": [], "inactive": []}
	"""


def last_project(projects):


def create_app(last_project):
	app = tk.Tk()
	app.geometry("600x300")
	app.title(f"TimeClock - Project - {last_project.name}")
	
	return app