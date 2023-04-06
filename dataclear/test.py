import pandas as pd

if __name__ == '__main__':
    path = '/root/shellLearning/Pytorch/day_08_TaskBot/neo4j/relationshipMAP.csv'
    df = pd.read_csv(path)
    print(df)
    dict = {}
    for i in df['name']:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict, len(dict))
    print(len(set(df['name'].tolist()))                                                                     )
