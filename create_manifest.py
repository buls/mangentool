'''
Reads the current directory for .mp4 video files,
    Checks if each filename meets the naming convention,
        Then renames files to lowercase if not already so,
            Then creates a JSON array of all the .mp4 videos as JSON objects and outputs to a manifest.iq file
'''

#ADD: gui, specify directory

import os
import json
import re


class Video(object):
    def __init__(self, video, file_format):
        self.vclass = video[0]
        self.subject = video[1]
        self.term = video[2]
        self.theme =  video[3]
        self.topic = video[4]
        self.lesson = video[5]
        self.lesson_part = video[6]
        self.videotitle = video[7]
        self.file_format = file_format

    def __str__(self):
        return self.vclass+"\t"+ self.subject+"\t"+ self.term+"\t"+ self.theme+"\t"+ self.topic+"\t"+ \
               self.lesson+"\t"+ self.lesson_part+"\t"+ self.videotitle+"\t"+ self.file_format
'''The video class represents each video file and it's different attributes'''

namingConvention = """Naming convention: class(p1-p3)_subject(mth,eng,bsc)_term(f,s,t)_theme(00)_topic(00)_lesson(000)\
_part(a-z)_videotitle(1 to 50 characters not begining with a space).mp4
\tExample: p1_mth_f_01_01_001_a_counting.mp4\n"""

file_format = ".mp4"
failedErrMsg = "FAILED.... \n\nThe folder contains " +file_format+ " files that do not meet the naming convention, \nplease correct and try again.\n"


def filename_is_valid(filename):
    name_pattern = re.compile("^p[1-3]_(mth|eng|bsc)_(f|s|t)_[0-9][0-9]_[0-9][0-9]_[0-9][0-9][0-9]_[a-z]_\S.{0,49}$")
        
    if name_pattern.match(filename):
        #print name + " is in a valid format"
        return True
    else:
        #print name + " is in an INVALID format"
        return False
"""checks that the file name matches the naming convention:"""


def rename_to_lower(originalfilename):
    #NEED TO ADD: if folder already contains originalfilename.lower(), return error a file with that name already exists
    print "\nrenaming " + "'" + originalfilename + "'" + " to " + originalfilename.lower(),
    os.rename(originalfilename, originalfilename.lower())

    #check success
    files = os.listdir( os.getcwd() )
    if originalfilename.lower() in files:
        print "...OK"
        return True
    else:
        print "...FAILED"
        return False
"""converts filenames to lowercase"""


video_files = []    #list containing names of videos
invalid_files = []  #list containing invalid file names
final_list = []


files = os.listdir( os.getcwd() )

for filename in files:
    if filename.lower().endswith(file_format):
        if filename_is_valid(filename.lower().rstrip(file_format)):
            if filename != filename.lower():
                rename_to_lower(filename)
            video = filename.lower().rstrip(file_format).split("_")         
            vidObjects = Video(video, file_format)
            video_files.append(vidObjects)
        else:
            invalid_files.append(filename)

#print "Class\tSubject\tTerm\tTheme\tTopic\tLesson\tPart\tFormat"
for thefiles in video_files:
    final_list.append(vars(thefiles))

f = open('manifest.iq', 'w')
json.dump(final_list, f, indent=2)
f.close()

if not invalid_files:
    print "\n" + "completed"
else:
    print failedErrMsg, "\n", namingConvention, "\n\tINVALID FILES:"
    for fname in invalid_files:
        print fname

raw_input("\npress ENTER to end...")
