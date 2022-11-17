#import the global constants and redirect trickle as needed 
import projConstants

'''
Syntax: class argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars=’-‘, fromfile_prefix_chars=None, argument_default=None, conflict_handler=’error’, add_help=True, allow_abbrev=True)

Parameters:

    prog– name of the program (default=sys.argv[0])
    usage– string describes the program usage(default: generated from arguments added to the parser)
    description– text to display before the argument help(default: none)
    epilog– text to display after the argument help (default: none)
    parents– list of ArgumentParser objects whose arguments should also be included
    formatter_class– class for customizing the help output
    prefix_chars– set of characters that prefix optional arguments (default: ‘-‘)
    fromfile_prefix_chars– set of characters that prefix files from which additional arguments should be read (default: None)
    argument_default– global default value for arguments (default: None)
    conflict_handler– strategy for resolving conflicting optionals (usually unnecessary)
    add_help– Add a -h/–help option to the parser (default: True)
    allow_abbrev– Allows long options to be abbreviated if the abbreviation is unambiguous. (default: True)

Syntax: ArgumentParser.add_argument(name or flags…[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])

Parameters:

    name or flags– either a name or list of option string
    action– basic type of action to be taken when this argument is encountered at the command line
    nargs– number of command-line arguments that should be consumed
    const– constant value required by some action and nargs selections
    default– value produced if the arguments are absent from the command line
    type– type to which the command line arguments should be converted.
    choices – A container of the allowable values for the argument
    required – Whether or not the command-line option may be omitted (optionals only)
    help– brief description of what the argument does
    metavar – A name for the argument in usage messages
    dest – The name of the attribute to be added to the object returned by parse_args()


Syntax: ArgumentParser.parse_args(args=None, namespace=None)

Parameter:

    args – List of strings to parse. The default is taken from sys.argv.
    namespace – An object to take the attributes. The default is a new empty Namespace object
'''

import argparse
import os

def __computeRelPath(string):
    # Check input does not contain spaces
    if (' ' in string):
        msg = f'\"{string}\" is not a single word'
        raise argparse.ArgumentTypeError(msg)
    else:
        string = os.path.abspath(string)
    return string

import src.nuutJob

#read from the command line 
parser = argparse.ArgumentParser(description="Use this program to troubleshoot the Flex to Pim integration events")

# Boolean flag (does not accept input data), with default value
parser.add_argument('-v', action="store_true", default=False)


# Retur the input via different parameter name
parser.add_argument('-f', '--filename',metavar='filename', dest='input_filename', required=True, type=__computeRelPath)

args = parser.parse_args()
#print(args.v) # verbosity

#call the nut scheduler with the arguments
src.nuutJob.nuutScheduler(filename=args.input_filename, rootPath=projConstants.ROOT_PATH)


