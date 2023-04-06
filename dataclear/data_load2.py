import pandas as pd
import time

# 记录开始时间
start = time.time()

# 常量定义
ENTITY_LABEL = 'ENTITY'
ENTITY_LABEL_1 = 'ENTITY1'
TYPE = 'RELATIONSHIP'
filePath = '/root/neo4j_dataSet/metaData/ownthinData.csv'
output1 = '/root/shellLearning/Pytorch/day_08_TaskBot/neo4j/splitBigdata2'
# 读取文件
file = pd.read_csv(filePath, iterator=True, chunksize=1000000, encoding="utf_8")
# 定义转存结构s
entity_map = {":ID": [], "name": [], ':LABEL': []}
rel_map = {":START_ID": [], "name": [], ':END_ID': [], ":TYPE": []}
# 记录当前实体
current_entity_name = ''
current_entity_id = ''
# 循环计次
j = 1
i = 1

# 循环
print('开始第{}次写入'.format(j))
for chunk in file:
    for _, row in chunk.iterrows():
        if current_entity_name != row['实体']:
            current_entity_name = str(row['实体']).replace('\r', '').replace('\n', '')
            current_entity_id = 'entity' + str(i) + 'e'
            entity_map[':ID'].append(current_entity_id)
            entity_map['name'].append(current_entity_name)
            entity_map[':LABEL'].append(ENTITY_LABEL)
        entity_map[':ID'].append('entity' + str(i))
        entity_map['name'].append(str(row['值']).replace('\r', '').replace('\n', ''))
        entity_map[':LABEL'].append(ENTITY_LABEL_1)
        rel_map[':START_ID'].append(current_entity_id)
        rel_map['name'].append(str(row['属性']).replace('\r', '').replace('\n', ''))
        rel_map[':END_ID'].append('entity' + str(i))
        rel_map[':TYPE'].append(TYPE)
        if i % 1000000 == 0:
            if j == 1:
                pd.DataFrame(entity_map, columns=[":ID", "name", ':LABEL']) \
                    .to_csv(output1 + '/en/entity{}.csv'.format(j), encoding="utf_8_sig", index=False)
                pd.DataFrame(rel_map, columns=[":START_ID", "name", ':END_ID', ":TYPE"]) \
                    .to_csv(output1 + '/real/rel{}.csv'.format(j), encoding="utf_8_sig", index=False)
            else:
                pd.DataFrame(entity_map, columns=[":ID", "name", ':LABEL']) \
                    .to_csv(output1 + '/en/entity{}.csv'.format(j), encoding="utf_8_sig", index=False, header=False)
                pd.DataFrame(rel_map, columns=[":START_ID", "name", ':END_ID', ":TYPE"]) \
                    .to_csv(output1 + '/real/rel{}.csv'.format(j), encoding="utf_8_sig", index=False, header=False)
            entity_map = {":ID": [], "name": [], ':LABEL': []}
            rel_map = {":START_ID": [], "name": [], ':END_ID': [], ":TYPE": []}
            j += 1
            print('开始第{}次写入'.format(j))
        i += 1

pd.DataFrame(entity_map, columns=[":ID", "name", ':LABEL']) \
    .to_csv(output1 + '/en/entity{}.csv'.format(j + 1), encoding="utf_8_sig", index=False)
pd.DataFrame(rel_map, columns=[":START_ID", "name", ':END_ID', ":TYPE"]) \
    .to_csv(output1 + '/en/rel{}.csv'.format(j + 1), encoding="utf_8_sig", index=False)
print('运行时间{}'.format(time.time() - start))
