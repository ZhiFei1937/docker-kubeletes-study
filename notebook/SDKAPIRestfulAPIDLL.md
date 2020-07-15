### SDK/API/RestfulAPI/DLL

随着软件规模的日益庞大，常常需要把复杂的系统划分成小的组成部分，编程接口的设计十分重要，程序设计的实践中，编程接口的设计首先要使软件系统的职责得到合理划分，良好的接口设计可以降低系统各部分的相互依赖，提高组成单元的内聚性，降低组成单元间的耦合程度，从而提高系统的维护性和扩展性。API是接口的一种，在程序交互中具有重要的作用，而SDK与API有着密不可分的关系。

#### API

API即“应用程序编程接口”，是一些预先定义的函数，目的是作为“介面”沟通两个不同的东西，提供应用程序与开发人员基于某软件或硬件得以访问一组例程的能力，而又无需访问源码，或理解内部工作机制的细节。其实就是使用别人已经使用好的可以实现特定功能的函数。

#### SDK

SDK即“软体开发工具包”，一般是一些被软件工程师用于为特定的软件包、软件框架、硬件平台、操作系统等建立应用软件的开发工具的集合。通俗点是指由第三方服务商提供的实现软件产品某项功能的工具包。开发者不需要再对产品的每个功能进行开发，选择合适稳定的SDK服务并花费很少的经历就可以在产品中集成某项功能。



**SDK相当于开发集成工具环境，API就是数据接口。在SDK环境下调用API数据。**



#### RestfulAPI

渐进呈现是用户界面设计中的一个概念，它提倡只在用户需要的时候呈现用户所需的信息。

Restful架构是为掌控变化而设计的。

理解如何使用URL来为资源命名，以及如何正确地使用HTTP方法？

资源：就是指用URL命名的事物

资源的表述：服务器对http请求的响应

可寻址性原则：每个资源应该有一个属于自己的URL

无状态性：指服务器不关心客户端的状态

客户端应用一个资源的主要方法：GET/ HEAD/ POST/PUT/ DELETE/PATCH 

#### DLL

[DLL](https://baike.baidu.com/item/DLL)，即Dynamic Link Library（[动态链接](https://baike.baidu.com/item/动态链接)库）。在[Windows](https://baike.baidu.com/item/Windows) 环境下含有大量 .[dll](https://baike.baidu.com/item/dll)格式的文件，这些文件就是[动态链接库文件](https://baike.baidu.com/item/动态链接库文件)，其实也是一种[可执行文件](https://baike.baidu.com/item/可执行文件)格式。跟.exe文件不同的是，.dll文件不能直接执行，通常由.exe在执行时装入，内含有一些资源以及[可执行代码](https://baike.baidu.com/item/可执行代码)等。其实Windows的三大模块就是以DLL的形式提供的（[Kernel32.dll](https://baike.baidu.com/item/Kernel32.dll)，[User32.dll](https://baike.baidu.com/item/User32.dll)，[GDI32.dll](https://baike.baidu.com/item/GDI32.dll)），里面就含有了API函数的执行代码。为了使用DLL中的API函数，必须要有API函数的声明（.h）和其[导入库](https://baike.baidu.com/item/导入库)（.lib），导入库可以先这样理解，导入库是为了在DLL中找到API的[入口点](https://baike.baidu.com/item/入口点)而使用的。

为了使用[API](https://baike.baidu.com/item/API/10154)函数，我们就要有跟API所对应的.h和.lib文件，而SDK正是提供了一整套开发Windows应用程序所需的相关文件、范例和工具的“工具包”。

SDK包含了使用API的必需资料，所以也常把仅使用API来编写[Windows](https://baike.baidu.com/item/Windows)应用程序的开发方式叫做“SDK编程”。而API和SDK是开发Windows应用程序所必需的东西，所以其它编程框架和类库都是建立在它们之上的，比如VCL和[MFC](https://baike.baidu.com/item/MFC)，虽然比起“SDK 编程”来有着更高的[抽象](https://baike.baidu.com/item/抽象/9021828)度，但这丝毫不妨碍在需要的时候随时直接调用[API](https://baike.baidu.com/item/API/10154)函数 。 [1]