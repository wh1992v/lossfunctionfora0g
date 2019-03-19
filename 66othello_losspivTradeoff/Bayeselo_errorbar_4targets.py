import numpy as np
import sys
sys.path.append("../")
import matplotlib.pyplot as plt
import re

elofile_onlypi_path1='pgn4onlypi/run1.txt'
elofile_onlypi_path2='pgn4onlypi/run2.txt'
elofile_onlypi_path3='pgn4onlypi/run3.txt'
elofile_onlypi_path4='pgn4onlypi/run4.txt'
elofile_onlypi_path5='pgn4onlypi/run5.txt'
elofile_onlypi_path6='pgn4onlypi/run6.txt'
elofile_onlypi_path7='pgn4onlypi/run7.txt'
elofile_onlypi_path8='pgn4onlypi/run8.txt'
elofile_onlyv_path1='pgn4onlyv/run1.txt'
elofile_onlyv_path2='pgn4onlyv/run2.txt'
elofile_onlyv_path3='pgn4onlyv/run3.txt'
elofile_onlyv_path4='pgn4onlyv/run4.txt'
elofile_onlyv_path5='pgn4onlyv/run5.txt'
elofile_onlyv_path6='pgn4onlyv/run6.txt'
elofile_onlyv_path7='pgn4onlyv/run7.txt'
elofile_onlyv_path8='pgn4onlyv/run8.txt'
elofile_pi_v_path1='pgn4pi_v/run1.txt'
elofile_pi_v_path2='pgn4pi_v/run2.txt'
elofile_pi_v_path3='pgn4pi_v/run3.txt'
elofile_pi_v_path4='pgn4pi_v/run4.txt'
elofile_pi_v_path5='pgn4pi_v/run5.txt'
elofile_pi_v_path6='pgn4pi_v/run6.txt'
elofile_pi_v_path7='pgn4pi_v/run7.txt'
elofile_pi_v_path8='pgn4pi_v/run8.txt'
elofile_piv_path1='pgn4piv/run1.txt'
elofile_piv_path2='pgn4piv/run2.txt'
elofile_piv_path3='pgn4piv/run3.txt'
elofile_piv_path4='pgn4piv/run4.txt'
elofile_piv_path5='pgn4piv/run5.txt'
elofile_piv_path6='pgn4piv/run6.txt'
elofile_piv_path7='pgn4piv/run7.txt'
elofile_piv_path8='pgn4piv/run8.txt'

elofiles_onlypi=[elofile_onlypi_path1,elofile_onlypi_path2,elofile_onlypi_path3,elofile_onlypi_path4,elofile_onlypi_path5,elofile_onlypi_path6,elofile_onlypi_path7,elofile_onlypi_path8]
elofiles_onlyv=[elofile_onlyv_path1,elofile_onlyv_path2,elofile_onlyv_path3,elofile_onlyv_path4,elofile_onlyv_path5,elofile_onlyv_path6,elofile_onlyv_path7,elofile_onlyv_path8]
elofiles_pi_v=[elofile_pi_v_path1,elofile_pi_v_path2,elofile_pi_v_path3,elofile_pi_v_path4,elofile_pi_v_path5,elofile_pi_v_path6,elofile_pi_v_path7,elofile_pi_v_path8]
elofiles_piv=[elofile_piv_path1,elofile_piv_path2,elofile_piv_path3,elofile_piv_path4,elofile_piv_path5,elofile_piv_path6,elofile_piv_path7,elofile_piv_path8]

elofiles=[elofiles_onlypi,elofiles_onlyv,elofiles_pi_v,elofiles_piv]

format_errorbar=['o','*','+','s']
color_errorbar=['r','b','g','pink']
for i in range(len(elofiles)):
    namelist=[[0]*101 for a in range(8)]
    elolist=[[0]*101 for a in range(8)]
    #print(len(namelist))
    for j in range(len(elofiles[0])):
        with open(elofiles[i][j],'r') as f:
            try:
                b=0
                line=f.readline()
                while line:
                    if 'Name' not in line:
                        
                        line=re.sub(r'\s+', ' ', line)
                        #for j in range(len(line.split(' '))):
                            #print(line.split(' ')[j])
                        namelist[j][b]=int(line.split(' ')[2].split('n')[1])
                        elolist[j][b]=int(line.split(' ')[3])
                        b=b+1
                    line=f.readline()
                #print(namelist,elolist)
                reranknamelist= np.arange(0,len(namelist[0]),1)
                rerankelolist=np.zeros([len(namelist[0])])
                for k in range(len(namelist[0])):
                    name=namelist[j][k]
                    rerankelolist[name]=(elolist[j][k])
                for l in range(len(namelist[0])):
                    namelist[j][l]=reranknamelist[l]
                    elolist[j][l]=rerankelolist[l]
            finally:
                f.close()
    mean=np.mean(elolist,axis=0)
    std=np.std(elolist,axis=0)
    x=np.arange(0,len(elolist[0]),1)
    plt.errorbar(x,mean,yerr=std,fmt=format_errorbar[i],ecolor=color_errorbar[i],color=color_errorbar[i],elinewidth=2,capsize=4)
SMALL_SIZE=20
BIGGER_SIZE=20
plt.rc('font', size=BIGGER_SIZE)
plt.rc('xtick', labelsize=SMALL_SIZE)
plt.rc('ytick', labelsize=SMALL_SIZE)
plt.gca().yaxis.get_major_formatter().set_powerlimits((0,1))
plt.ylim(-4000, 4000)
plt.yticks(np.arange (-4000,5000,1000))
plt.xticks(np.arange (0,len(namelist[0]), step=20))
plt.xlabel('Training iteration')
plt.ylabel('Elo rating')
plt.legend(['loss_pi','loss_v','sum','product'],"upper left")
plt.savefig('errorbar/elo_66othello_8runs.eps')
plt.show()
