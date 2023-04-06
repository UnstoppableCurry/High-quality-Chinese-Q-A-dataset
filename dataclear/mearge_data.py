import glob

from itertools import islice

inputfile_dir = '/root/shellLearning/Pytorch/day_08_TaskBot/neo4j/splitBigdata2/en'
inputfile_dir2 = '/root/shellLearning/Pytorch/day_08_TaskBot/neo4j/splitBigdata2/real'
outputfile = '/root/shellLearning/Pytorch/day_08_TaskBot/neo4j/relationship.csv'

csv_list = glob.glob(inputfile_dir2 + '/*.csv')
print(u'共发现%s个CSV文件' % len(csv_list))
print(u'正在处理............')
for i in csv_list:  # 循环读取同文件夹下的csv文件
    fr = open(i, 'rb').read()
    with open(outputfile, 'ab') as f:  # 将结果保存为result.csv
        f.write(fr)

print(u'合并完毕！')
