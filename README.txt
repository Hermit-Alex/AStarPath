Please run the FindPath.py for path.
Map.py and PriorityQueue.py is the support class for the A star algorithm.

PIL module is for read image into the np array.
to install please run the following command:

pip install pillow

since PIL is the name used in python 2.0+
In python 3.0+, the name of the module was changed in to pillow.

PRDCSG map is in 3 resolution:
x0 means the original resolution
x2 means the 0.5 size resolution
x4 means the 0.25 size resolution

process:
1 select the image map
2 input the start point and end point and check whether it is reachable.
3 run the FindPath.py