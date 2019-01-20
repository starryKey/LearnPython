

# CSS语法
## 1、由两部分构成：选择器，以及一条或多条声明

       selector {declaration1;declaration2;...declarationN}

## 2、每条声明由一个属性和一个值组成，属性(property)是您希望设置的样式属性(style attribute)。每一个属性都有一个值，属性和值被冒号分开
       selector {property: value}
       h1{color:red, font-size:14px;}
       值使用不同的写法
        p{ color:#ff0000;}
        p{ color:#f00;}
        p{ color:rgb(255,0,0)}
        p{ color:rgb(100%,0%,0%)}
 - 请注意，当使用 RGB 百分比时，即使当值为 0 时也要写百分比符号。但是在其他的情况下就不需要这么做了。比如说，当尺寸为 0 像素时，0 之后不需要使用 px 单位，因为 0 就是 0，无论单位是什么

## 3、记得写引号：如果值为若干单词，则要给值加引号。

     p {font-family: "sans serif";}

## 4、多重声明：
 - 如果要定义不止一个声明，则需要用分号将每个声明分开。下面的例子展示出如何定义一个红色文字的居中段落。最后一条规则是不需要加分号的，因为分号在英语中是一个分隔符号，不是结束符号。然而，大多数有经验的设计师会在每条声明的末尾都加上分号，这么做的好处是，当你从现有的规则中增减声明时，会尽可能地减少出错的可能性。
        
        p {text-align:center; color:red;}
 - 建议写法：每行只描述一个属性，这样可以增强样式定义的可读性
 
        p {
            text-align: center;
            color: black;
            font-family: arial;
        }
## 5、空格和大小写：大多数样式表包含不止一条规则，则大多数规则包含不止一个声明。多重声明和空格的使用使得样式表更容易被编辑
        
        body {
            color: #000;
            background: #fff;
            margin: 0;
            padding: 0;
            font-family: Georgia, Palatino, serif;
        }

## 6、选择器的分组
 - 可以对选择器进行分组，被分组的选择器就可以共享相同的声明。用逗号将需要分组的选择器隔开
            
        h1,h2,h3,h4,h5,h6 {
        color: green;
        }
## 7、继承及其问题：子元素从父元素继承属性
        
        body {
        font-family: Verdana, sans-serif;
        }
 - 根据上面这条规则，站点的 body 元素将使用 Verdana 字体（假如访问者的系统中存在该字体的话）。
通过 CSS 继承，子元素将继承最高级元素（在本例中是 body）所拥有的属性（这些子元素诸如 p, td, ul, ol, ul, li, dl, dt,和 dd）。不需要另外的规则，所有 body 的子元素都应该显示 Verdana 字体，子元素的子元素也一样。并且在大部分的现代浏览器中，也确实是这样的。
*但是 Netscape 4 就不支持继承，它不仅忽略继承，而且也忽略应用于 body 元素的规则
## 8、友善地对待Netscape 4
    body  {
        font-family: Verdana, sans-serif;
     }

    p, td, ul, ol, li, dl, dt, dd  {
        font-family: Verdana, sans-serif;
     }
 - 如果你不希望 "Verdana, sans-serif" 字体被所有的子元素继承，又该怎么做呢？比方说，你希望段落的字体是 Times。没问题。创建一个针对 p 的特殊规则，这样它就会摆脱父元素的规则

        body  {
            font-family: Verdana, sans-serif;
        }

        td, ul, ol, ul, li, dl, dt, dd  {
            font-family: Verdana, sans-serif;
        }

        p {
            font-family: Times, "Times New Roman", serif;
        }
# 9、派生选择器
 - 通过依据元素在其位置的上下文关系来定义样式。
 - 例如希望列表中的strong元素变为斜体
   
        li strong {
            font-style: italic;
            font-weight: normal;
        }
 - 与html文件中的上下文关系
 - <li><strong>我是斜体字。这是因为 strong 元素位于 li 元素内。</strong></li>
## 10、CSS规则
        strong {
            color: red;
        }

        h2 {
            color: red;
        }

        h2 strong {
            color: blue;
        }
         <p>The strongly emphasized word in this paragraph is<strong>red</strong>.</p>
         <h2>This subhead is also red.</h2>
         <h2>The strongly emphasized word in this subhead is<strong>blue</strong>.</h2>
# 11、id选择器：选择器可以为标有特定id的html元素指定特定的样式
 - id选择器以"#"的方式定义
 - 示例：id选择器
      
        #red {color:red;}
        #green {color:green;}
        
 - 下面的HTML代码中，id属性为red的p 元素显示为红色，而id属性为 green 的 p 元素显示为绿色。
 - id 属性只能在每个 HTML 文档中出现一次。[原因](http://www.w3school.com.cn/xhtml/xhtml_structural_01.asp)
## id选择器和派生选择器
 - 在现代布局中，id选择器常常用于建立派生选择器
        
        #sidebar p {
	        font-style: italic;
	        text-align: right;
	        margin-top: 0.5em;
	    }
 - 上面的样式只会应用于出现在 id 是 sidebar 的元素内的段落。这个元素很可能是 div 或者是表格单元，尽管它也可能是一个表格或者其他块级元素
 - 一个选择器，多种用法
    - 即使被标注为 sidebar 的元素只能在文档中出现一次，这个 id 选择器作为派生选择器也可以被使用很多次
    
    
         #sidebar p {
	        font-style: italic;
	        text-align: right;
	        margin-top: 0.5em;
	     }

        #sidebar h2 {
	        font-size: 1em;
	        font-weight: normal;
	        font-style: italic;
	        margin: 0;
	        line-height: 1.5;
	        text-align: right;
	    }
        与页面中的其他 p 元素明显不同的是，sidebar 内的 p 元素得到了特殊的处理，同时，与页面中其他所有 h2 元素明显不同的是，sidebar 中的 h2 元素也得到了不同的特殊处理
        
 - 单独的选择器
    - id 选择器即使不被用来创建派生选择器，它也可以独立发挥作用：
    
            #sidebar {
	            border: 1px dotted #000;
	            padding: 10px;
	        }
# 类选择器
 - 在选择器中，类选择器以一个点号显示：
        
        .center {text-align: center}
        在上面的例子中，所有拥有 center 类的 HTML 元素均为居中
        在下面的 HTML 代码中，h1 和 p 元素都有 center 类。这意味着两者都将遵守 ".center" 选择器中的规则。
        <h1 class="center">
        This heading will be center-aligned
        </h1>
    	
    	<p class="center">
        This paragraph will also be center-aligned.
        </p> 
        类名的第一个字符不能使用数字！它无法在 Mozilla 或 Firefox 中起作用。 
 - 和 id 一样，class 也可被用作派生选择器：       
        
        .fancy td {
	        color: #f60;
	        background: #666;
	    }
	    在上面这个例子中，类名为 fancy 的更大的元素内部的表格单元都会以灰色背景显示橙色文字。（名为 fancy 的更大的元素可能是一个表格或者一个 div	    
 - 元素也可以基于它们的类而被选择：
    
        td.fancy {
	        color: #f60;
	        background: #666;
	    }
 - 在上面的例子中，类名为 fancy 的表格单元将是带有灰色背景的橙色。
 
# 属性选择器
 - 对带有指定属性的 HTML 元素设置样式
        
        [title]
        {
            color:red;
        }
 - 属性和值选择器
    
        [title=W3School]
        {
            border:5px solid blue;
        }
 - 属性和值选择器 - 多个值 
    
        [title~=hello] { color:red; } 
        下面的例子为带有包含指定值的 lang 属性的所有元素设置样式。适用于由连字符分隔的属性值：
        [lang|=en] { color:red; }
 - 设置表单的样式
  - 属性选择器在为不带有 class 或 id 的表单设置样式时特别有用：
    
        input[type="text"]
        {
            width:150px;
            display:block;
            margin-bottom:10px;
            background-color:yellow;
            font-family: Verdana, Arial;
        }

        input[type="button"]
        {
            width:120px;
            margin-left:35px;
            display:block;
            font-family: Verdana, Arial;
        }
# 创建CSS
 - 如何插入样式表
 - 当读到一个样式表时，浏览器会根据它来格式化 HTML 文档。插入样式表的方法有三种：
 
        1、外部表样式
        
        <head>
        <link rel="stylesheet" type="text/css" href="mystyle.css" />
        </head>
        浏览器会从文件 mystyle.css 中读到样式声明，并根据它来格式文档。
        外部样式表可以在任何文本编辑器中进行编辑。文件不能包含任何的 html 标签。样式表应该以 .css 扩展名进行保存。下面是一个样式表文件的例子：
            
            hr {color: sienna;}
            p  {margin-left: 20px;}
            body {background-image: url("images/back40.gif");}
        
        2、内部表样式
        当单个文档需要特殊的样式时，就应该使用内部样式表。你可以使用 <style> 标签在文档头部定义内部样式表，就像这样:
        
            <head>
                <style type="text/css">
                hr {color: sienna;}
                p {margin-left: 20px;}
                body {background-image: url("images/back40.gif");}
                </style>
            </head>
        3、内联样式
        
        由于要将表现和内容混杂在一起，内联样式会损失掉样式表的许多优势。请慎用这种方法，例如当样式仅需要在一个元素上应用一次时
            
            <p style="color: sienna; margin-left: 20px">
            This is a paragraph
            </p>
        4、多重样式
        如果某些属性在不同的样式表中被同样的选择器定义，那么属性值将从更具体的样式表中被继承过来。
            
            例如，外部样式表拥有针对 h3 选择器的三个属性：
            h3 {
                color: red;
                text-align: left;
                font-size: 8pt;
                }
            而内部样式表拥有针对 h3 选择器的两个属性：
            h3 {
                text-align: right; 
                font-size: 20pt;
                }
            假如拥有内部样式表的这个页面同时与外部样式表链接，那么 h3 得到的样式是：
                color: red; 
                text-align: right; 
                font-size: 20pt;
            即颜色属性将被继承于外部样式表，而文字排列（text-alignment）和字体尺寸（font-size）会被内部样式表中的规则取代。
            
        
        
            

        
     
  
    	    
    
    
 	     
 
 
