import os
import shutil
from datetime import datetime


#Source directory
src = "c:/D/Documents"

#Destination directory
des = "C:/Devops/Projects"

#Create a timestamp folder for backup
timestamp = datetime.now().strftime('%Y%M%D_%H%M%S')
backup_folder = os.path.join(des, f'backup_{timestamp}')

#Create backup of the folder
try:
    shutil.copytree(src,des)
    print ("Back up completed at {backup_folder}")
except Exception as e:
    print("Error during backing {e}")
