import pickle
import os

class FileManager:
    @staticmethod
    def load(filename):
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                return pickle.load(f)
        return []

    @staticmethod
    def save(filename, data):
        with open(filename, "wb") as f:
            pickle.dump(data, f)
