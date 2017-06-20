# GitterLogger
A Gitter Log Archiver in Py3k (Just Works™)

### Description

This dumps the Gitter log starting from the last message, it works perfectly iteratively so to update with new messages just run it again. It dumps a json file with {id{date,name,html}}. The first run may take a lot of time if the chat has lots of messages. In extreme situations it may hog your system because it doesn't have checks and is somewhat naive. It's used in production with success though (100k+ messages).

### How to use:
1. Paste your token in a token.txt file.
2. Configure the room name, also check the message it sends (bottom of script)
3. Make sure line 4 is commented and line 5 uncommented. Either install gitterpy (opt comment line 3) or clone recursive.
