First version of bot only responds to some key words that may be used in text channels.
Almost all of the code is in the main.py file.

The keep_alive.py file is a program that keeps the bot working on a replit server. To
use it, this import should be added:
import keep_alive as ka
And this function should be called before the last line of the code:
ka.keep_alive()

BEWARE: Should you use the code in replit:
	- The nest_asyncio module is not needed, neither is the function nest_asyncio.apply().
	It would be better to delete those lines.
	- VERY IMPORTANT: It is very risky to keep the Bot's Token in the code in repplit, since
	it is public by default, and can only be turned to private by buying premium.
	So, in the last line of the code, instead of the token itself, a TOKEN variable should
	be used instead:
		-Define the variable TOKEN in the 'Secrets' section of the replit sidebar
		-Add 'import os' in the begining of the code and write this function instead
		of the token itself:
		os.getenv('TOKEN')