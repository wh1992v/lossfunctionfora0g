import numpy as np
import sys
sys.path.append("../")
from transdata import *
import matplotlib.pyplot as plt



logfile_path1='/data/wangh/hyperparametertuning_a0g/pi_v/pitresult/playwitheachother_55othello.log'
logfile_path2='/data/wangh/hyperparametertuning_a0g/pi_v/pitresult/playwitheachother_66othello.log'
logfile_path3='/data/wangh/hyperparametertuning_a0g/pi_v/pitresult/playwitheachother_66connect4.log'
logfile_path4='/data/wangh/hyperparametertuning_a0g/pi_v/pitresult/playwitheachother_55connect4.log'
logfiles=[logfile_path1,logfile_path2,logfile_path3,logfile_path4]
#logfiles=[logfile_path1,logfile_path2,logfile_path3,logfile_path4,logfile_path5,logfile_path6,logfile_path7,logfile_path8,logfile_path9,logfile_path10]
pgn_path1='pgn4pit_55othello.pgn'
pgn_path2='pgn4pit_66othello.pgn'
pgn_path3='pgn4pit_66connect4.pgn'
pgn_path4='pgn4pit_55connect4.pgn'
pgnfiles=[pgn_path1,pgn_path2,pgn_path3,pgn_path4]

for i in range(len(logfiles)):
    with open(logfiles[i],'r') as f:
        try:
            s=0
            line=f.readline()
            while line:
                if 'wanghui|' in line:
                    whiteplayer=line.split('|')[1]
                    blackplayer=line.split('|')[2]
                    line=f.readline()
                if 'Arena' in line:
                    line=f.readline()
                if 'wanghuiscore' in line:
                    s+=1
                    cur_win=line.split('(')[1].split(',')[0]
                    cur_loss=line.split('(')[1].split(',')[1]
                    cur_draw=line.split('(')[1].split(',')[2].split(')')[0]
                    rounds=int(cur_win)+int(cur_loss)+int(cur_draw)
                    fw = open(pgnfiles[i], 'a')
                    for rd in range(rounds):
                        fw.write('[Event "'+pgnfiles[i]+'"]\n')
                        fw.write('[Iteration "'+str(s)+'"]\n')
                        fw.write('[Site "liacs server, Leiden"]\n')
                        fw.write('[Round "'+str(rd)+'"]\n')
                        fw.write('[White "'+str(whiteplayer)+'"]\n')
                        fw.write('[Black "'+str(blackplayer)+'"]\n')
                        if rd<int(cur_win):
                            fw.write('[Result "1-0"]\n')
                        elif rd<(int(cur_win)+int(cur_loss)):
                            fw.write('[Result "0-1"]\n')
                        else:
                            fw.write('[Result "1/2-1/2"]\n')
                        fw.write('Here are detailed game moves for [Iteration "'+str(s)+', round'+str(rd)+'"]\n')
                        fw.write('\n')
                    fw.close()
                line=f.readline()
        finally:
            f.close()


