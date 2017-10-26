from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from project.backup import backup

backup()


# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()
#
# drive = GoogleDrive(gauth)

# file1 = drive.CreateFile({'title': 'Hello.txt'})
# file1.SetContentString('Hello')
# file1.Upload() # Files.insert()
# #
# # file1['title'] = 'HelloWorld.txt'  # Change title of the file
# # file1.Upload() # Files.patch()
# # file1.GetContentFile('Hello.txt')
#
#
# # Paginate file lists by specifying number of max results
# for file_list in drive.ListFile({'q': "title contains 'xcom1'"}):
#   print('Received %s files from Files.list()' % len(file_list)) # <= 10
#   for file1 in file_list:
#     print('title: %s, id: %s' % (file1['title'], file1['id']))
