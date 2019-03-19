import numpy as np
import sys
sys.path.append("../")
from transdata import *
import matplotlib.pyplot as plt

logfile_path1='/data/wangh/hyperparametertuning_a0g/pi_v/66othellodata/logfiles/66othello_pi_v_run1.log'
logfile_path2='/data/wangh/hyperparametertuning_a0g/pi_v/66othellodata/logfiles/66othello_pi_v_run2.log'
logfile_path3='/data/wangh/hyperparametertuning_a0g/pi_v/66othellodata/logfiles/66othello_pi_v_run3.log'
logfile_path4='/data/wangh/hyperparametertuning_a0g/pi_v/66othellodata/logfiles/66othello_pi_v_run4.log'
logfile_path5='/data/wangh/hyperparametertuning_a0g/pi_v/66othellodata/logfiles/66othello_pi_v_run5.log'
logfile_path6='/data/wangh/hyperparametertuning_a0g/pi_v/66othellodata/logfiles/66othello_pi_v_run6.log'
logfile_path7='/data/wangh/hyperparametertuning_a0g/pi_v/66othellodata/logfiles/66othello_pi_v_run7.log'
logfile_path8='/data/wangh/hyperparametertuning_a0g/pi_v/66othellodata/logfiles/66othello_pi_v_run8.log'
logfile_path9='/data/wangh/hyperparametertuning_a0g/pi_v/66othellodata/logfiles/66othello_pi_v_run9.log'
logfile_path10='/data/wangh/hyperparametertuning_a0g/pi_v/66othellodata/logfilel/66othello_pi_v_run10.log'


pi_vlogs=[logfile_path1,logfile_path2,logfile_path3,logfile_path4,logfile_path5,logfile_path6,logfile_path7,logfile_path8]
color=['red','blue','green','pink','black','cyan','magenta','yellow','#FA000F','#0FB0FF']

list_pi=[[0]*100 for i in range(8)]
list_v=[[0]*100 for i in range(8)]
list_pi_v=[[0]*100 for i in range(8)]
for i in range(len(pi_vlogs)):
    with open(pi_vlogs[i],'r') as f:
        try:
            j=0
            line_previous=f.readline()
            while line_previous:
                line=f.readline()
                if 'PITTING AGAINST PREVIOUS VERSION' in line:
                    t=transdata(line_previous)
                    cur_pi,cur_v=t.trans_pi_v()
                    list_pi[i][j]=float(cur_pi)
                    list_v[i][j]=float(cur_v)
                    list_pi_v[i][j]=(float(list_pi[i][j])+float(list_v[i][j]))
                    j=j+1
                line_previous=line
        finally:
            f.close()

mean_pi=np.mean(list_pi,axis=0)
mean_v=np.mean(list_v,axis=0)
mean_pi_v=np.mean(list_pi_v,axis=0)
print(list_pi_v)
std_pi=np.std(list_pi,axis=0)
std_v=np.std(list_v,axis=0)
std_pi_v=np.std(list_pi_v,axis=0)

x_pi=np.arange(0,len(list_pi[0]),1)
x_v=np.arange(0,len(list_v[0]),1)
x_pi_v=np.arange(0,len(list_pi_v[0]),1)

#print(len(x_pi),len(mean_pi),len(std_pi))
plt.errorbar(x_pi,mean_pi,yerr=std_pi,fmt='o',ecolor='r',color='r',elinewidth=2,capsize=4)
plt.errorbar(x_v,mean_v,yerr=std_v,fmt='*',ecolor='b',color='b',elinewidth=2,capsize=4)
plt.errorbar(x_pi_v,mean_pi_v,yerr=std_pi_v,fmt='+',ecolor='g',color='g',elinewidth=2,capsize=4)
SMALL_SIZE=20
BIGGER_SIZE=20
plt.rc('font', size=BIGGER_SIZE)
plt.rc('xtick', labelsize=SMALL_SIZE)
plt.rc('ytick', labelsize=SMALL_SIZE)
plt.yticks(np.arange (0,2.75,0.25))
plt.ylim(0,2.5)
plt.xticks(np.arange (0,len(list_pi[0]), step=20))
plt.xlabel('Training iteration')
plt.ylabel('Loss')
plt.legend(['loss_pi','loss_v','sum'],'upper right')
plt.savefig("errorbar/errorbar_pi_v_66othello_loss_8runs.eps")
plt.show()

