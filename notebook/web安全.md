### web安全
Web应用的各种安全隐患
- 注入型隐患

  ```sql
  数据库注入：
  	select * from users where id='$id'
  	将$id的值传成';delete from users -- 造成隐患
  ```

  通过插入引号或分隔符等用于表示“数据部分边界”的字符，从而改变了文本的结构。

- 输入处理与安全性

  web应用中的输入即由http请求传入的信息，比如get、post、cookie等，web应用接收到这些值时的处理

  n个小球   1个或2个

  1 1 2 2 2 1 1 2 

  n == 1 n == 2

  return a(n+1) a(n+2)
