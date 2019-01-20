# JS 基础

## JS的基本使用
 - 基础        
        1、HTML 中的脚本必须位于 <script> 与 </script> 标签之间。
            脚本可被放置在HTML页面的<body>和<head>部分中
        2、<script> 标签
            如需在 HTML 页面中插入 JavaScript，请使用 <script> 标签。
            <script> 和 </script> 会告诉 JavaScript 在何处开始和结束。
            <script> 和 </script> 之间的代码行包含了 JavaScript：
            
            <script>
            alert("My First JavaScript");
            </script>
            
        3、<body> 中的 JavaScript
        
            <!DOCTYPE html>
            <html>
            <body>
            .
            .
            <script>
            document.write("<h1>This is a heading</h1>");
            document.write("<p>This is a paragraph</p>");
            </script>
            .
            .
            </body>
            </html>
            
        4、<head> 中的 JavaScript 函数
        
            <!DOCTYPE html>
            <html>

            <head>
            <script>
            function myFunction()
            {
                document.getElementById("demo").innerHTML="My First JavaScript Function";
            }
            </script>
            </head>

            <body>

            <h1>My Web Page</h1>

            <p id="demo">A Paragraph</p>

            <button type="button" onclick="myFunction()">Try it</button>

            </body>
            </html>
        
        5、<body> 中的 JavaScript 函数
            该函数会在点击按钮时被调用：
            
            <!DOCTYPE html>
            <html>
            <body>

            <h1>My Web Page</h1>

            <p id="demo">A Paragraph</p>

            <button type="button" onclick="myFunction()">Try it</button>

            <script>
            function myFunction()
            {
                document.getElementById("demo").innerHTML="My First JavaScript Function";
            }
            </script>

            </body>
            </html>
            提示：我们把 JavaScript 放到了页面代码的底部，这样就可以确保在 <p> 元素创建之后再执行脚本。
            
## JavaScript 函数和事件
 - 外部的JavaScript
 - 把脚本保存到外部文件中。外部文件通常包含被多个网页使用的代码。
        
        如需使用外部文件，请在 <script> 标签的 "src" 属性中设置该 .js 文件：
        <!DOCTYPE html>
        <html>
        <body>
        <script src="myScript.js"></script>
        </body>
        </html>
        在 <head> 或 <body> 中引用脚本文件都是可以的。实际运行效果与您在 <script> 标签中编写脚本完全一致。
        提示：外部脚本不能包含 <script> 标签。
 
 