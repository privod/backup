import subprocess

import os.path
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from config import Conf


class BackupConf(Conf):
    file_name = 'backup.cfg'
    default = [
        (None, 'path',     '.',                                'Путь к файлу/каталогу для архивирования'),
        (None, 'archiver', 'C:\\Program Files\\7-Zip\\7z.exe', 'Путь к архиватору'),
        (None, 'arc_name', 'name',                             'Имя файла архива'),
        (None, 'gd_id', '', 'id архива в GDrive'),
        (None, 'gd_parent_id', '', 'id родительского каталога в GDrive'),
    ]
    # path = '.'          # 'F:\\Games\\OpenXcom\\user\\xcom1'
    # archiver = "C:\\Program Files\\7-Zip\\7z.exe"
    # arc_name = 'name'   # 'xcom'


def upload():

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

    gd_id = conf.get('gd_id')
    gd_parent_id = conf.get('gd_parent_id')
    metadata = {}
    if gd_id != '':
        metadata['id'] = gd_id
    if gd_parent_id != '':
        metadata['parents'] = [{'id': gd_parent_id}]
    file1 = drive.CreateFile(metadata)
    file1.SetContentFile(arc_filename)
    file1.Upload()


if __name__ == "__main__":
    upload()
