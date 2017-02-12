from api import callApi

class Facility(object):
    '''
        Class for Facility. (https://publicfiles.fcc.gov/developer/)
    '''

    def __init__(self, id, metadata=None):
        '''Initiate an API Instance'''

        if type(id) is int or id.isnumeric():
            #Initiate using facility id
            self.id = id
            if not hasattr(self, 'metadata') and (metadata is None or len(metadata.keys()) <= 4):
                self.metadata = self.fetch()
            elif metadata is not None:
                self.metadata = metadata
            else:
                print('Bad id for facility')
                #TODO: Throw error if id is wrong
                return None
            print(self.metadata)
        #else:
            #ID has to be numeric, throw an error

    def search(keyword):
        '''
            Search for facility return array of results
            URL: https://publicfiles.fcc.gov/api/service/facility/search/WjLA.json
        '''

        entityUrl = "service/facility/search/{keyword}".format(keyword=keyword)
        response = callApi(entityUrl)
        return Facility.facilityList(response['results']['globalSearchResults']['tvFacilityList'])

    def facilityList(facilityList):
        '''
        Return Facility objects from facilityList JSON response.
        :return: list of objects of class facility.
        '''

        return [Facility(facility_obj['id'], facility_obj) for facility_obj in facilityList]

    def fetch(self, serviceType="tv"):
        '''
            Call the facility API and return a populated facility object. Throw error if not found or more than one found.
            URL: https://publicfiles.fcc.gov/api/service/tv/facility/id/{id}.json
        '''

        entityUrl = "service/{serviceType}/facility/id/{entityID}".format(serviceType=serviceType, entityID=self.id)
        return callApi(entityUrl)

    def getAll(serviceType="tv"):

        '''
        Fetch all available facilities for given serviceType
        :return: list of Facilities
        '''

        entityUrl = "service/{serviceType}/facility/getall".format(serviceType=serviceType)
        responses = callApi(entityUrl)
        facilityList = responses['results']['facilityList']
        if type(facilityList) is list and len(facilityList) > 0:
            return Facility.facilityList(facilityList)