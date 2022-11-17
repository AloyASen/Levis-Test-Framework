'''
the rules that are implemented while the string values of attributes are taken for comparison
'''
import sys, os
sys.path.insert(1, os.path.realpath('../master'))
import projConstants

def stringBLRO(compareKey:str) -> str :
    #make the string as lower case and remove any apostrophe in the string 
    return compareKey.replace("'", "").lower()


def searchBLRO(list, platform):
    for i in range(len(list)):
        if list[i]['attribute name'] == platform:
            return True
    return False