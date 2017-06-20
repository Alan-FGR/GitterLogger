# GitterLogger
A Gitter Log Archiver in Py3k (Just Works™)

### Description
This dumps the Gitter log starting from the last message, it works iteratively so to update with new messages just run it again. It dumps a json file with {id:{date,name,html}}. The first run may take some time if the chat has lots of messages. In extreme situations it may hog your RAM because it doesn't have checks and is somewhat naive. It's used in production with success though (100k+ messages chats).

### How to use:
1. Paste your token in a token.txt file
2. Configure the room name, also check the message it sends (bottom of script)
3. Make sure line 4 is commented and line 5 isn't. Either install gitterpy (opt comment line 3) or clone recursively
