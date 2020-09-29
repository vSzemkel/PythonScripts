# python -m pip install azure.storage.blob
# set PATH=d:\Program Files\Python38;%PATH%

"""
Archive daily materials.

Compress daily materials from graphics studio
and upload it to Azure. Clean workspace afterwards.
"""

from datetime import datetime, timedelta
from os import path, remove
from shutil import make_archive, rmtree
from sys import argv, exit
from time import time

from azure.storage.blob import BlobClient

# parameters
days_lag = 3
date_format = "%Y-%m-%d"
dir_to_collect = r"\\nas-work.agora.pl\work\arch\Warszawa"
blob_connstr = "***** ***"
blob_container = "collectwa"

# create archive
if len(argv) == 2:
    zip_filename = argv[1]
else:
    zip_filename = (datetime.now() + timedelta(days=-days_lag)).strftime(date_format)

start = time()
dir_to_collect = path.join(dir_to_collect, zip_filename)
try:
    make_archive(zip_filename, "zip", dir_to_collect)
except FileNotFoundError:
    exit("Archive {0} doesn't exist".format(zip_filename))
except Exception as exc:
    exit("Error comressing archive {0}: {1}".format(zip_filename, exc))

zip_filename += ".zip"
print("Archive {0} of size {1} compressed in {2:.2f} sec.".format(zip_filename, path.getsize(zip_filename), time() - start))

# upload to azure blob
start = time()
blobname = zip_filename.replace("-", "/", 1)
try:
    blob = BlobClient.from_connection_string(conn_str=blob_connstr, container_name=blob_container, blob_name=blobname)
    with open(zip_filename, "rb") as dayarch:
        blob.upload_blob(dayarch)
except Exception as arg:
    exit("Error uploading blob: ", arg)

print("Blob uploaded in {0:.2f} sec.".format(time() - start))

# clean
remove(zip_filename)
# rmtree(dir_to_collect)
