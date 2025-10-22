import getpass


def get_username() -> str:
    username = getpass.getuser()
    return username
