# 还是搞专业一点，把只在GA里用的放在这里面，而不是全都放在base_agent里面
import os.path
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import argparse
import agent.base_agent as base_agent
import random 

class arrangeEnv():
    def __init__(self):
        self.gene = [] 
        self.__init_net()
        self.__init_agent()
        self.__init_dim()

        pass

    def __init_net(self):

        parser = argparse.ArgumentParser(description='Provide arguments for agent.')
        parser.add_argument("--ip", type=str, default="127.0.0.1", help="Ip to connect")
        # parser.add_argument("--ip", type=str, default="192.168.43.93", help="Ip to connect")
        parser.add_argument("--port", type=str, default=20001, help="port to connect")
        parser.add_argument("--epochs", type=int, default=200, help="Number of training epochs to run")  # 设置训练轮次数
        parser.add_argument("--max-episode-len", type=int, default=3000, help="maximum episode length")
        net_args = parser.parse_args()
        return net_args

    def __init_dim(self):
        # self.action_dim = 30*3 # 30个弹，每个有三个维度
        self.action_dim = self.agent.action_dim
        self.state_dim = 0 # 这个好像不怎么需要了
        self.reward = 0 # 准备直接用从平台读出来的分数了

    def __init_agent(self):
        self.agent = base_agent.BaseAgent()
    
    def reset(self):
        self.gene = []
        self.agent.reset()

    def gene_to_arrange(self, gene):
        missile_arrange = [] 
        for i in range(30):
            missile_arrange_single = []
            missile_arrange_single.append(gene[3*i])
            missile_arrange_single.append(gene[3*i+1])
            missile_arrange_single.append(gene[3*i+2])
            missile_arrange.append(missile_arrange_single)
        return missile_arrange
        pass
    
    def arrange_to_gene(self, missile_arrange):
        gene = []
        for i in range(30):
            gene.append(missile_arrange[i][0])
            gene.append(missile_arrange[i][1])
            gene.append(missile_arrange[i][2])
        return gene

    def step(self, gene):
        status_debug = dict()
        # 这里的step是给GA调用的，包含一个完整的从gene到arrange，然后再到act然后再到reward的一个东西。
        # 懒得折腾了，直接取整了
        gene_int = self.round_all(gene)
        self.gene = gene_int
      
        # 然后转成missile_arrange
        missile_arrange = self.gene_to_arrange(gene_int)
        self.agent.missile_arrange = missile_arrange

        # 然后在agent里面走一波。
        self.agent.step(status_debug)
        self.agent.get_reward(status_debug)
        self.reward = self.agent.reward
        return self.reward
    
    def round_all(self,float_list):
        return [round(i) for i in float_list]

    def get_gene_debug(self):
        # 这个就是生成一个随机的gene，用来debug的
        missile_arrange = []
        for i in range(30):
            arrange_single = [random.randint(0,16),random.randint(0,3000),random.randint(0,1)]
            missile_arrange.append(arrange_single)
        gene_random = self.arrange_to_gene(missile_arrange)
        return gene_random
    
    def generate_range(self):
        # 这个就调用之前的
        xiajie, shangjie = self.agent.generate_range()
        return xiajie, shangjie

if __name__ == "__main__":
    # 姑且把这个称作单元测试吧，搞得阳间一点
    env = arrangeEnv()
    for i in range(10):
        gene = env.get_gene_debug()
        # print(gene)
        reward = env.step(gene)
        # print(reward)

