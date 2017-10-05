import json

class Conf(object):
    _file_name = 'backup.cfg'

    @classmethod
    def _get_file_name_bad(cls):
        return cls._file_name + '.bad'

    def __init__(self):
        file_name = self.__class__._file_name

        s = open(file_name).read()
        self._conf = json.loads(s)

    def get(self, key):
        return self._conf.get(key)