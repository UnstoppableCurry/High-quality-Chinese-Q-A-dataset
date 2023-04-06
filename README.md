# High-quality-Chinese-Q-A-dataset
最大开源中文问答数据集 ,助力中文LLM.The largest open-source Chinese Q&amp;A dataset, supporting Chinese LLM

此项目通过清洗ownthink_v2 知识图谱三元组数据来实现 Q&A数据 以及Prompt qa 多轮 COT数据
  - 原始数据 Example
    -  ![image](https://user-images.githubusercontent.com/65523997/230326683-6175c2e8-ee27-4008-b71e-eb4f5e29f594.png)
    - ![image](https://user-images.githubusercontent.com/65523997/230321437-e89f0e6f-fa68-417c-89df-a6f1381a32e6.png) 
    - ownthink 数据共有 1.5亿行左右的 关系实体三元组数据, 若做成neo4j数据库 基本等价于简易版的百度百科或维基百科
    - 有些特殊的关系与实体难以构造通顺语句 此项工作需要更细致的清洗工作,但不影响此为一个高质量知识库数据集

  - Q&A 数据 Example
    - ![image](https://user-images.githubusercontent.com/65523997/230324020-5a481e73-420c-48fd-9eb3-2ef2491ab969.png)
    - 下载链接：https://pan.baidu.com/s/1JnRp8orT8kAIjAoZI9QA4g?pwd=kbge 提取码：kbge 
    - 做法 1.拼接三元组数据构造QA数据 2.将数据shuffle
  
  - Q&A & Cot Prompt 数据
    - 1轮shuffle 数据下载链接：https://pan.baidu.com/s/1K1rCqOmJ0ZsUd4FFY6z4rg?pwd=fw69 提取码：fw69 
    - 50轮 shuffle 数据下载链接：https://pan.baidu.com/s/1MF-QJTLOXpvuzrGxt0GQiw?pwd=ctou 提取码：ctou 
    - ![image](https://user-images.githubusercontent.com/65523997/230334017-121df4a8-a991-43b8-b1fe-775cd88ad287.png)
    - 上图整理了一下\n 与 \t 为了方便理解 真实数据格式如下
      - q:什么是梨果寄生属？\n  a:我们可以这样做, 先考虑一下我们知道梨果寄生属的什么信息？\n 我们知道:\n\t0. 如何描述梨果寄生属。\n\t1. 梨果寄生属的中文学名。\n\t2. 梨果寄生属的拉丁学名。\n\t3. 梨果寄生属的界。\n\t4. 梨果寄生属的科。\n\t5. 梨果寄生属的物种数量。\n\t6. 梨果寄生属的中国植物志。\n\t7. 梨果寄生属的标签。\n那么很显然答案是\n\t0. 这样描述其梨果寄生属，分布于亚洲东南部和南部，我国产11种，其中红花寄生S. parasitica L. 供药用。\n\t1. 其中文学名是梨果寄生属。\n\t2. 其拉丁学名是Scurrula L.。\n\t3. 其界是植物界。\n\t4. 其科是桑寄生科。\n\t5. 其物种数量是约60种。\n\t6. 其中国植物>志是24:108。\n\t7. 梨果寄生属的标签可以是自然,生物物种,植物。\n

- 本人使用rwkv 1B5 微调了少量 Cot Q&A数据
  - 发现 少量的prompt cot数据进行LORA 模型拥有良好的zeroshot能力,将原有知识能力迁移到微调任务中

- 如果想要加入此项目一起贡献欢迎发邮箱 294957500@qq.com 此诚存亡之秋,期望大家一起努力构建中文数据集




  


