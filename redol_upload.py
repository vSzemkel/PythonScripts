# python -m pip install azure.storage.blob
# set PATH=C:\Python310;%PATH%
# python -m flake8 redol_upload.py

"""
Archive daily materials.

Compress daily materials from regional editorial houses
and upload it to Azure. Clean workspace afterwards.
"""

from datetime import datetime, timedelta
from os import path, remove
from shutil import make_archive, rmtree
from sys import argv, exit
from time import time

from azure.storage.blob import BlobClient, StandardBlobTier


def collect(dir_name, arch_name):
    start = time()
    try:
        make_archive(arch_name, "zip", dir_name)
    except FileNotFoundError:
        exit(f"Compression source: {dir_name} not found")
    except Exception as exc:
        exit(f"Error comressing archive {arch_name}.zip: {exc.exc_msg}")

    arch_name += ".zip"
    print(f"Archive {arch_name} of size {path.getsize(arch_name)} compressed in {time() - start:.2f} sec.")
    return arch_name


def cloud_push(name, src_file):
    start = time()
    try:
        blob = BlobClient.from_connection_string(conn_str=blob_connstr, container_name=blob_container, blob_name=name)
        with open(src_file, "rb") as dayarch:
            blob.upload_blob(dayarch, standard_blob_tier=StandardBlobTier.Cool)
    except Exception as arg:
        exit("Error uploading blobs: " + arg.exc_msg)

    print(f"Blob {name} uploaded in {time() - start:.2f} sec.")


# parameters
days_lag = 90
date_format = "%Y-%m-%d"
dir_to_collect = r"\\arch01-d02.agora.pl\archolredakcja"
blob_connstr = "DefaultEndpointsProtocol=https;AccountName=saredakcjaol;AccountKey=***** ***;EndpointSuffix=core.windows.net"
blob_container = "redol"

# create archives
if len(argv) == 2:
    zip_filename = argv[1]
else:
    zip_filename = (datetime.now() + timedelta(days=-days_lag)).strftime(date_format)

arch_filename = zip_filename
arch_to_collect = path.join(dir_to_collect, zip_filename[:4], zip_filename)
arch_filename = collect(arch_to_collect, arch_filename)

fs_filename = zip_filename + "-fs"
fs_to_collect = path.join(dir_to_collect, zip_filename[:4], '!!! Fotosepia !!!', zip_filename[:4] + zip_filename[5:7] + zip_filename[8:])
fs_filename = collect(fs_to_collect, fs_filename)

# upload to azure blobs
blobname = arch_filename.replace("-", "/", 1)
cloud_push(blobname, arch_filename)
blobname = fs_filename.replace("-", "/", 1)
cloud_push(blobname, fs_filename)

# clean
remove(arch_filename)
remove(fs_filename)
rmtree(arch_to_collect)
rmtree(fs_to_collect)
