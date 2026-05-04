import zlib
import os
import hashlib
import json
import datetime


def convertfilecontentToBytes(file):
    with open(file, "rb") as f:
        content = f.read()
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


def createhashfromtree(content):
    header = f"Tree {content}\x00".encode("utf-8")
    combinedata = header + content
    result = hashlib.sha1(combinedata).hexdigest()
    obj_dir = f".mgit/objects/{result[:2]}"
    obj_path = f"{obj_dir}/{result[2:]}"

    os.makedirs(obj_dir, exist_ok=True)
    with open(obj_path, "wb") as f:
        f.write(zlib.compress(combinedata))

    return result


def testing():
    array = []
    for dirpath, sub_dirnames, filenames in os.walk("test", topdown=False):
        if sub_dirnames:
            for sub_dir in sub_dirnames:
                sub_dir_item = ""
                if filenames:
                    for filename in filenames:
                        item = os.path.join(dirpath, filename)
                        sub_dir_item += createblob(item) + "\n"

        elif filenames:
            for filename in filenames:
                item = os.path.join(dirpath, filename)
                array.append((item, createblob(item)))

    return sub_dir_item


def testing2():
    array = []
    for dirpath, dirnames, filenames in os.walk("test", topdown=False):
        array.append((dirpath, dirnames, filenames))
    return array

    """
    def treeCreation():
    blob_bytes = bytes.fromhex(blob_hex)
    tree_node += f"{mode} {name}\0".encode("utf-8") + blob_bytes
    header = f"tree {len(tree_node)}\0".encode("utf-8")
    full_tree = header + tree_node
    return hashlib.sha1(full_tree).hexdigest()
    """


def tree_to_list_recursive(directory, result=None):
    if result is None:
        result = []
    if os.path.isdir(directory):
        # i will change the basename to directory and directory to sha_hex value later
        result.append((200644, os.path.basename(directory), directory))
        for elt in os.listdir(directory):
            elt_path = os.path.join(directory, elt)
            # Add current node
            tree_to_list_recursive(elt_path, result)  # Visit left
        #
    elif os.path.isfile(directory):
        result.append(
            (550644, os.path.basename(directory), directory, createblob(directory))
        )
    return result


# for elt in tree_to_list_recursive("test"):
#    print(str(elt)+"\n")

""" 
    def blob_tree(node_directory, result = None):
    if result is None:
        result = []
    for item in os.listdir(node_directory):
        item_path = os.path.join(node_directory, item)
        
        if os.path.isdir(item_path):
            result.append(item_path)
            blob_tree(item_path, result)
        elif os.path.isfile(item_path):
            result.append(createblob(item_path))
    return  result
        
        """


def blob_tree(node_directory):
    tree = b""
    final = b""
    t_path = ".mgit/Head"
    # t_path= os.path.join(t_path, "file")
    if os.listdir(node_directory) or os.path.isfile(node_directory):
        for item in os.listdir(node_directory):
            item_path = os.path.join(node_directory, item)

            if os.path.isdir(item_path):
                # tree.append(item_path)
                tree += f"123000 tree {blob_tree(item_path).decode('utf-8')} {item_path}\n".encode("utf-8")

                final = createblobfromtree(tree)
                # print(tree.decode("utf-8"))
                with open(t_path, "a") as f:
                    f.write(tree.decode())
                print(final)
                print("\n")
            elif os.path.isfile(item_path):
                tree += ( b"300444 blob " + f"{(createblob(item_path))} {item_path}\n".encode("utf-8")  )

                print(item_path)
                final = createblobfromtree(tree)
                with open(t_path, "a") as f:
                    f.write(tree.decode())
                # print(tree.decode("utf-8"))
                print(final)
                print("\n")
    return final


def createblobfromtree(tree):
    result = hashlib.sha1(tree).hexdigest()
    obj_dir = f".mgit/objects/{result[:2]}"
    obj_path = f"{obj_dir}/{result[2:]}"

    os.makedirs(obj_dir, exist_ok=True)
    print("done")
    with open(obj_path, "wb") as f:
        f.write(zlib.compress(tree))
    return result.encode("utf-8")


# blob_tree("test")


def staging(node_directory):

    data = {}
    if os.listdir(node_directory) or os.path.isfile(node_directory):
        for item in os.listdir(node_directory):
            item_path = os.path.join(node_directory, item)

            if os.path.isdir(item_path):
                # tree.append(item_path)
                data.update(staging(item_path))

            elif os.path.isfile(item_path):
                data_elt = {item_path: createblob(item_path)}
                data.update(data_elt)

    return data

def stagingFile(file_name):
    data = {}
    if os.path.isfile(file_name):
       data_elt = {file_name: createblob(file_name)}
       data.update(data_elt)
    return data



data = staging("test")

# with open('data.json', 'w') as file:
#           json.dump(data, file, indent=4)
#           print(data)
with open("data.json", "r") as file:
    stagingArea = json.load(file)

stagingArea

# 3. Write updated data back to the file


#with open('commitHistory.json', 'w') as file:
 #   json.dump(data, file, indent=4)
#   print(data)