# Bilibili 专栏文章下载器
## 介绍
一个基于 [Selenium](https://www.selenium.dev/) 的 Bilibili 专栏文章下载工具，可以将专栏文章下载为 Markdown 格式的文件。

支持两种模式（贴入链接自动识别）：
- 批量：下载指定专栏文集下的所有文章
- 单篇：下载指定专栏文章

## 使用
### 安装依赖
此脚本默认依赖于 Firefox 开发者版和 geckodriver，请确保已安装 Firefox 开发者版以及对应版本的 geckodriver。

如果想要使用其他浏览器，请直接修改 `b23_cv/init_driver.py` 的相关部分为其他浏览器的 WebDriver。

推荐使用系统自带的包管理器安装 geckodriver ，如果要手动下载 geckodriver：请前往 [mozilla/geckodriver: WebDriver for Firefox](https://github.com/mozilla/geckodriver) 的 releases 页面下载对应版本的 geckodriver，并将其解压后的路径添加到系统 `PATH` 环境变量中。

推荐使用虚拟环境以避免可能的依赖冲突：
```bash
python -m venv . && ./bin/activate # 创建虚拟环境并激活
pip install -r requirements.txt # 安装依赖
```

### 使用
直接运行 `main.py` 即可，根据提示输入支持的链接和输出文件夹（可选）即可下载。

链接示例：
1. 专栏文集： `https://www.bilibili.com/read/readlist/rl335022`
2. 单篇文章： `https://www.bilibili.com/read/cv12345678`

## 常见问题
### 为什么要使用 Firefox 开发者版？
因为这个脚本主要是为了方便自己使用，而我自己使用的浏览器就是 Firefox 开发者版，所以为了方便测试就直接用了。
### 导出格式问题？
由于选择内容容器的逻辑以及使用的`markdownify`模块的限制，一些特殊的排版可能会显示错误，暂时无法解决。

同时由于同样的原因，导出 HTML 暂时无法实现。

## TODO
- [ ] 直接调用默认浏览器以及对应的 WebDriver
- [ ] 支持导出 HTML 格式
- [ ] 支持自定义导出格式
- [ ] 命令行参数支持

## 贡献
目前这个脚本只是一个“能用”的下载器，如果有更多的需求或者想要添加更多的功能，欢迎提交 Issue 和 Pull Request。

## 许可证
GNU General Public License v3.0
