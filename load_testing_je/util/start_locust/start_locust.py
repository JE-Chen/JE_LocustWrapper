import subprocess
import os


def change_to_locust_file_dir(path):
    os.chdir(path)


def start_locust():
    global process
    process = subprocess.Popen(["locust"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
    return process


def stop_locust(stop_process):
    stop_process.terminate()

