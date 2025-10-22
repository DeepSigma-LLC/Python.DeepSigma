from src.DeepSigma.DataAccess import DataLoader


class SerializableMethods:

    @classmethod
    def from_dict(cls, data):
        return DataLoader.object_from_dict(cls, data)

    @classmethod
    def from_json(cls, json_str):
        return DataLoader.object_from_json(cls, json_str)
