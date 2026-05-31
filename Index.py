import struct
import hashlib
import os
import IndexEntry
from myGit import createblob

ENTRY_FORMAT = "!4sII"

# Meaning of "!4sII":
# !  = Network byte order (Big-Endian)
# 4s = 4-character byte string for the signature string(4 bytes)
# I  = Unsigned 32-bit integer for the version number(4 bytes)
# I  = Unsigned 32-bit integer for the number of entries(4 bytes)
# Total size = 12 bytes



def createShaBytes(file_name):
    with open(file_name, "rb") as f:
        content = f.read()
        
    content_size = len(content)
    
    header = f"blob {content_size}\x00".encode("utf-8")
    combinedata = header + content
    result = hashlib.sha1(combinedata).digest()
    return result
   
class Index:
    def __init__(self, index_path="./mgit/index"):
        self.index_path = index_path
        self.entries = {}

    def write(self):

        index_file_data = bytearray()
        header = struct.pack(ENTRY_FORMAT, b"DIRC", 2, len(self.entries))
        index_file_data.extend(header)

        for path in sorted(self.entries.keys()):
            entry = self.entries[path]
            index_file_data.extend(entry.to_bytes())

        sha1_checksum = hashlib.sha1(index_file_data).digest()
        index_file_data.extend(sha1_checksum)

        with open(self.index_path, "wb") as f:
            f.write(index_file_data)

    def read(self):
        if not os.path.exists(self.index_path):
            self.entries = {}
            print("Index file not existing.")
            return

        with open(self.index_path, "rb") as f:
            data = f.read()

        content, checksum = data[:-20], data[-20:]

        assert (
            hashlib.sha1(content).digest() == checksum
        ), "Index file is corrupted. Checksum mismatch."

        signature_string, version_number, num_of_entries = struct.unpack(
            ENTRY_FORMAT, content[:12]
        )
        entries_bytes = content[12:]

        assert signature_string == b"DIRC"  # DirCache
        assert version_number == 2, "Mygit  works on version 2"

        offset = 12
        for _ in range(num_of_entries):
            entry, offset = IndexEntry.from_bytes(entry, offset)
            self.entries[entry.path] = entry

    def rm(self, *filenames):
        self.read()
        for filename in filenames:

            if filename in self.entries:
                del self.entries[filename]
                os.remove(filename)

            else:
                print(f"fatal: pathspec '{filename}' did not match any files")

        self.write()

    def add(self, *file_paths):
        self.read()

        for file_path in file_paths:
            createblob(file_path)
            
            file_metadata = os.stat(file_path)
            
            ctime = file_metadata.st_ctime
            mtime = file_metadata.st_mtime
            dev = file_metadata.st_dev
            ino = file_metadata.st_ino
            mode = file_metadata.st_mode
            uid = file_metadata.st_uid
            gid = file_metadata.st_gid
            file_size = file_metadata.st_size
            sha1 = createShaBytes(file_paths)
            
            entry = IndexEntry( ctime, mtime, dev, ino, mode, uid, gid, file_size, sha1, file_path)
            self.entries[file_path] = entry
            
        self.write()