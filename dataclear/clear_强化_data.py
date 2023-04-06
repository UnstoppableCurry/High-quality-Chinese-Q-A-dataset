import glob
import pandas as pd
import csv
from random import shuffle
from util import parallelize
from clear_qa_data import 多线程_qa


def write(outputPath, input):
    output_f = open(outputPath, 'a+', encoding='utf-8', newline='')
    output_f.write(input)
    output_f.close()


def 多线程_强化(path):
    outputPath = '/www/dataset/qa/epoch_1_gun_data.txt'
    all_nothing = set()
    all_dict = {}
    print('path.lens------', len(path))
    shuffle(path)
    all_output_Data = []
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
                nothing = None
                if '[' in line_list[0]:
                    nothing = line_list[0].split('[')[1].replace(']', '')
                    line_list[0] = line_list[0].split('[')[0]
                    if not all_nothing.__contains__(nothing):
                        # print(line_list[0], '*******', nothing)
                        # write(outputPath, line_list[0] + '是' + nothing + '\n')
                        all_nothing.add(nothing)
                        # all_nothing_gloab = nothing
                name = line_list[0]
                value = line_list[2].replace('\n', '')
                # print(name, '-> ', reshape, '-> ', value)
                if len(all_dict.keys()) > 0:
                    if name != [x for x in all_dict.keys()][0]:
                        the_name = [x for x in all_dict.keys()][0]
                        question = '什么是' + the_name + '？\n '
                        mind_token = '我们可以这样做, 先考虑一下我们知道' + the_name + '的什么信息？\n 我们知道:\n'
                        mind_token2 = ''
                        nothing_token = ''
                        anwser = ''
                        repeat = False
                        anwser_index = 0
                        for dict_value in all_dict[the_name].keys():
                            if dict_value == 'None' and all_dict[the_name][dict_value] is not None:
                                nothing_token = the_name + '是' + all_dict[the_name][dict_value] + '。'
                                anwser_index += 1
                            elif dict_value != 'None':
                                if len(all_dict[the_name][dict_value]) == 1:
                                    if dict_value == '描述':
                                        mind_token2 += '\t' + str(anwser_index) + '. 如何描述' + the_name + '。\n'
                                        anwser += '\t' + str(anwser_index) + '. 这样描述' + '其' + \
                                                  all_dict[the_name][dict_value][0] + '。\n'
                                        anwser_index += 1
                                    elif dict_value == '标签':
                                        # if not repeat:
                                        #     repeat = True
                                        mind_token2 += '\t' + str(anwser_index) + '. ' + the_name + '的标签。\n'
                                        anwser += '\t' + str(
                                            anwser_index) + '. ' + the_name + '的' + dict_value + '可以是' + \
                                                  all_dict[the_name][dict_value][0] + '。\n'
                                        anwser_index += 1

                                    else:
                                        mind_token2 += '\t' + str(
                                            anwser_index) + '. ' + the_name + '的' + dict_value + '。\n'
                                        anwser += '\t' + str(anwser_index) + '. 其' + dict_value + '是' + \
                                                  all_dict[the_name][dict_value][0] + '。\n'
                                        anwser_index += 1
                                else:
                                    repeat_data = [x for x in all_dict[the_name][dict_value]]
                                    repeat_output = ''
                                    for i in repeat_data:
                                        repeat_output += i + ','
                                    if dict_value == '描述':
                                        mind_token2 += '\t' + str(anwser_index) + '. 如何描述' + the_name + '。\n'
                                        anwser += '\t' + str(anwser_index) + '. 这样描述' + '其可以为' + \
                                                  repeat_output + '。\n'
                                        anwser_index += 1
                                    elif dict_value == '标签':
                                        # if not repeat:
                                        #     repeat = True
                                        mind_token2 += '\t' + str(anwser_index) + '. ' + the_name + '的标签。\n'
                                        anwser += '\t' + str(
                                            anwser_index) + '. ' + the_name + '的' + dict_value + '可以是' + \
                                                  repeat_output + '。\n'
                                        anwser_index += 1

                                    else:
                                        mind_token2 += '\t' + str(
                                            anwser_index) + '. ' + the_name + '的' + dict_value + '。\n'
                                        anwser += '\t' + str(anwser_index) + '. 其' + dict_value + '可以是' + \
                                                  repeat_output + '。\n'
                                        anwser_index += 1

                        if len(nothing_token) > 0:
                            # print('****************', nothing_token)
                            all_nothing_gloab = ''
                            output = 'q:' + question + ' a:' + mind_token + mind_token2 + '\t' + str(
                                anwser_index) + '. ' + the_name + '是' + '\n' + nothing_token + '那么很显然答案是\n' + anwser
                        else:
                            output = 'q:' + question + ' a:' + mind_token + mind_token2 + '那么很显然答案是\n' + anwser
                        output = output.replace('。。', '。').replace(',。', '。').replace('。,', '。'). \
                            replace('\n', '\\n').replace('\t', '\\t')
                        # output = output.replace('。。', '。').replace(',。', '。').replace('。,', '。')
                        # print(output)
                        if len(all_output_Data) <= 100000:
                            all_output_Data.append(output + '\n')
                            print(output)
                        else:
                            shuffle(all_output_Data)
                            append_all_output_data=''
                            for all_output_data in all_output_Data:
                                # print(all_output_data.replace('\\n', '\n').replace('\\t', '\t'))
                                append_all_output_data+=all_output_data
                            write(outputPath, append_all_output_data)
                            all_output_Data = []
                        all_dict = {}
                if name in all_dict.keys():
                    if nothing is not None:
                        all_dict[name].update({'None': nothing})
                    if reshape in all_dict[name]:
                        all_dict[name][reshape].append(value)
                    else:
                        all_dict[name].update({reshape: [value]})
                    # all_dict[name].update({reshape:value})
                else:
                    all_dict[name] = {reshape: [value]}
                    all_dict[name].update({'None': nothing})

                index += 1

    print('z done')
if __name__ == '__main__':
    # epoch = 100
    # for i in range(epoch):
    #     print('epoch进度为***********-->', i)
    #     all_path = glob.glob('/root/shellLearning/Pytorch/day_08_TaskBot/neo4j/splitBigdata/*.csv')
    #     print('path.lens********', len(all_path))
    #
    #     shuffle(all_path)
    #     # print(path)
    #     parallelize(all_path, 多线程_qa)
    #     parallelize(all_path, 多线程_强化)
    epoch = 0
    for i in range(epoch):
        print('epoch进度为***********-->', i)
        all_path = glob.glob('/root/shellLearning/Pytorch/day_08_TaskBot/neo4j/splitBigdata/*.csv')
        print('path.lens********', len(all_path), all_path)

        shuffle(all_path)
        # print(path)
        # parallelize(all_path, 多线程_qa)
        parallelize(all_path, 多线程_强化)
        print('all done')

