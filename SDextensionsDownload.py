import os
from pathlib import *
import subprocess

# os.environ["http_proxy"] = "http://127.0.0.1:7809"
# os.environ["https_proxy"] = "http://127.0.0.1:7809"

extbasePath = Path.joinpath(Path.cwd(),"extensions")

extgitName=[
            "https://github.com/kohya-ss/sd-webui-additional-networks",#
            "https://github.com/AlUlkesh/stable-diffusion-webui-images-browser",
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


################################################################

vaeModelsPath = Path.joinpath(Path.cwd(),"models/VAE")

if vaeModelsPath.exists():
    print("%s 已经存在" %vaeModelsPath)
    pass
else:  
    Path.mkdir(vaeModelsPath)

vaeModelshugeName=[
    "https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors",
]

if len(vaeModelshugeName) != 0:
    for vaeModelshugeName in vaeModelshugeName:
        cmd = "cd %s && wget -N -c  %s" %(vaeModelsPath,vaeModelshugeName)
        subprocess.call(cmd, shell=True)


#####################################################
# embeddings、TEXTUAL INVERSION
embeddingsPath = Path.joinpath(Path.cwd(),"embeddings")


embeddingshugeName=[
    "https://huggingface.co/datasets/gsdf/EasyNegative/resolve/main/EasyNegative.safetensors",# EasyNegative 

    ]

embeddingscivitName=[
    "https://civitai.com/api/download/models/5119",# Pure Eros Face
    "https://civitai.com/api/download/models/20068",# badhandv4，坏手 
    "https://civitai.com/api/download/models/19837",# badv3，坏身体
    "https://civitai.com/api/download/models/5637",# ng_deepnegative_v1_75t

    ]

if len(embeddingshugeName) != 0:
    for embeddingshugeName in embeddingshugeName:
        cmd = "cd %s && wget -N -c  %s" %(embeddingsPath,embeddingshugeName)
        subprocess.call(cmd, shell=True)
if len(embeddingscivitName) != 0:
    for embeddingscivitName in embeddingscivitName:
        cmd = "cd %s && aria2c -V -c --disable-ipv6 %s" %(embeddingsPath,embeddingscivitName)
        subprocess.call(cmd, shell=True)    

