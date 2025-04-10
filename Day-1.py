import os

folders = input("Emter the names of folders separated by space").split()
for folder in folders:
  
  try:
    files = os.listdir(folder)

  except FileNotFoundError:
     print ("Provide valid dir name")
     continue
  
  print("=========Listing the files for folder========" + folder)

  for file in files:
     print(file)

 
  