import os
from pathlib import *
baseModelsPath = Path.joinpath(Path.cwd(),"models/Stable-diffusion")
loraModelsPath = Path.joinpath(Path.cwd(),"models/Lora")
print("0.SD 1.5基础模型")
print("1.chilloumix模型及其他Lora")
print("2.日式动漫风格")
print("3.国画水彩风格")
print("4.皮克斯3D风格")
print(".其他艺术风格")

selectModel=input("输入选项:")

if selectModel=="0":
#########################################################################################
#SD 1.5
    basecivitModelsName=[
    ]
    basehugModelsName=[
        "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.safetensors"#下载Stable-diffusion/v1-5-pruned.safetensors
    ]
    print (basehugModelsName)
    lorahugModelsName=[
            
    ]

    loracivitModelsName=[
    ]  
    

if selectModel=="1":
#########################################################################################
#真人照片风格
#下载chilloumix模型及其他Lora
    basecivitModelsName=[
                "https://civitai.com/api/download/models/11745", #chilloutmix_NiPrunedFp32Fix.safetensors
    ]
    basehugModelsName=[]
    lorahugModelsName=[
                "https://huggingface.co/Lyman/gwei/resolve/main/gwei_10.safetensors",
                "https://huggingface.co/Lyman/gwei/resolve/main/archives/japaneseDollLikeness_v10.safetensors",
                "https://huggingface.co/Lyman/gwei/resolve/main/archives/koreanDollLikeness_v10.safetensors",
    ]

    loracivitModelsName=["https://civitai.com/api/download/models/9969",#liuyifei_10.safetensors
                "https://civitai.com/api/download/models/20684",#taiwanDollLikeness_v10.safetensors
                "https://civitai.com/api/download/models/21656",#hanfu
                "https://civitai.com/api/download/models/16576",## epiNoiseoffset_v2.safetensors 史诗风格
                "https://civitai.com/api/download/models/19770",## Shallow Focus模拟聚焦

    ]    
else:
    pass

if selectModel=="2":
##############################################
# 日式动漫风格
    basecivitModelsName=[

    ]
    basehugModelsName=[
            "https://huggingface.co/andite/anything-v4.0/resolve/main/anything-v4.5-pruned.safetensors",#
    ]
    lorahugModelsName=[
            
    ]

    loracivitModelsName=["https://civitai.com/api/download/models/14533",# yojiShinkawaStyle
                "https://civitai.com/api/download/models/12610",#makotoShinkaiSubstyles 新海诚
                "https://civitai.com/api/download/models/7657",# studioGhibliStyle_offset.safetensors 吉卜力
                "https://civitai.com/api/download/models/6289",## ligneClaireStyleCogecha_v10.safetensors 焦茶
                "https://civitai.com/api/download/models/6617",# dalcefoNocopyV2.pt

    ]
else:
    pass
    
##############################################
# 国画水彩风格  
if selectModel=="3":

    basecivitModelsName=[

    ]
    basehugModelsName=[

    ]
    lorahugModelsName=[
            
    ]

    loracivitModelsName=["https://civitai.com/api/download/models/14856",# ## 墨心
                "https://civitai.com/api/download/models/20143",## 疏可走马1.1
                "https://civitai.com/api/download/models/20343",# ## 沁彩，水彩风格

    ]
else:
    pass
##############################################
# 下载3D风格的模型和Lora
if selectModel=="4":

    basecivitModelsName=[
        "https://civitai.com/api/download/models/18617",#pixarStyleModel_v10.safetensors 皮克斯风格 checkpoint
        "https://civitai.com/api/download/models/15236",#deliberate_v2.safetensors 基本模型
    ]
    basehugModelsName=[

    ]
    lorahugModelsName=[
            
    ]

    loracivitModelsName=["https://civitai.com/api/download/models/20450",#皮克斯lora
            "https://civitai.com/api/download/models/19770",## Shallow Focus模拟聚焦

    ]
else:
    pass

if len(basecivitModelsName) != 0:
    for basecivitModelsName in basecivitModelsName:
  
        cmd = "cd %s & aria2c -V -c  %s" %(baseModelsPath,basecivitModelsName)
        os.system(cmd)
if len(basehugModelsName) != 0:
    for basehugModelsName in basehugModelsName:
        cmd = "cd %s & wget -N -c  %s" %(baseModelsPath,basehugModelsName)
        os.system(cmd)
if len(loracivitModelsName) != 0:
    for loracivitModelsName in loracivitModelsName:
        cmd = "cd %s & aria2c -V -c  %s" %(loraModelsPath,loracivitModelsName)
        os.system(cmd)
if len(lorahugModelsName) != 0:
    for lorahugModelsName in lorahugModelsName:
        cmd = "cd %s & wget -N -c  %s" %(loraModelsPath,lorahugModelsName)
        os.system(cmd)
exit()



