import struct
import hashlib
import os
from IndexEntry import IndexEntry
from myGit import createblob
from pathlib import Path
from test import tree_to_dictionary_recursive, flat_to_tree

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
        self.commitable = False
        if not os.path.exists(index_path):
            with open(index_path, "wb") as f:
                pass

            print(f"Successfully created: {index_path}")

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
        if content != b"":
            assert (
                hashlib.sha1(content).digest() == checksum
            ), "Index file is corrupted. Checksum mismatch."

        signature_string, version_number, num_of_entries = struct.unpack(
            ENTRY_FORMAT, content[:12]
        )
        entries_bytes = content

        assert signature_string == b"DIRC"  # DirCache
        assert version_number == 2, "Mygit  works on version 2"

        offset = 12
        for _ in range(num_of_entries):

            entry, offset = IndexEntry.from_bytes(entries_bytes, offset)
            self.entries[entry.path] = entry

        # print(self.entries)

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
        if "." not in file_paths:

            for file_path in file_paths:

                try:
                    createblob(file_path)

                    file_metadata = os.stat(file_path)

                    ctime = int(file_metadata.st_ctime)
                    mtime = int(file_metadata.st_mtime)
                    dev = file_metadata.st_dev
                    ino = file_metadata.st_ino
                    mode = file_metadata.st_mode
                    uid = file_metadata.st_uid
                    gid = file_metadata.st_gid
                    file_size = file_metadata.st_size
                    sha1 = createShaBytes(file_path)
                    entry = IndexEntry(
                        ctime,
                        mtime,
                        dev,
                        ino,
                        mode,
                        uid,
                        gid,
                        file_size,
                        sha1,
                        file_path,
                    )
                    self.entries[file_path] = entry
                except FileNotFoundError:
                    print(f"The file {file_path} can't be found")

        else:

            all_files = tree_to_dictionary_recursive()

            for file_path, _ in all_files.items():
                try:
                    createblob(file_path)
                    file_metadata = os.stat(file_path)
                    ctime = int(file_metadata.st_ctime)
                    mtime = int(file_metadata.st_mtime)
                    dev = file_metadata.st_dev
                    ino = file_metadata.st_ino
                    mode = file_metadata.st_mode
                    uid = file_metadata.st_uid
                    gid = file_metadata.st_gid
                    file_size = file_metadata.st_size
                    sha1 = createShaBytes(file_path)
                    entry = IndexEntry(
                        ctime,
                        mtime,
                        dev,
                        ino,
                        mode,
                        uid,
                        gid,
                        file_size,
                        sha1,
                        file_path,
                    )
                    self.entries[file_path] = entry
                except FileNotFoundError:
                    print(f"The file {file_path} can't be found")

        self.commitable = True
        self.write()

    def status(self):

        working_dir_files = tree_to_dictionary_recursive()
        untracked = []
        unstaged = []
        print("status")
        for key, value in working_dir_files.items():
            if key not in self.entries:
                untracked.append(key)  
                continue
            else:
                if self.entries[key] != value:
                    unstaged.append(key)
                
                
                """On branch main
                Your branch is ahead of 'origin/main' by X commits.
                (use "git push" to publish your local commits)

                Changes not staged for commit:
                (use "git add <file>..." to update what will be committed)
                (use "git restore <file>..." to discard changes in working directory)
                        modified:   Index.py

                Untracked files:
                (use "git add <file>..." to include in what will be committed).
                """

    def commit(self):
        if not self.commitable:
            self.status()
            return
        else:
            self.read()
            nested_tree = flat_to_tree(self.entries)
            #print(nested_tree)
            print("I worked")
            
            # 1. convert entries into to a nested tree
            # 2. turn the nested tree into the commit
            #print(self.entries)
            
            self.commitable = False 

index = Index(".test")
index.write()
index.add(".")
#index.commit()
index.read()
