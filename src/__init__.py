import sys
import subprocess

# This command installs numpy specifically for the version of Python 
# currently being used by your VS Code editor.
subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])
print("NumPy is now installed for this environment!")

