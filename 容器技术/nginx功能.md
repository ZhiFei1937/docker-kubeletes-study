### nginx功能

- 可针对静态资源高速高并发访问及缓存

- 可使用方向代理加速，并且可进行数据缓存

- 具有简单负载均衡/节点健康检查和容错功能

- 支持Uwsgi等的加速和缓存

- 具有模块化的架构

  ```sh
  core   		核心的http参数配置，对应nginx的http区块
  access  	访问控制模块，用来控制网站用户对nginx的访问
  fastcgi  	fastcgi模块，和动态应用相关，如php
  gzip    	压缩模块，对nginx返回的数据压缩，性能优化模块
  log     	访问日志模块
  proxy   	proxy代理模块
  rewrite   	URL地址重写模块
  upstream  	负载均衡模块
  limit_conn  限制用户并发连接数及请求数模块
  limit_req   根据定义的key限制nginx请求过程的速率
  auth_basic  web认证模块，设置web用户账号密码访问
  ssl        	ssl模块，用于加密的http连接，如https
  stub_status 记录nginx基本访问状态信息
  ```

  ```sh
  ngx_http_core_module		包括一些核心的http参数配置，对应nginx的配置为http区块部分
  ngx_http_access_module		访问控制模块，用来控制网站用户对nginx的访问
  ngx_http_gzip_module		压缩模块，对nginx返回的数据压缩，属于性能优化模块
  ngx_http_fastcgi_module		fastcgi模块，和动态应用相关的模块，例如PHP
  ngx_http_proxy_module		proxy代理模块
  ngx_http_upstream_module	负载均衡模块，可以实现网站的负载均衡功能及节点的健康检查
  ngx_http_rewrite_module		URL地址重写模块
  ngx_http_limit_conn_module	限制用户并发连接数及请求数模块
  ngx_http_limit_req_module	根据定义的key限制nginx请求过程的速率
  ngx_http_log_module			访问日志模块，以指定的格式记录nginx客户访问日志等信息
  ngx_http_auth_basic_module	web认证模块，设置web用户通过账号密码访问nginx
  ngx_http_ssl_module			ssl模块，用于加密的http连接，如https
  ngx_http_stub_status_module	记录nginx基本访问状态信息等的模块
  ```

  ```config
  1  worker_processes  1;         	#worker进程的数量
  2  events {                    	#事件区块开始 
  3      worker_connections  1024;   #每个work进程支持的最大连接数
  4  }    							#事件区块结束
  5  http {    #http区块开始
  6      include       mime.types;   #nginx支持的媒体类型库文件包含
  7      default_type  application/octet-stream;    	#默认的媒体类型
  8      sendfile        on;            				#开启高效传输模式
  9      keepalive_timeout  65;          			#连接超时
  10      server {       		#第一个server区块开始，表示一个独立的虚拟主机站点
  11          listen       80;       #提供服务的端口，默认80
  12          server_name  localhost;    	#提供服务的域名主机名
  13          location / {               	#第一个location区块开始
  14              root   html;          	#站点的根目录，相对于nginx安装目录
  15              index  index.html index.htm;
  16          }
  17          error_page   500 502 503 504  /50x.html;
  18          location = /50x.html {
  19              root   html;
  20          }
  21      }
  22  }
  ```

- 所谓虚拟主机，在web服务里就是一个独立的网站站点，这个站点对应独立的域名（也可能是IP或端口），具有独立的程序及资源目录，可以独立地对外提供服务供用户访问。
   nginx使用一个server{}标签来标示一个虚拟主机，一个web服务里可以有多个虚拟主机标签对，即同时可以支持多个虚拟主机站点

- location(位置)指令的作用是可以根据用户请求的URI来执行不同的应用，URI的知识前面已经讲过，其实就是根据用户请求的网站的地址URL匹配，匹配成功即进行相关的操作

  ```sh
  location	[ = | ~ | ~* | ^~ | @ ]		uri					{...}
  指令				匹配标识			匹配的网站网址		匹配URI后要执行的配置段
  ```

  - ~ 区分大小写
  - ~* 不区分大小写
  - ! 取反
  - ^~ 在常规的字符串匹配检查之后，不做正则表达式的检查



```sh
location字符组合匹配顺序
1、 location = / {"					精确匹配
2、 location ^~ /images/ {"			匹配常规字符串，不做正则匹配检查
3、 location ~* .(gif|jpg|jpeg)$ {"	正则匹配
4、 location /document/ {"			匹配常规字符串，如果有正则则优先匹配正则
5、 location / {"					所有location都不能匹配后的默认匹配
```

