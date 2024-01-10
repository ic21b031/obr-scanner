import os
import subprocess

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
