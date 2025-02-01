import os

def file_exists(file_path):
    return os.path.isfile(file_path)

def log(message):
    with open("log.txt", "a") as log_file:
        log_file.write(message + "\n")
