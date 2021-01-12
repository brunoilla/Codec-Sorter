# moveCompleted
This python script is meant to sort types of media files that need to be reencoded. 

I use this script on my unraid server to sort out my new media between the files that are ready to go to plex and the ones that need to be reencoded to a more efficient codec. 

The  moveCompleted.py script, it is set to move all files that are not encoded in H.265 to the preConversion folder where handbreak will then reencode it.
If the file is already encoded in H.265 the script will move the file to the converted folder so It can be sent to the correct directory afterwards. 

