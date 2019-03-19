# lossfunctionfora0g
source code of different loss function optimizations for alphazero general and corresponding scripts for dealing with the training log files and bestmodels

Generally: 
The training part code is maily from the open source code from Alphazero General project, details see: https://github.com/suragnair/alpha-zero-general. 
We considered not to upload this part code, however, in order to do our experiments, we made a lot of changes, which are necessary for our data processing 
and elo computation. So we choose to also upload this part code. Importantly, we wrote scripts to deal with the data from training outputs files. Not only 
the training loss, but also based on arena comparison data, using bayesian elo system (following alphago series papers. see https://github.com/ddugovic/BayesianElo)
to compute elo ratings. Our scripts show how to transfer arena comparison data into .pgn file which is the input of bayesian elo system. Our scripts also extend for 
the best final players round-robin tournament. We suggest this tournament elo rating to compare the playing strength rather than the elo rating only based on self-play training. 
Besides, we provide examples of visualization for loss and elo ratings.

Our experiments mainly aims to assess the effect of different loss functions. see for example othello/tensorflow/OthelloNNet.py
####
self.loss_pi =  tf.losses.softmax_cross_entropy(self.target_pis, self.pi)
        self.loss_v = tf.losses.mean_squared_error(self.target_vs, tf.reshape(self.v, shape=[-1,]))
        self.total_loss = self.loss_pi + self.loss_v
        update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
        with tf.control_dependencies(update_ops):
            self.train_step = tf.train.AdamOptimizer(self.args.lr).minimize(self.total_loss)
####

In our experiments, we change "self.total_loss" in self.train_step = tf.train.AdamOptimizer(self.args.lr).minimize(self.total_loss) to self.loss_v, self.loss_pi, loss_v*loss_pi
Scripts related to training log files can only be run directly with log files input. 
Scripts realtes to best models can only be run with bestmodels.
Unfortunately, these files are too big to upload.

Some further improvements will be updated soon~

