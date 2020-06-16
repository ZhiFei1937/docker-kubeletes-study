### C编译过程中各种文件之间的关系

- .c	C语言源文件
- .h    C语言头文件，每一个模块，.c与.h都是成对关系的
- .o    C语言链接文件，标准的目标文件
- .a     C语言静态库，由若干个.o文件构成
- .so   C语言动态链接库(共享库) 将.so文件添加到 /user/lib目录下，否则动态库不能被调用到
- .lo:   使用libtool编译出的目标文件，其实就是在o文件中添加了一些信息
- .la:   使用libtool编译出的库文件，其实是个文本文件，记录同名动态库和静态库的相关信息

```makefile
all: test1.o test3.o test2.o test_main.o creat_liba testmain  clean
creat_liba:
	@echo "start creat static libxxx.a"
	ar cr libtest1.a test1.o test2.o
	ar cr libtest3.a test3.o
	@echo "Finish creat libxxx.a"

creat_libso:
	@echo "start creat so"
	gcc -shared test2.o -L. -ltest -o libtest2.so
	@echo "Finish creat so"
	
testmain:
	export LD_LIBRARY_PATH=$(LD_LIBRARY_PATH):/mnt/ao_so_demo
	gcc test_main.c -L. -ltest1 -ltest3 -o testmain	
 
test1.o: test1.c test1.h
	gcc -c test1.c
test3.o: test3.c test3.h
	gcc -c test3.c
test2.o: test2.c test1.h 
	gcc -c test2.c
test_main.o:test_main.c test1.h test2.h
	gcc -c test_main.c
```

[动态库与静态库的使用](https://www.cnblogs.com/CoderTian/p/5902154.html)

     静态库特点：
         1，库的代码会编译进程序里面，所以静态库编译的程序比较大
         2，由静态库编译的程序不用依赖于系统的环境变量，所以环境变量有没有这个库文件，也可以运行。
     动态库特点：
         1，库的代码不会编译进程序里面，所以动态库编译的程序比较小。
         2，由动态库编译的程序依赖于系统的环境变量有没有这个库文件，没有则运行不了。

[Linux-C动态库与静态库的编译与调用](https://blog.csdn.net/nanfeibuyi/article/details/81203021)

[C语言调用so动态库的两种方式](https://blog.csdn.net/shaosunrise/article/details/81161064)

[C语言中.h和.c文件解析](https://www.cnblogs.com/laojie4321/archive/2012/03/30/2425015.html)
