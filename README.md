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
    - ![image](https://user-images.githubusercontent.com/65523997/230326138-7b360181-a838-4ea6-a639-ddf25b79f880.png)
    - 上图整理了一下\n 与 \t 为了方便理解 真是数据格式如下
    - ![image](https://user-images.githubusercontent.com/65523997/230327435-225b1d8d-3db5-4122-aa6a-6fa185077521.png)
    - 1轮shuffle 数据下载链接：https://pan.baidu.com/s/1K1rCqOmJ0ZsUd4FFY6z4rg?pwd=fw69 提取码：fw69 
    - 50轮 shuffle 数据下载链接：https://pan.baidu.com/s/1MF-QJTLOXpvuzrGxt0GQiw?pwd=ctou 提取码：ctou 

- 本人使用rwkv 1B5 微调了少量 Cot Q&A数据
  - 发现 少量的prompt cot数据进行LORA 模型拥有良好的zeroshot能力,将原有知识能力迁移到微调任务中

- 如果想要加入此项目一起贡献欢迎发邮箱 294957500@qq.com 此诚存亡之秋,期望大家一起努力构建中文数据集




  


