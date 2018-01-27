import subprocess

import os.path

import argparse
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

def main_old():
    conf = BackupConf()
    if conf.file_created:
        print('Создан новый конфигурационный файл.')
        return

    upload(
        archiver=conf.get('archiver'),
        arc_name=conf.get('arc_name'),
        path=conf.get('path'),
        gd_id=conf.get('gd_id'),
        gd_parent_id=conf.get('gd_parent_id')
    )


def main():
  parser = argparse.ArgumentParser(description='Архивирует указанную папку и загружает в Google Drive')
  parser.add_argument('-a', '--archiver',       help='Путь к архиватору 7z')
  parser.add_argument('-n', '--arc-name',        help='Имя файла архива')
  parser.add_argument('-p', '--path',           help='Путь к файлу/каталогу для архивирования')
  parser.add_argument('-gd', '--gdrive-dir',    help='id архива в Google Drive')
  parser.add_argument('-gp', '--gdrive-parent', help='id родительского каталога в Google Drive')

  args = parser.parse_args()

  upload(
      args.archiver,
      args.arc_name,
      args.path,
      args.gdrive_dir,
      args.gdrive_parent
  )


def upload(archiver, arc_name, path, gd_id, gd_parent_id):

    if subprocess.call([archiver, 'a', arc_name, path], shell=True) != 0:
        print('Ошибка Архивирования!')
        return

    arc_filename = '.'.join([arc_name, '7z'])
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

    drive = GoogleDrive(gauth)

    metadata = {}
    if gd_id != '':
        metadata['id'] = gd_id
    if gd_parent_id != '':
        metadata['parents'] = [{'id': gd_parent_id}]
    file1 = drive.CreateFile(metadata)
    file1.SetContentFile(arc_filename)
    file1.Upload()


if __name__ == "__main__":
    main()
