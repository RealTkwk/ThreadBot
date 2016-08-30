# ThreadBot

This was made as a quick project to  see how the Reddit public API works. The script browses the comments section of r/all every two seconds checking for the '/thread' meme. When the desired string is found, the script simply replies to the comment with a message and stores the unique comment ID in order to avoid replaying more than once. 

To use simply install praw via `pip install praw` and create a file called `bot.cfg` that will have the Reddit account you wish to use in the first line and the password on the second line.

For more consistency this could vi run via a cron job on linux, erasing the `while True` loop. Right now it is written so it'd run without much hassle. 

