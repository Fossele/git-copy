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
- [ ] 