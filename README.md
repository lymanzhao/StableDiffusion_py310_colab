# StableDiffsion_py310_colab

## 1

### 开启GPU

.ipynb 文件用于colab，colab的安装脚本，注意在Colab菜单里面修改/笔记本设置为GPU。也可以在 代码执行程序 > 更改运行时类型，启用 GPU。

如果没有开启GPU，脚本会检测到，并立即退出连接的运行时，直接中断执行。因为是中断执行，来不及打印日志，需要自己注意。


### python 310预编译

笔记默认直接使用编译好的python 3.10.9，已上传在本项目的releases中。

https://github.com/lymanzhao/StableDiffusion_py310_colab/releases/download/1.0/Python-3.10.9.tar.gz

如果要自己编译，可以取消单元格中编译部分的注释。



## 2

### 下载

SDextensionsDownload.py，为插件下载更新脚本，笔记中已经使用。同样可以用于Windows环境下，脚本放置在stable-diffusion-webui文件夹下运行就可以。

SDModelDownload.py，为模型下载更新脚本，笔记中已经使用。同样可以用于Windows环境下，脚本放置在stable-diffusion-webui文件夹下运行就可以。

建议直接运行全部笔记，SDModelDownload.py运行的时候选择应用环境的模型。


SDcontrolnetExtensionsDownload.py，分类了controlnet安装下载脚本。


SDTrainingExtensionsDownload.py，分类了专门用于训练的脚本。


## 3
### for windows

Windows环境目前没有写全自动化部署，因为我用的是WinPython，
http://winpython.github.io/
该项目为便携环境，一次部署，复制黏贴就可以，无需重复部署。

Windows使用上面脚本，需要安装git for windows、wget for windows、aria2 for windows，并且确认能够在命令行里面运行。

windows重新安装，运行webui.bat的时候，会出现commit hash ＜none＞错误，直接按照提示 git config …… 就可以解决
https://blog.csdn.net/Xy_G__/article/details/128180356

