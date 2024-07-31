import os.path
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import inspyred
from inspyred.ec import emo
import pickle 
import time,os
from random import Random, seed
import numpy as np
from support.env_for_GA import arrangeEnv
from support.huatu import huatu

class GAoptimizer():
    def __init__(self) -> None:
        self.environment = arrangeEnv()
        self.action_dim = self.environment.action_dim
        self.xiajie, self.shangjie = self.environment.generate_range()
        self.N_call_env = 0

        self.__init_location()
        self.__init_GA()


    def __init_location(self):
        # 处理一下存结果的位置。
        location = r"auto_test"
        shijian = time.strftime("%Y-%m-%d", time.localtime())
        self.save_location = location + '\GAresults' + shijian
        try:
            os.mkdir(self.save_location)
        except:
            print('GAoptimizer: folder already there')
        pass      

    def __init_GA(self):
        # 初始化一些inspyred相关的东西
        rand = Random()
        rand.seed(time.time())
        self.ea = inspyred.ec.emo.NSGA2(rand)
        self.ea.terminator = inspyred.ec.terminators.generation_termination
        self.ea.variator = [inspyred.ec.variators.blend_crossover, inspyred.ec.variators.gaussian_mutation]

        self.converge_history = np.array([0,0]).reshape(1,2)
        self.converge_history_last = 0  

        self.candidates = 0 
        self.fitness = 0 

        self.step_number = 100 
        self.pop_size = 100 
        self.max_generations = 400              

    # def generate_env(self,random,args):
    #     size = args.get('num_inputs', 4) # if num_input are not setted 
    #     xiajie = self.environment.observation_space.low[0]
    #     shangjie = self.environment.observation_space.high[0]
    #     return [random.uniform(xiajie,shangjie) for i in range(size)]        
    #     pass
    def generate_env(self,random,args):
        # 这个我记得是生成初值的。
        size = args.get('num_inputs', 30*3) # if num_input are not setted 
        # xiajie, shangjie = self.environment.generate_range()
        return [random.uniform(self.xiajie[i],self.shangjie[i]) for i in range(size)]

    def evaluate_env(self,candidates, args):
        # pass
        fitness = []
        env = self.environment
        env.reset()
        for cs in candidates:
            reward = env.step(cs)
            self.N_call_env = self.N_call_env +1 
            fitness.append(emo.Pareto([reward]))
            env.reset()
        self.record_converge_history(self.N_call_env,np.max(fitness))
        rizhi = 'GAoptimizer: finish calculating one generation, N_call_env = '+str(self.N_call_env)+'\nmax fitness ='+str(np.max(fitness))
        self.jilu(rizhi)
        return fitness        
        pass 

    def record_converge_history(self,N_env,fitness ):
        # chicun = self.converge_history.shape
        self.converge_history = np.append(self.converge_history,np.array([N_env+self.converge_history_last,fitness]).reshape(1,2),axis=0)

    def train_env(self):
        print('GAoptimizer: start to train something interesting')

        # projdir = os.path.dirname(os.getcwd())
        stat_file_name = self.save_location + '/stat_file.csv'
        ind_file_name = self.save_location + '/ind_file_name.csv'
        stat_file = open(stat_file_name, 'w')
        ind_file = open(ind_file_name, 'w')
        
        
        final_pop = self.ea.evolve(generator=self.generate_env,evaluator=self.evaluate_env,pop_size=100,seed=[],maximize=True,bounder=inspyred.ec.Bounder(self.xiajie,self.shangjie),max_generations=3,mutation_rate=0.25,num_inputs=self.action_dim,statistics_file=stat_file,individuals_file=ind_file)

        stat_file.close()
        ind_file.close()

        final_pop.sort(reverse=True)
        self.final_pop = final_pop
        # self.converge_history = np.array([self.N_call_env,final_pop[0].fitness])
        rizhi = '\n\nMXairfoil: (GA) finished, final_pop[0] = '+str(final_pop[0])+'\n converge in '+str(self.converge_history)
        self.jilu(rizhi)
        return final_pop
    
    def jilu(self,strBuffer):
        shijian = time.strftime("%Y-%m-%d-%H:%M", time.localtime()) 

        wenjianming = self.save_location + '/log.txt'
        rizhi = open(wenjianming,'a')
        rizhi.write(strBuffer)
        rizhi.write('\n'+shijian+'\n')
        rizhi.close()
        print(strBuffer)
        return
    
    def load_GA(self,**kargs):
        
        if 'location' in kargs:
             self.save_location = kargs['location']

        location = self.save_location

        final_pop_location = location + '/final_pop.pkl' 
        self.final_pop = pickle.load(open(final_pop_location,'rb'))


        converge_history_location = location + '/converge_history.pkl' 
        self.converge_history = pickle.load(open(converge_history_location,'rb'))

        candidates_history_location = location + '/candidates.pkl' 
        self.candidates = pickle.load(open(candidates_history_location,'rb'))

        fitness_location = location + '/fitness.pkl' 
        self.fitness = pickle.load(open(fitness_location,'rb'))    

    def save_GA(self):
        # output something. result, time consumption,and so on.
        # shijian = time.strftime("%Y-%m-%d-%H:%M", time.localtime())
        location = self.save_location 
        if not(os.path.exists(location)):
            #which means there are no such folder, then mkdir.
            try:
                os.mkdir(location)
            except:
                print('MXairfoil: can not make dir for saveing GA. ',location)
                location = r"C:\temp"
        
        final_pop_location = location + '/final_pop.pkl' 
        
        try:
            pickle.dump(self.final_pop,open(final_pop_location,'wb'))
        except:
            print('MXairfoil: GA running, no final pop to save.')

        converge_history_location = location + '/converge_history.pkl' 
        pickle.dump(self.converge_history,open(converge_history_location,'wb'))

        candidates_history_location = location + '/candidates.pkl' 
        pickle.dump(self.candidates,open(candidates_history_location,'wb'))

        fitness_location = location + '/fitness.pkl' 
        pickle.dump(self.fitness,open(fitness_location,'wb'))

    def huatu_converge(self):
        tu = huatu(self.converge_history)
        tu.set_location(self.save_location)
        tu.huatu2D('Steps Number','Best Pop','GA Converge history')
        tu.save_all()        

if __name__ == '__main__':
    total_time_start = time.time()
    flag = 1
    if flag == 0:
        print("GAoptimizer: test initialize")
        shishi = GAoptimizer()
    elif flag == 1:
        print("GAoptimizer: test running")
        shishi = GAoptimizer()
        final_pop = shishi.train_env()
        shishi.save_GA()
        shishi.huatu_converge()
    pass