# 成语接龙工具

[TOC]

## 安装

该项目 Python3 环境运行（开发环境为 Python 3.7.3），可以从 [Python官网](https://www.python.org) 下载安装

将本项目下载到本地，可以点击右侧绿色的 `Clone or download` 或在命令行中输入 

```bash
$ https://github.com/Mzhhh/ChineseIdiomHelper.git
```

项目依赖包：`pypinyin` （可自行使用 pip 安装）

```bash
$ pip install pypinyin
```

## 使用

基本使用方法为

```bash
$ python idiom.py [option] [argument]
```

其中 `option` 可以为：

* 匹配模式相关：
    * `-e`：精确匹配，匹配汉字
    * `-t`：匹配语调，匹配带声调的音标
    * `-v`：模糊匹配，匹配无声调的音标

* 注音模式相关：
    * `-h`：（可选）若打开，则可匹配多音字（只要源与目标之间存在交集则判定匹配）

相应地，`argument` 在不同模式下为：

* `-e`：汉字（e.g., 翠）
* `-t`：汉字（e.g., 翠）或注音音标（e.g.,  cui4）
* `-v`：汉字（e.g., 翠）或无注音音标（e.g.,  cui）

## Examples

```bash
$ python idiom.py -e 翠
Results found:
  翠绕珠围
  翠围珠绕
  翠消红减
  翠竹黄花
  
$ python idiom.py -t 翠
Results found:
  脆而不坚
  啛啛喳喳
  翠绕珠围
  翠围珠绕
  翠消红减
  翠竹黄花
  
$ python idiom.py -v cui
Results found:
  催人泪下
  摧锋陷坚
  摧锋陷阵
  摧刚为柔
  摧坚获丑
  摧坚陷阵
  摧枯拉腐
  摧枯拉朽
  摧枯折腐
  摧枯振朽
  摧兰折玉
  摧眉折腰
  摧身碎首
  摧陷廓清
  摧心剖肝
  摧朽拉枯
  摧折豪强
  榱崩栋折
  榱栋崩折
  璀璨夺目
  脆而不坚
  啛啛喳喳
  翠绕珠围
  翠围珠绕
  翠消红减
  翠竹黄花
```

