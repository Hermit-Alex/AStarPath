# -*- coding = utf-8 -*-
# @Time : 2021/5/19 17:41
# @Author : Hermit 
# @Fill : PriorityQueue.py
# @software : PyCharm

'''
This script define the priority queue for a star
'''
import heapq
from typing import List, Tuple


class PriorityQueue:
    def __init__(self):
        self.elements: List[Tuple[float, Tuple]] = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item: Tuple, priority: float):
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> Tuple:
        return heapq.heappop(self.elements)[1]