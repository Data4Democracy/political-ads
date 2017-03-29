import os
from .api import callApi, downloadFile
from pymodm import MongoModel, fields

class PoliticalFile(MongoModel):

    def __init__(self, fileObj):
        '''
        Initiate a political file

        {
            "file_id": "e84e063a-eb1e-bd96-3f32-db76d78c9f36",
            "file_name": "NextGen 01-18-17 to 01-23-17",
            "file_extension": "pdf",
            "file_size": "181094",
            "file_status": "com_cvt",
            "file_folder_path": "Political Files/2017/Non-Candidate Issue Ads/NextGen Climate Action/01-18-17 to 01-23-17",
            "folder_id": "57bab4e3-b517-9126-12cf-d9adf9d87cbc",
            "file_manager_id": "751f01eb-a938-41db-93dd-b47b719c2889",
            "create_ts": "2017-01-19T13:18:08-05:00",
            "last_update_ts": "2017-01-19T13:18:10-05:00"
        }

        '''

    id = fields.MongoBaseField()
    downloaded = fields.MongoBaseField(default=False)
    needs_ocr = fields.MongoBaseField(default=False)
    status = fields.MongoBaseField(default='initialized')
    isnab = fields.MongoBaseField(default=False)

    def fetchAll(entityId):
        '''
        Fetch all political files for a given facility
        https://publicfiles.fcc.gov/api/manager/search/key/Political%20File.json?entityId=1051
        '''
        entityUrl = "manager/search/key/Political File.json"
        params = {"entityId":entityId}
        folder_results = callApi(entityUrl, params)
        if folder_results:
            return [PoliticalFile(id=file.pop('file_id', 'Missing'), metadata=file) for file in folder_results['searchResult']['files']]
        else:
            return None


    def download(self):
            '''
            Download a political file.
            https://publicfiles.fcc.gov/api/manager/download/d51881d5-fe65-e976-81ee-3e5a626aaee6/7a21d601-1c1c-41b4-b8f2-a22dca06cade.pdf
            :param self:
            :return:
            '''
            folder_id = self.metadata['folder_id']
            file_manager_id = self.metadata['file_manager_id']
            file_name = self.metadata['file_name']
            if 'NAB' not in file_name:
                entityUrl = 'manager/download/{folder_id}/{file_manager_id}.pdf'.format(folder_id=folder_id, file_manager_id=file_manager_id)
                print(downloadFile(entityUrl))
            else:
                self.isnab = True


    def needOcr(self):
        '''
        Check for embedded text to decide if OCR is needed
        :return:
        '''
    def doOcr(self):
        '''
        Execute the OCR pipeline
        :return:
        '''

    def tabulaExtraction(self):
        '''
        Do Tabula extraction for current file
        :return: JSON output from Tabula.
        '''