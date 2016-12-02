#aliyun ECS
---
这是一个自动的工具，用来解决自己的一个问题，因为伟大的GWF，很多资料不能下载或者下载极慢，比如git clone。
使用购买的vpn服务，效果也不是很好，于是希望购买那种按量计费的阿里云主机，需要的时候启动，用完后就释放，成本也不高，效果很不错。 但是阿里云购买流程复杂，不方便，使用aliyun的API自动创建一个临时的云主机就是一个好的选择。 如果使用预先做好的自定义镜像，那就更快了。 1分钟内就可以搞定购买云盘、启动、配置，直接可以使用业务（ssh git axel下载 nginx vpn）

## 准备
### 下载准备库
按[官方文档](https://develop.aliyun.com/sdk/python?spm=5176.doc25699.2.2.r9MSs2)的说明安装aliyun-python-sdk-ecs

### 修改配置
修改aliyun_instance的__init__函数

* self.__region  
**地域ID**  
* self.__imageId 
**镜像ID** 
* self.__InstanceType 
**实例类型** 'ecs.n1.tiny' 表示1核1G 
* self.__SecurityGroupId **安全组** 自己在网站上设置 

* self.__InternetChargeType='PayByTraffic' 网络按流量计费  

* self.__Password = "xxxxxxx" **云主机**的root登陆密码, 
self.__SystemDiskCategory = 'cloud_efficiency'

self.__InstanceChargeType = 'PostPaid' **按量计费**
self.__IoOptimized = 'optimized'
self.__ZoneId = 'cn-hongkong-b'
self.__InstanceId = None

self.__client = client.AcsClient("xxxxxxxxx", "xxxxxxxxx", self.__region)
第一个xxxxxx 填写accessKey,第二个xxxxxx填写AccessSecret

### 运行
`python aliyun.py [show, create, stop, delete]`
show 显示自己名下的所有云主机  
create 创建（购买)一个云主机，并启动，分配公网地址  
stop 停止运行一个主机  
delete 注销（释放）一个云主机  
allstop 停止所有的主机  
clean 释放所有的主机
