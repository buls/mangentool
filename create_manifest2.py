#Creates a JSON array of all the .mp4 videos in the root folder as JSON objects'''
import os
import json

class Video(object):
    def __init__(self, video, file_format):
        self.vclass = video[0]
        self.subject = video[1]
        self.term = video[2]
        self.term_week = video[3]
        self.lesson = video[4]
        self.lesson_part = video[5]
        self.file_format = file_format

    def __str__(self):
        return self.vclass+"\t"+ self.subject+"\t"+ self.term+"\t"+ self.term_week+"\t"+ self.lesson+"\t"+ self.lesson_part+"\t"+ self.file_format
'''The video class represents each video file with it's different attributes'''


file_format = ".mp4"
video_files = [] #list containing names of videos
final_list = []

files = os.listdir( os.getcwd() )

#f = open("manifest.txt", "w+")

for filename in files:
    if filename.lower().endswith(file_format):
         #f.write(filename+"\n")
         video = filename.lower().rstrip(file_format).split("_")
         vidObjects = Video(video, file_format)
         video_files.append(vidObjects)
#f.close()

#print "Class\tSubject\tTerm\tWeek\tLesson\tPart\tFormat"
for thefiles in video_files:
    final_list.append(vars(thefiles))

f = open('manifest.json', 'w')
json.dump(final_list, f, indent=2)
f.close()
