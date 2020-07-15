### Redis学习

#### 开始使用Redis

```python
redis-server	:	Redis服务端
redis-cli		:	Redis命令行工具
启动redis：redis-server(使用默认config启动redis)，redis-server redis.conf 
关闭redis：redis-cli shutdown
```

Redis中的术语实例代表一个redis-server进程。同一台主机上可以运行多个Redis实例，只要这些实例使用不同的配置即可，比如绑定到不同的端口、使用不同的路径保存数据持久化相关的文件，或采用不同的日志路径等。

