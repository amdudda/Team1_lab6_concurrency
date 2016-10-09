'''
This module object supposed to download the image links return from the googleApi.py module
in the main, then save it into the PIcs Directory for a later usage
'''

import urllib
from os.path import expanduser, join


def savePic(url):   #function that download image from the web and save it

    fileName = url.split('/')[-1]   #get the filename from the url

    # os method that joins the path name to the file name
    fullfileName = join("C:/Users/Yanirash/PycharmProjects/Team1_lab6_concurrency/Pics/", fileName)

    try:     # try to catch some anything that will stop this to be successfully executed

        print("saving file name:  {}".format(fileName))
        urllib.request.urlretrieve(url, fullfileName)
    except Exception as ie:
        print("Can't download file name {} error:".format(fileName), ie)


