from datetime import datetime

# 10:00:00.000000 and 11:59:59.999999 for the date range of 20170601 to 20180201
start = datetime(2017,6,1,0,0,0)
stop = datetime(2018,2,2,0,0,0)
trans = []

for i in range(1):
    filename = "data{:03}.txt".format(i)
    with open(filename) as f:
        content = f.readlines()
        for line in content:
            line = line[0:-1]
            when = datetime.strptime(line[:24], "%Y%m%d %H:%M:%S.%f")
            rest = line[25:].split(' ')
            curr = rest[0]
            rate = float(rest[1])
            vol = int(rest[2])
            stock = rest[3]
            if start <= when and when < stop and 10 <= when.hour and when.hour < 12 and curr == "BTC":
                trans.append([rate, vol, stock, line])

stats = dict()
for r,v,s,l in trans:
    t = abs(r * v)
    if s in stats and stats[s] < t:
        stats[s] = [t,l]
    else:
        stats[s] = [t,l]

for s in stats:
    print s
    print stats[s][0]
    print stats[s][1]
    print




    