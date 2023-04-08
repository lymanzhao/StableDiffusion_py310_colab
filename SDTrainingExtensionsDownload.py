import os
from pathlib import *
import subprocess

extbasePath = Path.joinpath(Path.cwd(),"extensions")

extgitName=[
            
            "https://github.com/AlUlkesh/stable-diffusion-webui-images-browser",
            "https://github.com/hako-mikan/sd-webui-supermerger",
            "https://github.com/d8ahazard/sd_dreambooth_extension",
            "https://github.com/KohakuBlueleaf/a1111-sd-webui-locon",

    ]



for extgitName in extgitName:
    gitPath = Path.joinpath(extbasePath, Path(extgitName).name)
    if gitPath.exists():
        cmd = "cd %s && git pull" %(gitPath)
        subprocess.call(cmd, shell=True)
    
    else:

        cmd = "cd %s && git clone %s" %(extbasePath,extgitName)
        subprocess.call(cmd, shell=True)
