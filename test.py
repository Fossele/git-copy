import os
from myGit import createblob


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
    print(tree)
        
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



