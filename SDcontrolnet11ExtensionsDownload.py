import os
from pathlib import *
import subprocess

extbasePath = Path.joinpath(Path.cwd(),"extensions")

extgitName=[
            "https://github.com/Mikubill/sd-webui-controlnet",
            "https://github.com/jexom/sd-webui-depth-lib",
            "https://github.com/nonnonstop/sd-webui-3d-open-pose-editor",
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
"https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11e_sd15_ip2p_fp16.safetensors",
"https://huggingface.co/lllyasviel/ControlNet-v1-1/blob/main/control_v11e_sd15_ip2p.yaml",
"https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11e_sd15_shuffle_fp16.safetensors",
"https://huggingface.co/lllyasviel/ControlNet-v1-1/blob/main/control_v11e_sd15_shuffle.yaml",
"https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11f1p_sd15_depth_fp16.safetensors",
"https://huggingface.co/lllyasviel/ControlNet-v1-1/blob/main/control_v11f1p_sd15_depth.yaml",
"https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11f1e_sd15_tile.pth",
"https://huggingface.co/lllyasviel/ControlNet-v1-1/blob/main/control_v11f1e_sd15_tile.yaml",
"https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_canny_fp16.safetensors",
"https://huggingface.co/lllyasviel/ControlNet-v1-1/blob/main/control_v11p_sd15_canny.yaml",
"https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_inpaint_fp16.safetensors",
"https://huggingface.co/lllyasviel/ControlNet-v1-1/blob/main/control_v11p_sd15_inpaint.yaml",
"https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_lineart_fp16.safetensors",
"https://huggingface.co/lllyasviel/ControlNet-v1-1/blob/main/control_v11p_sd15_lineart.yaml",
"https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_mlsd_fp16.safetensors",
"https://huggingface.co/lllyasviel/ControlNet-v1-1/blob/main/control_v11p_sd15_mlsd.yaml",
"https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_normalbae_fp16.safetensors",
"https://huggingface.co/lllyasviel/ControlNet-v1-1/blob/main/control_v11p_sd15_normalbae.yaml",
"https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_openpose_fp16.safetensors",
"https://huggingface.co/lllyasviel/ControlNet-v1-1/blob/main/control_v11p_sd15_openpose.yaml",
"https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_scribble_fp16.safetensors",
"https://huggingface.co/lllyasviel/ControlNet-v1-1/blob/main/control_v11p_sd15_scribble.yaml",
"https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_seg_fp16.safetensors",
"https://huggingface.co/lllyasviel/ControlNet-v1-1/blob/main/control_v11p_sd15_seg.yaml",
"https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_softedge_fp16.safetensors",
"https://huggingface.co/lllyasviel/ControlNet-v1-1/blob/main/control_v11p_sd15_softedge.yaml",
"https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15s2_lineart_anime_fp16.safetensors",
"https://huggingface.co/lllyasviel/ControlNet-v1-1/blob/main/control_v11p_sd15s2_lineart_anime.yaml",
]

for controlnetModels in controlnetModels:
    cmd = "cd %s && wget -N -c %s" %(controlnetModelsPath,controlnetModels)
    subprocess.call(cmd, shell=True)
