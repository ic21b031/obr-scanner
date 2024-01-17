import os
import time
from datetime import date

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess


# Define a class to watch a specific directory
class InputFolderWatcher:

    # Initialize the observer
    def __init__(self, watch_directory):
        self.observer = Observer()
        self.watch_directory = watch_directory

    # Run the observer
    def run(self):
        # Create an event handler
        event_handler = Handler()
        # Schedule the observer to watch the directory and its subdirectories
        self.observer.schedule(event_handler, self.watch_directory, recursive=True)
        # Start the observer
        self.observer.start()
        try:
            # Wait for changes in the directory
            while True:
                print('Waiting for change')
                time.sleep(5)
        except:
            # If an exception occurs, stop the observer
            self.observer.stop()
            print('Observer Stopped')

        # Wait until the observer has finished
        self.observer.join()


# Define a class to handle file system events
class Handler(FileSystemEventHandler):
    # Handle any event
    @staticmethod
    def on_any_event(event):
        # If the event is on a directory, ignore it
        if event.is_directory:
            return None
        # If the event is a file creation or modification
        elif event.event_type in ['created']:
            # Print the event details
            print(f'Watchdog received {event.event_type} event - {event.src_path}')
            # here we got a lock, because the scanner process uses this file
            # prefix = f'{date.today()}-'
            # suffix = '-example'
            # file_name = os.path.basename(event.src_path)
            # dir_name = os.path.dirname(event.src_path)
            # extension = os.path.splitext(file_name)[1]
            # file_name = f'{prefix}{os.path.splitext(file_name)[0]}{suffix}{extension}'
            # file = os.path.join(dir_name, file_name)
            # os.rename(event.src_path, file)
            # print(f'Rename file {event.src_path} to {event.src_path}')
            # Set the language
            language = 'EN'
            # This is the script from AngelinaReader
            # Edit the Path to run_local.py so the script can be found
            # Also the results folder path has to be changed, so it matches your results folder path
            os.system(f'python D:\\work\\AngelinaReader\\run_local.py -l {language} {event.src_path} '
                      f'"D:\\work\\AngelinaReader\\results"')


if __name__ == '__main__':
    scanner_exe_path = os.getenv("scanner_exe")
    if scanner_exe_path is None:
        raise Exception("scanner_exe environment variable does not exist")
    print("Start scanner software")
    process = subprocess.Popen([scanner_exe_path],
                               shell=True,
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               close_fds=True)

    watch = InputFolderWatcher('D:\\work\\AngelinaReader\\input')
    watch.run()
