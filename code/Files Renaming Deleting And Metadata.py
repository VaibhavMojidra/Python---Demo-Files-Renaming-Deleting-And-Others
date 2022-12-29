#Files Renaming Deleting And Metadata

#!imp library for files
import os

#Removing file

os.remove('files/ToBeRemove.txt')
print('Deleted Done')


#Rename file
os.rename('files/Old.txt','files/New.txt')
print('Deleted Done')


#Checking if exists file
print(os.path.exists("Finish.txt"))

print(os.path.exists("Finish2.txt"))

#Get size of  file
print(os.path.getsize("Finish.txt"))

#Get file creation time
print(os.path.getmtime("Finish.txt"))

#Get Absoulte Path
print(os.path.abspath("Finish.txt"))

os.remove('files/NoSuchFileWillGiveError.txt')
print('Deleted Done')

