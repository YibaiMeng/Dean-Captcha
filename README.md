# DeanCaptcha——机器学习识别验证码

这是我们《数据结构与算法实习》课程的作业。我们要写一个识别北京大学教务网的验证码的程序。

# 我们的思路

- 数据的获取：
- {
  原始数据：curl "http://dean.pku.edu.cn/student/yanzheng.php?act=init&rand=[0-5]" -o "#1.gif" 一行脚本
  正确的值：手输！ 做了个网站手输。

}

预处理：去噪声 二值化 分割 naive算法

学习的三种方法：
- k邻近 没用！全失败了！
- 机器学习！成了！
- 深度学习：没写完那！

封装成成品程序。

体会：
- 不要瞎用数据库。
- 


need json like:

{ '10101...1010':'A', '1010101001..1':'1', ..............}

Attention! :
numbers like '1' must be given by char
alphabet like 'A' must be given by Capital char

curl "http://dean.pku.edu.cn/student/yanzheng.php?act=init&rand=[0-5]" -o "#1.gif"
