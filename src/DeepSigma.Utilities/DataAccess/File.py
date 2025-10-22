

def get_text_file_data(file_path: str) -> str:
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def save_text_to_file(text_content: str, file_path: str, encoding: str = "utf-8") -> None:
    with open(file_path, "w", encoding=encoding) as f:
        f.write(text_content)
