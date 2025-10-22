from string import digits


def remove_all_numbers(string: str) -> str:
    remove_digits = str.maketrans("", "", digits)
    return string.translate(remove_digits)

def remove_all_spaces(string: str) -> str:
    return string.replace(" ", "")

def capitalize_each_word(string: str) -> str:
    return string.title()
