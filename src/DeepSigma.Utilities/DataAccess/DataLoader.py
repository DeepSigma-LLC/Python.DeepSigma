import json
from dataclasses import is_dataclass, fields, asdict
from typing import Type, TypeVar, List, Union, Any
import pandas


class DataLoader:
    T = TypeVar('T')

    @staticmethod
    def dataframe_from_csv(file_path: str) -> pandas.DataFrame:
        """Loads data frame with data from CSV."""
        df = pandas.read_csv(file_path)
        return df


    @staticmethod
    def dataframe_to_csv(df: pandas.DataFrame, save_file_path: str) -> None:
        """
        Sends data frame data to saved CSV file.
        :param df:
        :param save_file_path:
        :return:
        """
        df.to_csv(save_file_path, index=False)


    @staticmethod
    def object_from_csv(file_path: str, class_type_to_load: Type) -> List[Type]:
        """
        Loads list of custom objects with data from CSV by matching column headers to property names.
        :param file_path:
        :param class_type_to_load: Type of class ment to store data.
        :return: List[Object]
        """
        df = pandas.read_csv(file_path)
        objects: List[Type] = []

        for index, row in df.iterrows():
            obj = class_type_to_load(**row.to_dict())
            objects.append(obj)

        return objects


    @staticmethod
    def object_from_dict(cls: Type[T], data: Union[dict, List[dict]]) -> Union[T, List[T]]:
        """
        Loads object(s) from a dictionary or list of dictionaries.
        Handles nested dataclasses as well.
        """
        if isinstance(data, list):
            return [DataLoader.object_from_dict(cls, item) for item in data]

        kwargs = {}
        for field in fields(cls):
            value = data.get(field.name)
            if is_dataclass(field.type) and isinstance(value, dict):
                value = DataLoader.object_from_dict(field.type, value)
            kwargs[field.name] = value
        return cls(**kwargs)


    @staticmethod
    def object_to_dict(obj: Any) -> Union[dict, List[dict]]:
        """
        Converts an object into a dictionary.
        Supports dataclasses, regular objects, and nested structures.
        """
        if is_dataclass(obj):
            return asdict(obj)

        if isinstance(obj, dict):
            return {k: DataLoader.object_to_dict(v) for k, v in obj.items()}

        if isinstance(obj, (list, tuple, set)):
            return [DataLoader.object_to_dict(item) for item in obj]

        if hasattr(obj, "__dict__"):
            return {k: DataLoader.object_to_dict(v) for k, v in obj.__dict__.items() if not k.startswith("_")}

        return obj  # primitive type


    @staticmethod
    def object_from_json(cls: Type[T], json_text: str) -> Union[T, List[T]]:
        """Loads object(s) with data from JSON text."""
        data = json.loads(json_text)

        if isinstance(data, list):
            return [DataLoader.object_from_dict(cls, item) for item in data]
        else:
            return DataLoader.object_from_dict(cls, data)


    @staticmethod
    def object_to_json(obj: Union[T, List[T]]) -> str:
        return json.dumps(obj, indent=4)

