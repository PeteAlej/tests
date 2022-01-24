# dev_test_v1

import pandas
import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler

directory = "."


class watcher:			# Inicialización de la clase "watcher", la cual establece las instancias con los argumentos ingresados.
	def __init__(self, directory = directory, handler = FileSystemEventHandler()):		# Argumentos:
		self.observer = Observer() # Clase propia del watchdog para monitorear.		# 1. Directorio a monitorear.
		self.directory = directory # Instancia del directorio.						# 2. El handler a utilizar en caso de cambios en el directorio.
		self.handler = handler     # Instancia del handler.

	def execute(self):
		self.observer.schedule(self.handler, self.directory, recursive = True) # Programar monitoreo utilizando instancias anteriores.
		self.observer.start()

class handler(FileSystemEventHandler):

	def on_any_event(self, event):
		if event = 


if __name__ == "__main__":	# Requerimiento, útil si se llega a importar a otro módulo.
	a = watcher()
	print(a.directory)




'''
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    '''