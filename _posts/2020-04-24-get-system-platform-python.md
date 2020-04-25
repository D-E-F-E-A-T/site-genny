---
layout: post
title:  "Getting the System Platform in Python"
date:   2020-04-24 19:00:42 -0400
author: Noah Broyles
tags:
  - python
  - tutorials
github:
  has_repo: quite
  repository_url: https://github.com/noahbroyles/noahbroyles.github.io/blob/master/2020/04/24/get-system-platform-python.html
---

You know how sometimes you want to write a Python application that depends on knowing what platform it is being run on? (<em>e.g.</em> MacOS, Linux, or - heaven forbid - Windows?) Well, I wrote these instructions just for that purpose. <br><br>
Thankfully, this is not very hard to do in Python, thanks to the `platform` module.<br> Here is a class I wrote for this purpose:
{% highlight python %}

import platform
class Computer:
    def isMac():
        return platform.system() == "Darwin"

    def isLinux():
        return platform.system() == "Linux"

    def isWindows():
        return platform.system() == "Windows"

{% endhighlight %}

If only `Computer.isMac()` would return `True` all the time! The world would be a better place. But it would never do to have `Computer.isMac()` return `True` on a Windows 10 P<s>O</s>C, or a nice Linux machine for that matter.   
<br>
## MacOS Test Case:
<em><kbd>Cmd</kbd>+<kbd>Tab</kbd> to iTerm</em>
{% highlight python %}
nbroyles@noahsmacmini ~ % python3
Python 3.7.7 (v3.7.7:d7c567b08f, Mar 10 2020, 02:56:16)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from computer import Computer
>>> Computer.isMac()
True
>>> Computer.isLinux()
False
>>> Computer.isWindows()
False
>>>
{% endhighlight %}
<br>
## Linux Test Case:
<em>Nice lil' `ssh` into my desktop raspberry pi</em>
{% highlight python %}
pi@pi3:~ $ python3
Python 3.7.3 (default, Dec 20 2019, 18:57:59)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from computer import Computer
>>> Computer.isMac()
False
>>> Computer.isLinux()
True
>>> Computer.isWindows()
False
>>>
{% endhighlight %}
<br>
## Windows Test Case:
<em>I had to fire up an online VM just for this!</em>
{% highlight python %}
C:\Users\User>python
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from computer import Computer
>>> Computer.isMac()
False
>>> Computer.isLinux()
False
>>> Computer.isWindows()
True
>>>
{% endhighlight %}