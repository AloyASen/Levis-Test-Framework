from unittest import result
from ..abstracts import __abstractComparator
import os, sys, json, configparser
#sector selector
from . import sectorSelect as sectors
#import  configuration command parser 
from . import commandParser as cmd
from . import businessLogic as br_rules
#import project level constants
sys.path.insert(1, os.path.realpath('../master'))
import projConstants


"""
Concrete Products are created by corresponding Concrete Factories.
"""

from ..abstracts import __abstractSource
from ..abstracts import __abstractTarget

class _comparator(__abstractComparator.AbstractComparator):
    def __init__(self) -> None:
        self.results =[]

    def useful_function_a(self) -> dict:
        return self.results

    def _comparator(self, collaborator_a_res , collaborator_b_res ):
        parser_proj= configparser.ConfigParser(delimiters=('='),interpolation=configparser.ExtendedInterpolation())
        parser_proj.read(projConstants.rs_flex_product_pyConfig_path)

        brandConfig = parser_proj.get ('Brand', projConstants.pyConfig_path_FlexBrandKey).split( sep=" ")
        brandVal = cmd.flexCmdControlCenter(brandConfig[0] , brandConfig[1], brandConfig[3], payload= collaborator_a_res, retrievalkey = parser_proj.get('flexCommon','DAOFieldvalue'))
        #selction of the parser sections required 
        if (brandVal == "Levi\'s") : 
            brandVal = 'Levis'
        categoryConfig = parser_proj.get ('Product Category', projConstants.pyConfig_path_FlexBrandKey).split( sep=" ")
        categoryVal = cmd.flexCmdControlCenter(categoryConfig[0] , categoryConfig[1], categoryConfig[3], payload= collaborator_a_res, retrievalkey = parser_proj.get('flexCommon','DAOFieldvalue'))
        genderConfig = parser_proj.get ('Gender', projConstants.pyConfig_path_FlexBrandKey).split( sep=" ")
        genderVal = cmd.flexCmdControlCenter(genderConfig[0] , genderConfig[1], genderConfig[3], payload= collaborator_a_res, retrievalkey = parser_proj.get('flexCommon','DAOFieldvalue'))

        sectionproxy = sectors.sectorSelect(brand= brandVal, gender=genderVal, category=categoryVal)

        for section_name in sectionproxy:
            # print ('Section:', section_name)
            # print ('Options:', parser.options(section_name))
            compareLock = 0
            print('sector Compute ::' , section_name)
            for name, value in parser_proj.items(section_name):

                if (compareLock <2 ):
                    if name == projConstants.pyConfig_path_FlexBrandKey :
                        # parse the flex commandlet and generate the value
                        flex = value.split(sep=" ")
                        flexCmpKey_inter = cmd.flexCmdControlCenter(flex[0] , flex[1], flex[3], payload= collaborator_a_res, retrievalkey = parser_proj.get('flexCommon','DAOFieldvalue'))
                        flexCmpKey = br_rules.stringBLRO(flexCmpKey_inter)
                        compareLock +=1
                        print('Lockval', compareLock)
                        print(flexCmpKey)
                    elif name == projConstants.pyConfig_path_PimBrandKey :
                        pimCmpKey_inter =cmd.RSCmdControlCenter(value, payload=collaborator_b_res)
                        pimCmpKey = br_rules.stringBLRO(pimCmpKey_inter)
                        compareLock +=1
                        print('Lockval', compareLock)
                        print(pimCmpKey)
                    else :
                        print (' error in the log enty ')
                        raise SystemExit
                
                if (compareLock ==2 ):
                    # prefill the results dictionary
                    if (flexCmpKey == pimCmpKey):
                        self.results.append({'attribute name' : section_name , 'FLEX Compare Key' : flexCmpKey_inter, 'PIM Compare Key' : pimCmpKey_inter, 'comparison result' : 'success'})
                        print( 'cmparison success')
                    else: 
                        self.results.append({'attribute name' : section_name , 'FLEX Compare Key' : flexCmpKey_inter, 'PIM Compare Key' : pimCmpKey_inter, 'comparison result' : 'failed'})
                        print( 'comapre not successful')
                        raise SystemExit
                    #refresh the lock 
                    compareLock =0
                    print ( 'lock refreshed ')
                    #refresh the data stores
                    flexCmpKey , pimCmpKey = '', ''        
        return self.results