# -*- coding = utf-8 -*-
# @Time : 2021/5/19 17:38
# @Author : Hermit 
# @Fill : FindPath.py
# @software : PyCharm
'''
Please run this script to  find the path using A star algorithm
BW means black and white
x0 means the original resolution
x2 means the 0.5 size resolution
x4 means the 0.25 size resolution
'''
import time
from typing import Tuple, Dict, Optional
from PIL import Image # this module is for reading the map
import numpy as np
from Map import Map
from PriorityQueue import PriorityQueue

GridLocation = Tuple[int, int]
Location = Tuple[int, int]


def readMap(path):
    img = Image.open(path).convert('L')
    img = np.array(img)  #打开图像并转化为数字矩阵
    return img


def heuristic(a: GridLocation, b: GridLocation) -> float:
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(graph, start: Location, goal: Location):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from: Dict[Location, Optional[Location]] = {}
    cost_so_far: Dict[Location, float] = {}
    came_from[start] = None# 起点
    cost_so_far[start] = 0

    while not frontier.empty():
        current: Location = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next, goal)
                frontier.put(next, priority)
                came_from[next] = current
    # print("end Navi")
    return came_from, cost_so_far

def showRoute(map,came_fromDir:Dict,goal:Tuple):
    key = goal
    route = []
    route.append(goal)

    while(came_fromDir[key]!= None):
        cor = came_fromDir[key]
        route.append(cor)
        key = cor
    for cor in route:
        map[cor[0]][cor[1]] = 125

    return  map ,route

def EuclideanDistance(P1,P2):
    return np.sqrt((P1[0]-P2[0])**2 + (P1[1]-P2[1])**2 )


def calDistance(routineList):
    res = 0
    for index in range(len(routineList)-1):
        res += EuclideanDistance(routineList[index],routineList[index+1])
    return res

if __name__ =="__main__":
    startTime = time.time()
    path = r'PRDCSG_FloorplanBWx4.png' # change this path to select the map image
    mapArr = readMap(path)
    myMap = Map(mapArr)
    # myMap.show()
    start = [5,5] # start point  (x,y)
    end = [143,69] # end point
    #reverse for arr index
    start.reverse()
    end.reverse()
    # convert to tuple for speeding up
    start = tuple(start)
    end = tuple(end)
    if(myMap.passable(start) and myMap.passable(end)):
        came_from,t_so_far = a_star_search(myMap,start,end)
        try:
            resMap,route = showRoute(mapArr,came_from,end)
            print(calDistance(route))
            myResMap = Map(resMap)
            endTime = time.time()
            print(endTime - startTime)
            myResMap.show()
        except KeyError:
            print("The end point is not assessable!")

    else:
        if(not myMap.passable(start)):
            print("the start point you select is not passable!")
        if (not myMap.passable(end)):
            print("the end point you select is not passable!")
