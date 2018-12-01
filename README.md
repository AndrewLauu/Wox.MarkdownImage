# Wox.MarkdownImage <!-- omit in toc --> 
[![requires][requires_pic]][wox]
[![release][release_pic]][release]
[![lisense][license_pic]][license]

平时在写 Markdown 的时候，在文档里插图片是个大痛点，于是乎写了这个插件，使用 Wox 调用图床 API 生成 Url，同时为了拓展使用场景，支持图片转 Base64。

[English][en]

* [安装](#安装)
* [用法](#用法)
	* [图床模式](#图床模式)
	* [Base64模式](#base64模式)
	* [我该使用那个？](#我该使用那个)
* [致谢](#致谢)
* [后记](#后记)

## 安装
- 首先你需要一个 [`Wox`][wox] 软件，用来调用这个插件。
  
- 在Wox中使用 `wpm install Wox.MarkdownImage` 命令来在线安装。
  
- 如果你需要离线安装，在[这里][release]下载最终插件，然后拖到到Wox中。

## 用法
插件支持上传到 sm.ms 图床，然后给出 Url，或将图片转为 Base64 格式。
  
> 注意：受 API 限制，只接受图片文件，即 jpg, gif, png 等

### 图床模式
- 使用 `md u C:\pic.jpg` 来上传图片，`Enter` 复制 Url。
  
- 你可以在 `main.py` 的 `upload` 里更换其他图床。

### Base64模式
- 使用 `md b C:\pic.jpg` 离线转为 Base64 格式。

### 我该使用那个？
- 上传到图床是推荐的使用方式，因为这样可以使Markdown文档更简洁，同时减小文档大小。
- Base64 是在离线状态下折衷办法，因为将图片嵌入到了文件中，避免图片无法打开的尴尬。
	- 但是需要注意的是，由于 Base64 的自身特性，转换后的数据将比原图占用空间多 33.3%。
	- 因为 Base64 字符实在是太长了，所以推荐使用下面的当时插入：
	```markdown
	![pic][tag]
	其他内容
	……
	（文档最后）
	[tag]:Base64编码
	```
## 致谢
图床调用了 [SM.MS][sm] 的 API，在此向他表示感谢。

## 后记
限于作者能力有限，如果有奇怪的 Bug，欢迎来发 issue，或者 pull request。:heart:


[sm]:https://sm.ms/
[en]:https://github.com/AndrewLauu/Wox.MarkdownImage/blob/master/README-en.md
[release_pic]:https://img.shields.io/github/release/qubyte/rubidium.svg?maxAge=2592000
[release]:https://github.com/AndrewLauu/Wox.MarkdownImage/releases
[requires_pic]:https://img.shields.io/badge/requires-wox-%2337BB96.svg
[wox]:http://www.wox.one
[license_pic]:https://img.shields.io/hexpm/l/plug.svg
[license]:http://www.apache.org/licenses