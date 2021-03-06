from Coach import Coach
from connect4.Connect4Game import Connect4Game as Game
from connect4.tensorflow.NNet import NNetWrapper as nn
from utils import *

args = dotdict({
    'numIters':200, #1000,
    'numEps': 50, #100,
    'tempThreshold': 15,
    'updateThreshold': 0.6,
    'maxlenOfQueue': 200000,
    'numMCTSSims': 100,
    'arenaCompare': 40,
    'cpuct': 1,

    'checkpoint': './temp/',
    'load_model': False,
    'load_folder_file': ('/dev/models/8x100x50','best.pth.tar'),
    'numItersForTrainExamplesHistory': 20,

})

if __name__=="__main__":
    g = Game(5,5,4,None)
    nnet = nn(g)

    if args.load_model:
        nnet.load_checkpoint(args.load_folder_file[0], args.load_folder_file[1])

    c = Coach(g, nnet, args)
    if args.load_model:
        print("Load trainExamples from file")
        c.loadTrainExamples()
    c.learn()
