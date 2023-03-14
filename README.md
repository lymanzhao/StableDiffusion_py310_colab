# DF_Ubuntu_py310_colab

## 1
.ipynb 文件用于colab，colab的安装脚本，注意在Colab菜单里面修改/笔记本设置为GPU。

Colab默认Ubuntu 20环境。

笔记默认直接使用编译好的python 3.10.9，上传在本项目的releases中。

https://github.com/lymanzhao/DF_Ubuntu_py310_colab/releases

如果要自己编译，可以取消单元格中编译部分的注释。



## 2

SDextensionsDownload.py，为插件下载更新脚本，笔记中已经使用。同样可以用于Windows环境下，脚本放置在stable-diffusion-webui文件夹下运行就可以。

SDModelDownload.py，为模型下载更新脚本，笔记中已经使用。同样可以用于Windows环境下，脚本放置在stable-diffusion-webui文件夹下运行就可以。

建议直接运行全部笔记，SDModelDownload.py运行的时候选择应用环境的模型。


## 3
Windows环境目前没有写自动化部署，因为我用的是WinPython，
http://winpython.github.io/
该项目为便携环境，一次部署，复制黏贴就可以，无需重复部署。

Windows使用上面脚本，需要安装git for windows、wget for windows、aria2 for windows，并且确认能够在命令行里面运行。

windows重新安装，运行webui.bat的时候，会出现commit hash ＜none＞错误，直接按照提示 git config ……就可以
https://blog.csdn.net/Xy_G__/article/details/128180356

