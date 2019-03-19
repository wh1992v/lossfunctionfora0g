import numpy as np
import sys
sys.path.append("../")
from transdata import *
import matplotlib.pyplot as plt

logfile_path1='/data/wangh/hyperparametertuning_a0g/pi_v/66connect4data/logfiles/66connect4_pi_v_run1.log'
logfile_path2='/data/wangh/hyperparametertuning_a0g/pi_v/66connect4data/logfiles/66connect4_pi_v_run2.log'
logfile_path3='/data/wangh/hyperparametertuning_a0g/pi_v/66connect4data/logfiles/66connect4_pi_v_run3.log'
logfile_path4='/data/wangh/hyperparametertuning_a0g/pi_v/66connect4data/logfiles/66connect4_pi_v_run4.log'
logfile_path5='/data/wangh/hyperparametertuning_a0g/pi_v/66connect4data/logfiles/66connect4_pi_v_run5.log'
logfile_path6='/data/wangh/hyperparametertuning_a0g/pi_v/66connect4data/logfiles/66connect4_pi_v_run6.log'
logfile_path7='/data/wangh/hyperparametertuning_a0g/pi_v/66connect4data/logfiles/66connect4_pi_v_run7.log'
logfile_path8='/data/wangh/hyperparametertuning_a0g/pi_v/66connect4data/logfiles/66connect4_pi_v_run8.log'
logfile_path9='/data/wangh/hyperparametertuning_a0g/pi_v/66connect4data/logfiles/66connect4_pi_v_run9.log'
logfile_path10='/data/wangh/hyperparametertuning_a0g/pi_v/66connect4data/logfiles/66connect4_pi_v_run10.log'

logfiles=[logfile_path1,logfile_path2,logfile_path3,logfile_path4,logfile_path5,logfile_path6,logfile_path7,logfile_path8]
#logfiles=[logfile_path1,logfile_path2,logfile_path3,logfile_path4,logfile_path5,logfile_path6,logfile_path7,logfile_path8,logfile_path9,logfile_path10]
pgn_path1='pgn4pi_v/run1.pgn'
pgn_path2='pgn4pi_v/run2.pgn'
pgn_path3='pgn4pi_v/run3.pgn'
pgn_path4='pgn4pi_v/run4.pgn'
pgn_path5='pgn4pi_v/run5.pgn'
pgn_path6='pgn4pi_v/run6.pgn'
pgn_path7='pgn4pi_v/run7.pgn'
pgn_path8='pgn4pi_v/run8.pgn'
pgn_path9='pgn4pi_v/run9.pgn'
pgn_path10='pgn4pi_v/run10.pgn'

pgnfiles=[pgn_path1,pgn_path2,pgn_path3,pgn_path4,pgn_path5,pgn_path6,pgn_path7,pgn_path8,pgn_path9,pgn_path10]



for i in range(len(logfiles)):
    with open(logfiles[i],'r') as f:
        try:
            iteration=1
            blackplayer=iteration-1
            whiteplayer=iteration
            line_previous=f.readline()
            while line_previous:
                line=f.readline()
                if 'REJECTING NEW MODEL' in line:
                    t=transdata(line_previous)
                    cur_win,cur_loss,cur_draw=t.trans_winloss()
                    rounds=int(cur_win)+int(cur_loss)+int(cur_draw)
                    fw = open(pgnfiles[i], 'a')
                    for rd in range(rounds):
                        fw.write('[Event "'+pgnfiles[i]+'"]\n')
                        fw.write('[Iteration "'+str(iteration)+'"]\n')
                        fw.write('[Site "liacs server, Leiden"]\n')
                        fw.write('[Round "'+str(rd)+'"]\n')
                        fw.write('[White "Iteration'+str(whiteplayer)+'"]\n')
                        fw.write('[Black "Iteration'+str(blackplayer)+'"]\n')
                        if rd<int(cur_win):
                            fw.write('[Result "1-0"]\n')
                        elif rd<(int(cur_win)+int(cur_loss)):
                            fw.write('[Result "0-1"]\n')
                        else:
                            fw.write('[Result "1/2-1/2"]\n')
                        fw.write('Here are detailed game moves for [Iteration "'+str(iteration)+', round'+str(rd)+'"]\n')
                        fw.write('\n')
                    fw.close()
                    iteration+=1
                    blackplayer=blackplayer
                    whiteplayer=whiteplayer+1
                if 'ACCEPTING NEW MODEL' in line:
                    t=transdata(line_previous)
                    cur_win,cur_loss,cur_draw=t.trans_winloss()
                    rounds=int(cur_win)+int(cur_loss)+int(cur_draw)
                    fw = open(pgnfiles[i], 'a')
                    for rd in range(rounds):
                        fw.write('[Event "'+pgnfiles[i]+'"]\n')
                        fw.write('[Iteration "'+str(iteration)+'"]\n')
                        fw.write('[Site "liacs server, Leiden"]\n')
                        fw.write('[Round "'+str(rd)+'"]\n')
                        fw.write('[White "Iteration'+str(whiteplayer)+'"]\n')
                        fw.write('[Black "Iteration'+str(blackplayer)+'"]\n')
                        if rd<int(cur_win):
                            fw.write('[Result "1-0"]\n')
                        elif rd<(int(cur_win)+int(cur_loss)):
                            fw.write('[Result "0-1"]\n')
                        else:
                            fw.write('[Result "1/2-1/2"]\n')
                        fw.write('Here are detailed game moves for [Iteration "'+str(iteration)+', round'+str(rd)+'"]\n')
                        fw.write('\n')
                    fw.close()
                    iteration+=1
                    blackplayer=whiteplayer
                    whiteplayer=whiteplayer+1
                line_previous=line
        finally:
            f.close()


