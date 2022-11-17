from __future__ import annotations
from abc import ABC, abstractmethod

#this is used for entity mediation  
from .abstracts import __abstractRegressor

#import the differnt entity regressors into codebase 
from .Product import productRegressor
from .consumerChoice import consumerChoiceRegressor


def client_code(factory: __abstractRegressor, product_a_args:str='',product_b_args:str='', storageFilePath:str='') -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    product_a = factory.create_product_a()  # this should place the instances of individual product into the factory
    product_b = factory.create_product_b()  # this should place the instances of individual product into the factory
    product_c = factory.create_comparator_AB()   # this should place the comparator instance for the products in the factory
    product_d = factory.create_reportSyndicator() # this would store the comparator result into a csv

    print(f"{product_a.useful_function_a(product_a_args) }", end=" \n \n")
    print(f"{product_b.useful_function_b(product_b_args) }", end=" \n \n")


    print(f"{product_c._comparator(product_a.useful_function_a(product_a_args),product_b.useful_function_b(product_b_args))}", end=" \n \n")
    print(f"{product_d.storeResults(payload =product_c.useful_function_a(),blobstore= storageFilePath)}", end=" \n\n ")

# Function to convert number into string
# Switcher is dictionary data type here
def factorySwitcher(argument) -> __abstractRegressor.AbstractRegressor :
    switcher = {
        "product-Create": productRegressor.ProductRegressorFactory(),
        "product-Update": productRegressor.ProductRegressorFactory(),
        # "ConsumerChoice-Create": consumerChoiceRegressor.ConsumerChoiceRegressorFactory()

    }
 
    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(argument, None)


def nuutScheduler(filename='', rootPath='') :
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    import configparser 
    import os
    datagramLocator_parser = configparser.ConfigParser(delimiters=('='),interpolation=configparser.ExtendedInterpolation())
    datagramLocator_parser.read(filename)
    
    for section in datagramLocator_parser.sections():
        print (section)

        flexJSONpath = os.path.realpath(os.path.join(rootPath,'dataset','flex',datagramLocator_parser.get(section , 'flexFileRelPath'), datagramLocator_parser.get(section, 'flexFilename')))
        rsProductEntityID = datagramLocator_parser.get(section, 'pimEntityId')
        rsEntityStoragePath = os.path.realpath(os.path.join(rootPath,'dataset','pim',datagramLocator_parser.get(section, 'pimFileRelPath'), rsProductEntityID+'.json'))
        result_reporter = os.path.realpath(os.path.join(rootPath,'results',flexJSONpath.split(sep="\\")[-1] +'__compare__' + rsProductEntityID + '.xlsx'))
        client_code(factorySwitcher(section), product_a_args=flexJSONpath, product_b_args=rsProductEntityID, storageFilePath=result_reporter)
    # client_code(consumerChoiceRegressor.RegressorFactory())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    #client_code(ConcreteFactory2())