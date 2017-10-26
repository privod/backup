import subprocess

import os.path
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

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

    if subprocess.call([archiver, 'a', arc_name, path], shell=True) != 0:
        print('Ошибка Архивирования!')
        return

    arc_filename = '.'.join([arc_name, '7z'])
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

    drive = GoogleDrive(gauth)

    file1 = drive.CreateFile({
        'id': '0B4TgAHk1RvhXS1BIV3JYYkxxamc',
        'parents': [{'id': '0B4TgAHk1RvhXS2FTd3JzUUJkSDg'}]
    })
    file1.SetContentFile(arc_filename)
    file1.Upload() # Files.insert()

