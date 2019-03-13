#import time
import operator
#start = time.time()

minm = ['',None] #list to store id and balance with the lowest balance
result=dict() #dict to store result
c = 0 #count number of row
for i in range(40):
    filename = 'data/bintang_pradana_{:02d}.csv'.format(i)
    with open(filename) as f:
        #print('processing file: {}'.format(filename))
        next(f)
        for line in f:
            id, balance = line.split(',')
            if c<1000000: #if row < 1M, store the id and balance
                c+=1
                b = int(balance)
                result[id]=b
                if c==1: #finding lowest value balance
                    minm = [id,b]
                elif b<=minm[1]:
                    minm = [id,b]
            elif int(balance) > minm[1]: #if row > 1M, store only when bigger than minimum
                b = int(balance)
                result[id]=b
                del result[minm[0]]
                minm = [id,b]

#write to file
out = open('task_3_result.csv', 'w')
out.write('account_id,account_balance\n')
for key, value in sorted(result.items(), key=operator.itemgetter(1), reverse=True):
    out.write('{},{}\n'.format(key,value))
out.close()
#end = time.time()
#print(end-start)