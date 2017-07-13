[Conforming overview](https://www.rubbermonkeysoftware.com/support/monkey_extract/conforming/)

The following explains the workflow for getting footage from an editing software 
grading application.

What is conforming?
Conforming is the process of getting the footage of a finished cut out of the 
editing software, where it was edited using low quality footage, and into the 
grading software where it will be graded with high quality footage.

There's more to conforming - but let's focus on the task of getting footage into 
a grading system.

Conforming film projects
In order to understand conforming of digital footage, it's useful to know the 
workflow for projects shot on film, because that's what most grading tools were
designed for. Each step is explained further below.

1. The Editor edits low quality files, usually standard definition footage from DV tape.
2. The Editor exports an EDL of the finished cut.
3. The Film Lab scans the original negative to DPX files at high quality.
4. The colorist loads the EDL and the high quality DPX files into their system.
5. The colorist grades the high quality files and exports the finished product.

Conforming Red projects
The workflow for red footage is similar:

1. The editor edits low quality files - Quicktime Proxy files
2. The Editor exports an EDL of the finished cut.
3. Someone in post exports DPX files from original R3D negative at high quality.
4. The colorist loads the EDL and the high quality DPX files into their system.
5. The colorist grades the high quality files and exports the finished product.

Note that the 'Someone in post' position hasn't been defined. If you're reading 
this, then it's probably you!

Step 1: Editing
When editing footage, the editor is typically cutting a low quality representation 
of the actual footage. Why is that?

In the case of movies shot on film, the high quality footage is the film negative 
itself, which obviously can't be cut in a computer.

In the case of Red footage, none of the editing platforms can load the high quality 
files (R3D) and so editors cut using the low quality (Quicktime proxy) files. There 
are good technical reasons for this, but mainly it's due to processing power. 
One day we'll be able to edit R3D files, but not for a while.

Getting the RED footage into your editing system is beyond the scope of 
this document, but for Final Cut users, you can either edit the proxy files directly, 
or convert them to ProRes quicktimes.
Avid users need to import the proxy Quicktimes, which converts them to MXF files. 
See [RedUser.net](http://www.reduser.net/) for more information.

Step 2: Exporting an EDL or XML
After a cut is complete, the editor exports a text file containing a list of all
the edits of the film. You can export an 'Edit Decision List'(EDL) or an XML file. 
All editing software can export an EDL. Monkey extract also supports XML files 
from Avid or Final Cut. Export your EDL in the 'CMX 3600' format if you're 
going to use Monkey Extract in the next step.

Step 3: Creating high quality DPX files
Up until now, your project has been using low quality files. It's time to go 
back to the original footage and create high quality files.
Unlike editing software, grading software likes to work with image sequences.
Each frame is scanned or rendered as a DPX file, which is just an image file, 
but uncompressed.
Each file is at least 8 Mb in size, and a 90 minute feature will have 129,600 
of them.

Creating DPX files for projects shot on film
Each reel is loaded into a film scanner, and each frame scanned and saved as a 
DPX file.  These files are stored in folders numbered to match the reel number 
used in the editing software.

Creating DPX files for projects shot on Red
For Red projects we need to export the R3D files to DPX frames.
This is a time consuming process: If your system renders one frame per second, 
you are looking at one full day of rendering per hour of footage shot.

This is where Monkey Extract fits in - it speeds up the process by only exporting
frames that made the finished cut, so that you don't have to render everything.
Click here for [Monkey Extract documentation](https://www.rubbermonkeysoftware.com/support/monkey_extract.asp)

Step 4. Using an EDL to import DPX files into the grading system.
Ideally this is as simple as loading the EDL into the grading software, and 
pointing it at the folder containing the DPX files. Your colorist will have 
done this many times and should be right at home.

However it's useful to know the actual method the software uses to do the import, 
as it will help you prepare your exported footage correctly and understand any 
problems that occur.


DPX Files: what they are, and how should they be named
Each clip of your project needs to be exported to DPX files, one per frame. A 
one minute clip will export to 60 x 24 = 1440 files.

A DPX file is just a still image file, like a JPEG. You can load them into 
photoshop. DPX are unlike JPEG in that they are uncompressed, and so don't have 
any weird artifacts like you see in low res web images. They are high enough 
quality to use as the digital master for feature films - in fact, they are the standard.

Timecode
Each file is given a seven digit number, which represents it's timecode.
The file 0000001.dpx has the timecode 00:00:00:01

Each increment in timecode increments the file number by 1. So 00:00:05:00 is 
file number 0000120.dpx (5 seconds x 24 frames per second = frame 120) and so on.

Footage shot at different frames per second will equate to different frame 
numbers. You usually don't need to manually convert between frame number and 
timecode, but it's nice to know that you can.

DPX files also contain metadata - extra information stored in the header. The 
timecode number can be stored in the header and most grading software is capable 
of reading it, in fact that's where it will look first. However it's probably 
a good idea to export your DPX files with the timecode number as well.

File names
Most grading software will look at the metadata, or the last seven digits of 
the file name, and ignore everything else. So we can still keep the original 
Red file name, in case we have problems and need to figure out where a particular 
file came from.

A typical file name for an exported DPX frame would look like:

    A001_C001_20080909.0000001.dpx

    Monkey Extract can export Red File names, frame numbers only, or user specified 
    file names.

    Reels, Folders and Folder names
    The frames from each reel of footage are stored in folders, the folder name 
    being the same as the reel name used in the editing system. For Reel A001, it would be:

        /A001/A001_C001_20080909.0000001.dpx
	    /A001/A001_C001_20080909.0000002.dpx
	        etc.

		For Red projects, there is potential for a little bit of confusion.

		The reel number in an EDL can only be 8 characters.
		Red reel names when created on the camera are only 4 characters - e.g. A001.
		However, the Reel field on the quicktime proxy files contains the 
		entire clip name - e.g. A001_C001_20080808.
		When exporting an EDL, editing systems shorten the name so the 
		reel ends up being called A001C001.
		As far as the EDL is concerned, each clip used is in fact it's 
		own Reel.
		You might have used ten clips from Reel A001, but the EDL will 
		consider them to be 10 different reels because they have 10 different 
		names.

		This isn't a problem, but is something to bear in mind.
		A feature film shot on 100 reels that uses 1500 shots would have 
		100 folders, each containing the DPX frames for a number of clips.
		The same feature shot on Red would have 1500 folders each containing 
		one clip.

		If this is a problem for you, Monkey Extract can place the DPX frames 
		into one folder per reel, and create a new EDL converting the reel 
		names from A001C001 etc. to A001.


		EDL files explained
		An EDL is just a text file. It contains a list of all the footage 
		used, each edit, and each transition in your project. It lists the 
		footage by the reel name and the timecode.

		It's actually human readable. Here are three cuts from a typical EDL:

		cutreelClip INClip OUTProject INProject OUT
		001 B004C014 V C 01:53:10:20 01:54:49:09 01:00:00:00 01:01:38:14
		002 B004C016 V C 02:02:55:18 02:03:56:22 01:01:38:14 01:02:39:18
		003 B004C024 V C 02:30:04:17 02:31:15:05 01:02:39:18 01:03:50:06

		The first number on the left is the cut number. They start at 1
		and go up.
		The next block of 8 characters is the reel name. As you can see, 
		the Red reel name / clip name combo has been shortened from 
		B004_C014_20080909 to B004C014.
		The 4 right hand timecodes are In and Out points of the Project, 
		and the actual Clip used.
		Looking at the right hand project columns, you will see that the 
		first cut starts at 01:00:00:00 or 1 hour, and runs for 38 seconds 
		and 14 frames until 01:01:38:14.
		The second cut on line 2 starts at the point the first cut ended, 
		01:01:38:14.

		It's not usually necessary to open up an EDL but it can help you 
		solve problems if a shot is missing in the conform.

		The reason we're looking at it is to see what the grading system 
		sees.
		For Cut 001, it is going to look in a folder called B004C014 for 
		DPX frames numbered 169770 to 172234 - which equate to timecode 
		01:53:10:20 to 01:54:49:09

		If it doesn't find these files there will be a hole on the grading 
		system's timeline.
		If you're missing shots from your timeline, the way to find them 
		is to open the EDL, find the shot number, look up the folder and 
		see if there are exported DPX files in there.

		Conclusion

references:
[1](http://www.digital-intermediate.co.uk/DI/DIconform.htm) Conforming & Editing (EDLs / AAF) 

[2](http://blingdigital.com/blog/index.php/conforming-made-simple/) Conforming Made Simple


[3](https://www.crcpress.com/Film-and-Video-Production-in-the-Cloud-Concepts-Workflows-and-Best-Practices/James/p/book/9781138925045)
Film and Video Production in the Cloud: Concepts, Workflows, and Best Practices

[4](https://www.crcpress.com/Digital-Intermediates-for-Film-and-Video/James/p/book/9780240807027) Digital Intermediates for Film and Video
