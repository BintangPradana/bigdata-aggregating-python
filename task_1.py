#import time
#start = time.time()
total = 0
for i in range(40):
    filename = 'data/bintang_pradana_{:02d}.csv'.format(i)
    with open(filename) as f:
        print('processing file: {}'.format(filename))
        next(f)
        for line in f:
            id, balance = line.split(',')
            total += int(balance) #summing balance

out = open('task_1_result.txt', 'w')
out.write(str(total)) #write file
out.close()
#end = time.time()
#print(end-start)