This code is ready to use, but its functionality is very poor, it will just play one song with !play
It can also !pause !resume and !stop. If you want it to, the bot can also !leave a voice channel.
I still didn't try to make it work on repplit to have it working 24/7 in the cloud, but I'm willing to.
Also will add more features soon, like playlist creation and search for music.

IMPORTANT INFFO PWEAS READ:

To get this bot working it is mandatory to have FFMPEG installed in your PC. In this link https://ffmpeg.org/download.html
are all the updated versions.

Windows instructions:
	- Download the latest build from this option: https://www.gyan.dev/ffmpeg/builds/
	- Extract files to any location and rename the folder that contains bin, doc and presets to 'ffmpeg'
	- Place the 'ffmpeg' folder in C:/Programs/ffmpeg
	- "Install" the program by adding the directory 'C://Programs/ffmpeg/bin' to the PATH, so it can be callable from
	anywhere in windows.
	- Note: You can place the ffmpeg folder in any other directory, but it is very important to add it to the PATH.

LINUX instructions to run 'on the go':
	- Go to the 'dependencies' folder and read the README.md file.
	- Once the previous step is done, you should be able to run the bot by:
		python3 music_player.py