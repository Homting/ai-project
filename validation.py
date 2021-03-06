import toolkit as tk
import pandas as pd
import numpy as np
from AI_knn import *
from AI_id3 import *
from naivebayes.naive_bayes import *

# Leave one out procedure

# leave one out from dataset

def leave_1_ins(dataset, index):
    '''
    pop the dataset[index] out
    :param dataset: matrix
    :return: (dataset, one sample)
    '''
    ins = dataset[index, :]
    remain_dataset = np.delete(dataset, index, 0)
    return ins, remain_dataset


def cross_vali_split_data(dataset, cv=10):
    '''
    :param dataset: type matrix
    :param cv: the number of validation fold
    :return: K-1 length list contain the dataset
    '''
    # 向下取整
    size = int(np.floor(len(dataset) / cv))
    result = []
    begin = 0
    end = size
    for i in range(cv - 1):
        testset = dataset[begin:end, :]
        trainset = np.row_stack((dataset[0:begin, :], dataset[end:, :]))
        begin = end
        end = end + size
        result.append([trainset, testset])
    result.append([ dataset[:begin, :],dataset[begin:, :]])
    return result


def accuracy_score(right, predict):
    num = 0
    for i in range(len(right)):
        if right[i] == predict[i]:
            num += 1
    return num / len(right)


def kappa(predict, right,classi):
    #TP, FP, FN, TN = 0, 0, 0, 0
    a,b, c, d = 0, 0, 0, 0
    for i in range(len(predict)):
        if predict[i] == classi:
            if right[i] == classi:
                a += 1
            else:
                b += 1
        else:
            if right[i] == classi:
                c += 1
            else:
                if predict[i]==right[i]:
                    d += 1
    print(a,b,c,d)
    kappa = ((a+d)/(a+b+c+d)-((a+c)*(a+b)+(b+d)*(c+d))/(a+b+c+d)**2)/(1.0-((a+c)*(a+b)+(b+d)*(c+d))/(a+b+c+d)**2)

    return kappa


# test cross validation
att, x = tk.readDataSet("./iris.csv")
a = cross_vali_split_data(x, 16)
right1 = x[:,-1]
pre = []
#for i in a:
 #   res = knn(att,i[0])
  #  for i in res.getPrediction(i[1])[1]:
   #     pre.append(i)



def cross(model,attr,dataset,cvfold=10):
    np.random.shuffle(dataset)
    right = dataset[:,-1]
    train_test_pair_list = cross_vali_split_data(dataset,cvfold)
    prediction = []
    if model==id3:
        for train_test in train_test_pair_list:
            mod = model(list(attr),(train_test[0]).tolist())
            for i in mod.getPrediction(train_test[1].tolist())[1]:
                prediction.append(i)
    else:
        for train_test in train_test_pair_list:
            mod = model(attr,train_test[0])
            for i in mod.getPrediction(train_test[1])[1]:
                prediction.append(i)
    #print(right)
    #print(prediction)
    score = accuracy_score(right,prediction)
    return score,right,prediction


att, x = tk.readDataSet("./iris.csv")

a,right,pre = cross(id3,att,x,10)
a,right,pre = cross(knn,att,x,10)

car_attr,car = tk.readDataSet("./car.csv")
#a,right,pre = cross(Naive_bayes,car_attr,car)

def kappa_dict(predict,right):
    key_list = []
    for i in right:
        if i in key_list:
            pass
        else:
            key_list.append(i)

    k_value = {}
    for i in key_list:
        k_value[i] = kappa(predict,right,i)
    return k_value

print(kappa_dict(pre,right))


def classify_map(predict,right):
    key_list = []
    for i in right:
        if i in key_list:
            pass
        else:
            key_list.append(i)

    map_dict = {}
    for i in key_list:
        dict_t ={}
        for j in key_list:
            dict_t[j] = 0
        map_dict[i] = dict_t
    for i in range:
        map = pd.DataFrame(map_dict)
    return map

#print(classify_map(pre,right))






