import os


def check_root():
    user = os.getenv("SUDO_USER")
    if user is None:
      return False
    else:
      return True
