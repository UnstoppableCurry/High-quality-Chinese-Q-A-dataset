import glob
import pandas as pd
import csv
from random import shuffle
from util import parallelize


def write(outputPath, input):
    output_f = open(outputPath, 'a+', encoding='utf-8', newline='')
    output_f.write(input)
    output_f.close()




def 多线程_qa(path):
    all_Data = set()
    outputPath = '/www/dataset/qa/epoch_50_all_qa_Data.txt'
    all_nothing = set()
    all_output_Data = []
    shuffle(path)

    for paths in path:
        fi = open(paths)
        lens = len(fi.readlines())
        with open(paths) as f:
            index = 0
            # lens=len(f.readlines())

            # Read current line and put content to line
            lines = f.readlines()
            # shuffle(lines)
            for line in lines:
                # print('进度为-->', index / lens)
                if index == 0:
                    index += 1
                    continue
                # print(line)
                line_list = line.split('\t')
                if len(line_list) < 3:
                    # print('error')
                    continue
                reshape = line_list[1]
                if '[' in line_list[0]:
                    nothing = line_list[0].split('[')[1].replace(']', '')
                    line_list[0] = line_list[0].split('[')[0]
                    if not all_nothing.__contains__(nothing):
                        # print(line_list[0], '*******', nothing)
                        # write(outputPath, line_list[0] + '是' + nothing + '\n')
                        all_output_Data.append(line_list[0] + '是' + nothing + '\n')
                        all_nothing.add(nothing)

                if reshape == '描述':
                    question = '如何描述' + line_list[0] + '？'
                    anwser = '这样描述' + line_list[0] + ' ' + line_list[2].replace('\n', '') + '。'

                else:
                    question = line_list[0] + '的' + reshape + '是什么？'
                    anwser = line_list[0] + '的' + reshape + '是' + line_list[2].replace('\n', '') + '。'
                # print(question, anwser)
                # Print the line
                # all_Data.add(reshape)
                # If there is no line exit from loop
                index += 1
                read = 'q:' + question + ' a:' + anwser + '\n'
                if len(all_output_Data) <= 100000:
                    all_output_Data.append(read)
                else:
                    shuffle(all_output_Data)
                    append_all_output_data = ''
                    for all_output_data in all_output_Data:
                        # print(all_output_data.replace('\\n', '\n').replace('\\t', '\t'))
                        append_all_output_data += all_output_data
                    write(outputPath, append_all_output_data)
                    all_output_Data = []
                # write(outputPath, read)
                # print(read)
                # with open(outputPath, 'a', 'utf8') as out_f:
                #     out_f.write(read)
                #     out_f.close()

    print('z done')

# if __name__ == '__main__':
    # epoch = 100
    # for i in range(epoch):
    #     print('进度为-->', i)
    #     path = glob.glob('/root/shellLearning/Pytorch/day_08_TaskBot/neo4j/splitBigdata/*.csv')
    #     shuffle(path)
    #     # print(path)
    #     parallelize(path, 多线程)
