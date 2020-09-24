# python3 -m pip install azure.storage.blob
from datetime import datetime, timedelta
from azure.storage.blob import BlobClient
import os
import shutil

# parameters
days_lag = 3
dir_to_collect = "/Users/velvet/GitHub/GCC"
blob_connstr = ""
blob_container = "collectwa"

# create archive
zip_filename = (datetime.now() + timedelta(days=-days_lag)).strftime("%Y-%m-%d")
shutil.make_archive(zip_filename, 'zip', dir_to_collect)
zip_filename += ".zip"
print("Archive {} of size {} compressed".format(zip_filename, os.path.getsize(zip_filename)))

# upload to azure blob
try:
    blob = BlobClient.from_connection_string(conn_str=blob_connstr, container_name="my_container", blob_name=zip_filename)
    with open(zip_filename, "rb") as data:
        blob.upload_blob(data)
except Exception as arg:
    print("Error uploading blob: ", arg)

# clean
os.remove(zip_filename)

