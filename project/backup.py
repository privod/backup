import subprocess

import os

import argparse
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def main():
    parser = argparse.ArgumentParser(description='Архивирует указанную папку и загружает в Google Drive')
    parser.add_argument('-a', '--archiver',       help='Путь к архиватору 7z')
    parser.add_argument('-n', '--arc-name',        help='Имя файла архива')
    parser.add_argument('-p', '--path',           help='Путь к файлу/каталогу для архивирования')
    parser.add_argument('-gd', '--gdrive-dir',    help='id архива в Google Drive')
    parser.add_argument('-gp', '--gdrive-parent', help='id родительского каталога в Google Drive')
    args = parser.parse_args()

    if subprocess.call([args.archiver, 'a', args.arc_name, args.path], shell=True) != 0:
        print('Ошибка Архивирования!')
        return

    arc_filename = '.'.join([args.arc_name, '7z'])
    try:
        upload(
            arc_filename,
            args.gdrive_dir,
            args.gdrive_parent,
        )
    finally:
        os.remove(arc_filename)


def upload(arc_filename, gd_id, gd_parent_id):

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
