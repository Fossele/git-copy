import os
import hashlib
import pwd
from myGit import createblob
#from simulation import createblobfromtree


def createEntries(directory):
    """not used because it is not yet finished"""
    array = []
    if os.path.isfile(directory):
        print("make a node out of")
        array.append((100644, os.path.basename(directory), createblob(directory)))

    elif os.path.isdir(directory):
        print("working")
        for elt in os.listdir(directory):
            elt_path = os.path.join(directory, elt)
            array.append((600233, os.path.basename(elt_path)))
            createEntries(elt_path)
            print(elt_path)
    return array


def tree_to_dictionary_recursive(directory=".", result=None):
    """turns a directory  into a entries tuples that can be used  in the createEntries function"""
    if result is None:
        result = {}

    if os.path.isdir(directory):

        if os.listdir(directory):
            for elt in os.listdir(directory):
                elt_path = os.path.relpath(os.path.join(directory, elt), ".")
                # Add current node
                tree_to_dictionary_recursive(elt_path, result)  # Visit left

        #
    elif os.path.isfile(directory):
        result.update({f"{directory}": f"{createblob(directory)}"})
    return result


flat_dict = tree_to_dictionary_recursive("test")


def flat_to_tree(flat_dict):
    "turn a flat dictionary into a nested tree"
    tree = {}

    for path, sha in flat_dict.items():
        parts = path.split("/")  # e.g., ['test', 'cool', 'good.txt']
        current = tree

        # 1. Traverse or create the directory folders
        for folder in parts[:-1]:
            current = current.setdefault(folder, {})

        # 2. Place the file name and its hash at the final leaf node
        file_name = parts[-1]
        current[file_name] = sha

    return tree


def flatten_tree(tree, current_path=""):
    flat = {}
    for key, value in tree.items():
        # Build the path dynamically (e.g., "test/cool")
        new_path = f"{current_path}/{key}" if current_path else key

        if isinstance(value, dict):
            # If it's a folder (dictionary), go deeper recursively
            flat.update(flatten_tree(value, new_path))
        else:
            # If it's a file string, we hit the leaf node. Store it!
            flat[new_path] = value

    return flat


def blob_tree_from_dict(dictionary):
    "creates blobs(sha values) for folders and files recursively out of a given nested dict."
    tree = b""
    blobValue = b""
    destination_path = ".mgit/Dest"

    if isinstance(dictionary, dict):
        for key, value in dictionary.items():

            if isinstance(value, dict):
                tree += f"123000 tree {blob_tree_from_dict(item_path).decode('utf-8')} {item_path}\n".encode(
                    "utf-8"
                )

                blobValue = createblobfromtree(tree)
                # print(tree.decode("utf-8"))
                with open(destination_path, "a") as f:
                    f.write(tree.decode())
                print(blobValue)
                print("\n")

            else:
                tree += (
                    b"300444 blob "
                    + f"{(createblob(item_path))} {item_path}\n".encode("utf-8")
                )

                print(item_path)
                blobValue = createblobfromtree(tree)
                with open(destination_path, "a") as f:
                    f.write(tree.decode())
                # print(tree.decode("utf-8"))
                print(blobValue)
                print("\n")
    else:
        blobValue = value

    return blobValue


def blob_tree_from_dict(node_directory):
    "creates blobs(sha values) for folders and files recursively out of a given nested dict."
    tree = b""
    final = b""
    t_path = ".mgit/Head"
    # t_path= os.path.join(t_path, "file")
    if os.listdir(node_directory) or os.path.isfile(node_directory):
        for item in os.listdir(node_directory):
            item_path = os.path.join(node_directory, item)

            if os.path.isdir(item_path):  # if dir is node, recurse
                # tree.append(item_path)
                tree += f"123000 tree {blob_tree_from_dict(item_path).decode('utf-8')} {item_path}\n".encode(
                    "utf-8"
                )

                final = createblobfromtree(tree)
                # print(tree.decode("utf-8"))
                with open(t_path, "a") as f:
                    f.write(tree.decode())
                print(final)
                print("\n")
            elif os.path.isfile(item_path):
                tree += (
                    b"300444 blob "
                    + f"{(createblob(item_path))} {item_path}\n".encode("utf-8")
                )

                print(item_path)
                final = createblobfromtree(tree)
                with open(t_path, "a") as f:
                    f.write(tree.decode())
                # print(tree.decode("utf-8"))
                print(final)
                print("\n")
    return final


def createTreefromDict(nested_dict, current_path=""):
    path = ""
    tree = b""
    for key, value in nested_dict.items():

        new_path = os.path.join(current_path, key) if current_path else key
        if isinstance(value, dict):
            tree += f"110 tree  {createTreefromDict(value, new_path).decode('utf-8')}\n".encode('utf-8')
            
        else:
            tree +=  b"300444 blob "+ f"{value}\n".encode("utf-8")
                
        
    print(tree.decode('utf-8'))
    return hashlib.sha1(tree).hexdigest().encode("utf-8")





nested_tree = {
    "src": {
        "components": {
            "Button.js": "ann",
            "Header.js": "hhaas",
        },
        "utils": {"helpers.js": "hhhs"},
        "index.js": "hhsahh",
    },
    "package.json": "hallo",
}

def get_user_email():
    email = os.environ.get('EMAIL')
    print(email)

def get_linux_user_info():
    # Obtain the numeric user ID of the current process
    uid = os.getuid()
    # Query system database for user details
    user_entry = pwd.getpwuid(uid)
    
    username = user_entry.pw_name
    # The gecos field typically stores the user's Full Name
    full_name = user_entry.pw_gecos.split(',')[0]
    
    # System mail configurations default locally or look at $EMAIL variable
    email = os.environ.get('EMAIL') or f"{username}@localhost"
    
    print(f"Username: {username}")
    print(f"Full Real Name: {full_name}")
    print(f"System Email: {email}")

get_linux_user_info()