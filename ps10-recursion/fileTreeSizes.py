# Your name: Daphka Alius, Anika Shields
# Your username: dalius, ashields
# CS111 Spring 2018 PS10 Task 3
# fileTreeSizes.py
# Submission date: 5/1/18

import os
from printNice import printNice 

#--------------------------- Subtask a: fileTreeSize --------------------------
def fileTreeSize(root):
    """
    Assume that root is the pathname (a string) of a file or directory
    relative to the current working directory.

    If root is the pathname of a nondirectory file, returns the size (in
    bytes) of that file.
    
    If root is the pathname of a directory, returns the sum of the sizes (in
    bytes) of all tne nondirectory files in the file tree rooted at root. This
    sum should *exclude* the sizes of hidden files (files or directories whose
    name begins with a dot) and should also *exclude* the size of any
    metainformation associated with the directory itself.
    """
    if isHiddenFile(root):
        return 0
    elif os.path.isfile(root):
        return os.path.getsize(root)
    elif os.path.isdir(root):
        fileSums = 0
        for item in os.listdir(root):
            pathname = os.path.join(root, item)
            fileSums += fileTreeSize(pathname)
        return fileSums

#--------------------------- Subtask b: fileTreeList --------------------------
def fileTreeList(root):
    """
    Assume that root is the pathname (a string) of a file or directory
    relative to the current working directory.
    
    Returns a list of pathnames (relative to the current working directory) of
    all nonhidden files and directories in the file tree rooted at root. The
    pathnames should be listed in an order such that:

    (1) the pathname of a directory should appear directly *after* the
        pathnames of all files and directories rooted at that directory.

    (2) if fileOrDirA comes before fileOrDirB in the list returned by
        os.listdir, then in the result list, all files rooted at fileOrDirA
        should come before all files rooted at fileOrDirB.
    """
    if isHiddenFile(root):
        return []
    elif os.path.isfile(root):
        return [root]
    elif os.path.isdir(root):
        treelist = []
        for aFile in sorted(os.listdir(root)):
            pathname = os.path.join(root, aFile)
            treelist = treelist + fileTreeList(pathname)
        return treelist + [root]
    

#---------------------- Subtask c: fileTreeListWithSizes ----------------------

def fileTreeListWithSizes(root):
    """
    Assume that root is the pathname (a string) of a file or directory
    relative to the current working directory.

    Returns a list of *pairs* of (1) pathnames (relative to the current
    working directory) and (2) file tree sizes of those pathnames.

    The pairs should have the same order (determined by their pathname) as
    specified in fileTreeList.
    """
    if isHiddenFile(root):
       return []
    elif os.path.isfile(root):
        return [(root, os.path.getsize(root))]
    elif os.path.isdir(root):
       newList = []
       size = 0
       for aFile in sorted(os.listdir(root)):
           newList += fileTreeListWithSizes(os.path.join(root, aFile))
           if newList != []:
            size += newList[-1][1]
       return newList + [(root, size)]
       
        
            
            
        
         # Replace this stub

#------------------------------ Helper Functions ------------------------------

# Use this to filter out hidden files in Subtasks a, b, and c 
def isHiddenFile(path):
    base = os.path.basename(path)    
    return (len(base) > 0 
            and base[0] == '.'             
            and base != '.'            
            and base != '..')  

# You may use the following helper function in Subtasks b and c
# (but are not required to use it) 
def combineListOfLists(listOfLists):
    """Returns a single list whose elements are all the elements of the lists
       in the given listOfLists
    """
    result = []
    for list in listOfLists:
        result.extend(list)
    return result

# ------------------- Testing functions (do not change these) ------------------
 
def testFileTreeSize(root):
    print "fileTreeSize('{}') -> {}".format(root, fileTreeSize(root))

def testFileTreeList(root):
    print "\nfileTreeList('{}'):".format(root)
    printNice(fileTreeList(root))

def testFileTreeListWithSizes(root):
    print "\nfileTreeListWithSizes('{}'):".format(root)
    printNice(fileTreeListWithSizes(root))
        
def dashedLine(): 
    print "-"*78    
 
if __name__ == "__main__":
    """Here are some test cases using the above testing functions."""
    # dashedLine()
    # testFileTreeSize("testdir/remember/ephemeral.py")
    # testFileTreeSize("testdir/remember/memories.txt")
    # testFileTreeSize("testdir/remember/persistent.py")
    # testFileTreeSize("testdir/remember")    
    # testFileTreeSize("testdir/hyp.py")
    # testFileTreeSize("testdir/pset")
    # testFileTreeSize("testdir/pubs.json")
    # testFileTreeSize("testdir/tracks.csv")
    # testFileTreeSize("testdir")
    # testFileTreeSize("testdir/remember/.DS_Store")

    dashedLine()
    # testFileTreeList("testdir/remember/memories.txt")
    # testFileTreeList("testdir/remember")
    # testFileTreeList("testdir")
    # testFileTreeList("testdir/remember/.DS_Store")

    # dashedLine()
    # testFileTreeListWithSizes("testdir/remember/memories.txt")
    # testFileTreeListWithSizes("testdir/remember")
    # testFileTreeListWithSizes("testdir")
    # testFileTreeListWithSizes("testdir/remember/.DS_Store")
