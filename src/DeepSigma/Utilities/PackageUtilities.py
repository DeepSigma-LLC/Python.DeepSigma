from importlib.metadata import version


def get_package_version(package_name: str) -> str:
    return version(package_name)
