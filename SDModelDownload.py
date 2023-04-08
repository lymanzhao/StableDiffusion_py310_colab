import os
from pathlib import *
import subprocess

baseModelsPath = Path.joinpath(Path.cwd(),"models/Stable-diffusion")
loraModelsPath = Path.joinpath(Path.cwd(),"models/Lora")
vaeModelsPath = Path.joinpath(Path.cwd(),"models/VAE")

if loraModelsPath.exists():
    print("%s 已经存在" %loraModelsPath)
    pass
else:  
    Path.mkdir(loraModelsPath)
if vaeModelsPath.exists():
    print("%s 已经存在" %vaeModelsPath)
    pass
else:  
    Path.mkdir(vaeModelsPath)

print("0.SD 1.5基础模型及Lora")
print("1.chilloumix模型及Coser")
print("1a.照片")
print("2.日式动漫风格")
print("3.国画水彩风格")
print("4.皮克斯3D风格")
print("5.故事板和分镜风格")
print("6.电影风格")
print("7.2.5D 混合风格")
print("8.纯艺术")
print("9.SD 2.1及同类")
print("10.科幻风格")
print("11.训练用基本模型")
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

        ]

        loracivitModelsName=[
                "https://civitai.com/api/download/models/27946",#hanfu
                "https://civitai.com/api/download/models/16677",#Cute_girl_mix4
        ]  
        

    if selectModel=="1":
    #########################################################################################
  
    #下载chilloumix模型及其他Coser
        basecivitModelsName=[
                   "https://civitai.com/api/download/models/11745", #chilloutmix_NiPrunedFp32Fix
                    #"https://civitai.com/api/download/models/11732", #chilloutmix_NiPrunedFp16Fix
                    #"https://civitai.com/api/download/models/22033", #chilled_re-generic_v3
        ]
        basehugModelsName=[

        ]
        lorahugModelsName=[
                    "https://huggingface.co/Lyman/gwei/resolve/main/gwei_10.safetensors",
                    "https://huggingface.co/Lyman/gwei/resolve/main/archives/japaneseDollLikeness_v10.safetensors",
                    "https://huggingface.co/Lyman/gwei/resolve/main/archives/koreanDollLikeness_v10.safetensors",
                    "https://huggingface.co/AzureKn1ght/RandomCoser/resolve/main/randomCoserFaceCoser_randomCoserFace.safetensors",# 随机
        ]

        loracivitModelsName=["https://civitai.com/api/download/models/9969",#liuyifei_10.safetensors
                    "https://civitai.com/api/download/models/20684",#taiwanDollLikeness_v10.safetensors
                    "https://civitai.com/api/download/models/16677",#Cute_girl_mix4
                    "https://civitai.com/api/download/models/16557",#少女感
                    "https://civitai.com/api/download/models/27343"# huge/nice,<lora:huge_v2:1>,huge/nice
                    "https://civitai.com/api/download/models/23250",#breastInClass: Better Bodies，<lora:breastinclassbetter_v141:0.5>
                    "https://civitai.com/api/download/models/27946",#hanfu
                    "https://civitai.com/api/download/models/30796",#hanfu3.0ming,"ming hanfu"
                    "https://civitai.com/api/download/models/31284",#KoreanDollLikeness
                    "https://civitai.com/api/download/models/31264",# "sgroupe, mgroupe, lgroupe",EZ Group Photo

        ]    
    else:
        pass

    if selectModel=="1a":
    #########################################################################################
    #照片
    
        basecivitModelsName=[
                    
                    "https://civitai.com/api/download/models/29460", #Realistic Vision V2
        ]
        basehugModelsName=[

        ]
        lorahugModelsName=[
                  
        ]

        loracivitModelsName=[
            "https://civitai.com/api/download/models/30459",#virtual-buildings"

        ]    
    else:
        pass

    if selectModel=="2":
    ##############################################
    # 日式动漫风格
        basecivitModelsName=[
            "https://civitai.com/api/download/models/7425",#girl,Counterfeit-V2.5
            "https://civitai.com/api/download/models/25853",# 

        ]
        basehugModelsName=[
                "https://huggingface.co/andite/anything-v4.0/resolve/main/anything-v4.5-pruned.safetensors",#Animelike 2D
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
                    "https://civitai.com/api/download/models/25661",# ## 小人书·连环画 xiaorenshu v2
                    "https://civitai.com/api/download/models/27946",#hanfu
                    "https://civitai.com/api/download/models/30796",#hanfu3.0ming,"ming hanfu"

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
            "https://civitai.com/api/download/models/27747",# db01,storyboard
            #"https://civitai.com/api/download/models/15236",#deliberate_v2
        ]
        basehugModelsName=[
            "https://huggingface.co/Sandro-Halpo/SamDoesArt-V3/resolve/main/SamDoesArt-V3.safetensors",#SamDoesArt
            "https://huggingface.co/andite/anything-v4.0/resolve/main/anything-v4.5-pruned.safetensors",#
            "https://huggingface.co/jinofcoolnes/sammod/resolve/main/samdoartsultmerge.safetensors",#Samdoesarts Ultmerge v1

        ]
        lorahugModelsName=[
                
        ]

        loracivitModelsName=[       
                "https://civitai.com/api/download/models/7804",#"Sam Yang" SamDoesArts (Sam Yang) Style LoRA
                "https://civitai.com/api/download/models/14533",# “shinkawa youji”
                "https://civitai.com/api/download/models/23169"#limited palette
                "https://civitai.com/api/download/models/25729"#jb,Carbon painting

        ]
    else:
        pass
    ####################################################################
    # 电影风格
    if selectModel=="6":

        basecivitModelsName=[
            # "https://civitai.com/api/download/models/12763",#The Ally's Mix III: Revolutions
         
        ]
        basehugModelsName=[
       
        ]
        lorahugModelsName=[
                
        ]

        loracivitModelsName=[       
                "https://civitai.com/api/download/models/19770",## Shallow Focus模拟聚焦
                "https://civitai.com/api/download/models/7804",#"Sam Yang" SamDoesArts (Sam Yang) Style LoRA

        ]
    else:
        pass


    ##############################################
    # 2.5D 混合风格  
    if selectModel=="7":

        basecivitModelsName=[
            "https://civitai.com/api/download/models/23558",# dalcefo，dalcefo_painting V4

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
    # 纯艺术
    if selectModel=="8":

        basecivitModelsName=[
            "https://civitai.com/api/download/models/23979",#Oil painting

        ]
        basehugModelsName=[
            "https://huggingface.co/dallinmackay/Van-Gogh-diffusion/resolve/main/Van-Gogh-Style-lvngvncnt-v2.ckpt",#lvngvncnt style

        ]
        lorahugModelsName=[
      
        ]

        loracivitModelsName=[    

        ]
    else:
        pass

    ##############################################
    # 科幻风格
    if selectModel=="9":

        basecivitModelsName=[
            "https://civitai.com/api/download/models/13259",# Illuminati Diffusion

        ]
        basehugModelsName=[
            #"https://huggingface.co/stabilityai/stable-diffusion-2-1/resolve/main/v2-1_768-ema-pruned.safetensors",# SD2.1
  

        ]
        lorahugModelsName=[
           
                
        ]

        loracivitModelsName=[
            

        ]
    else:
        pass

    ##############################################
    # SD 2.1 
    if selectModel=="10":

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
    # 训练Training 
    if selectModel=="11":

        basecivitModelsName=[
            "https://civitai.com/api/download/models/11732", #chilloutmix_NiPrunedFp16Fix
            "https://civitai.com/api/download/models/11745", #chilloutmix_NiPrunedFp32Fix

        ]
        basehugModelsName=[
            "https://huggingface.co/SG161222/Realistic_Vision_V2.0/resolve/main/Realistic_Vision_V2.0.safetensors",# Realistic_Vision_V2.0
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
            cmd = "cd %s && aria2c -V -c --disable-ipv6 %s" %(baseModelsPath,basecivitModelsName)
            # os.system(cmd)
            subprocess.call(cmd, shell=True)
    if len(basehugModelsName) != 0:
        for basehugModelsName in basehugModelsName:
            cmd = "cd %s && wget -N -c  %s" %(baseModelsPath,basehugModelsName)
            # os.system(cmd)
            subprocess.call(cmd, shell=True)
    if len(loracivitModelsName) != 0:
        for loracivitModelsName in loracivitModelsName:
            cmd = "cd %s && aria2c -V -c --disable-ipv6 %s" %(loraModelsPath,loracivitModelsName)
            # os.system(cmd)
            subprocess.call(cmd, shell=True)
    if len(lorahugModelsName) != 0:
        for lorahugModelsName in lorahugModelsName:
            cmd = "cd %s && wget -N -c  %s" %(loraModelsPath,lorahugModelsName)
            # os.system(cmd)
            subprocess.call(cmd, shell=True)





