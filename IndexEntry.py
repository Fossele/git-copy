import struct
import os
import hashlib

# This matches the 62 bytes of fixed metadata we discussed:
    # ! = Big-endian (Network byte order)
    # q = ctime (8 bytes), q = mtime (8 bytes)
    # i = dev (4 bytes), i = ino (4 bytes)
    # I = mode (4 bytes)
    # I = uid (4 bytes), I = gid (4 bytes)
    # I = file_size (4 bytes)
    # 20s = SHA-1 hash (20 bytes)
    # H = path_length (2 bytes unsigned short)
    # Total: 8+8+4+4+4+4+4+4+20+2 = 62 bytes



class IndexEntry:
    METADATA_FORMAT = "!qqiIIIII20sH"
    METADATA_SIZE = 62
    def __init__(self, ctime, mtime, dev, ino, mode, uid, gid, file_size, sha1, path):
        self.ctime = ctime
        self.mtime = mtime
        self.dev = dev
        self.ino = ino
        self.mode = mode
        self.uid = uid
        self.gid = gid
        self.file_size = file_size
        self.sha1 = sha1
        self.path = path
        

    def to_bytes(self) -> bytes:
        path_bytes = self.path.encode("utf-8")
        path_len = len(path_bytes)
        header_data_bytes = struct.pack(self.METADATA_FORMAT, self.ctime, self.mtime,self.dev, self.ino, self.mode,  self.uid ,self.gid, self.file_size, self.sha1, path_len)
        entry_data_bytes = header_data_bytes + path_bytes
        return entry_data_bytes

    @classmethod
    def from_bytes(cls, data: bytes, offset: int) -> tuple["IndexEntry", int]:
        metadata = struct.unpack_from(cls.METADATA_FORMAT, data, offset)
        path_len = metadata[9]
        path_start = offset + cls.METADATA_SIZE
        path_end = path_start + path_len 
        path_bytes = data[path_start, path_end]
        path = path_bytes.decode('utf-8')
        
        entry = cls(
            ctime = metadata[0],
            mtime = metadata[1],
            dev = metadata[2],
            ino = metadata[3],
            mode = metadata[4],
            uid = metadata[5],
            gid = metadata[6],
            file_size = metadata[7],
            sha1 = metadata[8],
            path = path
        )
        
        offset += cls.METADATA_SIZE + path_len  
        return entry, offset