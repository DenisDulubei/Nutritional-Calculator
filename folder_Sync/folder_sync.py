#importing the required modules

import os
import shutil
import hashlib
def main():
    source_folder=input("insert the path of the source folder")
    replica_folder=input("insert the path of the replica folder")
    #checking if replica folder exists and creating it if it does not
    if not os.path.exists(replica_folder):
        os.mkdir(replica_folder)
    folder_sync(source_folder,replica_folder)
#define a function that will initialize an instance of the md5 object from the hashlib module 
# open the file at the specified path and read the file in chunks of 4096 bytes
# for each chunk of bites read the function will update the hash object and will 
#generate a new hash value and in the end the funciton will return a hexadecimal string 
# of the computed hash value
def md5(file_path):
    hash_md5=hashlib.md5()
    with open (file_path, "rb") as file:
        for chunk in iter(lambda:file.read(4096),b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
#define a funciton that will check the presence of  each item form the source folder in the 
#replica folder
def folder_sync(source,replica):
    for item in os.listdir(source):
        source_path=os.path.join(source,item)
        replica_path=os.path.join(replica,item)

        if os.path.isdir(source_path):
            if not os.path.isdir(replica_path):
                os.mkdir(replica_path) #Create the folder in replica_folder if it does not exists
            folder_sync(source_path,replica_path) # recousively iterate throuch all the folders in the source folder
        else:
            source_md5=md5(source_path) #hash through the files of the source folder
            replica_md5=""
            if os.path.exists(replica_path):
                if os.path.isfile(replica_path):
                    replica_md5=md5(replica_path)#hash through the files of the replica folder
                else:continue
            
            if source_md5 != replica_md5:#if there are folders or files that are present in the source folder but not in the replica
                shutil.copy2(source_path,replica_path)#coppy those files into the replica folder
                print(f"Copying file, {source_path} to {replica_path}")
            else:
                print(f"Skipping file {source_path}")
            
if __name__=="__main__":
    main()


