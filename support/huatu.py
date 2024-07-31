# establish a universal huatu class
# from pyexpat import model
# from tkinter import N
from turtle import width
from matplotlib.colors import Colormap
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib import rcParams
import matplotlib as mpl

import numpy as np
import os 
import pickle
import time

from numpy.lib.type_check import real

# from parameters import parameters
# from transfer import transfer

class huatu():
    def __init__(self,input,**kargs):
        self.input = input
        self.x_name = 'x'
        self.y_name = 'y'
        self.title = 'huatu'
        self.yanse = ['C0','C1','C2','C3','C4','C5','C6']
        # if os.environ['COMPUTERNAME'] == 'DESKTOP-GMBDOUR' :
        #     #which means in my diannao
        #     self.location = 'C:/Users/y/Desktop'
        # else:
        #     # which means in 106 server   
        #     self.location = 'C:/Users/106/Desktop'
        self.location = r"auto_test" # 试试改个相对路径，这玩意一直就有点没玩明白。
        self.x = [] 
        self.y = []
        self.flag = 0 # 0 for uninitialized x,y
        # self.transfer = transfer()        
        if 'real_dim' in kargs:
            self.real_dim = kargs['real_dim']
        else:
            self.real_dim = 2 
        self.end_point=np.array([]).reshape(0,self.real_dim)
        config = {
                    "font.family":'serif',
                    "font.size": 10,
                    "mathtext.fontset":'stix',
                    "font.serif": ['SimSun'],
                }
        rcParams.update(config)

        # define some color for average reward and optimization reward.
        # https://matplotlib.org/stable/gallery/color/named_colors.html
        self.ave_r_color_chosen = 'royalblue'
        self.ave_r_color_normal = 'lightsteelblue'
        self.opt_r_color_chosen = 'orange'
        self.opt_r_color_normal = 'moccasin'

        self.zihao = 10
        self.xianxing = ['solid','dotted','dashed','dashdot']

        
    def huatu2D(self,x_name,y_name,title,**kargs):
        #simple line.
        self.title = 'simple line'
        self.x_name = x_name
        self.y_name = y_name
        self.title = title

        try:
            data = np.array(self.input)
        except:
            print('MXairfoil: invalide data for huatu2D')
            return
        
        if self.flag == 0:
            #which means uninitialized 
            x = data[:,0]
            y = data[:,1]
            self.x = x
            self.y = y 
        else :
            x = self.x
            y = self.y
        
        fig, ax = plt.subplots()
        
        bili = 2
        fig.set_figheight(4.3267717*bili)
        fig.set_figwidth(5.9251969*bili) # 5.9251969 inches = 15.05cm which is used in MS word
        self.set_chicun(fig)

        ax.plot(x, y)

        x_changdu = x.max() - x.min()
        y_changdu = y.max() - y.min()
        ax.set_xlim(x.min()-0.1*x_changdu, x.max()+0.1*x_changdu)
        ax.set_ylim(y.min()-0.1*y_changdu, y.max()+0.1*y_changdu)

        x_label = np.arange(x.min(),x.max(),0.1*x_changdu)
        y_label = np.arange(y.min(),y.max(),0.1*y_changdu)
        plt.yticks(fontproperties = 'Times New Roman', size = 14)
        plt.xticks(fontproperties = 'Times New Roman', size = 14) 
        plt.legend(prop={"family" : "Times New Roman" ,'size' : '12'})
        ax.set_xticks(x_label)
        ax.set_yticks(y_label)
        ax.set_xlabel(self.x_name,fontsize=20,fontproperties='Times New Roman')
        ax.set_ylabel(self.y_name,fontsize=20,fontproperties='Times New Roman')
        ax.set_title(self.title,fontsize=20,fontproperties='Times New Roman')
        ax.grid()

        wenjianjia = self.location + '/' + self.title
        try:
            os.mkdir(wenjianjia)
        except:
            print('MXairfoil: wenjianjia already there.')
        wenjianming_tu = wenjianjia + '/' + self.title + '.png'
        plt.savefig(wenjianming_tu,dpi=1200)
        # plt.show()
        self.fig = fig 
        self.ax = ax 
        plt.close()

    def huatu2(self,x_name,y_name,title,**kargs):
        #this is something like huatu2.m in matlab.
        if 'x_name' in kargs:
            self.x_name = kargs['x_name']
        else:
            self.x_name = 'x_name'
        if 'y_name' in kargs:
            self.y_name = kargs['y_name']
        else:
            self.y_name = 'y_name'
        if 'title' in kargs:
            self.title = kargs['title']
        else:
            self.title = 'simple line'
            
        try:
            data = np.array(self.input)
        except:
            print('MXairfoil: invalide data for huatu2D')
            return
        
        if self.flag == 0:
            #which means uninitialized 
            x = data[:,0]
            y = data[:,1]
            self.x = x
            self.y = y 
        else :
            x = self.x
            y = self.y
        
        fig, ax = plt.subplots()
        
        bili = 2
        fig.set_figheight(4.3267717*bili)
        fig.set_figwidth(5.9251969*bili) # 5.9251969 inches = 15.05cm which is used in MS word

        ax.plot(x, y)

        x_changdu = x.max() - x.min()
        y_changdu = y.max() - y.min()
        ax.set_xlim(x.min()-0.1*x_changdu, x.max()+0.1*x_changdu)
        ax.set_ylim(y.min()-0.1*y_changdu, y.max()+0.1*y_changdu)

        x_label = np.arange(x.min(),x.max(),0.1*x_changdu)
        y_label = np.arange(y.min(),y.max(),0.1*y_changdu)

        ax.set_xticks(x_label)
        ax.set_yticks(y_label)
        ax.set_xlabel(self.x_name,fontsize=20,fontproperties='Times New Roman')
        ax.set_ylabel(self.y_name,fontsize=20,fontproperties='Times New Roman')
        ax.set_title(self.title,fontsize=20,fontproperties='Times New Roman')
        ax.grid()

        # wenjianjia = self.location + '/' + self.title
        # try:
        #     os.mkdir(wenjianjia)
        # except:
        #     print('MXairfoil: wenjianjia already there.')
        # wenjianming_tu = wenjianjia + '/' + self.title + '.png'
        # plt.savefig(wenjianming_tu,dpi=1200)
        plt.show()
        self.fig = fig 
        self.ax = ax 
        # plt.close()
        
    def huatu2D_mul(self,x_name,y_name,title,names):
        # simple lines, and its legend.
        N_mul = len(names)
        
        self.x_name = x_name
        self.y_name = y_name
        self.title = title

        try:
            data = np.array(self.input)
        except:
            print('MXairfoil: invalide data for huatu2D')
            return
        x = data[:,0]
        y = data[:,1:]
        self.x = x
        self.y = y 
        fig, ax = plt.subplots()
        ax.plot(x, y)
        for i in range(N_mul):
            ax.plot(x, y[:,i],label=names[i])
        plt.legend()
        x_changdu = x.max() - x.min()
        y_changdu = y.max() - y.min()
        ax.set_xlim(x.min()-0.1*x_changdu, x.max()+0.1*x_changdu)
        ax.set_ylim(y.min()-0.1*y_changdu, y.max()+0.1*y_changdu)

        x_label = np.arange(x.min(),x.max(),0.1*x_changdu)
        y_label = np.arange(y.min(),y.max(),0.1*y_changdu)

        ax.set_xticks(x_label)
        ax.set_yticks(y_label)
        ax.set_xlabel(self.x_name)
        ax.set_ylabel(self.y_name)
        ax.set_title(self.title)
        ax.grid()
        # weizhi = self.location + '/' + self.title + '.png'
        # plt.savefig(weizhi,dpi=300)
        wenjianjia = self.location + '/' + self.title
        try:
            os.mkdir(wenjianjia)
        except:
            print('MXairfoil: wenjianjia already there.')
        wenjianming_tu = wenjianjia + '/' + self.title + '.png'
        plt.savefig(wenjianming_tu,dpi=1200)
        # plt.show()
        self.fig = fig 
        self.ax = ax
        # self.save_all()
        plt.close()

    def huatu2D_mul2(self,x_name,y_name,title,*names,title_flag=True,align_flag = True,x_min = 0,y_min=0,**kargs):
        N_mul = len(names)
        xianxing = ['solid','dotted','dashed','dashdot']
        yanse = self.yanse
        self.xianxing = xianxing
        self.x_name = x_name
        self.y_name = y_name
        self.title = title

        N_mul2 = len(self.x)
        if N_mul != N_mul2:
            print('MXairfoil: unmatch number of lines and names')
            return

        if 'redraw' in kargs:
            redraw = kargs['redraw']
            if  redraw ==True:
                fig =self.fig
                ax = self.ax 
                ax2 = self.ax2
            else:
                fig, ax = plt.subplots()
        else:
            redraw = False
            fig, ax = plt.subplots()

        if 'case' in kargs:
            if kargs['case'] == 'CDA' : 
                self.set_chicun(fig,width=10,height=6,adjust=[0.2,0.8,0.4,0.8]) # this is for big ones.
                # bottom=shuzi[0], right=shuzi[1], left = shuzi[2],top=shuzi[3]
                zihao = 10 
                xiankuan =1 
            elif kargs['case'] == 'demo' :
                self.set_chicun(fig) # this is for democase.
                zihao = 12 
                xiankuan =2 
            elif kargs['case'] == 'demo18':
                self.set_chicun(fig) # this is for democase.
                zihao = 10 
                xiankuan =1                 
        else:
            self.set_chicun(fig) # this is for democase.
            zihao = 10 
            xiankuan =1
        self.zihao = zihao 
        # self.set_chicun(fig,width=20,height=4,adjust=[0.2,0.8,0.4,0.8]) # this is for big ones.
        # self.set_chicun(fig) # this is for democase.
        rcParams.update({'font.size': str(zihao)})

        y_max = 0 
        y_min = y_min 
        x_max = 0
        x_min = x_min
        for i in range(N_mul):
            if self.y[i][0] > 10:
                # which means there must be something wrong 
                self.x[i] = np.append(np.array([0]),self.x[i] )
                self.y[i] = np.append(np.array([0]),self.y[i] )
                print('MXairfoil: there must be something wrong in data.')
            x_max = np.max([self.x[i].max(),x_max])
            x_min = np.min([self.x[i].min(),x_min])
            y_max = np.max([self.y[i].max(),y_max])
            y_min = np.min([self.y[i].min(),y_min])        

        for i in range(N_mul):
            if align_flag:
                self.x[i] = np.append(self.x[i],x_max)
                self.y[i] = np.append(self.y[i],self.y[i][-1])
            ax.plot(self.x[i], self.y[i],label=names[i],linestyle=xianxing[i%4],linewidth=xiankuan,color=yanse[i%4])

        if 'single_ax' in kargs:
            pass 
            plt.legend(prop={"family" : "Times New Roman" ,'size' : str(zihao-2)},loc='upper left')
        else:
            plt.legend(prop={"family" : "Times New Roman" ,'size' : str(zihao-2)},loc='lower right')

        x = self.x[i]
        y = self.y[i] 
        x_changdu = x_max - x_min
        y_changdu = y_max - y_min

        # ax.set_xlim(x.min()-0.1*x_changdu, x.max()+0.1*x_changdu)
        # # ax.set_ylim(y.min()-0.1*y_changdu, y.max()+0.1*y_changdu)
        # # ax.set_ylim(y_min-0.1*y_changdu, y_max+0.1*y_changdu)
        # ax.set_ylim(0, y_max+0.1*y_changdu)

        # more modification to set integer.
        # x_one_grid = round(self.get_one_grid(0.2*x_changdu))
        # y_one_grid = round(self.get_one_grid(0.2*y_changdu))
        x_one_grid = self.get_one_grid(0.2*x_changdu)
        if abs(x_one_grid)>0.51:
            x_one_grid = round(x_one_grid)
        y_one_grid = self.get_one_grid(0.2*y_changdu)
        if abs(y_one_grid)>0.51:
            y_one_grid = round(y_one_grid)

        x_offset = x_min % x_one_grid
        y_offset = y_min% y_one_grid
        
        ax.set_xlim(x_min-x_offset-0.5*x_one_grid, x_max+0.05*x_changdu)
        ax.set_ylim(y_min-y_offset, y_max+0.05*y_changdu)
        # ax.set_ylim(y_min-y_offset, y_max+0.05*y_changdu)
        x_label = np.arange(x_min-x_offset, x_max,x_one_grid)
        y_label = np.arange(y_min-y_offset,y_max,y_one_grid)

        ax.set_xticks(x_label)
        ax.set_yticks(y_label)

        
        ax.set_xlabel(self.x_name,fontsize=zihao,fontproperties='Times New Roman')
        if 'single_ax' in kargs:
            ax.set_ylabel(y_name,fontsize=zihao,fontproperties='Times New Roman')
        else:
            ax.set_ylabel(names[1],fontsize=zihao,fontproperties='Times New Roman')

        ax.tick_params(axis='y', labelcolor='k',labelsize=zihao-2)
        ax.tick_params(axis='x', labelcolor='k',labelsize=zihao-2)
        if title_flag:
            ax.set_title(self.title,fontsize=zihao,fontproperties='Times New Roman')
        
        # ax.grid()
        
        # get another coordinate zhou. This zuobiao axis is for detected optimization.
        if 'single_ax' in kargs:
            print('MXairfoil: single_ax')
            color = 'k'
            y_label = np.arange(y_min-y_offset,y_max,y_one_grid)
            ax.set_yticks(y_label)
            ax.set_ylabel(self.y_name, color=color,fontsize=zihao,fontproperties='Times New Roman')  # we already handled the x-label with ax1
        else:
            if redraw ==True:
                pass
            else:
                ax2 = ax.twinx()
                self.ax2 = ax2
            color = 'k'
            ax2.set_ylim((y_min-y_offset)/100, (y_max+0.05*y_changdu)/100)
            ax2.set_yticks(y_label/100)
            ax2.set_ylabel(names[0], color=color,fontsize=zihao,fontproperties='Times New Roman')  # we already handled the x-label with ax1
            ax2.tick_params(axis='y', labelcolor=color,labelsize=zihao-2)
            fig.tight_layout()


        # plt.yticks(fontproperties = 'Times New Roman', size = zihao-2)
        # plt.xticks(fontproperties = 'Times New Roman', size = zihao-2) 
        for l in ax.yaxis.get_ticklabels():
            l.set_family('Times New Roman') 
 
        for l in ax.xaxis.get_ticklabels():
            l.set_family('Times New Roman') 
        if 'single_ax' in kargs:
            print('MXairfoil: single_ax')
        else:
            for l in ax2.yaxis.get_ticklabels():
                l.set_family('Times New Roman')

        # weizhi = self.location + '/' + self.title + '.png'
        # plt.savefig(weizhi,dpi=300)
        wenjianjia = self.location + '/' + self.title
        try:
            os.mkdir(wenjianjia)
        except:
            print('MXairfoil: wenjianjia already there.')
        wenjianming_tu = wenjianjia + '/' + self.title + '.png'
        
        if 'model' in kargs:
            if kargs['model']=='all':
                self.fig = fig 
                self.ax = ax
                self.ax2 = ax2
                self.x_max = x_max
        else:
            self.fig = fig 
            self.ax = ax
            self.ax2 = ax2
            self.x_max = x_max
            # self.ax2 = ax2
            # self.png2tiff(fig,wenjianming_tu)
            # plt.savefig(wenjianming_tu,dpi=1200)
            # plt.show()
            # self.save_all()
            # plt.close()

    def save_all(self,loc=None):
        #make a folder for saveing the data and figure
        wenjianjia = self.location + '/' + self.title
        try:
            os.mkdir(wenjianjia)
        except:
            print('MXairfoil: wenjianjia already there.')

        # wenjianming_tu = wenjianjia + '/' + self.title + '.png'
        # self.plt.savefig(wenjianming_tu,dpi=300)
        wenjianming_tu = wenjianjia + '/' + self.title + '.png'
        self.fig.savefig(wenjianming_tu,dpi=1200)

        wenjianming_x = wenjianjia + '/x.pkl' 
        pickle.dump(self.x,open(wenjianming_x,'wb'))

        wenjianming_y = wenjianjia + '/y.pkl'
        pickle.dump(self.y,open(wenjianming_y,'wb'))

    def set_location(self,work_folder):
        self.location = work_folder
        if not(os.path.exists(self.location)):
            #which means there are no such folder, then mkdir.
            try:
                os.mkdir(self.location)
            except:
                print('MXairfoil: can not make dir for huatu. ',self.location,'\nreset to Desktop')
                if os.environ['COMPUTERNAME'] == 'DESKTOP-GMBDOUR' :
                    #which means in my diannao
                    self.location = 'C:/Users/y/Desktop'
                else:
                    # which means in 106 server   
                    self.location = 'C:/Users/106/Desktop'

    # def visual_2D(self,flag,id,**kargs):
    #     print('MXairfoil: Unify all the huatu function!')
    #     shijian = time.strftime("%Y-%m-%d", time.localtime())
    #     x_name = parameters['chi_in']
    #     y_name = parameters['chi_out']

    #     agent0_location = self.location
    #     location = self.location
    #     zihao = 12 

    #     wenjianing_X1 = location + '/visual2DX1.pkl'
    #     wenjianing_X2 = location + '/visual2DX2.pkl'
    #     wenjianing_Y1 = location + '/visual2DY1.pkl'
    #     wenjianing_Y2 = location + '/visual2DY2.pkl'
    #     wenjianing_Y3 = location + '/visual2DY3.pkl'

    #     # these data comes from Surrogate_01de.py there are visual_2D.
    #     X1 = pickle.load(open(wenjianing_X1,'rb'))
    #     X2 = pickle.load(open(wenjianing_X2,'rb'))
    #     # Y1 = pickle.load(open(wenjianing_Y1,'rb'))
    #     # Y2 = pickle.load(open(wenjianing_Y2,'rb'))
    #     # biaoti = r'$\omega$'
    #     # biaoti = r'$Rise$'
    #     # choose to draw in omega back ground, or rise back ground 
    #     if 'flag_background' in kargs:
    #         flag_background = kargs['flag_background']
    #     else:
    #         flag_background  = 0
    #     if flag_background == 0 :
    #         biaoti = r'$\omega$'
    #         qianzhui = '/visual2Domega'
    #         Y1 = pickle.load(open(wenjianing_Y1,'rb'))
    #     elif flag_background ==1 :
    #         biaoti = r'$\pi$'
    #         qianzhui = '/visual2Drise'
    #         Y1 = pickle.load(open(wenjianing_Y2,'rb'))
    #     elif flag_background ==2:
    #         biaoti = r'$\Delta\beta$'
    #         qianzhui = '/visual2Dturn'
    #         Y1 = pickle.load(open(wenjianing_Y3,'rb'))
    #     elif flag_background == 3:
    #         # this is for DemoFunction huatu.
    #         biaoti = 'Demo Function'
    #         qianzhui = '/visual2DDemoFunction'
    #         Y1 = pickle.load(open(wenjianing_Y1,'rb'))
    #     else :
    #         print('MXairfoil: wrong in huatu.visual_2D')
    #         # this would never happen logically. no need in fact 
    #         return 

    #     # flag = 2
    #     # these data comes from shishienv83 or its further modifictaion, generated by saved_agent_test.
    #     if flag == 0:
    #         wenjianming_lujing = agent0_location + '/lujing' + str(id) + '.pkl'
    #         lujing = pickle.load(open(wenjianming_lujing,'rb'))
    #         tu_name = qianzhui+str(id)+shijian+'.png'
    #     elif flag ==1 :
    #         wenjianming_lujing = agent0_location + '/raw_state_save0.pkl'
    #         lujing = pickle.load(open(wenjianming_lujing,'rb'))
    #         # lujing = self.translate_surrogate(lujing)
    #         lujing = self.transfer.normal_to_surrogate(lujing[:,0:2])
    #         tu_name = '/visual2Draw_state'+shijian+'.png'
    #     elif flag ==2:
    #         tu_name = qianzhui+'kong' +shijian+'.png'
    #         lujing = np.array([]).reshape(0,7)
    #     elif flag ==4:
    #         # this is for new architecture with dynamic constraints and 
    #         lujing,lujing_new,performace = self.get_lujing(id)
    #         tu_name = qianzhui+str(id)+shijian+'.png'
    #     # wenjianming_lujing = agent0_location + '/lujing' + str(3) + '.pkl'
    #     if 'only_data' in kargs:
    #         if kargs['only_data']:
    #             print('MXairfoil: only get data, do not huatu.')
    #             return
    #         else:
    #             print('MXairfoil: continue to huatu.')
            

    #     chicun = lujing.shape
    #     pingjun = np.sum(lujing,axis=0)
    #     pingjun = pingjun / chicun[0]

    #     # then plot, omega 
    #     norm = plt.cm.colors.Normalize(vmax=Y1.max(), vmin=Y1.min())
    #     fig, ax = plt.subplots()
    #     bili = 0.397 # transfer from cm into inches.
    #     fig.set_figheight(7.7*bili)
    #     fig.set_figwidth(9*bili) # 5.9251969 inches = 15.05cm which is used in MS word % 3.5433071 inches = 9 cm 
    #     # ax.axis('equal')
    #     plt.subplots_adjust(bottom=0.15, right=0.95, left = 0.15,top=0.9)
    #     cset1 = ax.contourf(X1, X2, Y1, 60,norm=norm,alpha=0.7,cmap=plt.cm.rainbow)
    #     ax.set_xlim(0, 1)
    #     ax.set_ylim(0, 1)
    #     x_label = np.arange(0,1.1,0.1)
    #     ax.set_xticks(x_label)
    #     ax.set_yticks(x_label)
    #     # ax.set_xlabel(r'$\chi_{in}$')
    #     # ax.set_ylabel(r'$\chi_{out} $')
    #     if 'labels' in kargs:
    #         ax.set_xlabel(kargs['labels'][0],fontsize=zihao)
    #         ax.set_ylabel(kargs['labels'][1],fontsize=zihao)
    #     else:
    #         ax.set_xlabel(parameters.get_equation(x_name,normal=True),fontsize=zihao)
    #         ax.set_ylabel(parameters.get_equation(y_name,normal=True),fontsize=zihao)  
    #     if 'biaoti' in kargs:
    #         biaoti = kargs['biaoti']   
 
    #     # biaoti_omega = r'$\omega$'
    #     # biaoti_rise = r'$Rise$'
    #     ax.set_title(biaoti,fontsize=zihao,fontproperties = 'Times New Roman')
    #     ax.set(xlim=(0, 1), ylim=(0, 1))
    #     cb = plt.colorbar(cset1,ax=ax)
    #     plt.yticks(fontproperties = 'Times New Roman', size = zihao-2)
    #     plt.xticks(fontproperties = 'Times New Roman', size = zihao-2) 
    #     for l in cb.ax.yaxis.get_ticklabels():
    #         l.set_family('Times New Roman') 
    #     for l in cb.ax.xaxis.get_ticklabels():
    #         l.set_family('Times New Roman') 

    #     # then plot the lujing, show how the state get into optimal.

    #     x_lujing = lujing[:,x_name.value] # parameter.py is not conbiniet to use.
    #     y_lujing = lujing[:,y_name.value]
    #     tu_lujing = ax.plot(x_lujing, y_lujing, color='red', marker='o', linestyle='solid',linewidth=1, markersize=2)

    #     # then save and show.
    #     # plt.show()
    #     # self.png2tiff(fig,self.location+tu_name)
    #     plt.savefig(self.location+tu_name,dpi=1200)
    #     # plt.savefig(self.location+'/visual2Drise'+shijian+'.png',dpi=300)
    #     # plt.show()
    #     plt.close()

    # def visual_3D(self,flag,id,**kargs):
    #     print('MXairfoil: plotting 3D results')
    #     shijian = time.strftime("%Y-%m-%d", time.localtime())
    #     x_name = parameters['chi_in']
    #     y_name = parameters['chi_out']
    #     z_name = parameters['umxthk']

    #     agent0_location = self.location
    #     location = self.location    

    #     wenjianing_X1 = location + '/visual2DX1.pkl'
    #     wenjianing_X2 = location + '/visual2DX2.pkl'
    #     wenjianing_Y1 = location + '/visual2DY1.pkl'
    #     wenjianing_Y2 = location + '/visual2DY2.pkl'

    #     # these data comes from Surrogate_01de.py there are visual_2D.
    #     X1 = pickle.load(open(wenjianing_X1,'rb'))
    #     X2 = pickle.load(open(wenjianing_X2,'rb'))
    #     flag_background  = 0
    #     if flag_background == 0 :
    #         biaoti = r'$\omega$'
    #         qianzhui = '/visual3Domega'
    #         Y1 = pickle.load(open(wenjianing_Y1,'rb'))
    #     elif flag_background ==1 :
    #         biaoti = r'$Rise$'
    #         qianzhui = '/visual3Drise'
    #         Y1 = pickle.load(open(wenjianing_Y2,'rb'))
    #     else :
    #         print('MXairfoil: wrong in huatu.visual_3D')
    #         # this would never happen logically. no need in fact 
    #         return  

    #     # qianzhui = 'Vistual3D'
    #     # biaoti = r'$\omega$'

    #     # flag = 0
    #     # these data comes from shishienv83 or its further modifictaion, generated by saved_agent_test.
    #     if flag == 0:
    #         wenjianming_lujing = agent0_location + '/lujing' + str(id) + '.pkl'
    #         lujing = pickle.load(open(wenjianming_lujing,'rb'))
    #         tu_name = qianzhui+str(id)+shijian+'.png'
    #     elif flag ==1 :
    #         wenjianming_lujing = agent0_location + '/raw_state_save0.pkl'
    #         lujing = pickle.load(open(wenjianming_lujing,'rb'))
    #         # lujing = self.translate_surrogate(lujing)
    #         lujing = self.transfer.normal_to_surrogate(lujing)
    #         tu_name = '/visual3Draw_state'+shijian+'.png'
    #     elif flag ==2:
    #         tu_name = '/visual3Dkong'+shijian+'.png'
    #         lujing = np.array([]).reshape(0,7) 
    #     elif flag ==4:
    #         # this is for new architecture with dynamic constraints and 
    #         lujing,lujing_new,performace = self.get_lujing(id)
    #         tu_name = qianzhui+str(id)+shijian+'.png'
    #     # wenjianming_lujing = agent0_location + '/lujing' + str(3) + '.pkl'
    #     if 'only_data' in kargs:
    #         if kargs['only_data']:
    #             print('MXairfoil: only get data, do not huatu.')
    #             return
    #         else:
    #             print('MXairfoil: continue to huatu.')
    #     # then prepare the data for continue
    #     lujing = lujing[1:]
    #     biaozhu = lujing[-1]
    #     x_lujing = lujing[:,x_name.value] # parameter.py is convenient to use.
    #     y_lujing = lujing[:,y_name.value]
    #     z_lujing = lujing[:,z_name.value]
    #     r_lujing = lujing[:,7-1]
    #     omega_lujing = lujing[:,7-3]
    #     omega_huatu = -500*omega_lujing + 28.2


    #     # then prepare a color map  
    #     # norm = plt.cm.colors.Normalize(vmax=r_lujing.max, vmin=r_lujing.min)
    #     norm = plt.cm.colors.Normalize(vmax=omega_huatu.max, vmin=omega_huatu.min)
    #     # norm = plt.cm.colors.Normalize(vmax=omega_lujing.max, vmin=omega_lujing.min)

    #     # then start to huatu. this is something called Multicolored lines.
    #     # trying to zhao cat hua tiger.
    #     points = np.array([x_lujing, y_lujing,z_lujing]).T.reshape(-1, 1, 3)
    #     # segments = np.concatenate([points[:-1], points[1:]], axis=1)
    #     segments = np.concatenate([points[:-1], points[1:]], axis=1)
    #     fig= plt.figure()
  
    #     bili = 1.2
    #     fig.set_figheight(4.3267717*bili)
    #     fig.set_figwidth(5.9251969*bili) # 5.9251969 inches = 15.05cm which is used in MS word
    #     fontsize_zhou=15
    #     fontsize_title = 20
    #     fontsize_tip = 19
    #     ax = plt.axes(projection='3d')
    #     ax.grid(False)

    #     lc = Line3DCollection(segments,cmap=plt.cm.rainbow) # cao? it get right by mishandleing. no norm or it will fall.

    #     # Set the values used for colormapping
    #     lc.set_array(omega_huatu)
    #     lc.set_linewidth(2)

    #     line = ax.add_collection3d(lc)

    #     # then try some projection.
    #     ax.plot3D(x_lujing,y_lujing,zdir='z',linewidth =1,color=(0.3, 0.3, 0.3))
    #     ax.plot3D(x_lujing,z_lujing,1,zdir='y',linewidth =1,color=(0.3, 0.3, 0.3))
    #     ax.plot3D(y_lujing,z_lujing,zdir='x',linewidth =1,color=(0.3, 0.3, 0.3))

    #     # then plot some lines to show porjection
    #     self.chuixian(ax,x_lujing[0],y_lujing[0],z_lujing[0])
    #     self.chuixian(ax,x_lujing[-1],y_lujing[-1],z_lujing[-1])

    #     ax.text(biaozhu[0], biaozhu[1], biaozhu[3]+0.01, r'$P_0$', color='k',fontsize=fontsize_tip,fontproperties='Times New Roman')


    #     # labels 
    #     ax.set_xlim(0, 1)
    #     ax.set_ylim(0, 1)
    #     ax.set_zlim(0, 1)

    #     x_label = np.arange(0,1.1,0.1)
    #     ax.set_xticks(x_label)
    #     ax.set_yticks(x_label)
    #     ax.set_zticks(x_label)
    #     ax.set_xlabel(parameters.get_equation(x_name),fontsize=fontsize_zhou,fontproperties = 'Times New Roman')
    #     ax.set_ylabel(parameters.get_equation(y_name),fontsize=fontsize_zhou,fontproperties = 'Times New Roman')
    #     ax.set_zlabel(parameters.get_equation(z_name),fontsize=fontsize_zhou,fontproperties = 'Times New Roman')
    #     ax.set_title(biaoti,fontsize=fontsize_title,fontproperties = 'Times New Roman')

    #     plt.yticks(fontproperties = 'Times New Roman', size = 10)
    #     plt.xticks(fontproperties = 'Times New Roman', size = 10) 
    #     # plt.zticks(fontproperties = 'Times New Roman', size = 15)
    #     for l in ax.yaxis.get_ticklabels():
    #         l.set_family('Times New Roman') 
    #     for l in ax.zaxis.get_ticklabels():
    #         l.set_family('Times New Roman') 

    #     # plt.savefig('shishi.png',dpi=700)
    #     plt.savefig(self.location+tu_name,dpi=1200)
    #     # plt.show()
    #     plt.close()

    def load_data(self,location,title):
        # coordinate with save_all, load prepared data, for further modification.
        self.location = location
        self.title = title
        wenjianjia = self.location + '/' + self.title
        wenjianming_x = wenjianjia + '/x.pkl' 
        self.x = pickle.load(open(wenjianming_x,'rb'))

        wenjianming_y = wenjianjia + '/y.pkl'
        self.y = pickle.load(open(wenjianming_y,'rb'))

        self.flag = 1 

    def load_data_mul(self,*arg):
        #locations are in arg.
        geshu = len(arg)
        self.x = [] 
        self.y = []
        for i in range(geshu):
            wenjianjia = arg[i]
            wenjianming_x = wenjianjia + '/x.pkl' 
            wenjianming_y = wenjianjia + '/y.pkl'
            x_i = pickle.load(open(wenjianming_x,'rb'))
            y_i = pickle.load(open(wenjianming_y,'rb'))
            # if i ==0:
            #     y_i = y_i * 100 
            if max(y_i) < 1:
                y_i = y_i * 100 
            self.x.append(x_i)
            self.y.append(y_i)
    
    def load_data_add(self,data,**kargs):
        # just add a set of x-y into huatu.
        if 'location' in kargs:
            wenjianjia = kargs['location']
            wenjianming_x = wenjianjia + '/x.pkl' 
            data_x = pickle.load(open(wenjianming_x,'rb'))

            wenjianming_y = wenjianjia + '/y.pkl'
            data_y = pickle.load(open(wenjianming_y,'rb'))
        else:
            if len(data) == 1:
                data = data[0]
                
            if type(data) == list:
                self.x.append(data[:][0])
                self.y.append(data[:][1]) 
            elif type(data) == np.ndarray :
                self.x.append(data[:,0])
                self.y.append(data[:,1])
            else:
                raise Exception('MXairfoil: invalid input in load_data_add:'+type(data[0]))

    '''        
    def translate_surrogate(self,state):
        dx = 0.1

        normal_obs_space_h =np.array([1,1,1,1,1,1,1])
        normal_obs_space_l =np.array([-1,-1,-1,-1,-1,-1,-1]) 
        surrogate_obs_space_h = np.array([1+dx,1+dx,1+dx,1+dx])
        surrogate_obs_space_l = np.array([0-dx,0-dx,0-dx,0-dx])

        # first, transfer from agent/env([-1,1]) into surrogate([0,1])
        bili1 = (surrogate_obs_space_h-surrogate_obs_space_l)/(normal_obs_space_h[0:4] - normal_obs_space_l[0:4])
        zhong_normal = (normal_obs_space_h[0:4] + normal_obs_space_l[0:4])/2
        zhong_surrogate = (surrogate_obs_space_h+surrogate_obs_space_l)/2

        chicun = state.shape
        state_surrogate = state
        for i in range(chicun[0]):
            state_surrogate[i][0:4] = (state[i][0:4] - zhong_normal) * bili1 + zhong_surrogate
        # state_surrogate = (state[0:4] - zhong_normal) * bili1 + zhong_surrogate

        # state[0:4] = state_surrogate
        return state_surrogate
    '''
    def shishi(self,*arg,**kargs):
        # this is to learn how to use *arg and **karg
        changdu = len(kargs)
        changdu2 = len(arg)
        # if kargs.has_key('canshu'):
        if 'canshu' in kargs:
            shuzi = kargs['canshu'] * 2
        print('MXairfoil: end a learning method shishi.')

    def chuixian(self,ax,x,y,z):
        #this is to draw some chuixian
        x_xian = np.array([x,x]).reshape(2,)
        y_xian = np.array([y,y]).reshape(2,)
        z_xian = np.array([z,z]).reshape(2,)

        x_ling = np.array([0,x]).reshape(2,)
        y_ling = np.array([1,y]).reshape(2,)
        z_ling = np.array([0,z]).reshape(2,)

        canshu = {'linewidth' :0.5,'color':(0.7, 0.7, 0.7),'linestyle' : '--'}
        # ax.plot3D(x_xian,y_xian,z_ling,linewidth =1.5,color='k',linestyle = '--')#  color=(0.7, 0.7, 0.7)
        ax.plot3D(x_xian,y_xian,z_ling,linewidth =canshu['linewidth'],color=canshu['color'],linestyle =canshu['linestyle'])
        ax.plot3D(x_xian,y_ling,z_xian,linewidth =canshu['linewidth'],color=canshu['color'],linestyle =canshu['linestyle'])
        ax.plot3D(x_ling,y_xian,z_xian,linewidth =canshu['linewidth'],color=canshu['color'],linestyle =canshu['linestyle'])

    def plot_surrogate(self,**kargs):
        # this is to plot that diagonal like picture, showing surrogate model is good. 
        data_location = kargs['location']
        location_X_test = data_location+'/X_test.pkl'
        location_yy1 = data_location+'/yy1.pkl'
        location_yy2 = data_location+'/yy2.pkl'
        location_yy3 = data_location+'/yy3.pkl'


        try:
            X_rand = pickle.load(open(location_X_test,'rb'))
            yy1 = pickle.load(open(location_yy1,'rb'))
            yy2 = pickle.load(open(location_yy2,'rb'))
            yy3 = pickle.load(open(location_yy3,'rb'))
        except:
            print('MXairfoil: no valid data in '+ data_location)

        shijian = time.strftime("%Y-%m-%d", time.localtime())
        daxiao_label = 8 
        daxiao_title = 8 
        bili = 1.0/2
        def huatu_surrogate(i,shuju,title,x_lable,y_lable,name):
            yy = shuju
            fig = plt.figure(i)
            fig.set_figheight(5.5*bili)
            fig.set_figwidth(6.5*bili) # 5.9251969 inches = 15.05cm which is used in MS word
            plt.subplots_adjust(bottom=0.15, right=0.95, left = 0.15,top=0.9)
            # plt.xlabel(x_lable,fontsize=daxiao_label*2) 
            # plt.ylabel(y_lable,fontsize=daxiao_label*2)        
            plt.yticks(fontproperties = 'Times New Roman', size = daxiao_label)
            plt.xticks(fontproperties = 'Times New Roman', size = daxiao_label) 
            # plt.title('Total pressure loss coefficient',fontproperties='Times New Roman',fontsize=daxiao_title)
            plt.title(title,fontproperties='Times New Roman',fontsize=daxiao_title*2)
            # marker = '.'
            plt.plot(yy[:,0],yy[:,0],marker='.',markersize = 5,ls='None',color = 'red',label = 'Real') 
            plt.plot(yy[:,0],yy[:,1],marker='2',markersize = 5,markeredgewidth=1,ls='None',color = 'green',label = 'Predict')
            plt.legend(prop={"family" : "Times New Roman" ,'size' : str(daxiao_label)})
            # plt.show() # if show, then savefig would fall. shabi logic
            wenjianming_omega = self.location + '/'+name+shijian+'.png'
            # self.png2tiff(fig,wenjianming_omega)
            plt.savefig(wenjianming_omega, dpi=1200)
            plt.close(i)
        
        huatu_surrogate(0,yy1,r'$ \omega$',r'$ \omega_{real}$',r'$\omega_{predict}$','omega')
        huatu_surrogate(1,yy2,r'$ \pi$',r'$ \pi_{real}$',r'$\pi_{predict}$','pi')
        huatu_surrogate(2,yy3,r'$ \Delta\beta$',r'$ \Delta\beta_{real}$',r'$\Delta\beta_{predict}$','turn')

    def plot_surrogate_3D(self,yy_list,**kargs):
        # this is for 3D surrogate model, simplify the code.
        shijian = time.strftime("%Y-%m-%d", time.localtime())
        daxiao_label = 8 
        daxiao_title = 8 
        bili = 1.0/2
        def huatu_surrogate(i,shuju,title,x_lable,y_lable,name):
            yy = shuju
            fig = plt.figure(i)
            fig.set_figheight(5.5*bili)
            fig.set_figwidth(6.5*bili) # 5.9251969 inches = 15.05cm which is used in MS word
            plt.subplots_adjust(bottom=0.15, right=0.95, left = 0.15,top=0.9)
            # plt.xlabel(x_lable,fontsize=daxiao_label*2) 
            # plt.ylabel(y_lable,fontsize=daxiao_label*2)        
            plt.yticks(fontproperties = 'Times New Roman', size = daxiao_label)
            plt.xticks(fontproperties = 'Times New Roman', size = daxiao_label) 
            # plt.title('Total pressure loss coefficient',fontproperties='Times New Roman',fontsize=daxiao_title)
            plt.title(title,fontproperties='Times New Roman',fontsize=daxiao_title*2)
            # marker = '.'
            plt.plot(yy[:,0],yy[:,0],marker='.',markersize = 5,ls='None',color = 'red',label = 'Real') 
            plt.plot(yy[:,0],yy[:,1],marker='2',markersize = 5,markeredgewidth=1,ls='None',color = 'green',label = 'Predict')
            plt.legend(prop={"family" : "Times New Roman" ,'size' : str(daxiao_label)})
            # plt.show() # if show, then savefig would fall. shabi logic
            wenjianming_omega = self.location + '/'+name+shijian+'.png'
            # self.png2tiff(fig,wenjianming_omega)
            plt.savefig(wenjianming_omega, dpi=1200)
            plt.close(i)
        # name = [r'\dot{m}_{l}',r'\dot{m}_{u}',r'\eta_{i}',r'\pi_{i}'] 
        name = [r'\dot{m}_{l}',r'\dot{m}_{u}',r'\eta_{i}',r'\pi_{i}',r'\dot{m}_{w}',r'\eta_{w}',r'\pi_{w}'] 
        if len(name) < len(yy_list):
            raise Exception('MXairfoil: invalid data in plot_surrogate_3D')
        for i in range(len(yy_list)):
            huatu_surrogate(i,yy_list[i],r'$ '+name[i]+r'$',r'$ '+name[i]+r'_{real}$',r'$ '+name[i]+r'_{predict}$',name[i])

    # def visual_2D_mul(self,N,**kargs):
    #     # this is to plot more than one lines in one visual_2D fig.
    #     print('MXairfoil: Unify all the huatu function!')
    #     shijian = time.strftime("%Y-%m-%d", time.localtime())
    #     x_name = parameters['chi_in']
    #     y_name = parameters['chi_out']
    #     xianxing = ['solid','dotted','dashed','dashdot']
    #     yanse = ['r','k','b','g']
    #     biaozhi = ['o','s','D','^']

    #     agent0_location = self.location
    #     location = self.location

    #     wenjianing_X1 = location + '/visual2DX1.pkl'
    #     wenjianing_X2 = location + '/visual2DX2.pkl'
    #     wenjianing_Y1 = location + '/visual2DY1.pkl'
    #     wenjianing_Y2 = location + '/visual2DY2.pkl'
    #     wenjianing_Y3 = location + '/visual2DY3.pkl'

    #     # these data comes from Surrogate_01de.py there are visual_2D.
    #     X1 = pickle.load(open(wenjianing_X1,'rb'))
    #     X2 = pickle.load(open(wenjianing_X2,'rb'))
    #     # Y1 = pickle.load(open(wenjianing_Y1,'rb'))
    #     # Y2 = pickle.load(open(wenjianing_Y2,'rb'))
    #     # biaoti = r'$\omega$'
    #     # biaoti = r'$Rise$'
    #     # choose to draw in omega back ground, or rise back ground 
    #     if 'flag_background' in kargs:
    #         flag_background = kargs['flag_background']
    #     else:
    #         flag_background  = 0
    #     if flag_background == 0 :
    #         biaoti = r'$\omega$'
    #         qianzhui = '/visual2Domega'
    #         Y1 = pickle.load(open(wenjianing_Y1,'rb'))
    #     elif flag_background ==1 :
    #         biaoti = r'$\pi$'
    #         qianzhui = '/visual2Drise'
    #         Y1 = pickle.load(open(wenjianing_Y2,'rb'))
    #     elif flag_background ==2:
    #         biaoti = r'$\Delta\beta$'
    #         qianzhui = '/visual2Dturn'
    #         Y1 = pickle.load(open(wenjianing_Y3,'rb'))
    #     else :
    #         print('MXairfoil: wrong in huatu.visual_2D')
    #         # this would never happen logically. no need in fact 
    #         return 
        
    #     tu_name = qianzhui+'duibi'+shijian+'.png'
    #     lujing = [] 
    #     label = []
    #     for i in range(N):
    #         wenjianming_lujing = agent0_location + '/lujing' + str(i) + '.pkl'
    #         lujing_i = pickle.load(open(wenjianming_lujing,'rb'))
    #         lujing.append(lujing_i)
    #         label_i = 'line ' + str(i)
    #         label.append(label_i)
        
    #     if 'label' in kargs:
    #         label = kargs['label']

    #     # then plot, omega 
    #     norm = plt.cm.colors.Normalize(vmax=Y1.max(), vmin=Y1.min())
    #     fig, ax = plt.subplots()
    #     cset1 = ax.contourf(X1, X2, Y1, 60,norm=norm,alpha=0.7,cmap=plt.cm.rainbow)
    #     ax.set_xlim(0, 1)
    #     ax.set_ylim(0, 1)
    #     x_label = np.arange(0,1.1,0.1)
    #     ax.set_xticks(x_label)
    #     ax.set_yticks(x_label)
    #     ax.set_xlabel(parameters.get_equation(x_name),fontsize=20)
    #     ax.set_ylabel(parameters.get_equation(y_name),fontsize=20)
    #     ax.set_title(biaoti,fontsize=20)
    #     cb = plt.colorbar(cset1)
    #     plt.yticks(fontproperties = 'Times New Roman', size = 10)
    #     plt.xticks(fontproperties = 'Times New Roman', size = 10) 
    #     for l in cb.ax.yaxis.get_ticklabels():
    #         l.set_family('Times New Roman') 

    #     # then plot the lujing, show how the state get into optimal.
    #     for i in range(N):
    #         tu_lujing = ax.plot(lujing[i][:,x_name.value], lujing[i][:,y_name.value], color=yanse[i%4], marker=biaozhi[i%4], label=label[i],linestyle=xianxing[i%4],linewidth=1, markersize=2)

    #     plt.legend(prop={"family" : "Times New Roman" ,'size' : '10'})
            

    #     # then save and show.
    #     # plt.show()
    #     plt.savefig(self.location+tu_name,dpi=1200)
    #     # plt.savefig(self.location+'/visual2Drise'+shijian+'.png',dpi=300)
    #     # plt.show()
    #     plt.close()

    # def visual_2D_mul2(self,**kargs):
    #     # this is to plot more than one lines in one visual_2D fig.
    #     # unlike visual_2D, this is to using the data in different folders
    #     print('MXairfoil: Unify all the huatu function!')

    #     shijian = time.strftime("%Y-%m-%d", time.localtime())
    #     x_name = parameters['chi_in']
    #     y_name = parameters['chi_out']
    #     xianxing = ['solid','dotted','dashed','dashdot']
    #     yanse = ['r','k','b','g']
    #     biaozhi = ['o','s','D','^']
    #     zihao = 12 

    #     agent0_location = self.location
    #     location = self.location
    #     data_location = kargs['data_location']
    #     data_id = kargs['data_id'] 
    #     # data_id = np.array([1,1])

    #     wenjianing_X1 = location + '/visual2DX1.pkl'
    #     wenjianing_X2 = location + '/visual2DX2.pkl'
    #     wenjianing_Y1 = location + '/visual2DY1.pkl'
    #     wenjianing_Y2 = location + '/visual2DY2.pkl'
    #     wenjianing_Y3 = location + '/visual2DY3.pkl'

    #     # these data comes from Surrogate_01de.py there are visual_2D.
    #     X1 = pickle.load(open(wenjianing_X1,'rb'))
    #     X2 = pickle.load(open(wenjianing_X2,'rb'))
    #     # Y1 = pickle.load(open(wenjianing_Y1,'rb'))
    #     # Y2 = pickle.load(open(wenjianing_Y2,'rb'))
    #     # biaoti = r'$\omega$'
    #     # biaoti = r'$Rise$'
    #     # choose to draw in omega back ground, or rise back ground 
        
    #     if 'flag_background' in kargs:
    #         flag_background = kargs['flag_background']
    #     else:
    #         flag_background  = 0
    #     if flag_background == 0 :
    #         biaoti = r'$\omega$'
    #         qianzhui = '/visual2Domega'
    #         Y1 = pickle.load(open(wenjianing_Y1,'rb'))
    #         contour_levels = [0.0550,0.0555,0.0558,0.0560,0.0567]
    #         contour_fmt="%.4f"
    #     elif flag_background ==1 :
    #         biaoti = r'$(\pi-\pi_{0})\times10^{4}$'
    #         qianzhui = '/visual2Drise'
    #         xiuzheng = -1.051351
    #         xiuzheng2 = 10000
    #         Y1 = (pickle.load(open(wenjianing_Y2,'rb')) + xiuzheng)*xiuzheng2
    #         contour_levels = [(1.0508+xiuzheng)*xiuzheng2,(1.0512+xiuzheng)*xiuzheng2,(1.051351+xiuzheng)*xiuzheng2,(1.051463+xiuzheng)*xiuzheng2,(1.05152+xiuzheng)*xiuzheng2]
    #         # contour_fmt='$%.3f$×$10^{4}$'
    #         contour_fmt='$%.3f$'
    #     elif flag_background ==2:
    #         biaoti = r'$\Delta\beta$'
    #         qianzhui = '/visual2Dturn'
    #         Y1 = pickle.load(open(wenjianing_Y3,'rb'))
    #         contour_levels = [32,34,35.80,38,40]
    #         contour_fmt="$%.2f$"
    #         # contour_fmt2 = {
    #         # 'family' : 'Times New Roman',
    #         # 'color' : 'darked',
    #         # 'weight' : 'normal',
    #         # 'size' : 8,
    #         # }
    #     elif flag_background == 3:
    #         # this is for DemoFunction huatu.
    #         biaoti = r'$Demo Function$'
    #         qianzhui = '/visual2DDemoFunction'
    #         Y1 = pickle.load(open(wenjianing_Y1,'rb'))
    #     else :
    #         print('MXairfoil: wrong in huatu.visual_2D')
    #         # this would never happen logically. no need in fact 
    #         return 
        
    #     tu_name = qianzhui+'duibi'+shijian+'.png'
    #     lujing = [] 
    #     label = []
    #     for i in range(len(data_location)):
    #         lujing_i,lujing_new,performace = self.get_lujing(data_id[i],location = data_location[i])
    #         lujing.append(lujing_i)
    #         label_i = 'line ' + str(i)
    #         label.append(label_i)

    #     if 'label' in kargs:
    #         label = kargs['label']

    #     # then plot, omega 
    #     norm = plt.cm.colors.Normalize(vmax=Y1.max(), vmin=Y1.min())
    #     fig, ax = plt.subplots()

    #     self.set_chicun(fig)
    #     plt.subplots_adjust(bottom=0.15, right=0.95, left = 0.15,top=0.92)
    #     # this is for CDA 
    #     # 366.828,shangxia direction, 0.1 = 366.828 pixs

    #     cset1 = ax.contourf(X1, X2, Y1, 60,norm=norm,alpha=0.7,cmap=plt.cm.rainbow)


    #     if kargs['isoheight']:
    #         # then draw a isoheight
    #         cmap_line = (mpl.colors.ListedColormap(['red', 'black','cyan'])) # this is to define a color bar
    #         # cline1 = ax.contour(X1, X2, Y1*0.01, 10,cmap = cmap_line)
    #         cline1 = ax.contour(X1, X2, Y1, contour_levels, colors='grey',linewidths=0.5) # this is to draw the isoheight. k, grey, sliver, slategray
    #         manual_locations = [(0.1, 0.1),(0.6, 0.3),(0.7, 0.3),(0.8, 0.6),(0.9, 0.9)] # this is lable location.
    #         ax.clabel(cline1, inline=True, fontsize=zihao-6,fmt=contour_fmt,manual=manual_locations,colors='k',fontproperties = 'Times New Roman') # this is to add labels for contour lines.
    #         # ax.clabel(cline1, inline=True,fmt=contour_fmt, fontsize=10,colors='k',fontproperties = 'Times New Roman')

    #     ax.set_xlim(0, 1)
    #     ax.set_ylim(0, 1)
    #     x_label = np.arange(0,1.1,0.1)
    #     ax.set_xticks(x_label)
    #     ax.set_yticks(x_label)
    #     # ax.tick_params(axis='y', labelcolor='k',labelsize=zihao-2)
    #     # ax.tick_params(axis='x', labelcolor='k',labelsize=zihao-2)
    #     ax.set_xlabel(parameters.get_equation(x_name,normal=True),fontsize=zihao)
    #     ax.set_ylabel(parameters.get_equation(y_name,normal=True),fontsize=zihao)
    #     ax.set_title(biaoti,fontsize=zihao)
    #     plt.yticks(fontproperties = 'Times New Roman', size = zihao-2)
    #     plt.xticks(fontproperties = 'Times New Roman', size = zihao-2) 
        
    #     # handle the color bar
    #     # contour_fmt="$%.2f$"
    #     cb = plt.colorbar(cset1)
    #     for l in cb.ax.yaxis.get_ticklabels():
    #         l.set_family('Times New Roman') 
    #     # font = {
    #     #     'family' : 'serif',
    #     #     'color' : 'darked',
    #     #     'weight' : 'normal',
    #     #     'size' : 16,
    #     # }
    #     # cb.set_lable('colorbar',fontdic = font) #Exception has occurred: AttributeError    
    #     cb.ax.tick_params(labelsize=10) 

    #     # then plot the lujing, show how the state get into optimal.
    #     for i in range(len(data_id)):
    #         tu_lujing = ax.plot(lujing[i][:,x_name.value], lujing[i][:,y_name.value], color=yanse[i%4], marker=biaozhi[i%4], label=label[i],linestyle=xianxing[i%4],linewidth=1, markersize=2)

    #     plt.legend(prop={"family" : "Times New Roman" ,'size' : str(zihao-4)})
        


    #     # then save and show.
    #     # plt.show()
    #     # self.png2tiff(fig,self.location+tu_name)
    #     plt.savefig(self.location+tu_name,dpi=1200)
    #     # plt.savefig(self.location+'/visual2Drise'+shijian+'.png',dpi=300)
    #     # plt.show()
    #     plt.close()

    # def visual_2D_simplified(self,lujing_list,data_id = [1,2,3],x_index=0,y_index=1,meiju = parameters,tu_name = 'visual_2D_simplified' ,location=None,label=[],**kargs):
    #     # this is a simplified version, just draw some lines.
    #     shijian = time.strftime("%Y-%m-%d", time.localtime())
    #     if location == None:
    #         location = self.location
    #     x_enum = meiju(x_index)
    #     x_name = meiju.get_equation(x_enum)
    #     y_enum = meiju(y_index)
    #     y_name = meiju.get_equation(y_enum)
    #     xianxing = ['solid','dotted','dashed','dashdot']
    #     yanse = ['r','k','b','g']
    #     biaozhi = ['o','s','D','^']
    #     zihao = 12


    #     # then plot.
    #     fig, ax = plt.subplots()
        
    #     self.set_chicun(fig,width=7.4,height=7.4,**kargs)
        
    #     ax.set_xlim(0, 1)
    #     ax.set_ylim(0, 1)
    #     x_label = np.arange(0,1.1,0.1)
    #     ax.set_xticks(x_label)
    #     ax.set_yticks(x_label)
    #     ax.set_xlabel(x_name,fontsize=zihao)
    #     ax.set_ylabel(y_name,fontsize=zihao)
    #     # ax.set_title(biaoti,fontsize=zihao)
    #     plt.yticks(fontproperties = 'Times New Roman', size = zihao-2)
    #     plt.xticks(fontproperties = 'Times New Roman', size = zihao-2)

    #     for i in range(len(data_id)):
    #         tu_lujing = ax.plot(lujing_list[i][:,x_enum.value], lujing_list[i][:,y_enum.value], color=yanse[i%4], marker=biaozhi[i%4], label=label[i],linestyle=xianxing[i%4],linewidth=0.5, markersize=1)
    #     plt.legend(prop={"family" : "Times New Roman" ,'size' : str(zihao-2)})
        
    #     plt.savefig(location+'/'+tu_name+'.png',dpi=1200)
    #     plt.close()

    # def visual_3D_mul(self,N,**kargs):
    #     print('MXairfoil: plotting 3D results')
    #     shijian = time.strftime("%Y-%m-%d", time.localtime())
    #     x_name = parameters['chi_in']
    #     y_name = parameters['chi_out']
    #     z_name = parameters['umxthk']

    #     xianxing = ['solid','dotted','dashed','dashdot']
    #     yanse = ['r','k','b','g']
    #     biaozhi = ['o','s','D','^']

    #     agent0_location = self.location
    #     qianzhui = '/visual3Domega'
    #     biaoti = 'Comparison of Different Policy'

    #     tu_name = qianzhui+'duibi'+shijian+'.png'
    #     lujing = [] # it is a list rather than array now. 
    #     label = []
        
    #     for i in range(N):    
    #         if 'data_locations' in kargs:
    #             wenjianming_lujing = kargs['data_locations'][i]
    #         elif 'data_ids' in kargs:
    #             wenjianming_lujing = agent0_location + '/lujing' + str(kargs['data_ids'][i]) + '.pkl'
    #         else:
    #             wenjianming_lujing = agent0_location + '/lujing' + str(i) + '.pkl'
    #         lujing_i = pickle.load(open(wenjianming_lujing,'rb'))
    #         if i == 2:
    #             lujing_i = lujing_i[1:-1] # this is zuobi
    #         lujing.append(lujing_i)
    #         label_i = 'line ' + str(i)
    #         label.append(label_i)
        
    #     if 'label' in kargs:
    #         label = kargs['label']

    #     from mpl_toolkits.mplot3d import Axes3D
    #     fig= plt.figure()
    #     # ax = plt.axes(projection='3d')
    #     ax = Axes3D(fig)
    #     ax.grid(False)  
    #     self.set_chicun(fig)
    #     # plt.subplots_adjust(bottom=0.15, right=0.5, left = 0.15,top=0.9)
    #     ax.set_position([0,0.05,0.9,0.9])
    #     fontsize_zhou=14
    #     fontsize_title = 10
    #     fontsize_tip = 10
    #     fontsize_label = 8
    #     fontsize_tick = 10 

    #     # then plot the lujing, show how the state get into optimal.
    #     # get segments in this loop.
    #     def visual_3D_single(lujing):
    #         # tu_lujing = ax.plot(lujing[i][:,x_name.value], lujing[i][:,y_name.value], color=yanse[i%4], marker='o', label=label[i],linestyle=xianxing[i%4],linewidth=1, markersize=2)
    #         lujing = lujing[1:]
    #         biaozhu = lujing[-1]
    #         x_lujing = lujing[:,x_name.value] # parameter.py is convenient to use.
    #         y_lujing = lujing[:,y_name.value]
    #         z_lujing = lujing[:,z_name.value]
    #         r_lujing = lujing[:,7-1]
    #         omega_lujing = lujing[:,7-3]
    #         omega_huatu = -500*omega_lujing + 28.2
    #         norm = plt.cm.colors.Normalize(vmax=omega_huatu.max, vmin=omega_huatu.min)
    #         points = np.array([x_lujing, y_lujing,z_lujing]).T.reshape(-1, 1, 3)
    #         segments = np.concatenate([points[:-1], points[1:]], axis=1)
    #         lc = Line3DCollection(segments,cmap=plt.cm.rainbow) 
    #         lc.set_array(omega_huatu)
    #         lc.set_linewidth(1.5)

    #         line = ax.add_collection3d(lc)

    #         # then try some projection.
    #         ax.plot3D(x_lujing,y_lujing,zdir='z',linewidth =1,color=(0.3, 0.3, 0.3))
    #         ax.plot3D(x_lujing,z_lujing,1,zdir='y',linewidth =1,color=(0.3, 0.3, 0.3))
    #         ax.plot3D(y_lujing,z_lujing,zdir='x',linewidth =1,color=(0.3, 0.3, 0.3))
    #         self.chuixian(ax,x_lujing[0],y_lujing[0],z_lujing[0])
    #         self.chuixian(ax,x_lujing[-1],y_lujing[-1],z_lujing[-1])
    #         ax.text(biaozhu[0], biaozhu[1], biaozhu[3]+0.01, r'$P_0$', color='k',fontsize=fontsize_tip,fontproperties='Times New Roman')
        
    #     def visual_3D_single2(lujing):
    #         tu_lujing = ax.plot(lujing[:,x_name.value], lujing[:,y_name.value], lujing[:,z_name.value],color=yanse[i%4], marker=biaozhi[i%4], label=label[i],linestyle=xianxing[i%4],linewidth=1, markersize=1)
    #         ax.plot3D(lujing[:,x_name.value],lujing[:,y_name.value],zdir='z',linewidth =0.5,color=(0.5,0.5,0.5),linestyle=xianxing[i%4])
    #         ax.plot3D(lujing[:,x_name.value],lujing[:,z_name.value],1,zdir='y',linewidth =0.5,color=(0.5,0.5,0.5),linestyle=xianxing[i%4])
    #         ax.plot3D(lujing[:,y_name.value],lujing[:,z_name.value],zdir='x',linewidth =0.5,color=(0.5,0.5,0.5),linestyle=xianxing[i%4])
    #         self.chuixian(ax,lujing[0,x_name.value],lujing[0,y_name.value],lujing[0,z_name.value])
    #         self.chuixian(ax,lujing[-1,x_name.value],lujing[-1,y_name.value],lujing[-1,z_name.value])
    #     def visual_3D_single3(lujing):
    #         # this is for 4D GA 
    #         lujing = lujing[0:40,:]
    #         tu_lujing = ax.plot(lujing[:,x_name.value], lujing[:,y_name.value], lujing[:,z_name.value],color=yanse[i%4], marker=biaozhi[i%4], label=label[i],linestyle=xianxing[i%4],linewidth=1, markersize=1)
    #         ax.plot3D(lujing[:,x_name.value],lujing[:,y_name.value],zdir='z',linewidth =0.5,color=(0.5,0.5,0.5),linestyle=xianxing[i%4])
    #         ax.plot3D(lujing[:,x_name.value],lujing[:,z_name.value],1,zdir='y',linewidth =0.5,color=(0.5,0.5,0.5),linestyle=xianxing[i%4])
    #         ax.plot3D(lujing[:,y_name.value],lujing[:,z_name.value],zdir='x',linewidth =0.5,color=(0.5,0.5,0.5),linestyle=xianxing[i%4])
    #         if i == 0 :
    #             self.chuixian(ax,lujing[0,x_name.value],lujing[0,y_name.value],lujing[0,z_name.value])
    #         self.chuixian(ax,lujing[-1,x_name.value],lujing[-1,y_name.value],lujing[-1,z_name.value])

    #     for i in range(N):
    #         # visual_3D_single2(lujing[i]) # for 4D 
    #         visual_3D_single3(lujing[i]) # for 4D GA
        
    #     ax.text(lujing[0][0,x_name.value], lujing[0][0,x_name.value], lujing[0][0,x_name.value]-0.1, 'Original Point', color='k',fontsize=fontsize_tip,fontproperties='Times New Roman')
        
    #     ax.legend(prop={"family" : "Times New Roman" ,'size' : str(fontsize_label)},loc='upper right', bbox_to_anchor=(0.9, 0.9))
    #     ax.set_xlim(0, 1)
    #     ax.set_ylim(0, 1)
    #     ax.set_zlim(0, 1)

    #     x_label = np.arange(0,1.1,0.2)
    #     z_label = np.arange(0,1.1,0.2)
    #     ax.set_xticks(x_label)
    #     ax.set_yticks(x_label)
    #     ax.set_zticks(z_label)

    #     ax.tick_params(axis='both',direction = 'in',pad=-0.5,reset=False,labelsize=fontsize_tick)
        
    #     ax.text(0.5, -0.5,0, parameters.get_equation(x_name,normal=True), color='k',fontsize=fontsize_zhou,fontproperties='Times New Roman')
    #     ax.text(1.3, 0.3,0, parameters.get_equation(y_name,normal=True), color='k',fontsize=fontsize_zhou,fontproperties='Times New Roman')
    #     ax.text(1.2, 1,0.9, parameters.get_equation(z_name,normal=True), color='k',fontsize=fontsize_zhou,fontproperties='Times New Roman')
    #     # ax.set_xlabel(parameters.get_equation(x_name),fontsize=fontsize_zhou,fontproperties='Times New Roman')
    #     # ax.set_ylabel(parameters.get_equation(y_name),fontsize=fontsize_zhou,fontproperties='Times New Roman')
    #     # ax.set_zlabel(parameters.get_equation(z_name),fontsize=fontsize_zhou,fontproperties='Times New Roman')
    #     ax.set_title(biaoti,fontsize=fontsize_title,fontproperties='Times New Roman')

    #     # axes3d = Axes3D(fig,auto_add_to_figurebool=True)
    #     # axes3d = ax
    #     # labels = axes3d.get_xticklabels() + axes3d.get_yticklabels() + axes3d.get_zticklabels()
    #     # for label in labels:
    #     #     label.set_fontsize(fontsize_label) 
    #     #     label.set_fontweight('normal')
    #     # plt.zticks(fontproperties = 'Times New Roman', size = 5)
    #     for l in ax.xaxis.get_ticklabels():
    #         l.set_family('Times New Roman') 
    #     for l in ax.yaxis.get_ticklabels():
    #         l.set_family('Times New Roman') 
    #     for l in ax.zaxis.get_ticklabels():
    #         l.set_family('Times New Roman') 

    #     # ax.xaxis.set_label_coords(0,0,transform = (0.1,0.5))
    #     # plt.subplots_adjust(bottom=0.1, right=0.5, left = 0.01,top=0.95)
    #     # self.png2tiff(fig,self.location+tu_name)
    #     plt.savefig(self.location+tu_name,dpi=1200)
    #     # plt.show()
    #     plt.close()

    def get_lujing(self,id,**kargs):
        if 'location' in kargs:
            agent0_location = kargs['location']
        else:
            agent0_location = self.location
        # this is to get lujing from new architecture, make it compatiable.
        wenjianming_performance = agent0_location + '/performance' + str(id) + '.pkl'
        wenjianming_lujing = agent0_location + '/lujing' + str(id) + '.pkl'

        lujing_new = pickle.load(open(wenjianming_lujing,'rb'))
        try :
            performance = pickle.load(open(wenjianming_performance,'rb'))
        except:
            print('MXairfoil: attension, there are no performance.pkl here!')
            return lujing_new,0,0
        lujing = lujing_new*1 # how old are you? pass the value/pass the reference.

        if len(lujing_new[0])<7:
            # dimension changed.
            lujing = np.zeros((len(lujing_new),7))
            # lujing[:,0] = lujing_new[:,0]
            # lujing[:,1] = lujing_new[:,1]
            lujing[:,0:self.real_dim] = lujing_new[:,0:self.real_dim]
            try:
                lujing[:,-1] = lujing_new[:,self.real_dim] 
            except:
                lujing[:,-1] = performance[:,-1] # reward

        lujing[:,4] = performance[:,0] # assemble the omega into lujing
        lujing[:,5] = performance[:,1] # assemble the rise into lujing
        # now lujing is compatiable with old version.
        # print('Mxairfoil: jieguo of the agent is: '+str(performance[-1]) +'\nit should be'+ str(self.transfer.normal_to_real_constraints(lujing_new[-1][4:6])) + '\nthe point is '+str(lujing_new[-1][0:4]))
        print('Mxairfoil: jieguo of the agent is: '+str(performance[-1]) + '\nthe point is '+str(lujing_new[-1][0:4]))

        self.end_point = np.append(self.end_point,lujing_new[-1][0:self.real_dim].reshape(1,self.real_dim),axis=0)

        return lujing, lujing_new, performance

    # def plot_performance(self,**kargs):
    #     # this is to compare different paths and plot omega
    #     # first, load the data. 
    #     # get configuration from kargs
    #     shijian = time.strftime("%Y-%m-%d", time.localtime())
    #     x_name = parameters['chi_in']
    #     y_name = parameters['chi_out']
    #     xianxing = ['solid','dotted','dashed','dashdot']
    #     yanse = ['r','k','b','g']
    #     biaozhi = ['.','1','+','d']
    #     agent0_location = self.location
    #     location = self.location
    #     data_location = kargs['data_location']
    #     data_id = kargs['data_id'] 
    #     biaoti = r'$\omega$'
    #     biaoti = r'$(\omega-\omega_{min})\times10^{4}$'
    #     qianzhui = '/performance'

    #     # load data from existing file.
    #     tu_name = qianzhui+'duibi'+shijian+'.png'
    #     lujing = [] 
    #     label = []
    #     for i in range(len(data_location)):
    #         lujing_i,lujing_new,performace = self.get_lujing(data_id[i],location = data_location[i])
    #         lujing.append(lujing_i[1:])
    #         label_i = 'line ' + str(i)
    #         label.append(label_i)

    #     if 'label' in kargs:
    #         label = kargs['label']



    #     # then plot, omega 
    #     fig, ax = plt.subplots()
    #     self.set_chicun(fig)
    #     plt.subplots_adjust(bottom=0.15, right=0.95, left = 0.20,top=0.9)

    #     # then plot the lujing, show how the state get into optimal.
    #     y_max = 0
    #     y_min = 114514
    #     for i in range(len(data_id)):
    #         # hengzhou = np.arange(0,len(lujing[i]),1)
    #         # tu_lujing = ax.plot(hengzhou, lujing[i][:,4], color=yanse[i%4], marker=biaozhi[i%4], label=label[i],linestyle=xianxing[i%4],linewidth=1, markersize=4)

    #         y_min_i = lujing[i][:,4].min()
    #         y_max_i = lujing[i][:,4].max()
    #         y_max = np.max([y_max_i,y_max])
    #         y_min = np.min([y_min_i,y_min])
    #     for i in range(len(data_id)):
    #         # this is for y_label limit.
    #         hengzhou = np.arange(0,len(lujing[i]),1)
    #         y = (lujing[i][:,4] - y_min) * 10000 
    #         tu_lujing = ax.plot(hengzhou, y, color=yanse[i%4], marker=biaozhi[i%4], label=label[i],linestyle=xianxing[i%4],linewidth=1, markersize=4)

    #     ax.set_xlim(0, len(lujing[i]))
    #     # ax.set_ylim(y_min, y_max)
    #     # ax.set_ylim(y.min(), y.max())
    #     ax.set_ylim(0, y.max())
    #     x_label = np.arange(0,len(lujing[i])+1,round((len(lujing[i]))/10))
    #     y_label = np.arange(y_min,y_max+0.1*(y_max-y_min),(y_max-y_min)/10)
    #     y_label = np.around(y_label,4)
    #     ax.set_xticks(x_label)
    #     # ax.set_yticks(y_label)
    #     ax.set_xlabel('Steps',fontsize=10,fontproperties='Times New Roman')
    #     ax.set_ylabel(biaoti,fontsize=12,fontproperties='Times New Roman')
    #     ax.set_title('Performance',fontsize=12,fontproperties='Times New Roman')
    #     plt.legend(prop={"family" : "Times New Roman" ,'size' : '10'})
    #     plt.yticks(fontproperties = 'Times New Roman', size = 10)
    #     plt.xticks(fontproperties = 'Times New Roman', size = 10) 
        
    #     # self.png2tiff(fig,self.location+tu_name)
    #     # self.savesvg(fig,self.location+tu_name)
    #     plt.savefig(self.location+tu_name,dpi=1200)
    #     plt.close()

    def load_data_universal(self,x_names,y_names):
        # get e load data function for common use.
        self.x = [] 
        self.y = []
        for i in range(len(x_names)):
            wenjianming_x = x_names[i]
            wenjianming_y = y_names[i]
            x_i = pickle.load(open(wenjianming_x,'rb'))
            y_i = pickle.load(open(wenjianming_y,'rb'))
            self.x.append(np.array(x_i))
            self.y.append(np.array(y_i))
        print('MXairfoil: load the data')

    # def compare_performance(self,**kargs):
    #     # this is to get raw_state and end_point in a conviniet way, and compare
    #     if 'location' in kargs:
    #         weizhi = self.location+'/'+kargs['location']
    #     else:
    #         weizhi = self.location
    #     if 'kind' in kargs:
    #         kind = kargs['kind']
    #     else: 
    #         kind = 0 

    #     for i in range(10):
    #         tu.get_lujing(i,location = weizhi)

    #     end_point = np.mean(tu.end_point,axis=0)

    #     # then get raw_state for comparison.
        
    #     wenjianming = self.location + '/raw_state_save'+str(kind)+'.pkl'
    #     try:
    #         raw_state_save = pickle.load(open(wenjianming,'rb'))
    #     except:
    #         print('MXairfoil: no prepared raw_state_save there') 
    #         return 'wan nima, G!'
    #     lilunzhi = raw_state_save[-1]
    #     real_lillunzhi = self.transfer.normal_to_real(lilunzhi)
    #     lilunzhi = self.transfer.normal_to_surrogate(lilunzhi)
    #     jvli = np.sum( (end_point - lilunzhi[0:self.real_dim])**2) **(0.5) 
    #     rizhi ='\nMXairfoil: compared \nend point is: ' + str(end_point) + '\nraw_state is (in surrogate): ' + str(lilunzhi) +'\nraw_state is (in real): ' + str(real_lillunzhi)+ '\njvli is: '+str(jvli)
    #     print(rizhi)
    #     return end_point
    
    def png2tiff(self,fig,name):
        from PIL import Image
        import io
        name = name[0:-4]
        png1 = io.BytesIO()
        fig.savefig(png1, format="png",dpi=1200)
        png2 = Image.open(png1)
        png2.save(name+'.tiff')
        png1.close()

    def set_chicun(self,fig,**kargs):
        bili = 0.397 # transfer from cm into inches.

        if 'width' in kargs:
            fig.set_figwidth(kargs['width']*bili)
        else:
            
            fig.set_figwidth(7.4*bili)

        if 'height' in kargs :
            fig.set_figheight(kargs['height']*bili)
        else :
            fig.set_figheight(7.0*bili)
        
        if 'adjust' in kargs:
            shuzi = kargs['adjust']
            plt.subplots_adjust(bottom=shuzi[0], right=shuzi[1], left = shuzi[2],top=shuzi[3])
        else:
            plt.subplots_adjust(bottom=0.15, right=0.95, left = 0.15,top=0.9)

    def savesvg(self,fig,name):
        name = name[0:-4]
        name = name+'.svg'
        plt.savefig(name, format="svg",dpi=1200)

    # def huatu_contour(self,**kargs):
    #     # this is to draw the contours for calculated lujing.
        

    #     script_folder = 'C:/Users/y/Desktop/EnglishMulu/testCDA1'
    #     matlab_location = 'C:/Users/y/Desktop/EnglishMulu/MXairfoilCDA'
    #     target_folder = 'C:/Users/y/Desktop/EnglishMulu/figure-post'

    #     from call_components import call_components
    #     from transfer import transfer
    #     import shutil

    #     # calculate are needed.
    #     data_location = kargs['data_location']
    #     data_id = kargs['data_id']
    #     lujing, lujing_new, performance = self.get_lujing(data_id,location=data_location) 
    #     diaoyong = call_components(script_folder,matlab_location,case='CDA1') 
    #     # diaoyong = 'debug'  
    #     real_obs_space_h = np.array([0.35,-0.22,0.55,8])
    #     real_obs_space_l = np.array([0.25,-0.38,0.35,5])
    #     bianhuan = transfer(tishi = 0 , dim = 4,real_obs_space_h = real_obs_space_h,real_obs_space_l=real_obs_space_l)
    #     N =10        
    #     for i in range(N+1):
    #         index =int(i*(100/N))
    #         if index == 100:
    #             index = 99 # a patch that is very inurbanity/graceless/
    #         X_normal =  lujing[index][0:4]
    #         X = bianhuan.surrogate_to_real(X_normal) 
    #         # so called normal is [-1,1], while so called surrogate is [0,1]
    #         diaoyong.set_value(X[0],'chi_in')
    #         diaoyong.set_value(X[1],'chi_out')
    #         diaoyong.set_value(X[2],'mxthk')
    #         diaoyong.set_value(X[3],'umxthk')
    #         diaoyong.set_step_huatu(index)
    #         #start the calculation
    #         omega = 0
    #         rise = 0
    #         turn = 0
    #         diaoyong.call_matlab()
    #         diaoyong.call_IGG()
    #         diaoyong.call_Turbo()
    #         diaoyong.call_CFView_huatu()
    #         jieguo_data_folder = target_folder + '/' + str(i)
    #         shutil.copytree(diaoyong.result_folder,jieguo_data_folder)

    #     self.generate_gif(diaoyong.script_folder+'/output/contour-Ps',name='Ps_gif')
    #     self.generate_gif(diaoyong.script_folder+'/output/contour-Pt',name='Pt_gif')
    #     self.generate_gif(diaoyong.script_folder+'/output/contour-V',name='V_gif')

    #     diaoyong.save_huatu(target_folder)

    #     print('MXairfoil: contour finished, remember modifying the name and write a shuoming.txt')
    #     print('----------------En Taro XXH!----------------')
    #     os.system("pause")

    # def generate_gif(self,location,**kargs):
    #     # transfer pictures in one folder to one gif and save.
    #     import imageio 
    #     image_list = [location +'/'+ img for img in os.listdir(location)]
    #     shishi = [] 
    #     for image_name in image_list:
    #         if image_name.endswith('.tif'):
    #             print('mxairfoil: read picture, '+image_name)
    #             shishi.append(imageio.imread(image_name))
        
    #     if 'name' in kargs:
    #         name = location + '/'+kargs['name']+'.gif'
    #     else:
    #         name = location + '/dynamic_tu.gif'

    #     imageio.mimsave(name,shishi,'GIF',duration=0.1)

    #     return

    def huatu2D_add_grey_line(self,data,loc=None,linewidth=1,**kargs):
        # add single line into huatu
        fig = self.fig
    
        if 'model' in kargs:
            if kargs['model'] == 'existing data':
                x = self.x[-1]
                y = self.y[-1]  
        else:
            if type(data) == list:
                x=(data[:][0])
                y=(data[:][1]) 
            elif type(data) == np.ndarrary :
                x=(data[:,0])
                y=(data[:,1])
            else:
                raise Exception('MXairfoil: invalid input in huatu2D_add_grey_line:'+type(data[0]))            
            # x = data[:,0]
            # y = data[:,1]     
        yanse = 'black'
        linestyle='solid'
        if 'zhonglei' in kargs:
            if kargs['zhonglei']=='ave_chosen':
                yanse = self.ave_r_color_chosen
            elif kargs['zhonglei'] == 'ave_normal':
                yanse = self.ave_r_color_normal
            elif kargs['zhonglei'] == 'opt_chosen':
                yanse = self.opt_r_color_chosen
                ax =self.ax2
            elif kargs['zhonglei'] == 'opt_normal':
                yanse = self.opt_r_color_normal
                ax =self.ax2
            elif kargs['zhonglei'] == 'mean_line':
                yanse = 'black'
                linestyle = self.xianxing[2]
            else:
                raise Exception('MXairfoil: invalid zhonglei, G!')
        if 'ax' in kargs:
            if kargs['ax'] == 'ax':
                ax =self.ax
            elif kargs['ax'] == 'ax2':
                ax = self.ax2
            else:
                raise Exception('MXairfoil: invalid ax')
        else:
            ax =self.ax
        # ax.plot(x_lujing, y_lujing, color='red', marker='o', linestyle='solid',linewidth=1, markersize=2)
        if 'label' in kargs:
            label = kargs['label']
        else:
            label = None 

        if 'flag_cut' in kargs:
            flag_cut = kargs['flag_cut']
        else:
            flag_cut = False
        
        if flag_cut:
            index = 0 
            for index in range(len(x)):
                if x[index]>self.x_max:
                    break
            x_cut = x[0:index+1]
            y_cut = y[0:index+1]
            if x_cut[-1]<self.x_max*0.5:
                x_cut=np.append(x_cut,self.x_max)
                y_cut=np.append(y_cut,y_cut[-1])
        else: 
            x_cut = x
            y_cut = y


        ax.plot(x_cut, y_cut,color=yanse,linewidth=linewidth,label=label,linestyle=linestyle)
        if loc == None:
            pass
        else:
            plt.legend(prop={"family" : "Times New Roman" ,'size' : str(self.zihao-2)},loc=loc)


    def get_one_grid(self,buchang):
        # make the ireegular buchang to be regular, for example 114.514 to 100;
        # baoli chabiao
        for i in range(-3,5,1):
            if (buchang>(10**i)) & (buchang<(10**i*1.5)):
                buchang = 10**i 
                break 
            elif (buchang>(10**i*1.5)) & (buchang<10**i*3.5):
                buchang = 10**i*2
                break
            elif (buchang>(10**i*3.5)) & (buchang<10**i*7.5):
                buchang = 10**i*5
                break
            elif (buchang>(10**i*7.5)) & (buchang<10**i*10):
                buchang = 10**i*10
                break
        
        if abs(buchang)<0.000001:
            buchang = 0.5 
        
        return buchang
    
    def huatu_for_history(self,location,index):
        # this is for demo180 first. Many gray lines.
        tu.set_location(location) 
        N_lines = len(index)
        location_end = location+'/agent0indedx' + str(index[-1])
        # location1 = location_end+'/Optimization-Episode relation'
        location2 = location_end+'/Reward-Episode relation'
        # self.set_location(location_end)
        self.load_data_mul(location2)
        self.huatu2D_mul2('episode','average reward','Converge History','100 step total reward',modle='all',single_ax=True)
        for i in range(N_lines):
            weizhi = location+'/agent0indedx' + str(index[i])
            location2 = weizhi+'/Reward-Episode relation'
            self.load_data_mul(location2)
            if i == (N_lines-1) : 
                zhonglei= 'ave_chosen'
            else:
                zhonglei= 'ave_normal'
            self.huatu2D_add_grey_line(0,model='existing data',zhonglei=zhonglei)

        self.save_all()

    def debug_Pjudge(self):
        # this is to debug Pjudge.
        panduan = Pjudge(dim=2)
        # id = 0 
        # lujing,lujing_new,performace = self.get_lujing(id)
        # zhi = panduan.calculate_policy_consistency(lujing)
        
        lujing_list = []
        for i in range(10):
            lujing,lujing_new,performace = self.get_lujing(i)
            lujing_list.append(lujing)

        zhi = panduan.calculate_jvli(lujing_list)

        return zhi 

    def load_data_folder(self,folder):
        wenjianming = folder + '/Converge History/converge_history.pkl' 
        wenjianming_opt = folder + '/Converge History/converge_history_opt.pkl' 
        index = 0 
        converge_history = []
        converge_history_opt = []
        for index in range(114514) : 
            location_target = folder + '/agent0indedx'+str(index) 
            wenjianming_x = location_target + '/Reward-Episode relation/x.pkl' 
            wenjianming_y = location_target + '/Reward-Episode relation/y.pkl' 
            wenjianming_x_opt = location_target + '/Optimization-Episode relation/x.pkl' 
            wenjianming_y_opt = location_target + '/Optimization-Episode relation/y.pkl'             
            if os.path.exists(wenjianming) and os.path.exists(wenjianming_opt):
                converge_history = pickle.load(open(wenjianming,'rb'))
                converge_history_opt = pickle.load(open(converge_history_opt,'rb'))
                print('MXairfoil: converge_history loaded:\n'+wenjianming + '\nconverge_history loaded: \n' + wenjianming_opt)
                break
            elif os.path.exists(wenjianming_x) and os.path.exists(wenjianming_x_opt) :
                converge_history_x = pickle.load(open(wenjianming_x,'rb'))
                converge_history_y = pickle.load(open(wenjianming_y,'rb'))
                converge_history_x = converge_history_x.astype(float)
                converge_history_y = converge_history_y.astype(float)
                converge_history_single = [converge_history_x,converge_history_y]
                converge_history.append([converge_history_single])
                print('MXairfoil: converge_history loaded sperately:\n'+location_target)

                converge_history_x_opt = pickle.load(open(wenjianming_x_opt,'rb'))
                converge_history_y_opt = pickle.load(open(wenjianming_y_opt,'rb'))
                converge_history_x_opt = converge_history_x_opt.astype(float)
                converge_history_y_opt = converge_history_y_opt.astype(float)
                converge_history_single_opt = [converge_history_x_opt,converge_history_y_opt]
                converge_history_opt.append([converge_history_single_opt])
                print('MXairfoil: converge_history_opt loaded sperately:\n'+location_target)                
            else:
                print('MXairfoil: no such file:\n'+location_target)
                break

        return converge_history, converge_history_opt

    def add_lines_for_history(self,folder):
        converge_history, converge_history_opt = self.load_data_folder(folder)
        # then draw the normal lines.
        for line_single in converge_history:
            self.huatu2D_add_grey_line(line_single[0],zhonglei='opt_normal',linewidth=0.5,flag_cut=True,ax = 'ax')
        for line_single in converge_history_opt:
            self.huatu2D_add_grey_line(line_single[0],zhonglei='ave_normal',linewidth=0.5,flag_cut=True,ax = 'ax2')

    def recycle_log(self):
        wenjianming = self.location + '\log_for_agent.txt'
        wenjian = open(wenjianming,'r')
        neirong = wenjian.read()
        wenjian.close()
        index = 0 
        performance_list = [0.2] 
        episode_list = [0] 
        while index >= 0 :
            index = neirong.find('after')
            index_performance_l = neirong.find('performance:',index)+1+len('performance:')
            index_performance_u = neirong.find('artificial',index_performance_l)-2
            performance_i = neirong[index_performance_l:index_performance_u]
            performance = self.recycle_array(performance_i)
            performance_list.append(performance[-1])

            geshu = neirong.count('episode: ',0,index)
            index_episode_l = 0 
            for i in range(geshu):
                index_episode_l = neirong.find('episode: ',index_episode_l)+ len('episode: ')
            # index_episode_l = neirong.find('episode: ')+ len('episode: ')
            index_episode_u = neirong.find('agent',index_episode_l)-1
            episode_i = neirong[index_episode_l :index_episode_u]
            episode = self.recycle_array(episode_i,dim=1)
            episode_list.append(episode)

            index_new = neirong.find('episode: ',index_episode_u)
            neirong_new = neirong[index_new:]
            neirong = neirong_new 
            index = neirong.find('after')
        performance_array = np.array(performance_list,dtype=float).reshape(len(performance_list),1)
        episode_array = np.array(episode_list,dtype=float).reshape(len(episode_list),1)
        shuru = np.append(episode_array,performance_array,axis=1)
        # self.set_location()
        self.input = shuru
        self.huatu2D('episode','Optimization reward','Optimization-Episode relation')
        self.save_all()
    
    def recycle_array(self,array_str,dim=7):
        if dim ==1 :
            array = int(array_str)
            return array_str
        array_str_split = array_str.split()
        array= np.zeros(dim)
        index_array = 0 

        for index in range(len(array_str_split)):
            shuzi = float(array_str_split[index]) 
            array[index] = shuzi
            # if shuzi!=0:
            #     array[index_array] = shuzi
            #     index_array = index_array + 1

        return array

            

class Pjudge():
    
    def __init__(self,**kargs) -> None:
        if 'dim' in kargs:
            self.dim = kargs['dim']
        else:
            self.dim = 18
        
        if 'location_data' in kargs:
            self.location_data = kargs['location_data']
        else:
            self.location_data = '.'

        if 'jvli_threshold' in kargs:
            self.jvli_threshold = kargs['jvli_threshold']
        else:
            self.jvli_threshold = 0.04
        
        if 'guanghua_threshold' in kargs:
            self.guanghua_threshold = kargs['guanghua_threshold']
        else:
            self.guanghua_threshold = 0.995

        pass

    def load_lujing(self,wenjianming_lujing):
        # this is the most simple load.
        lujing = pickle.load(open(wenjianming_lujing,'rb'))
        return lujing

    def calculate_policy_consistency(self,lujing,**kargs):
        # trying to define something.
        if 'performance' in kargs:
            performance = kargs['performance']
        else:
            performance = 0 

        N_window = 5 # which define the range for averaging.
        dianshu = len(lujing)
        if dianshu < N_window*2:
            return 0 # which means GG thing
        n_w = round((N_window-1)/2)
        steps = lujing[1:] - lujing[0:-1] # delta vector, or action.
        steps_window = lujing[N_window:] - lujing[0:-N_window]
        steps = steps[:,0:self.dim]
        steps_window = steps_window[:,0:self.dim]
        cosjiajiao = 0 
        for i in range(dianshu-N_window):
            cosjiajiao = cosjiajiao +  np.dot(steps[i+n_w],steps_window[i])/np.linalg.norm(steps[i+n_w])/np.linalg.norm(steps_window[i])
            
        panju =  cosjiajiao / (dianshu-N_window)
        return panju

    def calculate_guanghua(self,lujing_list):
        # this is to calculate 10 guanhua and pingjun yixia.
        N_lujing = len(lujing_list)

        panju = 0 
        for lujing in lujing_list:
            panju = panju + self.calculate_policy_consistency(lujing)
        panju = panju / N_lujing 

        return panju

    def calculate_jvli(self,lujing_list):
        N_lujing = len(lujing_list)
        N_dianshu = len(lujing_list[0])
        s_end = np.zeros([N_lujing,self.dim])
        for i in range(N_lujing):
            s_end[i] = lujing_list[i][len(lujing_list[i])-1,0:self.dim]

        s_end_ave = np.mean(s_end,axis=0) 
        
        jvli = 0 
        for s_end_i in s_end:
            jvli = jvli + np.linalg.norm(s_end_i - s_end_ave)
        
        jvli = jvli / N_lujing

        return jvli

    def Pjudge_test(self,lujing_list,**kargs):
        # this is to decide if it is good engough
        if 'model' in kargs:
            model = kargs['model'] # str_on to return sentence for jilu
        else:
            model = 'str_off' 
        jvli = self.calculate_jvli(lujing_list)
        guanghua = self.calculate_guanghua(lujing_list)
        if jvli < self.jvli_threshold:
            flag_jvli = True
            str_jvil = 'MXairfoil: jvli judge pass. jvli = ' + str(jvli)
        else:
            flag_jvli = False
            str_jvil = 'MXairfoil: jvli judge fail. jvli = '+ str(jvli)
        
        if guanghua > self.guanghua_threshold:
            flag_guanghua = True
            str_guanghua = '  guanghua judge pass. guanghua = ' + str(guanghua) 
        else:
            flag_guanghua = False
            str_guanghua = '  guanghua judge fail. guanghua = '+ str(guanghua)

        
        jieguo = flag_guanghua and flag_jvli
        strbuffer = str_jvil + str_guanghua
        if model == 'str_on': 
            return  jieguo, strbuffer 
        elif model == 'str_off':
            print(strbuffer)
            return jieguo
        elif model == 'value':
            print(strbuffer)
            return jieguo,jvli,guanghua,strbuffer
        else:
            raise Exception('MXairfoil: invalid model for Pjudge_test')


if __name__ == '__main__':
    tu = huatu(0)
    # try to get some universality. set the real_location according to diannao.
    if os.environ['COMPUTERNAME'] == 'DESKTOP-GMBDOUR' :
        #which means in my diannao
        real_location2 = 'C:/Users/y/Desktop/DDPGshishi/agents/agent0_2dim'
        real_location4 = 'C:/Users/y/Desktop/DDPGshishi/agents/agent0_4dim'
    else:
        # which means in 106 server   
        real_location2 = 'C:/Users/106/Desktop/DDPGshishi/agents/agent0_2dim'
        real_location4 = 'C:/Users/106/Desktop/DDPGshishi/agents/agent0_4dim'
    
    flag = 42
    # 3 for demo function 
    # 4x for converge history, 1 for 2d huatu, , 5x for 3D huatu,5x for new.
    #  2x for purely getting lujing and Pjudge, 6x for surrogate model. 
    # 9x for new fig of old results, solid solidified, 8 for dynamic constraints. 
    # 10x for draw contour. 
    
    if flag ==0:
        tu.load_data('C:/Users/y/Desktop/DDPGshishi/agents/agent0_2dim','Reward-Episode relation')
        tu.huatu2D('episode','average reward','Reward-Episode relation')
        tu.load_data('C:/Users/y/Desktop/DDPGshishi/agents/agent0_2dim','Optimization-Episode relation')
        tu.huatu2D('episode','Optimization reward','Optimization-Episode relation')
    elif flag ==1 :
        # huatu for agent 2d.
        tu.set_location(real_location2)
        # tu.visual_2D(1,0) 
        # tu.visual_2D(2,0) # this is for kong de
        for i in range(10):
            tu.visual_2D(4,i)     
    elif flag == 2:
        weizhi = r'E:\常用-现役\研三下了吧应该是\DDPG配套\结果备份\静态限制的\四维带限制的\2021年9月7日一系列改进之后至少能收敛到一点了\agent0_4dim0.234956357247'
        tu.set_location(weizhi)
        tu.compare_performance()
    elif flag == 21:
        # this is for Pjudge.
        # weizhi = r'E:\常用-现役\研三下了吧应该是\DDPG配套\结果备份\CDA的\静态限制的\二维的\2021年8月10日姑且算是没作弊对了的\agent0_2dim'
        # weizhi = r'E:\常用-现役\主线的总备份\2021年12月10日开始三维之前的备份\GAPython\results\有说法的结果\GAresults2021-08-15二维无约束求策略100代带比较的'
        weizhi = r'E:\常用-现役\研三下了吧应该是\DDPG配套\结果备份\CDA的\静态限制的\二维的\2021年8月10日带限制的好像也一波推了？可能\agent0_2dim'
        tu.set_location(weizhi)
        tu.debug_Pjudge()
    elif flag == 3:
        weizhi = r'C:\Users\y\Desktop\DDPGshishi\agents\jieguo_DDPG_master6'
        tu.set_location(weizhi)
        tu.visual_2D(2,0,flag_background=3,labels = [r'$x_1$',r'$x_2$'])

        tu.load_data_universal([weizhi+'/episode0.pkl',weizhi+'/episode1.pkl'],[weizhi+'/reward0.pkl',weizhi+'/reward1.pkl'])
        # huatu2D_mul2(self,x_name,y_name,title,*names):
        tu.huatu2D_mul2('Episode','Average Reward','Converge History','Agent0','Agent1',single_ax=True)
    elif flag == 4:
        # this is to merge more than one lines.
        # weizhi = 'C:/Users/y/Desktop/DDPGshishi/agents/agent0_2dim'
        # weizhi = r'E:\常用-现役\研三下了吧应该是\DDPG配套\结果备份\静态限制的\二维的\2021年8月11日二维带限制的作弊倒是能到边上\agent0_2dim'
        weizhi =r'E:\常用-现役\研三下了吧应该是\DDPG配套\结果备份\静态限制的\二维的\2021年9月7日改了相应维度之后不带限制的\agent0_2dim0.0031137096088899694'
        location1 = weizhi+'/Optimization-Episode relation'
        location2 = weizhi+'/Reward-Episode relation'
        tu.set_location(weizhi)
        tu.load_data_mul(location1,location2)
        tu.huatu2D_mul2('Episode','average reward','Converge History','Detected Optimal Reward ','Average Reward')

        tu.save_all()
    elif flag == 5:
        # # this is for 3D plot 
        # weizhi = r'E:\常用-现役\研三下了吧应该是\DDPG配套\结果备份\静态限制的\四维不带限制的\2021年8月16日本地算的四维不带限制的更对一点的\agent0_4dim'
        weizhi = r'E:\常用-现役\研三下了吧应该是\DDPG配套\结果备份\静态限制的\未处理的四维带限制的结果\agent0_4dim0.234956357247'
        
        tu.set_location(weizhi)
        tu.visual_3D_mul(3,label=['From Original Point','From Random Point 1','From Random Point 2'],data_ids=[1,3,5])
        tu.plot_performance(data_location = [weizhi,weizhi,weizhi],label=['From Original Point','From Random Point 1','From Random Point 2'],data_id =[1,3,5])

        # # tu.set_location('C:/Users/y/Desktop/DDPGshishi/agents/agent0_2dim')
        # # tu.visual_3D(0,1) # this is start from 
        # tu.visual_3D(1,0) # for raw_state
        # for i in range(10):
        #     tu.visual_3D(0,i)

        # weizhi=r'C:\Users\y\Desktop\GAPython\results\有说法的结果\GAresults四维无约束四百代2021-08-17'
        # tu.set_location(weizhi)
        # # tu.visual_3D_mul(3,label=['GA result (400 generation)','GA result (100 generation)','RL result (~500 episode)'])
        # tu.plot_performance(data_location = [weizhi,weizhi,weizhi],label=['GA result (400 generation)','GA result (100 generation)','RL result (~500 episode)'],data_id = [0,1,2])
        pass
    elif flag == 6:
        # weizhi = 'C:/Users/y/Desktop/KrigingPython/结果类的/2021年8月10日5个点的进一步改了取值范围/backup'
        weizhi = 'C:/Users/y/Desktop/KrigingPython/结果类的/2021年10月4日4个点的NACA65'
        tu.set_location(weizhi)
        tu.plot_surrogate(location =weizhi)
    elif flag == 7:
        # this is to test the visual_2D mul, or other things in GA.
        tu.set_location(r'C:\Users\y\Desktop\GAPython\results\有说法的结果\GAresults2021-08-15二维无约束求策略100代带比较的')
        # C:\Users\y\Desktop\GAPython\results\GAresults2021-08-15
        # tu.visual_2D_mul(3,label = ['GA result (100 generation)', 'GA result (20 generation)','RL result (~500 episode)'])
        # tu.visual_3D(0,0)

        data_location3 = r'C:\Users\y\Desktop\GAPython\results\有说法的结果\GAresults2021-08-15二维无约束求策略100代带比较的'
        tu.plot_performance(data_location = [data_location3,data_location3,data_location3],label = ['GA result (100 generation)', 'GA result (20 generation)','RL result (~500 episode)'],data_id = np.array([0,1,2]))
    elif flag == 8 :
        # this is to huato for dynamic constraints.
        real_location2 = r'E:\常用-现役\研三下了吧应该是\DDPG配套\结果备份\CDA的\动态限制的\2021年8月28日完整备份一个版本\agent0_2dim'
        tu.set_location(real_location2)
        data_location1 = real_location2 + '/[ 1.0517 37.1   ]'
        data_location2 = real_location2 + '/[ 1.051 34.2  ]'
        data_location3 = r'E:\常用-现役\研三下了吧应该是\DDPG配套\结果备份\CDA的\静态限制的\二维的\2021年8月10日姑且算是没作弊对了的\agent0_2dim'# this is for comparison.
        weizhi = [data_location1,data_location2,data_location3]
        labels = ['Strict Constraints','Mild  Constraints','No     Constraints']
        index = np.array([1,1,1])
        tu.visual_2D_mul2(data_location =weizhi ,label=labels,flag_background=0,data_id = index,isoheight=False)
        tu.visual_2D_mul2(data_location = weizhi,label=labels,flag_background=1,data_id = index,isoheight=True)
        tu.plot_performance(data_location = weizhi,label=labels,data_id = index)
    elif flag == 91 :
        # this is for 2D unconstrained result,  solidified.
        data_location3 = r'E:\常用-现役\研三下了吧应该是\DDPG配套\结果备份\CDA的\静态限制的\二维的\2021年8月10日姑且算是没作弊对了的\agent0_2dim'
        data_id = np.array([7,9,1])
        label = ['Random Point 1','Random Point 2','Original Point']
        data_location = [data_location3,data_location3,data_location3]
        tu.set_location(data_location3)
        tu.visual_2D_mul2(data_location = data_location,label=label,data_id = data_id,flag_background=0,isoheight=False)
        tu.plot_performance(data_location = data_location,label=label,data_id = data_id)
    elif flag == 92 :
        # this is for 2D constrained 
        data_location3 = r'E:\常用-现役\研三下了吧应该是\DDPG配套\结果备份\CDA的\静态限制的\二维的\2021年8月10日带限制的好像也一波推了？可能\agent0_2dim'
        data_id = np.array([3,1])
        label = ['Random Point','Original Point']
        data_location = [data_location3,data_location3]
        tu.set_location(data_location3)
        tu.visual_2D_mul2(data_location = data_location,label=label,data_id = data_id,flag_background=0,isoheight=False)
        tu.visual_2D_mul2(data_location = data_location,label=label,data_id = data_id,flag_background=1,isoheight=True) # for pi
        tu.visual_2D_mul2(data_location = data_location,label=label,data_id = data_id,flag_background=2,isoheight=True) # for Delta beta
        tu.plot_performance(data_location = data_location,label=label,data_id = data_id)       
    elif flag == 93 :
        # this is for 2D compare with GA
        data_location3 = r'E:\常用-现役\主线的总备份\2021年12月10日开始三维之前的备份\GAPython\results\有说法的结果\GAresults2021-08-15二维无约束求策略100代带比较的'
        label = ['GA result (100 generation)', 'GA result (20  generation)','RL  result (~500  episode)']
        data_id = np.array([0,1,2])
        data_location = [data_location3,data_location3,data_location3]
        tu.set_location(data_location3)
        tu.visual_2D_mul2(data_location = data_location,label=label,data_id = data_id,flag_background=0,isoheight=False)
        tu.plot_performance(data_location = data_location,label=label,data_id = data_id)
    elif flag == 94 :
        # this is for NACA65 
        data_location_NACA652D = r'E:\常用-现役\研三下了吧应该是\DDPG配套\结果备份\NACA65的\二维无约束\第一个姑且能看得过去的2021年10月5日\agent0_2dim'
        data_id = np.array([6,4,1])
        label = ['Random Point 1','Random Point 2','Original Point']
        data_location = [data_location_NACA652D,data_location_NACA652D,data_location_NACA652D]
        tu.set_location(data_location_NACA652D)
        tu.visual_2D_mul2(data_location = data_location,label=label,data_id = data_id,flag_background=0,isoheight=False)
        tu.plot_performance(data_location = data_location,label=label,data_id = data_id)
    elif flag == 51 :
        # this is 4D unconstrained jieguo.
        weizhi = r'E:\常用-现役\研三下了吧应该是\DDPG配套\结果备份\CDA的\静态限制的\四维不带限制的\2021年8月16日本地算的四维不带限制的更对一点的\agent0_4dim'
        label = ['From Original Point','From Random Point 1','From Random Point 2']
        data_location = [weizhi,weizhi,weizhi]
        data_id = [1,8,5]
        tu.set_location(weizhi)
        tu.visual_3D_mul(3,label=label,data_ids=data_id)
        tu.plot_performance(data_location = data_location,label=label,data_id =data_id)
    elif flag == 52:
        # this is 4D constrained jieguo 
        weizhi = r'E:\常用-现役\研三下了吧应该是\DDPG配套\结果备份\CDA的\静态限制的\四维带限制的\2021年9月7日一系列改进之后至少能收敛到一点了\agent0_4dim0.234956357247'
        label = ['From Original Point','From Random Point 1','From Random Point 2']
        data_location = [weizhi,weizhi,weizhi]
        data_id = [1,3,5]
        tu.set_location(weizhi)
        tu.visual_3D_mul(3,label=label,data_ids=data_id)
        tu.plot_performance(data_location = data_location,label=label,data_id =data_id)      
    elif flag == 53:
        # this is for 4 dim design space GA compare.
        weizhi = r'E:\常用-现役\主线的总备份\2021年12月10日开始三维之前的备份\GAPython\results\有说法的结果\GAresults四维无约束四百代2021-08-17'
        tu.set_location(weizhi)
        label = ['GA result (400 generation)','GA result (100 generation)','RL result (~500 episode)']
        data_id = np.array([0,1,2])
        data_location = [weizhi,weizhi,weizhi]
        tu.visual_3D_mul(3,label=label,data_id=data_id)
        tu.plot_performance(data_location =data_location ,label=label,data_id = data_id)
    elif flag == 61:
        # this is for used surrogate model in CDA 
        # weizhi = r'C:\Users\y\Desktop\KrigingPython\结果类的\2021年8月10日5个点的进一步改了取值范围\backup'
        weizhi = r'E:\常用-现役\主线的总备份\2021年12月10日开始三维之前的备份\KrigingPython\结果类的\2021年8月10日5个点的进一步改了取值范围\backup'
        tu.set_location(weizhi)
        tu.plot_surrogate(location =weizhi)
    elif flag == 62:
        # this is for used surrogate model in NACA65 case 
        # weizhi = r'C:\Users\y\Desktop\KrigingPython\结果类的\2021年10月4日4个点的NACA65'
        weizhi = r'E:\常用-现役\比四上还更往后了烦的一笔\从桌面整理过来的\KrigingPython\结果类的\2021年10月4日4个点的NACA65'
        tu.set_location(weizhi)
        tu.plot_surrogate(location =weizhi)
    elif flag ==41 :
        # this is converge history for 2D unconstrained CDA case.
        weizhi =r'E:\常用-现役\研三下了吧应该是\DDPG配套\结果备份\CDA的\静态限制的\二维的\2021年8月10日姑且算是没作弊对了的\agent0_2dim'
        location1 = weizhi+'/Optimization-Episode relation'
        location2 = weizhi+'/Reward-Episode relation'
        tu.set_location(weizhi)
        tu.load_data_mul(location1,location2)
        tu.huatu2D_mul2('Episode','average reward','Converge History','Detected Optimal Reward ','Average Reward',case='CDA',model='all')
        
        # then add different grey lines.
        weizhi2 = r'E:\EnglishMulu\agents\二维无约束'
        tu.add_lines_for_history(weizhi2)

        tu.load_data_mul(location1,location2)
        tu.huatu2D_mul2('Episode','average reward','Converge History','Detected Optimal Reward ','Average Reward',case='CDA',model='all',redraw=True)
        tu.save_all()
    elif flag ==42 :
        # this is converge history for 2D constrained CDA case.
        weizhi =r'E:\常用-现役\研三下了吧应该是\DDPG配套\结果备份\CDA的\静态限制的\二维的\2021年8月11日二维带限制的作弊倒是能到边上\agent0_2dim'
        weizhi = r'E:\EnglishMulu\agents\二维有约束\agent0indedx0'
        location1 = weizhi+'/Optimization-Episode relation'
        location2 = weizhi+'/Reward-Episode relation'
        tu.set_location(weizhi)
        tu.load_data_mul(location1,location2)
        tu.huatu2D_mul2('Episode','average reward','Converge History','Detected Optimal Reward ','Average Reward',case='CDA')

        # then add different grey lines.
        weizhi2 = r'E:\EnglishMulu\agents\二维有约束'
        tu.add_lines_for_history(weizhi2)

        tu.load_data_mul(location1,location2)
        tu.huatu2D_mul2('Episode','average reward','Converge History','Detected Optimal Reward ','Average Reward',case='CDA',model='all',redraw=True)
        tu.ax2.plot(tu.x[0], tu.y[0]/100.0,label='Detected Optimal Reward ',linestyle='solid',linewidth=1,color='C0')

        tu.save_all()
    elif flag == 44:
        # this is for 18 dim demo function.
        weizhi =r'E:\常用-现役\研三下了吧应该是\DDPG配套\结果备份\Demo18维的\agent0_18dim'
        location1 = weizhi+'/Optimization-Episode relation'
        location2 = weizhi+'/Reward-Episode relation'
        tu.set_location(weizhi)
        tu.load_data_mul(location1,location2)
        tu.huatu2D_mul2('Episode','average reward','Converge History','Detected Optimal Reward ','Average Reward',case='demo18')
        tu.save_all()
    elif flag == 45:
        # this is for demo180 first. Many gray lines.
        data_folder = r'E:\EnglishMulu\agents'
        
        index = [0,1,2,3,4,5,6,7,8,9]
        tu.huatu_for_history(data_folder,index)
    elif flag == 46:
        # huatu by hand.
        weizhi = r'E:\EnglishMulu\agents\二维有约束\agent0indedx'
        for i in range(31):
            weizhi2 = weizhi+str(i)
            tu.set_location(weizhi2)
            tu.recycle_log()

    elif flag == 10:
        # this is to debug things related to contour huatu.
        data_location3 = r'C:\Users\y\Desktop\EnglishMulu\figure-post\二维无约束10图的CDA\CDA12022-03-10\contour-Ps'
        tu.generate_gif(data_location3,name='shishi')
    elif flag == 101 :
        # this is for 2D unconstrained result,  solidified.
        data_location3 = r'E:\常用-现役\研三下了吧应该是\DDPG配套\结果备份\CDA的\静态限制的\二维的\2021年8月10日姑且算是没作弊对了的\agent0_2dim'
        data_id = np.array([7,9,1])
        label = ['Random Point 1','Random Point 2','Original Point']
        data_location = [data_location3,data_location3,data_location3]
        tu.set_location(data_location3)
        tu.huatu_contour(data_id = data_id[2],data_location=data_location[2])
    elif flag == 102 :
        # this is for 2D constrained result,  solidified.
        data_location3 = r'E:\常用-现役\研三下了吧应该是\DDPG配套\结果备份\CDA的\静态限制的\二维的\2021年8月10日带限制的好像也一波推了？可能\agent0_2dim'
        data_id = np.array([3,1])
        label = ['Random Point','Original Point']
        data_location = [data_location3,data_location3]
        tu.set_location(data_location3)
        tu.huatu_contour(data_id = data_id[1],data_location=data_location[1])
    elif flag == 103:
        # this is for 4D design space 
        # this is 4D unconstrained jieguo.
        weizhi = r'E:\常用-现役\研三下了吧应该是\DDPG配套\结果备份\CDA的\静态限制的\四维不带限制的\2021年8月16日本地算的四维不带限制的更对一点的\agent0_4dim'
        label = ['From Original Point','From Random Point 1','From Random Point 2']
        data_location = [weizhi,weizhi,weizhi]
        data_id = [1,8,5]
        tu.real_dim = 4 
        tu.set_location(weizhi)
        tu.huatu_contour(data_id = data_id[0],data_location=data_location[0]) 
    elif flag == 104:
        # this is 4D constrained jieguo 
        tu = huatu(0,real_dim=4)
        weizhi = r'E:\常用-现役\研三下了吧应该是\DDPG配套\结果备份\CDA的\静态限制的\四维带限制的\2021年9月7日一系列改进之后至少能收敛到一点了\agent0_4dim0.234956357247'
        label = ['From Original Point','From Random Point 1','From Random Point 2']
        data_location = [weizhi,weizhi,weizhi]
        data_id = [1,3,5]
        tu.real_dim = 4 
        tu.set_location(weizhi)
        tu.huatu_contour(data_id = data_id[0],data_location=data_location[0]) 


    print('MXairfoil: huatu.')
        