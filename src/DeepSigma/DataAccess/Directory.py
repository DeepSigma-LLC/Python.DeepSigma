import os
from typing import List


def get_files_with_scandir(directory_path: str) -> List[str]:
    files = []
    for entry in os.scandir(directory_path):
        if entry.is_file():
            files.append(entry.name)
    return files
