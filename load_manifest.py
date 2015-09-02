#test loading the manifest file
import json

f = open('manifest.json')

videos = json.load(f)

#print videos[0]["term"]

for i in videos:
     print i
