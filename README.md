# GitterLogger
A Gitter Log Archiver in Py3k (Just Works™)

This dumps the Gitter log starting from the last message, it works perfectly iteratively so to update with new messages just run it again. It dumps a json file with {id{date,name,html}}.

How to use:
1-Paste your token in a token.txt file.
2-Configure the room name, also check the message it sends (bottom of script)
3-Make sure line 4 is commented and line 5 uncommented. Either install gitterpy (opt comment line 3) or clone recursive.
