'''
This module object supposed to download the image links return from the googleApi.py module
in the main, then save it into the PIcs Directory for a later usage
'''

import urllib, time
from os.path import expanduser, join


def savePic(fname, url):   #function that download image from the web and save it

    #fileName = url.split('/')[-1]   #get the filename from the url
    cur_time = (time.localtime())
    datestamp = str(cur_time[0]) + str(cur_time[1]) + str(cur_time[2])
    fileName = datestamp + fname + ".jpg"
    # os method that joins the path name to the file name
    fullfileName = join("Pics/", fileName)

    try:     # try to catch some anything that will stop this to be successfully executed

        print("saving file name:  {}".format(fileName))
        urllib.request.urlretrieve(url, fullfileName)
    except Exception as ie:
        print("Can't download file name {} error:".format(fileName), ie)


