import subprocess
import sys

out = subprocess.run(['ping', sys.argv[1]], capture_output=True)
print(out.stdout.decode())
