#https://medium.com/geekculture/understanding-merkle-trees-f48732772199
#https://medium.com/girl-writes-code/git-is-a-directed-acyclic-graph-and-what-the-heck-does-that-mean-b6c8dec65059
import hashlib
import zlib
import os
from tree import Tree

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
        
        
    return(result)
    #print("blob successfully created")
    #print(obj_path)

def read_blob(path):
    if os.path.isfile(path):
        file_name = path
        with open(file_name,"rb") as f:
            result = zlib.decompress(f.read())
            result = result.decode("utf-8")
    return result

#read_blob(".mgit/objects/72/7a3f43e4d2df134be0242cafec07c5d13f0748")
        

def createEntries(directory):
    array = []
    if os.path.isfile(directory):
        print("make a node out of")
        array.append((100644,os.path.basename(directory),createblob(directory)))
     
    elif os.path.isdir(directory):
        print("working")
        for elt in os.listdir(directory):
            elt_path = os.path.join(directory,elt)
            array.append((600233,os.path.basename(elt_path)))
            createEntries(elt_path)
            print(elt_path)
    return array



#print(createEntries("test"))



def createTree(entries):
    # an array of entries in the format [(mode, name, blobfile)]
    entries.sort(Key=lambda x: x[1])

    tree_node = b""
    for mode, name, blob_hex in entries:
        blob_bytes = bytes.fromhex(blob_hex)
        tree_node += f"{mode} {name}\0".encode("utf-8") + blob_bytes
    header = f"tree {len(tree_node)}\0".encode("utf-8")
    full_tree = header + tree_node
    return hashlib.sha1(full_tree).hexdigest()


def enterTree(test):
    node = Tree(os.path.basename(test))
    print(test)
    if os.path.isdir(test):
     for sub_dir in os.listdir(test):
         item_path = os.path.join( test, sub_dir)
         node.add_child(enterTree(item_path))       
    return node


def tree_to_list_recursive(directory, result=None):
    if result is None:
        result = []
    if os.path.isdir(directory):
        #i will change the basename to directory and directory to sha_hex value later
        result.append((200644, os.path.basename(directory), directory))
        for elt in os.listdir(directory):
            elt_path = os.path.join(directory,elt)
            # Add current node
            tree_to_list_recursive(elt_path, result)  # Visit left
        #
    elif os.path.isfile(directory):
        
        
             result.append((550644, os.path.basename(directory), createblob(directory)))
    return result
    ù
print(tree_to_list_recursive("test"))
#enterTree("test")
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
