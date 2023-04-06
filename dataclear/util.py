import pandas as pd
import numpy as np
from multiprocessing import cpu_count, Pool

# 计算当前服务器CPU的数量
cores = cpu_count()
# 将分块个数设置为CPU的数量
partitions = cores
print(cores)


def parallelize(df, func):
    # 数据切分
    data_split = np.array_split(df, int(partitions))
    # 初始化线程池
    pool = Pool(cores)
    # 数据分发, 处理, 再合并
    # print(pool.map(func, data_split))
    pool.map(func, data_split)
    # 关闭线程池
    pool.close()
    # 执行完close后不会有新的进程加入到pool, join函数等待所有子进程结束
    pool.join()
    # 返回处理后的数据


