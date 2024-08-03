# Bilibili 专栏文章下载器
## 介绍
一个基于 [Selenium](https://www.selenium.dev/) 的 Bilibili 专栏文章下载工具，可以将专栏文章下载为 Markdown 或 HTML 格式的文件。

支持两种模式（贴入链接自动识别）：
- 批量：下载指定专栏文集下的所有文章
- 单篇：下载指定专栏文章

## 使用
### 安装依赖
此脚本默认依赖于 geckodriver，请确保已安装兼容的 geckodriver。

如果想要使用其他浏览器，请直接修改 `b23_cv/init_driver.py` 的相关部分为其他浏览器的 WebDriver。

推荐使用系统自带的包管理器安装 geckodriver ，如果要手动下载 geckodriver：请前往 [mozilla/geckodriver: WebDriver for Firefox](https://github.com/mozilla/geckodriver) 的 releases 页面下载对应版本的 geckodriver，并将其解压后的路径添加到系统 `PATH` 环境变量中。

推荐使用虚拟环境以避免可能的依赖冲突：
```bash
python -m venv . && ./bin/activate # 创建虚拟环境并激活
pip install -r requirements.txt # 安装依赖
```

### 使用
```bash
python bcv.py [-h] [-o OUTPUT] [-f html/markdown ] url
```
比如：
```bash
python bcv.py https://www.bilibili.com/read/cv12345678
```
在终端中运行 `python bcv.py -h` 查看帮助信息。

或者运行 `bcv_ia.py`，根据提示输入支持的链接和输出文件夹（可选）即可下载。

链接示例：
1. 专栏文集： `https://www.bilibili.com/read/readlist/rl335022`
2. 单篇文章： `https://www.bilibili.com/read/cv12345678`

## 常见问题
### 导出格式问题？
由于选择内容容器的逻辑以及使用的`markdownify`模块的限制，一些特殊的排版可能会显示错误，暂时无法解决。

同时由于同样的原因，导出 HTML 暂时无法实现。

## TODO
- [ ] 直接调用默认浏览器对应的 WebDriver
- [x] 支持导出带有样式的 HTML （目前样式仍然比较简单）
- [x] 支持自定义导出格式
- [x] 命令行参数支持

## 贡献
目前这个脚本只是一个“能用”的下载器，如果有更多的需求或者想要添加更多的功能，欢迎提交 Issue 和 Pull Request。

## 许可证
GNU General Public License v3.0:

    b23_cv - simple bilibili column downloader
    Copyright (C) 2024  Grassblock

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

