import os
from pathlib import *
import subprocess
currentPath = Path.cwd()

#print(extbasePath)

os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"

# [path for path in extbasePath.iterdir() if extbasePath.is_dir()]
# print([path for path in extbasePath.iterdir() if extbasePath.is_dir()])
extbasePath = Path.joinpath(Path.cwd(),"extensions")
extPath = [path for path in extbasePath.iterdir() if extbasePath.is_dir()]

for extPath in extPath:
    # print(extPath)
    extPath = extPath.as_posix()
    print(extPath)
    cmd = "cd %s && git config --global --add safe.directory %s && git pull" %(extPath,extPath)
    print(cmd)
    subprocess.call(cmd, shell=True)

    #print(extPath)

repobasePath = Path.joinpath(Path.cwd(),"repositories")
repoPath = [path for path in repobasePath.iterdir() if repobasePath.is_dir()]
for repoPath in repoPath:
    # print(repoPath)
    repoPath=repoPath.as_posix()
    cmd = "cd %s && git config --global --add safe.directory %s && git pull" %(repoPath,repoPath)
    print(cmd)
    subprocess.call(cmd, shell=True)