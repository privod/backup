import subprocess

from project.conf import Conf

_path = 'F:\\Games\\OpenXcom\\user\\xcom1'
_archiver = "C:\\Program Files\\7-Zip\\7z.exe"
_arc_name = 'xcom'


def backup():
    if subprocess.call([_archiver, 'a', _arc_name, _path], shell=True) == 0:
        print('Архивирование успешно завершено.')
