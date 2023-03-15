import os
from pathlib import *
import subprocess

baseModelsPath = Path.joinpath(Path.cwd(),"models/Stable-diffusion")
loraModelsPath = Path.joinpath(Path.cwd(),"models/Lora")

if loraModelsPath.exists():
    print("%s 已经存在" %loraModelsPath)
    pass
else:  
    Path.mkdir(loraModelsPath)


print("0.SD 1.5基础模型及Lora")
print("1.chilloumix模型及Lora")
print("2.日式动漫风格")
print("3.国画水彩风格")
print("4.皮克斯3D风格")
print("5.故事板和分镜风格")
print("6.艺术和混合风格")
print("7.SD 2.1及同类")
print("可多选，以逗号分隔……")

selectModelclass=input("输入选项:")
selectModel=[item.strip() for item in selectModelclass.split(',')]

for selectModel in selectModel:
        
    if selectModel=="0":
    #########################################################################################
    #SD 1.5
        basecivitModelsName=[
        ]
        basehugModelsName=[
            "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.safetensors"#下载Stable-diffusion/v1-5-pruned.safetensors
        ]
    
        lorahugModelsName=[
                "https://huggingface.co/Lyman/gwei/resolve/main/gwei_10.safetensors",
                "https://civitai.com/api/download/models/21656",#hanfu
                "https://civitai.com/api/download/models/16677",#Cute_girl_mix4
        ]

        loracivitModelsName=[
        ]  
        

    if selectModel=="1":
    #########################################################################################
    #真人照片风格
    #下载chilloumix模型及其他Lora
        basecivitModelsName=[
                    #"https://civitai.com/api/download/models/11745", #chilloutmix_NiPrunedFp32Fix
                    "https://civitai.com/api/download/models/11732", #chilloutmix_NiPrunedFp16Fix
        ]
        basehugModelsName=[

        ]
        lorahugModelsName=[
                    "https://huggingface.co/Lyman/gwei/resolve/main/gwei_10.safetensors",
                    "https://huggingface.co/Lyman/gwei/resolve/main/archives/japaneseDollLikeness_v10.safetensors",
                    "https://huggingface.co/Lyman/gwei/resolve/main/archives/koreanDollLikeness_v10.safetensors",
        ]

        loracivitModelsName=["https://civitai.com/api/download/models/9969",#liuyifei_10.safetensors
                    "https://civitai.com/api/download/models/20684",#taiwanDollLikeness_v10.safetensors
                    "https://civitai.com/api/download/models/16677",#Cute_girl_mix4
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

        loracivitModelsName=[
            "https://civitai.com/api/download/models/14533",# yojiShinkawaStyle
                    "https://civitai.com/api/download/models/12610",#makotoShinkaiSubstyles 新海诚
                    "https://civitai.com/api/download/models/7657",# studioGhibliStyle_offset.safetensors 吉卜力
                    "https://civitai.com/api/download/models/10913",# studioGhibliStyle.safetensors 吉卜力
                    "https://civitai.com/api/download/models/22017",## Cogecha_v3 焦茶 https://civitai.com/models/5406/ligne-claire-stylecogecha
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
                    "https://civitai.com/api/download/models/21173",# ## 沁彩，水彩风格 v4
                    "https://civitai.com/api/download/models/22652",# ## 小人书·连环画 xiaorenshu
                    "https://civitai.com/api/download/models/21656",#hanfu

        ]
    else:
        pass
    #########################################################################################
    # 下载皮克斯3D风格的模型和Lora
    if selectModel=="4":

        basecivitModelsName=[
            "https://civitai.com/api/download/models/18617",# "pixarstyle",pixarStyleModel_v10.safetensors" 皮克斯风格 checkpoint"
            "https://civitai.com/api/download/models/15236",#deliberate_v2.safetensors 基本模型
            # "https://civitai.com/api/download/models/22534",#ph.d.mix 基本模型
        ]
        basehugModelsName=[

        ]
        lorahugModelsName=[
                
        ]

        loracivitModelsName=["https://civitai.com/api/download/models/20450",#"pixarstyle"
                "https://civitai.com/api/download/models/19770",## Shallow Focus模拟聚焦
                "https://civitai.com/api/download/models/7804",#"Sam Yang" SamDoesArts (Sam Yang) Style LoRA

        ]
    else:
        pass

    ####################################################################
    # 故事板和分镜
    if selectModel=="5":

        basecivitModelsName=[
            "https://civitai.com/api/download/models/18446",# dalcefoPainting_3rd
            
            "https://civitai.com/api/download/models/15236",#deliberate_v2
        ]
        basehugModelsName=[
            "https://huggingface.co/Sandro-Halpo/SamDoesArt-V3/resolve/main/SamDoesArt-V3.safetensors",#SamDoesArt
            "https://huggingface.co/andite/anything-v4.0/resolve/main/anything-v4.5-pruned.safetensors",#

        ]
        lorahugModelsName=[
                
        ]

        loracivitModelsName=[       
                "https://civitai.com/api/download/models/7804",#"Sam Yang" SamDoesArts (Sam Yang) Style LoRA
                "https://civitai.com/api/download/models/14533",# “shinkawa youji”
                "https://civitai.com/api/download/models/23169"#limited palette

        ]
    else:
        pass


    ##############################################
    # 艺术和混合风格  
    if selectModel=="6":

        basecivitModelsName=[
            "https://civitai.com/api/download/models/18446",# dalcefoPainting_3rd

        ]
        basehugModelsName=[
            "https://huggingface.co/prompthero/openjourney/resolve/main/mdjrny-v4.safetensors",# "mdjrny-v4 style"
            #"https://huggingface.co/dallinmackay/Van-Gogh-diffusion/resolve/main/Van-Gogh-Style-lvngvncnt-v2.ckpt",#lvngvncnt style

        ]
        lorahugModelsName=[
            "https://huggingface.co/andite/pastel-mix/resolve/main/pastelmix-lora.safetensors",#pastelmix-lora
            "https://huggingface.co/prompthero/openjourney-lora/resolve/main/openjourneyLora.safetensors",#openjourneyLora #https://huggingface.co/prompthero/openjourney-lora
                
        ]

        loracivitModelsName=["https://civitai.com/api/download/models/6617",# dalcefoNocopyV2.pt
                

        ]
    else:
        pass

    ##############################################
    # SD 2.1 
    if selectModel=="7":

        basecivitModelsName=[
            "https://civitai.com/api/download/models/13259",# Illuminati Diffusion

        ]
        basehugModelsName=[
            "https://huggingface.co/stabilityai/stable-diffusion-2-1/resolve/main/v2-1_768-ema-pruned.safetensors",# SD2.1
  

        ]
        lorahugModelsName=[
           
                
        ]

        loracivitModelsName=[
            

        ]
    else:
        pass

    ##############################################

    if len(basecivitModelsName) != 0:
        for basecivitModelsName in basecivitModelsName:   
            cmd = "cd %s && aria2c -V -c  %s" %(baseModelsPath,basecivitModelsName)
            # os.system(cmd)
            subprocess.call(cmd, shell=True)
    if len(basehugModelsName) != 0:
        for basehugModelsName in basehugModelsName:
            cmd = "cd %s && wget -N -c  %s" %(baseModelsPath,basehugModelsName)
            # os.system(cmd)
            subprocess.call(cmd, shell=True)
    if len(loracivitModelsName) != 0:
        for loracivitModelsName in loracivitModelsName:
            cmd = "cd %s && aria2c -V -c  %s" %(loraModelsPath,loracivitModelsName)
            # os.system(cmd)
            subprocess.call(cmd, shell=True)
    if len(lorahugModelsName) != 0:
        for lorahugModelsName in lorahugModelsName:
            cmd = "cd %s && wget -N -c  %s" %(loraModelsPath,lorahugModelsName)
            # os.system(cmd)
            subprocess.call(cmd, shell=True)





