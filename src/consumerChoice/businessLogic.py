'''
the rules that are implemented while the string values of attributes are taken for comparison
'''

def stringBLRO(compareKey:str) -> str :
    #make the string as lower case and remove any apostrophe in the string 
    return compareKey.replace("'", "").lower()
