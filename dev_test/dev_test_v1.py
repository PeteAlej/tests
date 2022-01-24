# dev_test_v1

import fnmatch
import os, shutil
import pandas
import time
import keyboard
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import openpyxl as xl

dir = os.path.dirname(__file__)
xls_path = os.path.join(dir,'Processed\\')

# Cambiar los paths para hacer pruebas en otras computadoras
src_path = r"C:/Users/Peter/Documents/GitHub/tests/dev_test/"					# Directorio donde se van a "crear" los archivos
#xls_path = r"C:/Users/Peter/Documents/GitHub/tests/dev_test/Processed/"			# Directorio donde se van a mover los archivos .xls*
nonxls_path = r"C:/Users/Peter/Documents/GitHub/tests/dev_test/Not_applicable/"	# Directorio donde se van a mover los archivos != .xls*
directory = "."

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
						# -------------- Copiando valores de celda de un workbook a otro -------------
						src_wb = xl.load_workbook(src_path+file)
						src_sheet_num = len(src_wb.sheetnames)
						dest_wb = xl.load_workbook(src_path+"Master.xlsx")
						dest_sheet_num = len(dest_wb.sheetnames)
						print("sheet_num: "+ str(src_sheet_num))
						print("dest_sheet_num: "+ str(dest_sheet_num))
						current_sheet = 0
						while current_sheet < src_sheet_num:
							src_ws = src_wb.worksheets[current_sheet]
							dest_ws = dest_wb.worksheets[dest_sheet_num-1]
							src_rows = src_ws.max_row
							src_cols = src_ws.max_column
							for i in range(1, src_rows + 1):
								for j in range(1, src_cols + 1):
									cells = src_ws.cell(row = i, column = j)
									dest_ws.cell(row = i, column = j).value = cells.value
							dest_sheet_num = dest_sheet_num + 1
							dest_wb.create_sheet("Sheet"+str(dest_sheet_num))
							current_sheet = current_sheet + 1
						dest_wb.save(str(src_path+"Master.xlsx"))
						# ----------------------------------------------------------------------------
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