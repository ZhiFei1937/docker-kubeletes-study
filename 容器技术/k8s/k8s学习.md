### k8s学习图谱

`kubernetes是一个跨主机集群的开源的容器调度平台，它可以自动化应用容器的部署/扩展和操作，提供以容器为中心的基础架构。`

**特点**：

* 便携性：无论共有云/私有云/混合云还是多云架构都全面支持
* 可扩展：它是模块化/可插拔/可挂载/可组合的，支持各种形式的扩展
* 自修复：它可以自保持应用状态/可自重启/自复制/自缩放的，通过声明式语法提供了强大的自修复能力

**内容**：

1. 组件说明

2. 集群安装

3. 资源清单

4. pod控制器

   ```
   RC/RS/deployment:一般使用deployment支持RS/滚动更新
   HPA：根据服务器的状态与设定进行水平自动扩展
   有状态和无状态服务
   ```

5. 服务发现

```
云技术的基本特征是虚拟化( Virtualization)和分布式，其中虚拟化技术将计算机资源，如服务器、网络、内存以及存储等予以抽象、转换后呈现，使用户可以更好地应用这些资源，而且不受现有资源的物理形态和地域等条件的限制。分布式网络存储技术将数据分散地存储于多台独立的机器设备上，利用多台存储服务器分担存储负荷，不但解决了传统集中式存储系统中单存储服务器的瓶颈问题，还提高了系统的可靠性、可用性和拓展性。云计算被普遍认为具有三个特点：虚拟化、超大规模和高扩张性。云计算技术包括的具体内容有：数据存储技术、数据处理技术和虚拟化技术。
共享稀有资源和平衡负载是计算机分布式计算的核心思想之一。
```

**pod的概论**：

```
pod中所有的容器共用存储卷和网络资源，pause：pod启动使第一个默认且必须启动的容器
```

**网络通讯方式**：

k8s的网络模型假定了所有Pod都在一个可以直接联通的扁平的网络空间中

flannel：是k8s的网络规划服务，可以让集群中的不同节点主机创建的Docker容器都具有全集群唯一的虚拟IP地址。而且它还能在这些IP地址之间建立一个覆盖网络(overlay network)，通过这个覆盖网络，将数据包原封不动地传递到目标容器内。

```
etcd保存哪些flannel相关信息：
1. 存储管理flannel可分配的IP地址段资源
2. 监控etcd中每个pod的实际地址，并在内存中建立维护pod节点路由表
```

**kubernetes对象**：

```
名称：kubernetes REST API 中的所有对象都由名称和UID明确标识
metadata:
  name: nginx-demo
  
命名空间：kubernetes支持多个虚拟集群，它们底层依赖于同一个物理集群。这些虚拟集群就是命名空间

标签：标签可用于组织和选择对象的子集，为键值对
metadata:
  labels:
    environment: production
    app: nginx
    
注解：注解和标签一样，是键/值对，只起标注作用
metadata:
  annotations:
    imageregistry: "https://hub.docker.com/"
    
字段选择器：字段选择器允许您根据一个或多个资源字段的值筛选 Kubernetes 资源
kubectl get pods --field-selector metadata.name=my-service
kubectl get pods --field-selector=status.phase!=Running,spec.restartPolicy=Always

每个 Kubernetes 对象包含两个嵌套的对象字段，它们负责管理对象的配置：对象 spec 和 对象 status 。 spec 是必需的，它描述了对象的 期望状态（Desired State） —— 希望对象所具有的特征。 status 描述了对象的 实际状态（Actual State） ，它是由 Kubernetes 系统提供和更新的。
```

### 资源清单

#### k8s中的资源

```sh
名称空间级别：
	工作负载型资源/服务发现及负载均衡型资源/配置与存储型资源/特殊类型的存储卷

集群级别：
	namespace/node/role/clusterrole/rolebinding/clusterrolebing

元数据型：
	hpa/podtemplate/limitrange
```

#### 资源清单

一般称yaml文件为资源清单

#### kubectl 命令

```sh
kubectl create -f pod.yaml
kubectl delete pod myapp-pod
kubectl get pod -o wide
```

```sh
#针对k8s中多张网卡的问题
https://www.jianshu.com/p/ed1ae8443fff
```

