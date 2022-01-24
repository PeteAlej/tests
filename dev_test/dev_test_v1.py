# dev_test_v1

import fnmatch
import os, shutil
import pandas
import time
import keyboard
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import openpyxl as xl

src_path = r"C:/Users/Peter/Documents/GitHub/tests/dev_test/"
xls_path = r"C:/Users/Peter/Documents/GitHub/tests/dev_test/Processed/"
nonxls_path = r"C:/Users/Peter/Documents/GitHub/tests/dev_test/Not_applicable/"
directory = "."# "C:/Users/Peter/Documents/GitHub/tests/dev_test"

class watcher:			# Inicialización de la clase "watcher", la cual establece las instancias con los argumentos ingresados.
	def __init__(self, directory = directory, handler = FileSystemEventHandler()):	# Argumentos:
		self.observer = Observer() # Clase propia del watchdog para monitorear.		# 1. Directorio a monitorear.
		self.directory = directory # Instancia del directorio.						# 2. El handler a utilizar en caso de cambios en el directorio.
		self.handler = handler     # Instancia del handler.

	def execute(self):
		self.observer.schedule(self.handler, self.directory, recursive = True) # Programar monitoreo utilizando instancias anteriores.
		self.observer.start()
		try:
			while True:
				time.sleep(1)
		except Exception:
			self.observer.stop()
		self.observer.join()

class myHandler(FileSystemEventHandler):
	def on_any_event(self, event):
		if event.event_type == "created":
			for file in os.listdir(directory):
				if fnmatch.fnmatch(file, "*.xls*"):
					if fnmatch.fnmatch(file, "Master.xls*"):
						pass
					else:
						print(file+" has been processed")
						shutil.move(src_path+file, xls_path+file)
				elif not fnmatch.fnmatch(file, "*.xls*"):
					if fnmatch.fnmatch(file, "*.py") or fnmatch.fnmatch(file, "Not_applicable") or fnmatch.fnmatch(file, "Processed"):
						pass
					else:
						print(file+" is not applicable")
						shutil.move(src_path+file, nonxls_path+file)
		#if event =

if __name__ == "__main__":	# Requerimiento, útil si se llega a importar a otro módulo.
	directory = input("Establish the directory to be watched: ")
	wt = watcher(directory, myHandler())
	wt.execute()