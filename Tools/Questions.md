# Question1 
 - why?:为什么执行过一次迭代后，再迭代时没有值？
 - 原因：迭代器是一个单向的容器，走到末尾之后，不会自动再回到开始的位置，因此再打印时，不会打印任何结果
 - 解决方式：
 
        
        # 解决方式：方法1：遍历map之后，将元素位置恢复到0；方法2：复制两个map对象
        import csv
        import itertools
        参考 https://stackoverflow.com/questions/17416777/why-can-i-only-use-a-reader-object-once)
        
# Question2
 - 为什么Python的String前面加上"u/U"" "r/R" "b/B"？
 - 原因是：
    - "u/U":不是仅仅是针对中文, 可以针对任何的字符串，代表是对字符串进行unicode编码。一般英文字符在使用各种编码下, 基本都可以正常解析, 所以一般不带u；但是中文, 必须表明所需编码, 否则一旦编码转换就会出现乱码。 
        建议所有编码方式采用utf8
    - "r/R" 为了告诉编译器这个string是raw string；不要转义backslash"\"，例如\n在raw string中，是两个字符，\和n，而不会转义为换行符
        由于正则表达式和\会有冲突，因此，当一个字符串使用了正则表达式后，最好前面加上r。以r开头的字符，常用于正则表达式，对应着re模块。
    - "b/B"  python3.x里默认的str是(py2.x里的)unicode, bytes是(py2.x)的str, b”“前缀代表的就是bytes 
            python2.x里, b前缀没什么具体意义， 只是为了兼容python3.x的这种写法    
# Question3
 - 百度相关网站爬虫遇到问题
    - urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:777)>
 - 解决方案
    
        import ssl
        context = ssl._create_unverified_context()
        rsp = request.urlopen(baseurl, data=enData, context=context)
        

  