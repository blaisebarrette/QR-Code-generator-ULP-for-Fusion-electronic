import os
import sys

# Add the application directory to the Python path
INTERP = os.path.expanduser("/usr/local/bin/python3.9")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())

# Import the Flask application
from server import app as application 