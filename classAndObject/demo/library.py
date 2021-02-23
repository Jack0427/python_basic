# class Base:
# 寫好給子類用
# def read(self):
#     print('call read....')

# def write(self):
#     print('call write....')

# 抽象類
from abc import ABCMeta, abstractclassmethod


class Base(metaclass=ABCMeta):
    @abstractclassmethod
    def read(self):
        pass

    @abstractclassmethod
    def write(self):
        pass
