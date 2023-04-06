from random import shuffle

if __name__ == '__main__':
    outputPath = '/www/dataset/qa/all_qa_Data.txt'
    file = open(outputPath)
    lins = file.readlines()
    print(lins)
    print('aaa')
    shuffle(lins)
    print(lins)
    file.close()
