Multiple lines can be loaded in a single POST request against XMLRPC.php @ Wordpress using the "system.multicall" method.

That allows you to simplify a Brute Force attack, and avoid some IP restrictions by POST request number.

This simple tool creates a list of payloads with different passwords for a specific user that can be used in a single POST request.

USE; python3 wpMultiBuild.py USERNAME PASSWORD_DIC.txt OUTPUTFILE.txt
