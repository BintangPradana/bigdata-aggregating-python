#import time
import operator
import os
#start = time.time()
total = 0
top = 0
if os.path.isfile('./task_1_result.txt') and os.path.isfile('./task_3_result.csv'):
    #if output file from task_1 and task_3 already created, get the data from there
    f = open('task_1_result.txt')
    #print('processing file: {}'.format('task_1_result.txt'))
    total = int(f.readline())
    f.close()
    with open('task_3_result.csv') as f:
        #print('processing file: {}'.format('task_3_result.csv'))
        next(f)
        for line in f:
            id, balance = line.split(',')
            top += int(balance)
else: #else, calculate from begining
    minm = ['',None] #create list to store minimum value of balance
    result=dict()
    c=0
    for i in range(40):
        filename = 'data/bintang_pradana_{:02d}.csv'.format(i)
        with open(filename) as f:
            print('processing file: {}'.format(filename))
            next(f)
            for line in f:
                id, balance = line.split(',')
                b=int(balance)
                total += b #sum of all account
                #finding top 1M
                if c<1000000:
                    c+=1
                    result[id]=b
                    if c==1:
                        minm = [id,b]
                    elif b<=minm[1]:
                        minm = [id,b]
                elif b > minm[1]:
                    result[id]=b
                    del result[minm[0]]
                    minm = [id,b]
    #calculate the sum of top 1M
    top = sum(result.values())

out = open('task_4_result.txt', 'w')
out.write('{}\n{}'.format(str(top),str(100*top/total))) #write the top 1M and % ratio
out.close()
#end = time.time()
#print(end-start)