import os
ROOT_PATH = os.getcwd()



# the path to project level config  
pyConfig_path = os.path.realpath(os.path.join(ROOT_PATH, 'config'))

pyConfig_path_FlexBrandKey = 'flex'
pyConfig_path_PimBrandKey = 'pim' 

#the path for project level dataset folders
#-----------------------------------------------------------------------------------------------
pyDataset_path = os.path.realpath(os.path.join(ROOT_PATH, 'dataset'))
##########################################################
flex_pyConfig_path = os.path.realpath(os.path.join(pyDataset_path, 'flex'))
flex_product_pyConfig_path = os.path.realpath(os.path.join(flex_pyConfig_path, 'product'))
flex_consumerChoice_pyConfig_path = os.path.realpath(os.path.join(flex_pyConfig_path, 'sku'))

pim_pyConfig_path = os.path.realpath(os.path.join(pyDataset_path, 'pim'))
pim_product_pyConfig_path = os.path.realpath(os.path.join(pim_pyConfig_path, 'product'))
pim_consumerChoice_pyConfig_path = os.path.realpath(os.path.join(pim_pyConfig_path, 'sku'))
###########################################################
results_pyConfig_path = os.path.realpath(os.path.join(ROOT_PATH, 'results'))

#------------------------------------------------------------------------------------------
# the sector combinations for the comparator is sent to this file
rs_flex_product_pyConfig_path = os.path.realpath(os.path.join(pyConfig_path, 'productPC5config.ini'))
rs_flex_consumerChoice_pyConfig_path = os.path.realpath(os.path.join(pyConfig_path, 'colorwayPC9config.ini'))

#----------------------------------------------------------------------------------------------------
#api constants for pim
WEBURL = 'levisfs01.riversand.com'
USER_EMAIL = 'levissystemadmin@riversand.com'
USER_ROLE = 'systemadmin'
CLIENT_ID = 'fG81mJ5NcEruUf5Ajl7C1fluM3EP8YhV'
CLIENT_KEY = 'kyj7wYolmc_H7qrQs_8z23D1D1ZELnwwljHSPfr1maonHh_MQ1-ZlqycwTDzgZC8'
USER_ID = 'levissystemadmin@riversand.com'
# main api url
url = 'https://'+WEBURL+'/api/entityservice/get'