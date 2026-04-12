import hashlib
import zlib
import os


def convertfilecontentToBytes(file):
    with open(file, "rb") as f:
        content = f.read()
  #  print("Successful conversion")
    return content


def createblob(file_name):
    content = convertfilecontentToBytes(file_name)
    header = f"Blob {content}\x00".encode()
    combinedata = header + content
    result = hashlib.sha1(combinedata).hexdigest()
    obj_dir = f".mgit/objects/{result[:2]}"
    obj_path = f"{obj_dir}/{result[2:]}"
    print(obj_path)
    os.makedirs(obj_dir, exist_ok=True)
    with open(obj_path, "wb") as f:
        f.write(zlib.compress(combinedata))
    print("blob successfully created")
    print(obj_path)


def createEntries(directory):
    if os.path.isfile(directory): 
        print("make a node out of")
        createblob(directory)
        print(directory)
    elif os.path.isdir(directory):
       print("working")
       for elt in os.listdir(directory):
            createEntries(f"{directory}/{elt}")
            print(f"{directory}/{elt}")
            
    
createEntries("test")

def createTree(entries):
    # an array of entries in the format [(mode, name, blobfile)]
    entries.sort(Key=lambda x: x[1])

    tree_node = b""
    for mode, name, blob_hex in entries:
        blob_bytes = bytes.fromhex(blob_hex)
        tree_node += f"{mode} {name}/\0".encode("utf-8") + blob_bytes
    header = f"tree {len(tree_node)}\0".encode("utf-8")
    full_tree = header + tree_node
    return hashlib.sha1(full_tree).hexdigest()


"""
def file_digest(fileObj, digest_type):
    h = hashlib.new(digest_type) if isinstance(digest_type, str) else digest_type()
    
    while True:
        chunk = fileObj.read(2**18)
        if not chunk:
            break
        h.update(chunk)
        
    return h
    
filename = "text.txt"

with open(filename, "rb") as f:
     combinedata = filename.encode("utf-8") + f.read()
     digest = file_digest(combinedata, "sha1")

print(digest.hexdigest())
    """
