# this will eventually be totally recoded to run Google API stuff

#from urllib import request as Request, urlopen, URLError
import json, os, requests  # request documentation at http://requests.readthedocs.io/en/master/
import apikeys as AK
DEV = True  # set to false for production apps

def googleAPI(sitename, googleCustomSearchID, searchTerm = AK.G_SEARCH_STRING, gapikey = AK.G_API_KEY):
    #print(sitename,googleCustomSearchID)
    search_url = 'https://www.googleapis.com/customsearch/v1?q='
    search_url += searchTerm
    search_url += '&cx=' + googleCustomSearchID
    search_url += '&key=' + gapikey

    result = None

    try:
        response = requests.get(search_url)
        # response has a handy json methond that extracts JSON data from results
        json_data = response.json()
        # parse out the image URL found in the JSON object.  (Yes, it's buried that deep!)
        result = json_data['items'][0]['pagemap']['cse_image'][0]['src']
        # result=json_data
    except ConnectionError:
        # this happens if there's an error in the URL or somesuch.
        if DEV: print
        'No results retrieved. Got an error code.'
    except KeyError:
        # this happens if no results are returned - will silence this for production
        if DEV: print
        'No data returned.'
    finally:
        return(sitename,result)
