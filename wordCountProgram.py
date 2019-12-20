# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 18:09:11 2019

@author: helen
"""

from mrjob.job import MRJob
from mrjob.step import MRStep

class wordCount(MRJob):
        def steps(self):
                return [
                    MRStep(mapper_init=self.init_mapper,
                           mapper=self.mapper_get_uniquewords,
                           mapper_final=self.final_mapper,
                           reducer_final=self.final_reducer)
                       ]

        def final_reducer(self, key, value):
                yield key,sum(value)

        def init_mapper(self):
                self.check = []

        def final_mapper(self):
                for word in self.check:
                        yield word, 1

        def mapper_get_uniquewords(self, _, line):
                word = line.split("\n")[0].lower()
                print(word)
                if word not in self.check:
                        self.check.append(word)



if __name__ == '__main__':
        wordCount.run()
