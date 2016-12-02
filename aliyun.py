import sys
import time
import json
import os
from aliyunsdkcore import client

from aliyunsdkecs.request.v20140526 import CreateInstanceRequest, DeleteInstanceRequest, StartInstanceRequest, StopInstanceRequest, DescribeImagesRequest
from aliyunsdkecs.request.v20140526 import DescribeZonesRequest, DescribeRegionsRequest,DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import AllocatePublicIpAddressRequest

class aliyun_instance():
    def __init__(self):
        self.__region = 'cn-hongkong'
        self.__imageId = 'ubuntu1404_64_40G_cloudinit_20160727.raw'
        self.__InstanceType = 'ecs.n1.tiny'
        self.__SecurityGroupId = 'xxxxxxxxxxxxxx'
        self.__InstanceName = 'autocreateinstance'
        self.__InternetChargeType='PayByTraffic'
        self.__InternetMaxBandwidthOut = '100'
        self.__HostName = self.__InstanceName
        self.__Password = "xxxxxxx"
        self.__SystemDiskCategory = 'cloud_efficiency'
        self.__ClientToken = 'xxxxxxx'
        self.__InstanceChargeType = 'PostPaid'
        self.__IoOptimized = 'optimized'
        self.__ZoneId = 'cn-hongkong-b'
        self.__InstanceId = None

        self.__client = client.AcsClient("xxxxxxxxx", "xxxxxxxxx", self.__region)
    def __createInstance(self):
        request = CreateInstanceRequest.CreateInstanceRequest()
        request.set_ImageId(self.__imageId)
        request.set_InstanceType(self.__InstanceType)
        request.set_SecurityGroupId(self.__SecurityGroupId)
        request.set_InstanceName(self.__InstanceName)
        request.set_InternetChargeType(self.__InternetChargeType)
        request.set_InternetMaxBandwidthOut(self.__InternetMaxBandwidthOut)
        request.set_HostName(self.__HostName)
        request.set_Password(self.__Password)
        request.set_SystemDiskCategory(self.__SystemDiskCategory)
        request.set_InstanceChargeType(self.__InstanceChargeType)
        request.set_IoOptimized(self.__IoOptimized)
        request.set_ZoneId(self.__ZoneId)

        request.set_accept_format(u'json')


        try:
            result = self.__client.do_action(request)
            result_data = json.loads(result)
        except Exception as e:
            print "exception arised "
            print e
            return None

        if result_data.has_key(u'InstanceId'):
            print 'createInstance successful with InstanceId %s' % result_data[u'InstanceId']
            return result_data[u'InstanceId']
        else:
            print 'createInstance failed '
            print result_data
            return None

    def __allocPublicAddress(self):
        if self.__InstanceId is None:
            print ' instanceId is none exit'
            return 1

        request = AllocatePublicIpAddressRequest.AllocatePublicIpAddressRequest()
        request.set_InstanceId(self.__InstanceId)

        request.set_accept_format(u'json')

        try:
            result = self.__client.do_action(request)
            result_data = json.loads(result)
        except Exception as e:
            print "exception arised "
            print e
            return 2

        if result_data.has_key(u"Code"):
            print 'alloc Public Address instance failed Code %s with instanceid %s' % (result_data[u'Code'], self.__InstanceId)
            print result_data[u'Message']
            return 1

        else:
            print 'allow public  instance %s successful  ' % instance
            return 0




    def __deleteInstance(self):

        request = DeleteInstanceRequest.DeleteInstanceRequest()
        request.set_InstanceId(u'asdfsa')

        request.set_accept_format(u'json')
        try:
            result = self.__client.do_action(request)
            result_data = json.loads(result)
        except Exception as e:
            print "exception arised "
            print e
            return 1
        # only has RequestId

        return 0


    def __startInstance(self, instanceId=None):
        if instanceId is None:
            instance = self.__InstanceId
        else:
            instance = instanceId

        request = StartInstanceRequest.StartInstanceRequest()
        request.set_InstanceId(instance)

        request.set_accept_format(u'json')
        try:
            result = self.__client.do_action(request)
            result_data = json.loads(result)
        except Exception as e:
            print "exception arised "
            print e
            return 1

        if result_data.has_key(u"Code"):
            print 'start instance failed Code %s with instanceid %s' %(result_data[u'Code'], instance)
            print result_data[u'Message']
            return 1

        else:
            print 'start instance %s successful  ' %instance
            return 0

    def __deleteInstance(self, instanceId=None):
        if instanceId is None:
            instance = self.__InstanceId
        else:
            instance = instanceId

        request = DeleteInstanceRequest.DeleteInstanceRequest()
        request.set_InstanceId(instance)

        request.set_accept_format(u'json')
        try:
            result = self.__client.do_action(request)
            result_data = json.loads(result)
        except Exception as e:
            print "exception arised "
            print e
            return 1

        if result_data.has_key(u"Code"):
            print 'delete instance failed Code %s with instanceid %s' % (result_data[u'Code'], instance)
            print result_data[u'Message']
            return 1

        else:
            print 'delete instance %s successful  ' % instance
            return 0
    def __stopInstance(self, instanceId=None):
        if instanceId is None:
            instance = self.__InstanceId
        else:
            instance = instanceId

        request = StopInstanceRequest.StopInstanceRequest()
        request.set_InstanceId(instance)

        request.set_accept_format(u'json')
        try:
            result = self.__client.do_action(request)
            result_data = json.loads(result)
        except Exception as e:
            print "exception arised "
            print e
            return 1

        if result_data.has_key(u"Code"):
            print 'stop instance failed Code %s with instanceid %s' % (result_data[u'Code'], instance)
            print result_data[u'Message']
            return 1

        else:
            print 'stop instance %s successful  ' % instance
            return 0
    def __getImageList(self):
        request = DescribeImagesRequest.DescribeImagesRequest()
        request.set_accept_format(u'json')
        try:
            result = self.__client.do_action(request)
            result_data = json.loads(result)
        except Exception as e:
            print "exception arised "
            print e
            return 1

        return 0
    def __getZoneList(self):
        request = DescribeZonesRequest.DescribeZonesRequest()

        request.set_accept_format(u'json')
        try:
            result = self.__client.do_action(request)
            result_data = json.loads(result)
        except Exception as e:
            print "exception arised "
            print e
            return 1

        return 0


    def __getRegionList(self):
        request = DescribeRegionsRequest.DescribeRegionsRequest()

        request.set_accept_format(u'json')
        try:
            result = self.__client.do_action(request)
            result_data = json.loads(result)
        except Exception as e:
            print "exception arised "
            print e
            return 1

        return 0

    def __getInstanceList(self):
        request = DescribeInstancesRequest.DescribeInstancesRequest()

        request.set_accept_format(u'json')
        try:
            result = self.__client.do_action(request)
            result_data = json.loads(result)
        except Exception as e:
            print "exception arised "
            print e
            return None

        return result_data

    def __showAllInstances(self, instance_list):
        if instance_list is None:
            print 'failed with getInstanceList'
            return 2
        if instance_list.has_key(u'Instances') and instance_list[u'Instances'].has_key(u'Instance'):
            print 'has %d instances ' % len(instance_list[u'Instances'][u'Instance'])

            for instance in instance_list[u'Instances'][u'Instance']:
                print '------------------------------------------------------------'
                print 'instance_id : %s' % instance['InstanceId']
                print u'PublicIpAddress: %s' % instance[u'PublicIpAddress'][u'IpAddress']
                print u'InternetChargeType: %s' % instance[u'InternetChargeType']
                print u'Status: %s' % instance[u'Status']
                print u'HostName: %s' % instance[u'HostName']
                print u'ImageId: %s' % instance[u'ImageId']
                print u'InstanceType: %s' % instance[u'InstanceType']
                print u'InstanceChargeType: %s' % instance[u'InstanceChargeType']
                print u'SecurityGroupIds: %s' % instance[u'SecurityGroupIds'][u'SecurityGroupId']
                print u'InternetMaxBandwidthOut: %s' % instance[u'InternetMaxBandwidthOut']
                print u'ZoneId: %s' % instance[u'ZoneId']
        else:
            print 'has no instance'

        return 0

    def createAndStartInstance(self):
        self.__InstanceId = self.__createInstance()

        if self.__InstanceId is None:
            print 'failed with createInstance'
            return 1
        #self.__InstanceId = 'i-j6c9rzmdqarm8tg510l5'
        if self.__allocPublicAddress():
            print 'alloc public ipaddress failed'
            return 3


        if not self.__startInstance(self.__InstanceId):
            print 'start Instance successful'
        else:
            print 'start Instance failed'

        instance_list = self.__getInstanceList()
        if instance_list is None:
            print 'failed with getInstanceList'
            return 2

        self.__showAllInstances(instance_list)
    def showInstances(self):
        instance_list = self.__getInstanceList()
        if instance_list is None:
            print 'failed with getInstanceList'
            return 2

        self.__showAllInstances(instance_list)
    def deleteInstance(self, instanceId):
        self.__deleteInstance(instanceId)
    def stopInstance(self, instanceId):
        self.__stopInstance(instanceId)

    def cleanInstances(self):
        instance_list = self.__getInstanceList()
        if instance_list is None:
            print 'failed with getInstanceList'
            return 2

        self.__showAllInstances(instance_list)
        print '--------------now start stop & delete instances above---------------'
        if instance_list.has_key(u'Instances') and instance_list[u'Instances'].has_key(u'Instance'):
            for instance in instance_list[u'Instances'][u'Instance']:
                instanceId = instance[u'InstanceId']
                if u'Running' == instance[u'Status']:
                    print 'stoping instance %s ... wait for 20 sec' % instanceId
                    if self.__stopInstance(instanceId):
                        print 'stop instance %s failed' % instanceId
                        continue
                    time.sleep(20)
                if not self.__deleteInstance(instanceId):
                    print 'delete instance %s successful ' % instanceId
                else:
                    print 'delete instance %s failed ' % instanceId

        print '--------------------------------finished-----------------------------'

    def stopInstances(self):
        instance_list = self.__getInstanceList()
        if instance_list is None:
            print 'failed with getInstanceList'
            return 2

        self.__showAllInstances(instance_list)
        print '--------------now start stop all instances above---------------'
        if instance_list.has_key(u'Instances') and instance_list[u'Instances'].has_key(u'Instance'):
            for instance in instance_list[u'Instances'][u'Instance']:
                instanceId = instance[u'InstanceId']
                if u'Running' == instance[u'Status']:
                    print 'stoping instance %s ... ' % instanceId
                    if self.__stopInstance(instanceId):
                        print 'stop instance %s failed' % instanceId
                        continue
                    
                else:
                    print 'instance %s is not at running' % instanceId

        print '--------------------------------finished-----------------------------'



#clt = client.AcsClient("LTAI3OGPrKNGnrZJ", "3i3H0ffwcCkzq59fRjxQ2LrFB0Y96G")
def print_tips():
    print 'please use aliyun [command] '
    print 'command list is :  '
    print 'show'
    print 'create'
    print 'delete'
    print 'stop'
    print 'allstop'
    print 'clean'

if __name__ == "__main__":
    instance = aliyun_instance()
    if len(sys.argv) < 2:
        print_tips()

    else:
        cmd = sys.argv[1]
        if 'show' == cmd.lower():
            instance.showInstances()
        elif 'create' == cmd.lower():
            print '----------------------------------------------------------------'
            print 'are you sure to create new one instance?[yes|no]'
            input = raw_input()
            if input == 'yes':
                instance.createAndStartInstance()
        elif 'delete' == cmd.lower():
            instance.showInstances()
            print '----------------------------------------------------------------'
            print 'input the instance id'
            input = raw_input()

            instance.deleteInstance(input)
        elif 'stop' == cmd.lower():
            instance.showInstances()
            print '----------------------------------------------------------------'
            print 'input the instance id'
            input = raw_input()

            instance.stopInstance(input)
        elif 'allstop' == cmd.lower():
            instance.showInstances()
            print '----------------------------------------------------------------'
            print ' are you sure to delete all instances?[yes|no]'
            input = raw_input()
            if input == 'yes':
                instance.stopInstances()
        elif 'clean' == cmd.lower():
            instance.showInstances()
            print '----------------------------------------------------------------'
            print ' are you sure to delete all instances?[yes|no]'
            input = raw_input()
            if input == 'yes':
                instance.cleanInstances()


        else:
            print_tips()







