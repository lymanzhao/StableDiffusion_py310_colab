import os
from pathlib import *
import subprocess
currentPath = Path.cwd()
extbasePath = Path.joinpath(Path.cwd(),"extensions")
#print(extbasePath)

# os.environ["http_proxy"] = "http://127.0.0.1:7890"
# os.environ["https_proxy"] = "http://127.0.0.1:7890"

# [path for path in extbasePath.iterdir() if extbasePath.is_dir()]
# print([path for path in extbasePath.iterdir() if extbasePath.is_dir()])

extPath = [path for path in extbasePath.iterdir() if extbasePath.is_dir()]
for extPath in extPath:
    print(extPath)
    cmd = "cd %s && git config --global --add safe.directory %s" %(currentPath,extPath)
    subprocess.call(cmd, shell=True)
    #print(extPath)

repobasePath = Path.joinpath(Path.cwd(),"repositories")
repoPath = [path for path in repobasePath.iterdir() if repobasePath.is_dir()]
for repoPath in repoPath:
    print(repoPath)
    cmd = "cd %s && git config --global --add safe.directory %s" %(currentPath,repoPath)
    print(cmd)
    subprocess.call(cmd, shell=True)