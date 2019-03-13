#import time
#start = time.time()

result = {'account_group':'sum'} #column header
for i in range(40):
    filename = 'data/bintang_pradana_{:02d}.csv'.format(i)
    with open(filename) as f:
        #print('processing file: {}'.format(filename))
        next(f) #skipping first row (column header)
        for line in f:
            id, balance = line.split(',')
            if id[:2] in result: #if group id already stored, adding group value
                result[id[:2]] += int(balance)
            else: #else, create new one
                result[id[:2]] = int(balance)

out = open('task_2_result.csv', 'w')
for k, v in result.items():
    out.write('{},{}\n'.format(k,v)) #write every dict item to file
out.close()

#end = time.time()
#print(end-start)