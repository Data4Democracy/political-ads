from .api import callApi
from pymongo.write_concern import WriteConcern
from pymodm import MongoModel, fields
import hashlib

class Facility(MongoModel):
    '''
        Class for Facility. (https://publicfiles.fcc.gov/developer/)
    '''
    id = fields.MongoBaseField(primary_key=True)
    facilityId = fields.MongoBaseField()
    frequency = fields.MongoBaseField()
    callSign = fields.MongoBaseField()
    activeInd = fields.MongoBaseField()
    metadata = fields.MongoBaseField()

    def fetchMetadata(self):
        if not self.metadata:
            self.metadata = self.fetch()
        return self

    def search(keyword):
        '''
            Search for facility return array of results
            URL: https://publicfiles.fcc.gov/api/service/facility/search/WjLA.json
        '''

        entityUrl = "service/facility/search/{keyword}".format(keyword=keyword)
        response = callApi(entityUrl)
        return Facility.facilityList(response['results']['globalSearchResults']['tvFacilityList'])

    def facilityList(facilityList, fetchMetadata=False):
        '''
        Return Facility objects from facilityList JSON response.
        :return: list of objects of class facility.
        '''
        all_facilities = []

        for facility_obj in facilityList:
            facility_obj['facilityId'] = facility_obj.pop('id', None)
            facility_obj['id'] = hashlib.sha224(facility_obj['facilityId'].encode('utf-8')).hexdigest()
            all_facilities.append(Facility(**facility_obj))

        if fetchMetadata:
            facilities = [facility.fetchMetadata() for facility in all_facilities if facility]

        return facilities

    def fetch(self, serviceType="tv"):
        '''
            Call the facility API and return a populated facility object. Throw error if not found or more than one found.
            URL: https://publicfiles.fcc.gov/api/service/tv/facility/id/{id}.json
        '''

        entityUrl = "service/{serviceType}/facility/id/{entityID}".format(serviceType=serviceType, entityID=self.facilityId)
        results = callApi(entityUrl)['results']
        if results['facility']:
            metadata = results['facility']
        else: metadata = None
        return metadata

    def getAll(serviceType="tv", fetchMetaData=False, save=False):

        '''
        Fetch all available facilities for given serviceType
        :return: list of Facilities
        '''

        entityUrl = "service/{serviceType}/facility/getall".format(serviceType=serviceType)
        responses = callApi(entityUrl)
        facilityList = responses['results']['facilityList']
        if type(facilityList) is list and len(facilityList) > 0:
            facilities = Facility.facilityList(facilityList, fetchMetadata=fetchMetaData)
            if save:
                facilities = Facility.objects.bulk_create(facilities, retrieve=True)
            return facilities