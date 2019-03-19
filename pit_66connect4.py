import Arena
from MCTS import MCTS
from connect4.Connect4Game import Connect4Game, display
from connect4.Connect4Players import *
from connect4.tensorflowonlypi.NNet import NNetWrapper as NNetpi
from connect4.tensorflowonlyv.NNet import NNetWrapper as NNetv
from connect4.tensorflowpiv.NNet import NNetWrapper as NNetpiv
from connect4.tensorflowpi_v.NNet import NNetWrapper as NNetpi_v

import numpy as np
from utils import *

"""
use this script to play any two agents against each other, or play manually with
any agent.
"""
modelpath_pi_v_1='/data/wangh/hyperparametertuning_a0g/pi_v/66connect4data/bestmodels/bestmodel_66connect4_pi_v_run1'
modelpath_pi_v_2='/data/wangh/hyperparametertuning_a0g/pi_v/66connect4data/bestmodels/bestmodel_66connect4_pi_v_run2'
modelpath_pi_v_3='/data/wangh/hyperparametertuning_a0g/pi_v/66connect4data/bestmodels/bestmodel_66connect4_pi_v_run3'
modelpath_pi_v_4='/data/wangh/hyperparametertuning_a0g/pi_v/66connect4data/bestmodels/bestmodel_66connect4_pi_v_run4'
modelpath_pi_v_5='/data/wangh/hyperparametertuning_a0g/pi_v/66connect4data/bestmodels/bestmodel_66connect4_pi_v_run5'
modelpath_pi_v_6='/data/wangh/hyperparametertuning_a0g/pi_v/66connect4data/bestmodels/bestmodel_66connect4_pi_v_run6'
modelpath_pi_v_7='/data/wangh/hyperparametertuning_a0g/pi_v/66connect4data/bestmodels/bestmodel_66connect4_pi_v_run7'
modelpath_pi_v_8='/data/wangh/hyperparametertuning_a0g/pi_v/66connect4data/bestmodels/bestmodel_66connect4_pi_v_run8'
modelpath_pi_v_9='/data/wangh/hyperparametertuning_a0g/pi_v/66connect4data/bestmodels/bestmodel_66connect4_pi_v_run9'
modelpath_pi_v_10='/data/wangh/hyperparametertuning_a0g/pi_v/66connect4data/bestmodels/bestmodel_66connect4_pi_v_run10'
#modelpaths_pi_v=[modelpath_pi_v_1,modelpath_pi_v_2,modelpath_pi_v_3,modelpath_pi_v_4,modelpath_pi_v_5,modelpath_pi_v_6,modelpath_pi_v_7,modelpath_pi_v_8,modelpath_pi_v_9,modelpath_pi_v_10]
modelpaths_pi_v=[modelpath_pi_v_1,modelpath_pi_v_2,modelpath_pi_v_3,modelpath_pi_v_4,modelpath_pi_v_5,modelpath_pi_v_6,modelpath_pi_v_7,modelpath_pi_v_8]

modelpath_pi_1='/data/wangh/hyperparametertuning_a0g/onlypi/66connect4data/bestmodels/bestmodel_66connect4_onlypi_run1'
modelpath_pi_2='/data/wangh/hyperparametertuning_a0g/onlypi/66connect4data/bestmodels/bestmodel_66connect4_onlypi_run2'
modelpath_pi_3='/data/wangh/hyperparametertuning_a0g/onlypi/66connect4data/bestmodels/bestmodel_66connect4_onlypi_run3'
modelpath_pi_4='/data/wangh/hyperparametertuning_a0g/onlypi/66connect4data/bestmodels/bestmodel_66connect4_onlypi_run4'
modelpath_pi_5='/data/wangh/hyperparametertuning_a0g/onlypi/66connect4data/bestmodels/bestmodel_66connect4_onlypi_run5'
modelpath_pi_6='/data/wangh/hyperparametertuning_a0g/onlypi/66connect4data/bestmodels/bestmodel_66connect4_onlypi_run6'
modelpath_pi_7='/data/wangh/hyperparametertuning_a0g/onlypi/66connect4data/bestmodels/bestmodel_66connect4_onlypi_run7'
modelpath_pi_8='/data/wangh/hyperparametertuning_a0g/onlypi/66connect4data/bestmodels/bestmodel_66connect4_onlypi_run8'
modelpath_pi_9='/data/wangh/hyperparametertuning_a0g/onlypi/66connect4data/bestmodels/bestmodel_66connect4_onlypi_run9'
modelpath_pi_10='/data/wangh/hyperparametertuning_a0g/onlypi/66connect4data/bestmodels/bestmodel_66connect4_onlypi_run10'
#modelpaths_pi=[modelpath_pi_1,modelpath_pi_2,modelpath_pi_3,modelpath_pi_4,modelpath_pi_5,modelpath_pi_6,modelpath_pi_7,modelpath_pi_8,modelpath_pi_9,modelpath_pi_10]
modelpaths_pi=[modelpath_pi_1,modelpath_pi_2,modelpath_pi_3,modelpath_pi_4,modelpath_pi_5,modelpath_pi_6,modelpath_pi_7,modelpath_pi_8]

modelpath_v_1='/data/wangh/hyperparametertuning_a0g/onlyv/66connect4data/bestmodels/bestmodel_66connect4_onlyv_run1'
modelpath_v_2='/data/wangh/hyperparametertuning_a0g/onlyv/66connect4data/bestmodels/bestmodel_66connect4_onlyv_run2'
modelpath_v_3='/data/wangh/hyperparametertuning_a0g/onlyv/66connect4data/bestmodels/bestmodel_66connect4_onlyv_run3'
modelpath_v_4='/data/wangh/hyperparametertuning_a0g/onlyv/66connect4data/bestmodels/bestmodel_66connect4_onlyv_run4'
modelpath_v_5='/data/wangh/hyperparametertuning_a0g/onlyv/66connect4data/bestmodels/bestmodel_66connect4_onlyv_run5'
modelpath_v_6='/data/wangh/hyperparametertuning_a0g/onlyv/66connect4data/bestmodels/bestmodel_66connect4_onlyv_run6'
modelpath_v_7='/data/wangh/hyperparametertuning_a0g/onlyv/66connect4data/bestmodels/bestmodel_66connect4_onlyv_run7'
modelpath_v_8='/data/wangh/hyperparametertuning_a0g/onlyv/66connect4data/bestmodels/bestmodel_66connect4_onlyv_run8'
modelpath_v_9='/data/wangh/hyperparametertuning_a0g/onlyv/66connect4data/bestmodels/bestmodel_66connect4_onlyv_run9'
modelpath_v_10='/data/wangh/hyperparametertuning_a0g/onlyv/66connect4data/bestmodels/bestmodel_66connect4_onlyv_run10'
#modelpaths_v=[modelpath_v_1,modelpath_v_2,modelpath_v_3,modelpath_v_4,modelpath_v_5,modelpath_v_6,modelpath_v_7,modelpath_v_8,modelpath_v_9,modelpath_v_10]
modelpaths_v=[modelpath_v_1,modelpath_v_2,modelpath_v_3,modelpath_v_4,modelpath_v_5,modelpath_v_6,modelpath_v_7,modelpath_v_8]

modelpath_piv_1='/data/wangh/hyperparametertuning_a0g/piv/66connect4data/bestmodels/bestmodel_66connect4_piv_run1'
modelpath_piv_2='/data/wangh/hyperparametertuning_a0g/piv/66connect4data/bestmodels/bestmodel_66connect4_piv_run2'
modelpath_piv_3='/data/wangh/hyperparametertuning_a0g/piv/66connect4data/bestmodels/bestmodel_66connect4_piv_run3'
modelpath_piv_4='/data/wangh/hyperparametertuning_a0g/piv/66connect4data/bestmodels/bestmodel_66connect4_piv_run4'
modelpath_piv_5='/data/wangh/hyperparametertuning_a0g/piv/66connect4data/bestmodels/bestmodel_66connect4_piv_run5'
modelpath_piv_6='/data/wangh/hyperparametertuning_a0g/piv/66connect4data/bestmodels/bestmodel_66connect4_piv_run6'
modelpath_piv_7='/data/wangh/hyperparametertuning_a0g/piv/66connect4data/bestmodels/bestmodel_66connect4_piv_run7'
modelpath_piv_8='/data/wangh/hyperparametertuning_a0g/piv/66connect4data/bestmodels/bestmodel_66connect4_piv_run8'
modelpath_piv_9='/data/wangh/hyperparametertuning_a0g/piv/66connect4data/bestmodels/bestmodel_66connect4_piv_run9'
modelpath_piv_10='/data/wangh/hyperparametertuning_a0g/piv/66connect4data/bestmodels/bestmodel_66connect4_piv_run10'
#modelpaths_piv={modelpath_piv_1,modelpath_piv_2,modelpath_piv_3,modelpath_piv_4,modelpath_piv_5,modelpath_piv_6,modelpath_piv_7,modelpath_piv_8,modelpath_piv_9,modelpath_piv_10}
modelpaths_piv=[modelpath_piv_1,modelpath_piv_2,modelpath_piv_3,modelpath_piv_4,modelpath_piv_5,modelpath_piv_6,modelpath_piv_7,modelpath_piv_8]

player_pi_v_list=[]
player_pi_list=[]
player_v_list=[]
player_piv_list=[]

g=Connect4Game(6,6,4,None)

# base players
rp = RandomPlayer(g).play

# nnet players
for i in range(len(modelpaths_pi_v)):
    nnt_pi_v = NNetpi_v(g)
    nnt_pi_v.load_checkpoint(modelpaths_pi_v[i],'best.pth.tar')
    args_pi_v = dotdict({'numMCTSSims': 100, 'cpuct':1.0})
    mcts_pi_v = MCTS(g, nnt_pi_v, args_pi_v)
    nnt_pi_v_player = lambda x: np.argmax(mcts_pi_v.getActionProb(x, temp=0))
    player_pi_v_list.append(nnt_pi_v_player)
player_pi_v_list=np.array(player_pi_v_list)

for i in range(len(modelpaths_pi)):
    nnt_pi = NNetpi(g)
    nnt_pi.load_checkpoint(modelpaths_pi[i],'best.pth.tar')
    args_pi = dotdict({'numMCTSSims': 100, 'cpuct':1.0})
    mcts_pi = MCTS(g, nnt_pi, args_pi)
    nnt_pi_player = lambda x: np.argmax(mcts_pi.getActionProb(x, temp=0))
    player_pi_list.append(nnt_pi_player)
player_pi_list=np.array(player_pi_list)

for i in range(len(modelpaths_v)):
    nnt_v = NNetv(g)
    nnt_v.load_checkpoint(modelpaths_v[i],'best.pth.tar')
    args_v = dotdict({'numMCTSSims': 100, 'cpuct':1.0})
    mcts_v = MCTS(g, nnt_v, args_v)
    nnt_v_player = lambda x: np.argmax(mcts_v.getActionProb(x, temp=0))
    player_v_list.append(nnt_v_player)
player_v_list=np.array(player_v_list)


for i in range(len(modelpaths_piv)):
    nnt_piv = NNetpiv(g)
    nnt_piv.load_checkpoint(modelpaths_piv[i],'best.pth.tar')
    args_piv = dotdict({'numMCTSSims': 100, 'cpuct':1.0})
    mcts_piv = MCTS(g, nnt_piv, args_piv)
    nnt_piv_player = lambda x: np.argmax(mcts_piv.getActionProb(x, temp=0))
    player_piv_list.append(nnt_piv_player)
player_piv_list=np.array(player_piv_list)

arenacomparison=20

whiteplayer=rp
for i,blackplayer in enumerate(player_pi_v_list):
    #blackplayer=player_pi_v_list[i]
    arena_white_black= Arena.Arena(whiteplayer, blackplayer, g, display=display)
    print('wanghui|randomplayer|bestmodel_pi_v_run'+str(i)+'|')
    print('wanghuiscore',arena_white_black.playGames(arenacomparison, verbose=False))
for k,blackplayer in enumerate(player_pi_list):
    #blackplayer=player_pi_list[k]
    arena_white_black= Arena.Arena(whiteplayer, blackplayer, g, display=display)
    print('wanghui|randomplayer|bestmodel_pi_run'+str(k)+'|')
    print('wanghuiscore',arena_white_black.playGames(arenacomparison, verbose=False))
for l,blackplayer in enumerate(player_v_list):
    #blackplayer=player_v_list[l]
    arena_white_black= Arena.Arena(whiteplayer, blackplayer, g, display=display)
    print('wanghui|randomplayer|bestmodel_v_run'+str(l)+'|')
    print('wanghuiscore',arena_white_black.playGames(arenacomparison, verbose=False))
for m,blackplayer in enumerate(player_piv_list):
    #blackplayer=player_piv_list[m]
    arena_white_black= Arena.Arena(whiteplayer, blackplayer, g, display=display)
    print('wanghui|randomplayer|bestmodel_piv_run'+str(m)+'|')
    print('wanghuiscore',arena_white_black.playGames(arenacomparison, verbose=False))

for i in range(len(player_pi_v_list)):
    whiteplayer=player_pi_v_list[i]
    for j in range(i+1,len(player_pi_v_list)):
        blackplayer=player_pi_v_list[j]
        arena_white_black= Arena.Arena(whiteplayer, blackplayer, g, display=display)
        print('wanghui|bestmodel_pi_v_run'+str(i) + '|bestmodel_pi_v_run'+str(j)+'|')
        print('wanghuiscore',arena_white_black.playGames(arenacomparison, verbose=False))
    for k in range(len(player_pi_list)):
        blackplayer=player_pi_list[k]
        arena_white_black= Arena.Arena(whiteplayer, blackplayer, g, display=display)
        print('wanghui|bestmodel_pi_v_run'+str(i) + '|bestmodel_pi_run'+str(k)+'|')
        print('wanghuiscore',arena_white_black.playGames(arenacomparison, verbose=False))
    for l in range(len(player_v_list)):
        blackplayer=player_v_list[l]
        arena_white_black= Arena.Arena(whiteplayer, blackplayer, g, display=display)
        print('wanghui|bestmodel_pi_v_run'+str(i)+ '|bestmodel_v_run'+str(l)+'|')
        print('wanghuiscore',arena_white_black.playGames(arenacomparison, verbose=False))
    for m in range(len(player_piv_list)):
        blackplayer=player_piv_list[m]
        arena_white_black= Arena.Arena(whiteplayer, blackplayer, g, display=display)
        print('wanghui|bestmodel_pi_v_run'+str(i) + '|bestmodel_piv_run'+str(m)+'|')
        print('wanghuiscore',arena_white_black.playGames(arenacomparison, verbose=False))

for i in range(len(player_pi_list)):
    whiteplayer=player_pi_list[i]
    for j in range(i+1,len(player_pi_list)):
        blackplayer=player_pi_list[j]
        arena_white_black= Arena.Arena(whiteplayer, blackplayer, g, display=display)
        print('wanghui|bestmodel_pi_run'+str(i)+ '|bestmodel_pi_run'+str(j)+'|')
        print('wanghuiscore',arena_white_black.playGames(arenacomparison, verbose=False))
    for l in range(len(player_v_list)):
        blackplayer=player_v_list[l]
        arena_white_black= Arena.Arena(whiteplayer, blackplayer, g, display=display)
        print('wanghui|bestmodel_pi_run'+str(i) + '|bestmodel_v_run'+str(l)+'|')
        print('wanghuiscore',arena_white_black.playGames(arenacomparison, verbose=False))
    for m in range(len(player_piv_list)):
        blackplayer=player_piv_list[m]
        arena_white_black= Arena.Arena(whiteplayer, blackplayer, g, display=display)
        print('wanghui|bestmodel_pi_run'+str(i) + '|bestmodel_piv_run'+str(m)+'|')
        print('wanghuiscore',arena_white_black.playGames(arenacomparison, verbose=False))

for i in range(len(player_v_list)):
    whiteplayer=player_v_list[i]
    for j in range(i+1,len(player_v_list)):
        blackplayer=player_v_list[j]
        arena_white_black= Arena.Arena(whiteplayer, blackplayer, g, display=display)
        print('wanghui|bestmodel_v_run'+str(i) + '|bestmodel_v_run'+str(j)+'|')
        print('wanghuiscore',arena_white_black.playGames(arenacomparison, verbose=False))
    for m in range(len(player_piv_list)):
        blackplayer=player_piv_list[m]
        arena_white_black= Arena.Arena(whiteplayer, blackplayer, g, display=display)
        print('wanghui|bestmodel_v_run'+str(i) + '|bestmodel_piv_run'+str(m)+'|')
        print('wanghuiscore',arena_white_black.playGames(arenacomparison, verbose=False))

for i in range(len(player_piv_list)):
    whiteplayer=player_piv_list[i]
    for j in range(i+1,len(player_piv_list)):
        blackplayer=player_piv_list[j]
        arena_white_black= Arena.Arena(whiteplayer, blackplayer, g, display=display)
        print('wanghui|bestmodel_piv_run'+str(i) + '|bestmodel_piv_run'+str(j)+'|')
        print('wanghuiscore',arena_white_black.playGames(arenacomparison, verbose=False))



