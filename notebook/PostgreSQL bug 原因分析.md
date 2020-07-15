### PostgreSQL bug 原因分析

http://www.postgres.cn/docs/10/high-availability.html

1. 出现数据库宕机的情况

   `大量的 select waiting ...，导致数据库无法正常工作`

2. PostgresSQL学习

   在数据库术语里，PostgreSQL使用一种客户端/服务器的模型。一次PostgreSQL会话由下列相关的进程（程序）组成：

   - 一个服务器进程，它管理数据库文件、接受来自客户端应用与数据库的联接并且代表客户端在数据库上执行操作。 该数据库服务器程序叫做`postgres`。
   - 那些需要执行数据库操作的用户的客户端（前端）应用。 客户端应用可能本身就是多种多样的：可以是一个面向文本的工具， 也可以是一个图形界面的应用，或者是一个通过访问数据库来显示网页的网页服务器，或者是一个特制的数据库管理工具。 一些客户端应用是和 PostgreSQL发布一起提供的，但绝大部分是用户开发的。

   PostgreSQL服务器可以处理来自客户端的多个并发请求。 因此，它为每个连接启动（“forks”）一个新的进程。

   PostgreSQL用户名是和操作系统用户账号分开的。 如果你连接到一个数据库时，你可以选择以何种PostgreSQL用户名进行联接； 如果你不选择，那么缺省就是你的当前操作系统账号。

   如果你不提供数据库名字，那么它的缺省值就是你的用户账号名字

   PostgreSQL是一种*关系型数据库管理系统* （RDBMS）。这意味着它是一种用于管理存储在*关系*中的数据的系统。

   可以使用***`COPY***`从文本文件中装载大量数据

   `COPY weather FROM '/home/user/weather.txt';`

   这里源文件的文件名必须在运行后端进程的机器上是可用的， 而不是在客户端上，因为后端进程将直接读取该文件。

   同时访问同一个或者不同表的多个行的查询叫*连接*查询。

   ```sql
   SELECT *
       FROM weather, cities
       WHERE city = name;
   ```

   左连接/右连接/全外连接/自连接	

   ```sh
   将所有表中的元祖保存在结果关系中，而在某列上填NULL
   左连接：列出左边关系中所有的元祖
   右连接：列出右边关系中所有的元祖
   ```

   

   ```sql
   SELECT *
       FROM weather LEFT OUTER JOIN cities ON (weather.city = cities.name);
   ```

   ```sql
   SELECT W1.city, W1.temp_lo AS low, W1.temp_hi AS high,
       W2.city, W2.temp_lo AS low, W2.temp_hi AS high
       FROM weather W1, weather W2
       WHERE W1.temp_lo < W2.temp_lo
       AND W1.temp_hi > W2.temp_hi;
   ```

   PostgreSQL支持*聚集函数*。在一个行集合上计算`count`（计数）、`sum`（和）、`avg`（均值）、`max`（最大值）和`min`（最小值）的函数。

   聚集`max`不能被用于`WHERE`子句中

   ```sql
   SELECT city FROM weather
       WHERE temp_lo = (SELECT max(temp_lo) FROM weather);
   ```

   可以用`HAVING` 过滤这些被分组的行

   ```sql
   SELECT city, max(temp_lo)
       FROM weather
       GROUP BY city
       HAVING max(temp_lo) < 40;
   ```

   `LIKE`操作符进行模式匹配

   ```sql
   SELECT city, max(temp_lo)
       FROM weather
       WHERE city LIKE 'S%'            -- (1)
       GROUP BY city
       HAVING max(temp_lo) < 40;
   ```

   对视图的使用是成就一个好的SQL数据库设计的关键方面。

   ```sql
   CREATE VIEW myview AS
       SELECT city, temp_lo, temp_hi, prcp, date, location
           FROM weather, cities
           WHERE city = name;
   
   SELECT * FROM myview;
   ```

   外键：维持数据的*引用完整性*

   *事务*是所有数据库系统的基础概念。事务最重要的一点是它将多个步骤捆绑成了一个单一的、要么全完成要么全不完成的操作。步骤之间的中间状态对于其他并发事务是不可见的，并且如果有某些错误发生导致事务不能完成，则其中任何一个步骤都不会对数据库造成影响。

   一个事务被称为是*原子的*：从其他事务的角度来看，它要么整个发生要么完全不发生。

   ```sql
   BEGIN;
   UPDATE accounts SET balance = balance - 100.00
       WHERE name = 'Alice';
   -- etc etc
   COMMIT;
   
   BEGIN;
   UPDATE accounts SET balance = balance - 100.00
       WHERE name = 'Alice';
   SAVEPOINT my_savepoint;
   UPDATE accounts SET balance = balance + 100.00
       WHERE name = 'Bob';
   -- oops ... forget that and use Wally's account
   ROLLBACK TO my_savepoint;
   UPDATE accounts SET balance = balance + 100.00
       WHERE name = 'Wally';
   COMMIT;
   ```

   一个窗口函数调用总是包含一个直接跟在窗口函数名及其参数之后的`OVER`子句。这使得它从句法上和一个普通函数或非窗口函数区分开来。`OVER`子句决定究竟查询中的哪些行被分离出来由窗口函数处理。`OVER`子句中的`PARTITION BY`子句指定了将具有相同`PARTITION BY`表达式值的行分到组或者分区。对于每一行，窗口函数都会在当前行同一分区的行上进行计算。

   我们可以通过`OVER`上的`ORDER BY`控制窗口函数处理行的顺序（窗口的`ORDER BY`并不一定要符合行输出的顺序。）。下面是一个例子：

   ```sql
   SELECT depname, empno, salary,
          rank() OVER (PARTITION BY depname ORDER BY salary DESC) FROM empsalary;
   ```

   继承是面向对象数据库中的概念。它展示了数据库设计的新的可能性。

   ```sql
   CREATE TABLE cities (
     name       text,
     population real,
     altitude   int     -- (in ft)
   );
   
   CREATE TABLE capitals (
     state      char(2)
   ) INHERITS (cities);
   ```

   Unix类操作系统强制了许多种资源限制，这些限制可能干扰你的PostgreSQL服务器的操作。尤其重要的是对每个用户的进程数目的限制、每个进程打开文件数目的限制以及每个进程可用的内存的限制。这些限制中每个都有一个“硬”限制和一个“软”限制。实际使用的是软限制，但用户可以自己修改成最大为硬限制的数目。而硬限制只能由root用户修改。系统调用`setrlimit`负责设置这些参数。 shell的内建命令`ulimit`（Bourne shells）或`limit`（csh）被用来从命令行控制资源限制。

   如果发生了这样的事情，你会看到像下面这样的内核消息（参考你的系统文档和配置，看看在哪里能看到这样的消息）：

   ```
   Out of Memory: Killed process 12345 (postgres).
   ```

   这表明`postgres`进程因为内存压力而被终止了。尽管现有的数据库连接将继续正常运转，但是新的连接将无法被接受。要想恢复，PostgreSQL应该被重启。

   ```sh
   
   [root@VM_16_17_centos bin]# free 
                 total        used        free      shared  buff/cache   available
   Mem:        1882892      785272      280428       40496      817192      852060
   Swap:             0           0           0
   ```

   ### free 与 available 的区别

   `free` 是真正尚未被使用的物理内存数量。
   `available` 是应用程序认为可用内存数量，`available = free + buffer + cache` (注：只是大概的计算方法)

   Linux 为了提升读写性能，会消耗一部分内存资源缓存磁盘数据，对于内核来说，buffer 和 cache 其实都属于已经被使用的内存。但当应用程序申请内存时，如果 free 内存不够，内核就会回收 buffer 和 cache 的内存来满足应用程序的请求。这就是稍后要说明的 buffer 和 cache。

   **postgres参数**最基本的方法是编辑``postgresql.conf``文件， 它通常被保存在数据目录中



​		使用psql无法连接数据库，并报错 

1. psql: FATAL: 53300: **remaining connection slots are reserved for non-replication superuser connections**
2. 普通用户的连接已满，保留用于非复制的超级用户连接。

由于连接已满，可以关闭空闲的连接

1）查询当前所有连接的状态

select datname,pid,application_name,state from pg_stat_activity;

2）关闭当前state为 idle 空闲状态的连接

![img](https://img-blog.csdnimg.cn/20190311160049788.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3Q1MTh2czIwcw==,size_16,color_FFFFFF,t_70)

查看数据库剩余连接数：

select max_conn-now_conn as resi_conn from (select setting::int8 as max_conn,(select count(*) from pg_stat_activity) as now_conn from pg_settings where name = 'max_connections') t;
查看为超级用户保留的连接数: 
show superuser_reserved_connections;
psql: FATAL:  53300: sorry, too many clients already
数据库连接已满，无法建立新的连接。
1、关闭空闲连接
select datname,pid,application_name,state from pg_stat_activity; 
--查看目前所有的连接的进程id、应用名称、状态。
select pg_terminate_backend(pid) from pg_stat_activity; 
--通过pid终止空闲连接

当前总共正在使用的连接数：

select count(1) from pg_stat_activity;

显示系统允许的最大连接数

show max_connections;

显示系统保留的用户数

show superuser_reserved_connections ;



巨型页面的使用会导致更小的页面表以及花费在内存管理上的 CPU 时间更少，从而提高性能。

shared_buffers：设置数据库服务器将使用的共享内存缓冲区量

如果有一个专用的 1GB 或更多内存的数据库服务器， 一个合理的`shared_buffers`开始值是系统内存的 25%。 即使较大的`shared_buffers`有效， 也会造成一些工作负载， 但因为PostgreSQL同样依赖操作系统的高速缓冲区， 将`shared_buffers`设置为超过 40% 的RAM不太可能比一个小点值工作得更好。 为了能把对写大量新的或改变的数据的处理分布在一个较长的时间段内， `shared_buffers`更大的 设置通常要求对`max_wal_size`也做相应增加。

PostgreSQL使用*角色*的概念管理数据库访问权限。

每一个到数据库服务器的连接都是使用某个特定角色名建立的，并且这个角色决定发起连接的命令的初始访问权限。

在 SQL 标准中，用户和角色之间的区别很清楚，并且用户不会自动继承权限而角色会继承。

PostgreSQL的*统计收集器*是一个支持收集和报告服务器活动信息的子系统。