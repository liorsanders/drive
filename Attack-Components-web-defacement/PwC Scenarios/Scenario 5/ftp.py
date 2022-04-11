# upload
import ftplib
session = ftplib.FTP(<'server.address.com'>,<'USERNAME'>,<'PASSWORD'>)
file = open(<'filename'>,'rb')                  # file to send
session.storbinary('STOR <filename>', file)     # send the file
file.close()                                    # close file and FTP
session.quit()

# download
import urllib

urllib.urlretrieve(<'ftp://server/path/to/file>'>, <file name>)
