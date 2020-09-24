# python -m pip install azure.storage.blob
# set PATH=d:\Program Files\Python38;%PATH%

from sys import argv
from time import time
from os import path, remove
from shutil import make_archive, rmtree
from datetime import datetime, timedelta
from azure.storage.blob import BlobClient

'''
Compress daily materials from graphics studio
and upload it to Azure. Clean afterwards
'''

# parameters
days_lag = 3
date_format = "%Y-%m-%d"
dir_to_collect = r"\\nas-work.agora.pl\work\arch\Warszawa"
blob_connstr = "*****"
blob_container = "collectwa"

# create archive
if len(argv) == 2:
    zip_filename = argv[1]
else:
    zip_filename = (datetime.now() + timedelta(days=-days_lag)).strftime(date_format)

dir_to_collect = path.join(dir_to_collect, zip_filename)
make_archive(zip_filename, 'zip', dir_to_collect)
zip_filename += ".zip"
print("Archive {} of size {} compressed".format(zip_filename, path.getsize(zip_filename)))

# upload to azure blob
try:
    name = zip_filename.replace('-', '/', 1)
    blob = BlobClient.from_connection_string(conn_str=blob_connstr, container_name=blob_container, blob_name=name)
    start = time()
    with open(zip_filename, "rb") as data:
        blob.upload_blob(data)
    print("Blob uploaded in {:.2f} seconds".format(time() - start))
except Exception as arg:
    print("Error uploading blob: ", arg)

# clean
remove(zip_filename)
#rmtree(dir_to_collect)

