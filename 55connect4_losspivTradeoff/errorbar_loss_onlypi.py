import numpy as np
import sys
sys.path.append("../")
from transdata import *
import matplotlib.pyplot as plt

logfile_path1='/data/wangh/hyperparametertuning_a0g/onlypi/55connect4data/logfiles/55connect4_onlypi_run1.log'
logfile_path2='/data/wangh/hyperparametertuning_a0g/onlypi/55connect4data/logfiles/55connect4_onlypi_run2.log'
logfile_path3='/data/wangh/hyperparametertuning_a0g/onlypi/55connect4data/logfiles/55connect4_onlypi_run3.log'
logfile_path4='/data/wangh/hyperparametertuning_a0g/onlypi/55connect4data/logfiles/55connect4_onlypi_run4.log'
logfile_path5='/data/wangh/hyperparametertuning_a0g/onlypi/55connect4data/logfiles/55connect4_onlypi_run5.log'
logfile_path6='/data/wangh/hyperparametertuning_a0g/onlypi/55connect4data/logfiles/55connect4_onlypi_run6.log'
logfile_path7='/data/wangh/hyperparametertuning_a0g/onlypi/55connect4data/logfiles/55connect4_onlypi_run7.log'
logfile_path8='/data/wangh/hyperparametertuning_a0g/onlypi/55connect4data/logfiles/55connect4_onlypi_run8.log'
logfile_path9='/data/wangh/hyperparametertuning_a0g/onlypi/55connect4data/logfiles/55connect4_onlypi_run9.log'
logfile_path10='/data/wangh/hyperparametertuning_a0g/onlypi/55connect4data/logfiles/55connect4_onlypi_run10.log'

#onlypilogs=[logfile_path1,logfile_path2,logfile_path3,logfile_path4,logfile_path5,logfile_path6,logfile_path7,logfile_path8,logfile_path9,logfile_path10]
onlypilogs=[logfile_path1,logfile_path2,logfile_path3,logfile_path4,logfile_path5,logfile_path6,logfile_path7,logfile_path8]
color=['red','blue','green','pink','black','cyan','magenta','yellow','#FA000F','#0FB0FF']

list_pi=[[0]*200 for i in range(8)]
list_v=[[0]*200 for i in range(8)]
list_pi_v=[[0]*200 for i in range(8)]
for i in range(len(onlypilogs)):
    with open(onlypilogs[i],'r') as f:
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
                    j=j+1
                line_previous=line
        finally:
            f.close()
    for j in range(len(list_pi)):
        list_pi_v[i][j]=(float(list_pi[i][j])+float(list_v[i][j]))

#fig, ax = plt.subplots()
#bp1=ax.boxplot(zip(*list_pi),notch=True, sym='bs',vert=True, patch_artist=True, boxprops=dict(facecolor="C0"))
#bp2=ax.boxplot(zip(*list_v),notch=True, sym='bs',vert=True, patch_artist=True, boxprops=dict(facecolor="C2"))
#ax.legend([bp1["boxes"][0], bp2["boxes"][0]], ['loss_pi', 'loss_v'], loc='upper right')
#bp1=ax.boxplot(zip(*list_pi),notch=True, sym='rs',vert=True, patch_artist=True)
#for patch in bp1['boxes']:
#    patch.set_facecolor(color[0])
#bp2=ax.boxplot(zip(*list_v),notch=True, sym='bs',vert=True, patch_artist=True)
#for patch in bp2['boxes']:
#    patch.set_facecolor(color[1])
#ax.legend([bp1["boxes"][0], bp2["boxes"][0]], ['loss_pi', 'loss_v'], loc='upper right')

mean_pi=np.mean(list_pi,axis=0)
mean_v=np.mean(list_v,axis=0)

std_pi=np.std(list_pi,axis=0)
std_v=np.std(list_v,axis=0)
x_pi=np.arange(0,len(list_pi[0]),1)
x_v=np.arange(0,len(list_v[0]),1)
print(len(x_pi),len(mean_pi),len(std_pi))
plt.errorbar(x_pi,mean_pi,yerr=std_pi,fmt='o',ecolor='r',color='r',elinewidth=2,capsize=4)
plt.errorbar(x_v,mean_v,yerr=std_v,fmt='*',ecolor='b',color='b',elinewidth=2,capsize=4)
SMALL_SIZE=20
BIGGER_SIZE=20
plt.rc('font', size=BIGGER_SIZE)
plt.rc('xtick', labelsize=SMALL_SIZE)
plt.rc('ytick', labelsize=SMALL_SIZE)
plt.yticks(np.arange (0,2.75,0.25))
plt.ylim(0,2.5)
plt.xticks(np.arange (0,len(list_pi_v[0]), step=20))
plt.xlabel('Training iteration')
plt.ylabel('Loss')
plt.legend(['loss_pi','loss_v'],'upper right')
plt.savefig("errorbar/errorbar_onlypi_55connect4_loss_8runs.eps")
plt.show()

