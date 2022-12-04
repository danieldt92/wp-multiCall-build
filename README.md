Cuando se realiza un ataque de fuerza bruta contra XMLRPC.php en un Wordpress, se pueden incluir varias llamadas a usuario:contraseña en una sola petición POST usando el metodo interno "system.multicall", esto puede evitar ser bloqueado por execeder el numero de reintentos.

Esta sencilla herramienta carga un diccionario de contraseñas para un usuario especifico y devuelve un fichero txt con los payloads que pueden ser cargados en dicha peticion POST 


--

In a Brute Force attack against XMLRPC at Wordpress, multiple lines can be loaded in to a single POST request using the "system.multicall" method.

That allows you to simplify a Brute Force attack, and avoid some IP restrictions by POST request number.

This simple tool creates a list of payloads with different passwords for a specific user that can be used in that POST request.

Ex;
wpMultiBuild.py USERNAME PASSWORD_DIC.txt OUTPUTFILE.txt
