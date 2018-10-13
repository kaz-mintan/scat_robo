# coding:utf-8

import numpy as np

class Score:
    def __init__(self, filename):
        self.score=np.loadtxt(filename,delimiter=",")

    def get_state(self,episode):
        code_array=np.array([
                self.score[episode,0],
                self.score[episode,1]])
        code_array=code_array-np.ones_like(code_array)
        return code_array

if __name__ == '__main__':
    code_reader=Score("score.csv")
    for i in range(12):
        code_array=code_reader.get_state(i)
        print(i,code_array)
