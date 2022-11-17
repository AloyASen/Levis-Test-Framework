'''
this is utilized to parse the commands sent out from the config file into the nuutJobs

'''

#import the tokenizer
import json

def RSCmdControlCenter(searchpath:str, payload:dict={}) -> str :
    #calculating the search path 
    searchpage = searchpath.split(sep="/")
    JSON = payload
    #search for the value needed 
    # crude lookup 
    # print('datum path lookup :: ', searchpage)
    rsextract_intermediate = JSON[searchpage[0]] [searchpage[1]] [0] [searchpage[2]] [searchpage[3]] [searchpage[4]] [searchpage[5]]
    return rsextract_intermediate [0] [searchpage[6]] 
    


def flexCmdControlCenter(attriblist:str,fieldnameKey:str, searchPattern:str, payload:dict='.', retrievalkey= ' ') -> str :
    # search for array sequence and split according to LHS and RHS
    # load the file as JSON
    JSON = payload
    # print(JSON)
    for i in JSON[attriblist]:
        if (i[fieldnameKey]== searchPattern):
            print (f'{searchPattern} : {i[retrievalkey]}' )
            return i[retrievalkey]
