import sys
import csv
import pandas as pd

filePath = '/root/neo4j_dataSet/ownthinkV2'
outputPath = '/root/shellLearning/Pytorch/day_08_TaskBot/neo4j/splitBigdata'


#
# def split_data():
#     with open(filePath, "r", encoding="utf-8") as csvFile:
#         reader = csv.reader(csvFile)
#         for index, read in enumerate(reader):
#             i = 0
#             if index / 5636791 == 0:
#                 filename = 'splitBigdata/csvSplit' + str(i) + '.csv'
#                 i += 1
#                 f = open(filename, 'a+', encoding='utf-8', newline='')
#                 csv_writer = csv.writer(f, delimiter='\t')
#                 write = csv_writer.writerow(read)
#             f.close()


# 需要内存大小为318.3814  16g内存切片 处理数据
def split_datasets(path):
    '''
    读取结构化数据 加载到内存中
    :param path:
    :return:
    '''
    import os
    import fileinput

    disease_csv_list = os.listdir(path)
    # 获取文件名称列表
    for i in disease_csv_list:
        pt = filePath + '/' + i
        clearAndWrite(pt, i, outputPath)


def clearAndWrite(path, i, outputPath):
    with open(path, "r", encoding="utf-8") as csvFile:
        reader = csv.reader(csvFile)
        try:
            for index, read in enumerate(reader):
                f = open(outputPath + '/' + i, 'a+', encoding='utf-8', newline='')
                csv_writer = csv.writer(f, delimiter='\t')
                write = csv_writer.writerow(read)
                f.close()
        except:
            print(index, '为null')


# -*- coding: utf-8 -*-
# -------------------------------
# Name:dataProcessing.py
# Author:Nieson
# Date:2019-10-25 17:31
# -------------------------------
def createData2neo4j(n_r_b, le):
    # 读取三元组文件
    # n_r_b_name = [":START_ID", "relationship", ":END_ID"]
    # n_r_b = pd.read_csv("/root/neo4j_dataSet/ownthinkV2/ownthinData_0025.csv", sep=',', names=n_r_b_name)  # 使用少量的测试数据
    # n_r_b = pd.read_csv(path, sep=',', names=n_r_b_name)  # 使用少量的测试数据
    # n_r_b = pd.read_csv(filePath, sep=',', names=n_r_b_name)  # 使用全量的数据
    print(n_r_b.info())
    # print(n_r_b.head())
    n_r_b = n_r_b.dropna()

    # 去除重复实体
    entity = set()
    entity_n = n_r_b[':START_ID'].tolist()
    entity_b = n_r_b[':END_ID'].tolist()
    for i in entity_n:
        entity.add(i)
    for i in entity_b:
        entity.add(i)
    # print(entity)

    # 保存节点文件-entity.csv
    csvf_entity = open("entityE.csv", "a+", newline='', encoding='utf-8')
    w_entity = csv.writer(csvf_entity)
    # 实体ID，要求唯一，名称，LABEL标签，可自己不同设定对应的标签
    if le == 0:
        w_entity.writerow(("entity:ID", "name", ":LABEL"))
    entity = list(entity)
    entity_dict = {}
    for i in range(len(entity)):
        w_entity.writerow(("e" + str(le + i), entity[i], "my_entity"))
        entity_dict[entity[i]] = "e" + str(le + i)
    csvf_entity.close()
    # 生成关系文件-relationship.csv
    # 起始实体ID，终点实体ID，要求与实体文件中ID对应，:TYPE即为关系
    x = n_r_b.copy()
    # print(entity_dict)
    x.loc[:, ':START_ID'] = x.loc[:, ':START_ID'].map(entity_dict)
    x.loc[:, 'name'] = x.loc[:, 'relationship']
    x.loc[:, ':END_ID'] = x.loc[:, ':END_ID'].map(entity_dict)
    x.loc[:, ':TYPE'] = x.loc[:, 'relationship']
    x.pop('relationship').dropna()
    # n_r_b[':START_ID'] = n_r_b[':START_ID'].map(entity_dict)
    # n_r_b['name'] = n_r_b['relationship']
    # n_r_b[':END_ID'] = n_r_b[':END_ID'].map(entity_dict)
    # n_r_b[":TYPE"] = n_r_b['relationship']
    # n_r_b.pop('relationship')
    if le != 0:
        x.to_csv("relationshipE.csv", index=False, mode='a', header=False)
    else:
        x.to_csv("relationshipE.csv", index=False, mode='a')
    le += len(entity)
    '''
    relationship head :START_ID,:END_ID,name,:TYPE
    entity.csv head  entity:ID,name,:LABEL
    '''
    return le


def create_neo4j_meta_Data(path):
    import os
    from util import parallelize
    disease_csv_list = os.listdir(path)
    length = 0
    for i in disease_csv_list:
        # print(path + i)
        n_r_b_name = [":START_ID", "relationship", ":END_ID"]
        n_r_b = pd.read_csv(path + '/' + i, sep='\t', names=n_r_b_name)  # 使用少量的测试数据
        # parallelize(n_r_b, createData2neo4j)
        length = createData2neo4j(n_r_b, length)
        print('index不再重复后下标的值', length)


def demo():
    path = '/root/shellLearning/Pytorch/day_08_TaskBot/neo4j/relationship.csv'
    path2 = '/root/shellLearning/Pytorch/day_08_TaskBot/neo4j/relationship2.csv'
    csvf_entity = open(path2, "a+", newline='', encoding='utf-8')
    w_entity = csv.writer(csvf_entity)
    w_entity.writerow((':START_ID', ':END_ID', 'name', ':TYPE'))
    dict1 = {}
    df = pd.read_csv(path)
    print(df)
    lists = []
    c = 0
    for st in df.values:
        if st[0] in dict1.keys():
            dict1[st[0]] += 1
        else:
            dict1[st[0]] = 1
        if st[1] in dict1.keys():
            dict1[st[1]] += 1
        else:
            dict1[st[1]] = 1
        if dict1[st[0]] < 65535 and dict1[st[1]] < 65535:
            # lists.append(st)
            w_entity.writerow((st[0], st[1], st[2], st[3]))
        c += 1
        print('进度为:-->', c)
    print(dict1)
    # df2 = pd.DataFrame(lists, columns=[':START_ID', ':END_ID', 'name', ':TYPE'])
    # df2.to_csv(path2, index=False, mode='a')


if __name__ == '__main__':
    # split_datasets(filePath)
    # createData2neo4j()
    # n_r_b_name = [":START_ID", "relationship", ":END_ID"]
    # n_r_b = pd.read_csv(outputPath + '/ownthinData_0001.csv', sep='\t', names=n_r_b_name)  # 使用少量的测试数据
    # parallelize(n_r_b, createData2neo4j)
    # c = createData2neo4j(n_r_b, 0)
    create_neo4j_meta_Data(outputPath)
    # demo()
