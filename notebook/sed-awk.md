### Shell 脚本编程

- 位置变量

  ```sh
  指函数或脚本后跟的第n个参数 $1-$n,第10个开始要用花括号调用，例如${10}
  ```

- 变量赋值的时候，如果值有空格，需要用双引号或单引号括起来

  ```sh
  var="1 2 3"
  var='1 2 $PWD' #单引号会让shell忽略特殊字符，命令输出为：1 2 $PWD
  ```

  

#### grep sed awk

```sh
sed：流编辑器，过滤和替换文本
cat /etc/services | sed -n '/blp5/p'
p: 打印 d：删除 s：替换

awk: 处理文本的编程语言工具，能用简短的程序处理标准输入或文件、数据排序、计算以及生成报表等等
awk option 'pattern {action}' file
```

