import numpy as np
import sys
sys.path.append("../")
import matplotlib.pyplot as plt
import re

elofile_path1='55othello_pitresult.txt'
elofile_path2='66othello_pitresult.txt'
elofile_path3='66connect4_pitresult.txt'
elofile_path4='55connect4_pitresult.txt'
elofiles=[elofile_path1,elofile_path2,elofile_path3,elofile_path4]
fignames=['elo_55othelloplayers.eps','elo_66othelloplayers.eps','elo_66connect4players.eps','elo_55connect4players.eps']

for i in range(len(elofiles)):
    with open(elofiles[i],'r') as f:
        try:
            elopi=[]
            elov=[]
            elopi_v=[]
            elopiv=[]
            line=f.readline()
            while line:
                if 'Name' not in line:
                    line=re.sub(r'\s+', ' ', line)
                    if 'bestmodel_pi_run' in line:
                        elopi.append(int(line.split(' ')[3]))
                    if 'bestmodel_v_run' in line:
                        elov.append(int(line.split(' ')[3]))
                    if 'bestmodel_pi_v_run' in line:
                        elopi_v.append(int(line.split(' ')[3]))
                    if 'bestmodel_piv_run' in line:
                        elopiv.append(int(line.split(' ')[3]))
                line=f.readline()
            elopi=np.array(elopi)
            elov=np.array(elov)
            elopi_v=np.array(elopi_v)
            elopiv=np.array(elopiv)
        finally:
            f.close()
    all_data=[elopi,elov,elopi_v,elopiv]
    SMALL_SIZE=20
    BIGGER_SIZE=20
    plt.rc('font', size=BIGGER_SIZE)
    plt.rc('xtick', labelsize=SMALL_SIZE)
    plt.rc('ytick', labelsize=SMALL_SIZE)
    plt.rc('legend', fontsize=SMALL_SIZE)
    plt.boxplot(all_data,notch=True, sym='bs',vert=True, patch_artist=True) 
    plt.xticks(np.arange(1, 5, step=1),['loss_pi', 'loss_v', 'sum','product'])
    plt.yticks(np.arange(-400,550,50))
    plt.xlabel('Optimized target')
    plt.ylabel('Elo rating')
    plt.savefig(fignames[i])
    plt.show()
    print('Bye')

