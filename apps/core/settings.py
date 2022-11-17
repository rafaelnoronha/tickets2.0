from pathlib import Path
import json


class Environment():
    def __init__(self, base_dir):
        try:
            self._base_dir = base_dir or Path()
            self._environment_file = self._base_dir.joinpath('.env')
            self._data = json.loads(str(open(self.environment_file).read()))
        except:
            self._data = dict()

    def get(self, chave):
        return self._data.get(chave)
