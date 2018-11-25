# Wox.MarkdownImage <!-- omit in toc --> 
[![requires][requires_pic]][wox]
[![release][release_pic]][release]
[![lisense][license_pic]][license]
  
Sometimes inserting into a image is quite annoying when write in Markdown, so I coded this plugin for Wox to upload the image onto imagehost and callback a url. 
  
And also in order to extend the usage occasion, it also supports transforming Image f8ie into Base64 code.

* [Installation](#installation)
* [Usage](#usage)
	* [Upload mode](#upload-mode)
	* [Base64 mode](#base64-mode)
	* [Which ?](#which-)
* [致谢](#致谢)
* [后记](#后记)

## Installation
- First you need a [`Wox`][wox].
  
- Execute `wpm install Wox.MarkdownImage` in Wox to install online.
  
- You can also download a package [here][release] then drag it into Wox.

## Usage
This plugin supports uploading the image onto imagehost powered by sm.ms , or transforming into Base64.
> Read : Due to the constraint of API , only image files available, ie. *.jpg, *.gif, *.png etc. 

### Upload mode
- Use `md u C:\pic.jpg` to upload , then `Enter`复制Url.
  
- 你可以在`main.py`的`upload`里更换其他图床。

### Base64 mode
- 使用`md b C:\pic.jpg`离线转为Base64格式。

### Which ?
- 上传到图床是推荐的使用方式，因为这样可以使Markdown文档更简洁，同时减小文档大小。
- Base64是在离线状态下折衷办法，因为将图片嵌入到了文件中，避免图片无法打开的尴尬。
	- 但是需要注意的是，由于Base64的自身特性，转换后的数据将比原图占用空间多33.3%。
	- 因为Base64字符实在是太长了，所以推荐使用下面的当时插入：
	```markdown
	![pic][tag]
	something here
	……
	（EOF）
	[tag]:Base64 code
	```
## 致谢
图床调用了[SM.MS][sm]的API，在此向他表示感谢。

## 后记
限于作者能力有限，如果有奇怪的Bug，欢迎来发issue，或者pull request。:heart:

[sm]:https://sm.ms/
[release_pic]:https://img.shields.io/github/release/andrewlauu/wox.markdownimage.svg?maxAge=2592000
[release]:https://github.com/AndrewLauu/Wox.MarkdownImage/releases
[requires_pic]:https://img.shields.io/badge/requires-wox-%2337BB96.svg
[wox]:http://www.wox.one
[license_pic]:https://img.shields.io/hexpm/l/plug.svg
[license]:http://www.apache.org/licenses
