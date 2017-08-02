import configparser
import os
import sys

try:
    dir = os.path.dirname(os.path.realpath(__file__))
    config = configparser.ConfigParser()
    config.read([os.path.join(dir, 'credentials.cfg')])
except Exception as error:
    msg = os.linesep + 'An error occured - ' + str(type(error).__name__ + ' : ' + ' '.join(error.args)) + os.linesep
    print(msg)
    sys.stderr.write(msg)
    sys.exit(1)
