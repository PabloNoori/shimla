import os
import platform

def check_root():
    user = os.getenv("SUDO_USER")
    if user is None:
        return False
    else:
        return True


def is_linux():
    get_os =  platform.system().lower()
    if get_os == 'linux':
        return True
    else:
        return False
