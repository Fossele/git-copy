import zlib
import os
import hashlib


def convertfilecontentToBytes(file):
    with open(file, "rb") as f:
        content = f.read()
    #  print("Successful conversion")
    return content


def createblob(file_name):
    content = convertfilecontentToBytes(file_name)
    header = f"Blob {content}\x00".encode("utf-8")
    combinedata = header + content
    result = hashlib.sha1(combinedata).hexdigest()
    obj_dir = f".mgit/objects/{result[:2]}"
    obj_path = f"{obj_dir}/{result[2:]}"

    os.makedirs(obj_dir, exist_ok=True)
    with open(obj_path, "wb") as f:
        f.write(zlib.compress(combinedata))

    return result
    # print("blob su


def testing():
    array = []
    for dirpath, sub_dirnames, filenames in os.walk("test", topdown=False):
        if sub_dirnames:
            for sub_dir in sub_dirnames:
                if filenames:
                    for filename in filenames:
                        item = os.path.join(dirpath, filename)
                        array.append((item, createblob(item)))

        elif filenames:
            for filename in filenames:
                item = os.path.join(dirpath, filename)
                array.append((item, createblob(item)))

    return array


print(testing())
