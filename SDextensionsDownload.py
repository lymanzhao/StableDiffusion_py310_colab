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
            "https://github.com/d8ahazard/sd_dreambooth_extension",
            "https://github.com/jexom/sd-webui-depth-lib",
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


#################################################################
# 下载controlnet Models
import os
from pathlib import *
controlnetModelsPath = Path.joinpath(Path.cwd(),"extensions/sd-webui-controlnet/models") #/content/stable-diffusion-webui/extensions/sd-webui-controlnet/models
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
    cmd = "cd %s && wget -N -c %s" %(controlnetModelsPath,controlnetModels)
    subprocess.call(cmd, shell=True)


#####################################################
# embeddings
embeddingsPath = Path.joinpath(Path.cwd(),"embeddings")


embeddingshugeName=[
    "https://huggingface.co/datasets/gsdf/EasyNegative/resolve/main/EasyNegative.safetensors",# EasyNegative 
    "https://civitai.com/api/download/models/5119",# Pure Eros Face
    "https://civitai.com/api/download/models/20068",# badhandv4，坏手 
    "https://civitai.com/api/download/models/19837",# badv3，坏身体

    ]

if len(embeddingshugeName) != 0:
    for embeddingshugeName in embeddingshugeName:
        cmd = "cd %s && wget -N -c  %s" %(embeddingsPath,embeddingshugeName)
        subprocess.call(cmd, shell=True)
#####################################################
# TEXTUAL INVERSION
textualinversionPath = Path.joinpath(Path.cwd(),"textual_inversion")

textualinversionshugeName=[ 

    ]
textualinversioncivitName=[
    "https://civitai.com/api/download/models/20068",# badhandv4，坏手 
    "https://civitai.com/api/download/models/19837",# badv3，坏身体


    ]

if len(textualinversionshugeName) != 0:
    for textualinversionshugeName in textualinversionshugeName:
        cmd = "cd %s && wget -N -c  %s" %(textualinversionPath,textualinversionshugeName)
        subprocess.call(cmd, shell=True)
if len(textualinversioncivitName) != 0:
    for textualinversioncivitName in textualinversioncivitName:
        cmd = "cd %s && aria2c -V -c  %s" %(textualinversionPath,textualinversioncivitName)
        subprocess.call(cmd, shell=True)