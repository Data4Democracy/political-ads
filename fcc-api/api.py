import requests
import requests_cache
import simplejson as json

requests_cache.install_cache('fcc', backend='sqlite', allowable_methods=('GET', 'POST'))

baseUrl = "https://publicfiles.fcc.gov/api/"

def callApi(reqUrl):
    '''
        Holding this here in case we might want to do some rate limits or proxying to local DB
    '''
    print(baseUrl + reqUrl + '.json')
    response = requests.get(baseUrl + reqUrl + '.json')
    if response.status_code == 200:
        response = response.json()
        if response['status'] == 'OK':
            return response
        else:
            # throw error
            #TODO HANDLE ERRORS
            print(response)
            return None
    else:
        print(response.status_code)

def checkComments(content):
    '''
    Check if object is valid JSON, also remove comments from the top of the file if any.
    :param content:
    :return:
    '''