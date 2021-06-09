# -*- coding = utf-8 -*-
# @Time : 2021/5/19 17:39
# @Author : Hermit 
# @Fill : Map.py
# @software : PyCharm
'''
This script define the Map class for search the route
'''
from typing import Tuple, Iterator, Dict
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

GridLocation = Tuple[int, int]
class Map:
    def __init__(self,mapArr:np.array):
        self.mapArr = mapArr
        self.width = mapArr.shape[0]
        self.height = mapArr.shape[1]
        self.weights: Dict[GridLocation, float] = {}

    # 判断该点是否再边界
    def in_bounds(self, cor: GridLocation) -> bool:
        (x,y) = cor
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self,cor:GridLocation) -> bool:
        (x, y) = cor
        return  self.mapArr[x][y] == 255

    def neighbors(self,cor:GridLocation) ->Iterator[GridLocation]:
        (x, y) = cor
        ngbs = [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]
        # see "Ugly paths" section for an explanation:
        if (x + y) % 2 == 0: ngbs.reverse()  # S N W E
        results = filter(self.in_bounds, ngbs)
        results = filter(self.passable, results)
        return results

    def cost(self, from_node: GridLocation, to_node: GridLocation) -> float:
        return self.weights.get(to_node, 1)


    #绘制地图
    def show(self):
        colors = ['black','red','white']
        cmap = mpl.colors.ListedColormap(colors)
        plt.figure()
        # colmap = self.colorMap()
        plt.imshow(self.mapArr,cmap=cmap, vmin=0, vmax=255)
        plt.axis('off')
        plt.imsave("test.png",self.mapArr,cmap = cmap)
        plt.show()
