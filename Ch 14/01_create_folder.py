import os


if not os.path.exists("Test folder"):
    os.makedirs("Test folder")     #main line for create folder 


if not os.path.exists("Test folder/Inside Folder"):
    os.makedirs("Test folder/Inside Folder")     #make a folder in "Test folder" 

if not os.path.exists("Test folder/Inside Folder 2"):
    os.makedirs("Test folder/Inside Folder 2")     #make a folder in "Test folder" 