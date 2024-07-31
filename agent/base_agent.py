# 这个对应之前实现抽象状态层的那个base agent，这里面主要得做一下演化出来的结果和命令的映射关系，以及后续需要的一些别的。

import math
import copy
import numpy as np
import codecs
import sys, os
import xlrd
import time
from enum import Enum
import random

class BaseAgent(object):
    def __init__(self):
        self.act = []
        self.num = 0 
        self.reward = 0 
        self.missile_arrange = [] # 反正三十个，每个只要定了目标ID int、发射时间int 和弹种 int 三个维度，就行了呗。后面的等人家来解析
        self.action_dim = 30*3 
        self.target_ID_list = []
        self.detected_state = dict()
        self.__init_IDs()
        
    def __init_IDs(self):
        print("__init_IDs unfinshed ")
        self.target_ID_list.append("CVN76") 
        self.target_ID_list.append("CVN70")
        self.target_ID_list.append("CVN74")
        self.target_ID_list.append("CG54")
        self.target_ID_list.append("CG67")
        self.target_ID_list.append("DDG52")
        self.target_ID_list.append("DDG54")
        self.target_ID_list.append("DDG56")
        self.target_ID_list.append("DDG65")
        self.target_ID_list.append("DDG69")
        self.target_ID_list.append("DDG100")
        self.target_ID_list.append("DDG103")
        self.target_ID_list.append("DDG105")
        self.target_ID_list.append("DDG106")
        self.target_ID_list.append("DDG107")
        self.target_ID_list.append("DDG108")
        self.target_ID_list.append("DDG1000")

    def reset(self):
        pass
    
    def generate_range(self):
        # 这个是产生取值范围的上界和下界。主要是服务于后面的
        xiajie = [] 
        shangjie = [] 
        for i in range(30):
            xiajie.append(0)
            xiajie.append(0)
            xiajie.append(0)
            shangjie.append(16)
            shangjie.append(3000)
            shangjie.append(1)

        return xiajie, shangjie

    def arrange_to_action(self, missile_arrange):
        geshu = len(missile_arrange)
        if geshu != 30:
            raise Exception("missile_arrange length is not 30, G!")
        
        for i in range(geshu):
            missile_arrange_i = missile_arrange[i]
            act_single = self.arrange_to_action_single(missile_arrange_i)
            self.act.append(act_single)
    
    def arrange_to_action_single(self, missile_arrange_i):
        # 这个等看到程序本身再写。
        target_ID_int = missile_arrange_i[0]
        time_int = missile_arrange_i[1]
        warhead_type_int = missile_arrange_i[2]
        # 根据这些参数生成动作
        # 先把位置读出来,从数字读str，再从str去寻址位置。如果失败就找优先级最高的。
        target_ID_str = self.target_ID_list[target_ID_int]
        # 根据target_ID_str去寻址位置，这一版先别来什么提前量那些，优先把优化那个弄了。
        
        return [] 
        pass

    def get_detect_info(self, status):
        # LJD不会探测
        # filtered_status = self.__status_filter(self.status)
        unitIDList = list(status.keys())

        # detectinfo = dict()
        detected_state_new = self.detected_state
        for unit in unitIDList:
            try:
                for i in range(len(status[unit]['DetectorState'])):
                    for j in range(len(status[unit]['DetectorState'][i]['DetectedState'])):
                        # 只有活着的装备才更新，死了的不更新了。
                        enemy_unit_ID = status[unit]['DetectorState'][i]['DetectedState'][j]['targetID']
                        if enemy_unit_ID in detected_state_new:
                            # 那就是活着的装备，那就更新一下。
                            detected_state_new[enemy_unit_ID] = status[unit]['DetectorState'][i]['DetectedState'][j]
            except:
                pass
        self.detected_state = detected_state_new
        return detected_state_new
    
    def get_missile_arrange_debug(self):
        # 还是搞专业一点,来一个用于调试的arrange分布。全随机的，一点脑子都不带的那种。
        arrange_single = [random.randint(0,16),random.randint(0,3000),random.randint(0,1)]
        for i in range(30):
            self.missile_arrange.append(arrange_single)
        return self.missile_arrange
   
    def step(self, status):
        
        # 原则上是根据规划直接生成动作就行了，state是不是读进来甚至都没有特别大的关系
        self.status = status
        self.detected_state = self.get_detect_info(self.status)

        self.num += 1
        self.act = []
        for arrange_single in self.missile_arrange:
            # 按理来说每一个都寻址一遍其实是比较蠢的，但是先不管了，反正也没几个
            self.act = self.arrange_to_action_single(arrange_single)
        return self.act
        pass

    def get_reward(self,status):
        # 这个是从态势里面把奖励函数读出来。
        print("unfinished yet ")
        return random.randint(0,100)
        pass
    
class warhead_type(Enum):
    # 要比较优先级的，还是整个枚举类好了。
    slide = 0
    ballistic = 1

class target_type(Enum):
    # 这个是目标类型
    CVN = 0
    CG = 1
    DDG = 2

if __name__ == "__main__":
    shishi = BaseAgent()
    shishi.get_missile_arrange_debug()
    for i in range(3000):
        status = {}
        shishi.step(status)
    pass 
