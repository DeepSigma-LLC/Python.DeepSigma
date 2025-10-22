from typing import Type, Union
from enum import Enum


class DataField:

    def __init__(self, field_name: Union[str, Enum], data_type: Type, description: str = ""):
        self.data_type: Type = data_type
        self.description: str = description

        if isinstance(field_name, Enum):
            self.name: str = field_name.name
        elif isinstance(field_name, str):
            self.name: str = field_name
