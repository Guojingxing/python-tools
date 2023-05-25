# Python小工具合集
这个项目是一个合集，包含了多个小工具，用Python编写。
## 使用方法
运行每个文件夹下与文件夹同名的python文件即可。
## 克隆项目
使用以下命令克隆项目到本地：
```bat
git clone https://github.com/Guojingxing/python-tools.git
```
## 工具列表
### 1. 替换文本中的文字（[replace-words.py](replace-words/replace-words.py)）
该工具实现将`1.txt`中的文字按照`trans.txt`中的规则替换，并输出至同文件夹下的`2.txt`中。
在项目目录下，执行以下命令运行转换工具：
```bat
python .\replace-words.py
```
确保在执行命令之前已经将需要转换的文本文件和`replace-words.py`放在同一个文件夹下。

其中`trans.txt`中每个替换规则占一行，中间有一个空格分隔源文本和目标文本。你可以根据需要自定义替换规则。如：
```
视频 影片
网络 網路 
```
一般可用在文本文档中的词语或者文字批量转换（如大陆台湾用语批量转换），不支持多行以及带空格的文本替换。
## 授权许可
本项目使用 [MIT许可证](LICENSE)进行授权许可。
