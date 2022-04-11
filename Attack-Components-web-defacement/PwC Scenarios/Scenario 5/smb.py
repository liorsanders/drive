import urllib
from smb.SMBHandler import SMBHandler
opener = urllib.request.build_opener(SMBHandler)
fh = opener.open(<path like u put in the explorer>)
data = fh.read()
data = fh.write()
fh.close()
