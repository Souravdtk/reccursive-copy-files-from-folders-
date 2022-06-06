import shutil
import os

src=input('give complete source dir\n')
dest=input('give complete destination dir\n')

def rec(src):
    for s,d,f in os.walk(src):
        print(s,d,f)
        if f:
            for file in f:
                try:
                    shutil.copy(os.path.join(src,file), dest)
                except shutil.SameFileError:
                    print("Source and destination represents the same file.")
                except PermissionError:
                    print("Permission denied.")
                except:
                    print("Error occurred while copying file.")
        if d:
            for dirs in d:
                if os.path.join(src,dirs) == dest:
                    return
                else:
                    rec(os.path.join(src,dirs))
        else:
            return
    return


rec(src)
