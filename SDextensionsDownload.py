import os
from pathlib import *
import subprocess

# os.environ["http_proxy"] = "http://127.0.0.1:7809"
# os.environ["https_proxy"] = "http://127.0.0.1:7809"

extbasePath = Path.joinpath(Path.cwd(),"extensions")

extgitName=[
            "https://github.com/kohya-ss/sd-webui-additional-networks",#
            "https://github.com/AlUlkesh/stable-diffusion-webui-images-browser",
            "https://github.com/hako-mikan/sd-webui-supermerger",
            "https://github.com/Mikubill/sd-webui-controlnet",
            "https://github.com/fkunn1326/openpose-editor.git",
            "https://github.com/hnmr293/posex",

    ]



for extgitName in extgitName:
    gitPath = Path.joinpath(extbasePath, Path(extgitName).name)
    if gitPath.exists():
        cmd = "cd %s && git pull" %(gitPath)
        subprocess.call(cmd, shell=True)
    
    else:

        cmd = "cd %s && git clone %s" %(extbasePath,extgitName)
        subprocess.call(cmd, shell=True)
exit()

#################################################################
# 下载controlnet Models
import os
from pathlib import *
controlnetModelsPath = Path.joinpath(Path.cwd(),"extensions/sd-webui-controlnet/models")
controlnetModels=[
"https://huggingface.co/webui/ControlNet-modules-safetensors/resolve/main/control_canny-fp16.safetensors",
"https://huggingface.co/webui/ControlNet-modules-safetensors/resolve/main/control_depth-fp16.safetensors",
"https://huggingface.co/webui/ControlNet-modules-safetensors/resolve/main/control_hed-fp16.safetensors",
"https://huggingface.co/webui/ControlNet-modules-safetensors/resolve/main/control_mlsd-fp16.safetensors",
"https://huggingface.co/webui/ControlNet-modules-safetensors/resolve/main/control_normal-fp16.safetensors",
"https://huggingface.co/webui/ControlNet-modules-safetensors/resolve/main/control_openpose-fp16.safetensors",
"https://huggingface.co/webui/ControlNet-modules-safetensors/resolve/main/control_scribble-fp16.safetensors",
"https://huggingface.co/webui/ControlNet-modules-safetensors/resolve/main/control_seg-fp16.safetensors",

"https://huggingface.co/webui/ControlNet-modules-safetensors/resolve/main/t2iadapter_canny-fp16.safetensors",
"https://huggingface.co/webui/ControlNet-modules-safetensors/resolve/main/t2iadapter_color-fp16.safetensors",
"https://huggingface.co/webui/ControlNet-modules-safetensors/resolve/main/t2iadapter_depth-fp16.safetensors",
"https://huggingface.co/webui/ControlNet-modules-safetensors/resolve/main/t2iadapter_keypose-fp16.safetensors",
"https://huggingface.co/webui/ControlNet-modules-safetensors/resolve/main/t2iadapter_openpose-fp16.safetensors",
"https://huggingface.co/webui/ControlNet-modules-safetensors/resolve/main/t2iadapter_seg-fp16.safetensors",
"https://huggingface.co/webui/ControlNet-modules-safetensors/resolve/main/t2iadapter_sketch-fp16.safetensors",
"https://huggingface.co/webui/ControlNet-modules-safetensors/resolve/main/t2iadapter_style-fp16.safetensors",
]

for controlnetModels in controlnetModels:
    cmd = "cd %s & wget -N -c %s" %(controlnetModelsPath,controlnetModels)
    subprocess.call(cmd, shell=True)
exit()


