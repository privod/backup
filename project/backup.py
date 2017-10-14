import subprocess

from config import Conf


class BackupConf(Conf):
    file_name = 'backup.cfg'
    default = [
        (None, 'path',     '.',                                'Путь'),
        (None, 'archiver', 'C:\\Program Files\\7-Zip\\7z.exe', 'Путь к архиватору'),
        (None, 'arc_name', 'name',                             'Имя файла архива'),
    ]
    # path = '.'          # 'F:\\Games\\OpenXcom\\user\\xcom1'
    # archiver = "C:\\Program Files\\7-Zip\\7z.exe"
    # arc_name = 'name'   # 'xcom'


def backup():

    conf = BackupConf()
    if conf.file_created:
        print('Создан новый конфигурационный файл.')
        return
    archiver = conf.get('archiver')
    arc_name = conf.get('arc_name')
    path = conf.get('path')

    if subprocess.call([archiver, 'a', arc_name, path], shell=True) == 0:
        print('Архивирование успешно завершено.')
