import os

#print os.getcwd()

files = os.listdir( os.getcwd() )

f = open("manifest.txt", "w+")

for filename in files:
    if filename.endswith(".mp4"):
         f.write(filename+"\n")
f.close()

