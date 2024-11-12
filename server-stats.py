import subprocess
import os
import platform


print(os.cpu_count())
print(platform.system())

if platform.system() == "Darwin":
    result = subprocess.run(["top", "-i1", "-l1"], capture_output=True, text=True )
    output = result.stdout.splitlines()

