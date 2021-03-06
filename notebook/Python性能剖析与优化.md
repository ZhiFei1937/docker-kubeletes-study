### Python性能剖析与优化

利用 cProfile 定位性能瓶颈：

cProfile 是 Python 的标准库，可以统计程序里每一个函数的运行时间，并且提供了多样化的报表

```python
def foo():
    sum = 0
    for i in range(100):
        sum += i
    return sum
if __name__ == "__main__":
    import cProfile
    cProfile.run("foo()")
```

在当前的计算硬件资源发展形势下，对空间复杂度的关注远没有时间复杂度高，因此降低算法的复杂度主要集中在对其时间复杂度的考量。

实际上当需要在循环过程中依次处理一个序列中的元素的时候，就应该考虑生成器。yield 语句与 return 语句相似，当解释器执行遇到 yield 的时候，函数会自动返回 yield 语句之后的表达式的值。不过与 return 不同的是，yield 语句在返回的同时会保存所有的局部变量以及现场信息，以便在迭代器调用 `next()` 或 `send()` 方法的时候还原，而不是直接交给垃圾回收器（`return()` 方法返回后这些信息会被垃圾回收器处理）。这样就能够保证对生成器的每一次迭代都会返回一个元素，而不是一次性在内存中生成所有的元素。

充分利用了延迟评估（Lazy evaluation）的特性，仅在需要的时候才产生对应的元素，而不是一次生成所有的元素，从而节省了内存空间，提高了效率。

使用 `multiprocess` 克服 GIL 的缺陷

GIL 的存在使得 Python 中的多线程无法充分利用多核的优势来提高性能。多进程 `Multiprocess` 是 Python 中的多进程管理包，主要用来帮助处理进程的创建以及它们之间的通信和相互协调。它主要解决了两个问题：一是尽量缩小平台之间的差异，提供高层次的 API 从而使得使用者忽略底层 IPC 的问题；二是提供对复杂对象的共享支持，支持本地和远程并发。

线程的生命周期分为 5 个状态：创建、就绪、运行、阻塞和终止。自线程创建到终止，线程便不断在运行、就绪和阻塞这 3 个状态之间转换直至销毁。而真正占有 CPU 的只有运行、创建和销毁这 3 个状态。一个线程的运行时间由此可以分为 3 部分：线程的启动时间（Ts）、线程体的运行时间（Tr）以及线程的销毁时间（Td）。在多线程处理的情境中，如果线程不能够被重用，就意味着每次创建都需要经过启动、销毁和运行这 3 个过程。这必然会增加系统的相应时间，降低效率。而线程体的运行时间 Tr 不可控制，在这种情况下要提高线程运行的效率，线程池便是一个解决方案。

线程池通过实现创建多个能够执行任务的线程放入池中，所要执行的任务通常被安排在队列中。通常情况下，需要处理的任务比线程的数目要多，线程执行完当前任务后，会从队列中取下一个任务，直到所有的任务已经完成。

由于线程预先被创建并放入线程池中，同时处理完当前任务之后并不销毁而是被安排处理下一个任务，因此能够避免多次创建线程，从而节省线程创建和销毁的开销，带来更好的性能和系统稳定性。线程池技术适合处理突发性大量请求或者需要大量线程来完成任务、但任务实际处理时间较短的应用场景，它能有效避免由于系统中创建线程过多而导致的系统性能负载过大、响应过慢等问题。

Python 中利用线程池有两种解决方案：一是自己实现线程池模式，二是使用线程池模块。threadpool

使用 C/C++ 模块扩展高性能

比起直接使用 C/C++ 编写扩展模块，使用 Cython 的方法方便得多。

线程池基本原理： 我们把任务放进队列中去，然后开N个线程，每个线程都去队列中取一个任务，执行完了之后告诉系统说我执行完了，然后接着去队列中取下一个任务，直至队列中所有任务取空，退出线程。

