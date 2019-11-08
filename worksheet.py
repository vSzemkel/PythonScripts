import os
import stat

path = "D:\\Code\\x\\"

print("os.scandir()")
with os.scandir(path) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            print(entry.name)

print("os.listdir()")
for entry in os.listdir(path):
    if not entry.startswith('.'):
        s = os.stat(path + entry)
        if s.st_file_attributes & stat.FILE_ATTRIBUTE_DIRECTORY == 0:
            print(entry)
