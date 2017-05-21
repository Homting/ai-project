#!/usr/local/bin/python3
# File Name: main_kmeans.py
# Author: Jin LI
# mail: jin.li@vub.ac.be; homtingli@gmail.com
# Created Time: 2017-05-21 00:22:24

import toolkit as tk 
import numpy as np 
from AI_kmeans import kmeans 

attributes,instences = tk.readDataSet("dataset/iris.txt")

#for this one, instences = trainSet + testSet
#trainSet,testSet = tk.splitDataSet(instences,0.8)

mykmeans = kmeans(attributes,instences,3)
mykmeans.training()

mykmeans.getResult()