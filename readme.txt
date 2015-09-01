This document details the structure of the manifest file to be created by the Manifest Generation Tool.

Each video must be a .mp4 file.
The following are the video attributes we are interested in:

class: This denotes the class.
possible values are p1, p2, p3

subject: This denotes the subject.
possible values are mth, eng, bsc

term: This denotes the school term
possible values are f, s, t

week: This denotes the week in a term
possible values are 01, 02, 03, 04, 05, ..., 13

lesson: This denotes a subject's lesson
possible values are 01, 02, 03, ..., 45

part: This denotes the sub-part of a lesson. Lessons would be made up of multiple videos so this
attribute shows where a specific video falls as part of a lesson
possible values are a, b, c, d, e, ...

format: This denotes the file extension and format of the video file
possible values are mp4

SAMPLE VIDEO FILE NAME
Below os an example of video file name:

p1_mth_f_01_01_a.mp4

From the file name above we can tell the following:

p1 - primary 1
mth - maths
f - first term
01 - week 1
01 - lesson 1
a - part a (or the first video for the lesson)
mp4 - video file extension

STRUCTURE OF MANIFEST FILE
The structure of the manifest file should represent the content of the root folder together with the 
attributes of all the .mp4 videos contained in the root folder.
The contents of the manifest file should be in JSON format.

An example is given below:

{ class: "p1", subject: "mth", term: "f", week: "01", lesson: "01", part: "a" }

In pretty print format the JSON object above would look like so:

{
    class: "p1",
    subject: "mth",
    term: "f",
    week: "01",
    lesson: "01",
    part: "a" 
}

MODUS-OPERANDI
The manifest generation tool should therefore create a file that would have a JSON array of all the .mp4 videos in the 
specified root folder as JSON objects. An example is given below:

[{ class: "p1", subject: "mth", term: "f", week: "01", lesson: "01", part: "a", format: "mp4" },{ class: "p1", subject: "mth", term: "f", week: "01", lesson: "01", part: "b", format: "mp4" },
{ class: "p1", subject: "mth", term: "f", week: "01", lesson: "01", part: "c", format: "mp4" },{ class: "p1", subject: "mth", term: "f", week: "01", lesson: "01", part: "d", format: "mp4" }]

The JSON code above shows the contents of a typical manifest file

Have fun!