# Mgit

## 1. What is this?
This is a git-clone project.

## 2. How it works
- `arguments.py`: This is a testing file.
- `simulation.py`: this is the main testing file but for instance. For now, it contains function used in other files.
- `myGit.py`: holds the accessory functions used in creating the functions in cmdfns.py.
- `tree.py`: contains a tree class used in creating tree to represent the git commit tree.
- `cmdfns.py`: how all the functions that carry out the mgit functionalities.
- `commitTree.py`:

## 3. Why I built it this way
I split the code into two files so that I can change the math without breaking the user interface.

## 4. Current Bugs / To-Do
- [ ] Fix the crash when entering a zero.
- [ ] Create all the missing commands in main.py
- [ ] implement the staging area
- [ ] add status

## 5. Thoughts
- Git status: a function scans all the files/ if the file has the same name as it compared file/ the contents are compared if both are equal the files are tracked, else modified/ when a file in the working tree is not having a match in the index or staging area then it is Untracked. I may not add the option to know by how many commits you are ahead of main