import tkinter as tk





def create_app(last_project):
	app = tk.Tk()
	app.geometry("600x300")
	app.title(f"TimeClock - Project - {last_project.codename}")
	
	return app