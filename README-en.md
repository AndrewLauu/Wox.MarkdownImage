# Wox.MarkdownImage <!-- omit in toc --> 
[![Hex.pm](https://img.shields.io/hexpm/l/plug.svg)][license]
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)

  
Sometimes inserting into a image is quite annoying when write in Markdown, so I coded this plugin for Wox to upload the image onto imagehost and callback a url. 
  
And also in order to extend the usage occasion, it also supports transforming Image f8ie into Base64 code.

[TOC]

## Installation
- First you need a [`Wox`][wox].
  
- Execute `wpm install Wox.MarkdownImage` in Wox to install online.
  
- You can also download a package [here][release] then drag it into Wox.

## Usage
This plugin supports uploading the image onto imagehost powered by sm.ms, or transforming into Base64.
插件支持上传到sm.ms图床，然后给出Url，或将图片转为Base64格式。
  
> 注意：受限于API限制，只接受图片文件，即jpg, gif, png 等

### 图床模式
- 使用`md u C:\pic.jpg` 来上传图片，`Enter`复制Url。
  
- 你可以在`main.py`的`upload`里更换其他图床。

### Base64模式
- 使用`md b C:\pic.jpg`离线转为Base64格式。

### 我该使用那个？
- 上传到图床是推荐的使用方式，因为这样可以使Markdown文档更简洁，同时减小文档大小。
- Base64是在离线状态下折衷办法，因为将图片嵌入到了文件中，避免图片无法打开的尴尬。
	- 但是需要注意的是，由于Base64的自身特性，转换后的数据将比原图占用空间多33.3%。
	- 因为Base64字符实在是太长了，所以推荐使用下面的当时插入：
	```markdown
	![pic][tag]
	其他内容
	……
	（文档最后）
	[tag]:Base64编码
	```
## 致谢
图床调用了[SM.MS][sm]的API，在此向他表示感谢。

## 后记
限于作者能力有限，如果有奇怪的Bug，欢迎来发issue，或者pull request。:heart:

[wox]:http://www.wox.one
[sm]:https://sm.ms/
[hex]:https://img.shields.io/hexpm/l/plug.svg
[license]:http://www.apache.org/licenses
[release]:https://github.com/AndrewLauu/Wox.MarkdownImage/releases
