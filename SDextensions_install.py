import os
from pathlib import *

# os.environ["http_proxy"] = "http://127.0.0.1:7809"
# os.environ["https_proxy"] = "http://127.0.0.1:7809"

#########################################################################
#安装插件
## 安装stable-diffusion-webui-images-browser
## https://github.com/AlUlkesh/stable-diffusion-webui-images-browser
gitPath = Path.joinpath(Path.cwd(),"extensions/stable-diffusion-webui-images-browser")

if Path.exists(gitPath):
    print("已下载:%s" %(gitPath))
    cmd = "cd %s & git pull" %(gitPath)
    
    os.system(cmd)
   
else:
    gitPath = Path.joinpath(Path.cwd(),"extensions")
    cmd = "cd %s & git clone https://github.com/AlUlkesh/stable-diffusion-webui-images-browser" %(gitPath) 
    os.system(cmd)
    
## 安装sd-webui-controlnet
## https://github.com/Mikubill/sd-webui-controlnet.git
gitPath = Path.joinpath(Path.cwd(),"extensions/sd-webui-controlnet")

if Path.exists(gitPath):
    print("已下载:%s" %(gitPath))
    cmd = "cd %s & git pull" %(gitPath)
    
    os.system(cmd)
   
else:
    gitPath = Path.joinpath(Path.cwd(),"extensions")
    cmd = "cd %s & git clone https://github.com/Mikubill/sd-webui-controlnet.git" %(gitPath) 
    os.system(cmd)

    
## 安装openpose-editor
## https://github.com/fkunn1326/openpose-editor.git
gitPath = Path.joinpath(Path.cwd(),"extensions/openpose-editor")

if Path.exists(gitPath):
    print("已下载:%s" %(gitPath))
    cmd = "cd %s & git pull" %(gitPath)
    
    os.system(cmd)
   
else:
    gitPath = Path.joinpath(Path.cwd(),"extensions")
    cmd = "cd %s & git clone https://github.com/fkunn1326/openpose-editor.git" %(gitPath) 
    os.system(cmd)


## 安装posex
## https://github.com/hnmr293/posex
gitPath = Path.joinpath(Path.cwd(),"extensions/posex")

if Path.exists(gitPath):
    print("已下载:%s" %(gitPath))
    cmd = "cd %s & git pull" %(gitPath)
    
    os.system(cmd)
   
else:
    gitPath = Path.joinpath(Path.cwd(),"extensions")
    cmd = "cd %s & git clone https://github.com/hnmr293/posex" %(gitPath) 
    os.system(cmd)

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
    os.system(cmd)
exit()


#########################################################################################
