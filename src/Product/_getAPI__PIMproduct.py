from ..abstracts import __abstractTarget
import requests
import sys, os, json

#import project level constants
sys.path.insert(1,os.path.realpath('../master'))
import projConstants

"""
Concrete Products are created by corresponding Concrete Factories.
"""


class _getPIMProduct(__abstractTarget.AbstractTarget):
    def __init__(self) :
        self.headers = {
            'Content-Type':'application/json',
            'x-rdp-version':'8.1',
            'x-rdp-clientId':'rdpclient',
            'x-rdp-tenantId':'t1',
            'x-rdp-vendorName':'Nike',
            'x-rdp-userId': projConstants.USER_EMAIL,
            'x-rdp-userName':'Maryj',
            'x-rdp-firstName':'Mary',
            'x-rdp-lastName':'Jane',
            'x-rdp-userEmail': projConstants.USER_EMAIL,
            'x-rdp-userRoles':projConstants.USER_ROLE,
            'auth-client-id': projConstants.CLIENT_ID,
            'auth-client-secret': projConstants.CLIENT_KEY,
        }

    def useful_function_b(self,rsEntityId:str ='') -> str:
        payload = "{\n  \"params\": {\n    \"query\": {\n      \"ids\": [\""+rsEntityId+"\"],\n      \"filters\": {\n        \"typesCriterion\": [\n          \"style\"\n        ]\n      }\n    },\n    \"fields\": {\n      \"attributes\": [\"_ALL\"]\n    }\n  }\n}"
        response = requests.post(projConstants.url , headers= self.headers, data= payload).json()
        # response contains the geoJSON object,
        # store it to pim entity storage print it to the console
        #return the response for the comparator to use it 
        return response
    #todo ---- storage of pim results is remaining
    def storeResponseToFile(apiResponse, rsEntityStoragePath:str = ''):
        with open(rsEntityStoragePath , 'w') as res:
            res.write(json.dumps(apiResponse))