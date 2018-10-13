# coding:utf-8
# http://neuro-educator.com/rl1/

import numpy as np
import random
from read_score import *
from reward_calc import *

def argmax_ndim(arg_array):
    return np.unravel_index(arg_array.argmax(), arg_array.shape)


num_episodes = 12  #number of all trials

state_num = 2
action_num = 3 * 2

gamma = 0.9
alpha = 0.5

epsilon = 0.1
mu = 0.9
epoch = 1000

# [5] main tourine
state = np.zeros((state_num,num_episodes))
state_before = np.zeros_like(state) #for delta mode

action = np.zeros((action_num,num_episodes))
reward = np.zeros(num_episodes)
random = np.zeros(num_episodes)

val_range=np.array([4,4,3,3,2,3,3,2])

#q_table = np.zeros(tuple(val_range))
q_table=np.load("q_table.npy")


score=Score("score.csv")

past_state=score.get_state(0)
# main loop
for episode in range(num_episodes-1):
    #set state
    state[:,episode]=score.get_state(episode)

    ### calcurate a_{t} based on s_{t}

    ran=np.random.rand()
    if ran>0.3:
        action[:,episode]=argmax_ndim(q_table[int(state[0,episode]),
                            int(state[1,episode]),:,:,:,:,:,:])
                            #+np.ones_like(action[:,episode])
    else:
        print("random selected")
        for i in range(action_num):
              action[i,episode]=np.random.randint(val_range[i]-1)

    print(episode,"action",action[:,episode])

    #make list of stat_t and action_t
    stack=np.hstack((state[:,episode],action[:,episode]))
    #stack=stack-np.ones_like(stack)
    qt_list=tuple(stack.astype(np.int).tolist())

    state[:,episode+1]=score.get_state(episode+1)
    past_state=state[:,episode+1]

    action_predict=argmax_ndim(q_table[int(state[0,episode+1]),
                            int(state[1,episode+1]),:,:,:,:,:,:])

    #make list of stat_t+1 and action_t+1
    stack=np.hstack((state[:,episode+1],action_predict))
    #stack=stack-np.ones_like(stack)
    preq_list=tuple(stack.astype(np.int).tolist())

    dummy_reward=[4,2,3,1,5,4,3,1,2,3,4,3]
    reward[episode] = get_reward(dummy_reward,episode)
    #here to input face photos

    q_table[qt_list]+=alpha*(reward[episode]+gamma*q_table[preq_list]-q_table[qt_list])

    #sing(action[:,episode])
np.save("q_table.npy",q_table)
