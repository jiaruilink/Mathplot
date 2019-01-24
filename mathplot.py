import matplotlib.pyplot as plot
import numpy as np
import datetime as dt


def plotP1():
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    x = [30,50,70,90,99]
    y1 = [2388, 2082, 1570, 703, 46]
    y1=y1[::-1]
    y2=[925,598,358,174,50]
    y2=y2[::-1]
    y3=[1219,912,465,208,106]
    y3=y3[::-1]
    y=[y1, y2, y3]
    markers = ['*', 'o', 'D', ]
    colors = ['blue','green','y']
    labels = ['BLA-AL00','MLA-AL10','BLN-AL10']
    linestyle = '-'
    linewidth = 2.0
    for i in range(len(y)):
        plot.plot(x, y[i], marker=markers[i],color=colors[i],linestyle='-', label=labels[i],linewidth=2.0)

    plot.legend(loc='best')
    #plot.ylim(0,)
    plot.xlabel("Wi-Fi signal level",fontdict={'size':16,'color':'r'})
    plot.ylabel("speed",fontdict={'size':16,'color':'r'})
    plot.title('The effect of Wi-Fi signal level ',fontdict={'size':16,'color':'r'})
    #plot.text(4,5,r'$something annotation$',fontdict={'size':16,'color':'r'})
    plot.grid()
    plot.savefig('p1.png')
    plot.show()

def plotP2():
    x = [5,25,50,75,95]
    y = [9,884,2152,3680,5862]
    y2=[5,702,1936,3429,5660]
    y3=[114,145,275,376,1423]
    y4=[4,208,844,1775,3602]

    plot.plot(x, y,marker='*',color='blue',linestyle='-', label='CLT-AL00',linewidth=2.0)
    plot.plot(x, y2, marker='o', color='green', linestyle='-', label='BLA-AL00', linewidth=2.0)
    plot.plot(x, y3, marker='D', color='y', linestyle='-', label='CAZ-AL10', linewidth=2.0)
    plot.plot(x, y4, marker='d', color='y', linestyle='-', label='BLN-AL10', linewidth=2.0)
    plot.legend(loc='best')

    plot.xlabel("Proportion(%)",fontdict={'size':16,'color':'r'})
    plot.ylabel("Count",fontdict={'size':16,'color':'r'})
    plot.title('The distribution of download speed ',fontdict={'size':16,'color':'r'})
    plot.xticks(x)
    plot.grid()
    plot.savefig('p2.png')
    plot.show()


def plotP3():
    labels=['hw','tx','dl']
    x = np.arange(3)
    y = [481,164,163]
    plot.bar(x, y,width=0.5,facecolor = 'lightskyblue', edgecolor = 'white',align='center')
    plot.legend(loc='best')

    plot.xlabel('cdn facilitator', fontdict={'size': 16, 'color': 'r'})
    plot.ylabel("Download Count(M)", fontdict={'size': 16, 'color': 'r'})
    plot.title('The download sum of different cdn facilitator ', fontdict={'size': 16, 'color': 'r'})
    plot.xticks(x,labels)
    plot.grid()
    plot.savefig('p3.png')
    plot.show()

def plotP4():
    labels=[
        'tencent.mobileqq','huawei.intelligent','sankuai.meituan','sina.weibo',
        'vmall.client','android.article.news','baidu.netdisk','android.ugc.aweme',
        'android.browser','tencent.qqmusic']
    x = range(1,11,1)
    y = [93,81,80,67,47,34,31,29,28,25]
    plot.bar(x, y,facecolor = 'skyblue', edgecolor = 'white',align='center')
    plot.xlabel('most popular app', fontdict={'size': 16, 'color': 'r'})
    plot.ylabel("Download Count(M)", fontdict={'size': 16, 'color': 'r'})
    plot.title('The download sum of different popular apps', fontdict={'size': 16, 'color': 'r'})
    plot.xlim(0,11)
    plot.subplots_adjust(bottom=0.25)
    plot.xticks(x,labels,rotation=30)
    plot.grid()
    plot.savefig('p4.png')
    plot.show()

def plotP5():
    A=dt.datetime(year=2018,month=10,day=8)
    C=dt.timedelta(days=1)
    B = dt.datetime(year=2018, month=11, day=3)
    D=A
    labels=[]
    while D!=B:
        #print D.strftime('%m.%d')
        labels.append(D.strftime('%m.%d'))
        D=D+C
    x = np.arange(26)

    y = [606,5455,7948,6919,7249,3769,2201,6201,9981,174148,165996,132262,131872,66230,
         62642,103624,124566,135049,1422563,3451426,3134883,2925162,3195978,3198720,2843061,2869700]
    plot.figure(figsize=(15,10))
    plot.plot(x, y, marker='o', color='green', linestyle='-', label='Mate20/20Pro', linewidth=2.0)
    plot.legend(loc='best')

    plot.xlabel('Date', fontdict={'size': 16, 'color': 'r'})
    plot.ylabel("Download Count(M)", fontdict={'size': 16, 'color': 'r'})
    plot.title('The download count from 10.8 to 11.2 ', fontdict={'size': 16, 'color': 'r'})
    plot.annotate('Publishment in Lodon', xy=(8, 9981),xytext=(4, 350000),
                 arrowprops=dict(facecolor='blue', shrink=0.1,width=5),fontsize=18
                 )
    plot.annotate('Sale in China', xy=(18, 1422563), xytext=(19, 1700000),
                  arrowprops=dict(facecolor='blue', shrink=0.1,width=5),fontsize=18
                  )
    plot.xticks(x,labels,rotation=30)

    plot.grid()
    plot.savefig('p5.png')
    plot.show()

def plotP6():

    labels=[]
    x = np.arange(24)
    y = [39,21,13,10,10,14,20,31,33,29,27,30,35,38,47,59,69,71,71,68,71,76,70,51]
    A=dt.datetime(year=2018,month=10,day=31,hour=0,minute=0)
    C=dt.timedelta(hours=1,minutes=0)
    B=dt.datetime(year=2018,month=11,day=1,hour=0,minute=0)
    D=A
    print B
    while D!=B:
        labels.append(D.strftime('%H:%M'))
        D=D+C
    plot.figure(figsize=(14, 8))
    plot.plot(x, y, marker='o', color='green', linestyle='-', linewidth=2.0)
    plot.xlim(0,23)
    plot.xlabel("Time",fontdict={'size':16,'color':'r'})
    plot.ylabel("Download Count(M)",fontdict={'size':16,'color':'r'})
    plot.title('The download count in 10.31',fontdict={'size':16,'color':'r'})
    #plot.text(4,5,r'$something annotation$',fontdict={'size':16,'color':'r'})
    plot.xticks(x,labels)
    plot.subplots_adjust(left=0.05,right=0.95)
    plot.grid()
    plot.savefig('p6.png')
    plot.show()

def plotP7():

    ticks=['0-3','3-6','6-9','9-12','12-15','15-18','18-21','21-24']
    x = np.arange(8)
    y1 = [34,17,47,59,62,70,138,112]
    y2 = [33,15,42,50,56,63,66,53]
    y3 = [17,8,23,33,34,38,40,34]
    y4=[11,5,17,42,52,57,116,126]
    y = [y1, y2, y3,y4]
    markers = ['*', 'o', 'D', 'd']
    colors = ['blue', 'green', 'y','skyblue']
    labels = ['Fri.', 'Sat.', 'Sun.','Mon.']
    for i in range(len(y)):
        plot.plot(x, y[i], marker=markers[i], color=colors[i], linestyle='-', label=labels[i], linewidth=2.0)
    plot.legend(loc='best')
    plot.xlabel("Time Period",fontdict={'size':16,'color':'r'})
    plot.ylabel("Download Count(M)",fontdict={'size':16,'color':'r'})
    plot.title('The download count in a week',fontdict={'size':16,'color':'r'})
    plot.xticks(x,ticks)
    plot.grid()
    plot.savefig('p7.png')
    plot.show()


def plotP8():
    labels=[
        'Connection Timeout','Pause','Scheduling failure','Network Error',
        'Unknown','Error In Length Of Server File ']
    x = np.arange(6)
    y = [15000,14000,13000,44260,3499,3118]
    plot.figure(figsize=(15,8))
    plot.subplot()
    plot.bar(x, y,facecolor = 'skyblue', edgecolor = 'white',align='center')
    plot.xlabel('Fault Types', fontdict={'size': 16, 'color': 'r'})
    plot.ylabel("Fault Count(K)", fontdict={'size': 16, 'color': 'r'})
    plot.title('The ranking of fault types', fontdict={'size': 16, 'color': 'r'})
    plot.xticks(x,labels)
    plot.grid()
    plot.savefig('p8.png')
    plot.show()


def plotP9():
    a = [36874,21617,1078,187,67]
    total = [793662, 275315, 8095, 1205, 256]
    labels = ['0-50M', '50-100M', '100-150M', '150-200M', '200-250M']
    total.reverse()
    b=[]
    c=[]
    for i in a:
        c.append([i,total.pop()-i])
    print c
    plot.figure(figsize=(15,8))
    for i in range(len(a)):
        plot.subplot(151+i)
        plot.pie(c[i], colors=['gold','skyblue'],labels=['Fault','Normal'], autopct='%1.2f%%', explode=[0.2,0], shadow=False, labeldistance=1.1,
                 startangle=90,pctdistance=0.6,radius=10)
        plot.axis('equal')
        plot.title(labels[i])
    plot.savefig('plotP9.png')
    plot.show()


def plotP10():
    labels=['BLN-AL10','MLA-AL10','CAZ-AL10','TRT-AL00','LYA-AL00','BLA-AL00','CLT-AL00']
    x = np.arange(7)
    y = [680,277,363,292,2326,1741,1939]
    plot.figure(figsize=(14,8))
    plot.bar(x, y,width=0.8,color = 'lightskyblue', edgecolor = 'white',align='center')
    plot.xlabel('Type', fontdict={'size': 16, 'color': 'r'})
    plot.ylabel("Wifi Median Speed(kB/s)", fontdict={'size': 16, 'color': 'r'})
    plot.title('The wifi median speed of different types', fontdict={'size': 20, 'color': 'r'})
    plot.xticks(x,labels)
    plot.grid()
    plot.savefig('p10.png')
    plot.show()

def plotP11():
    labels=['BLN-AL10','MLA-AL10','CAZ-AL10','TRT-AL00','LYA-AL00','BLA-AL00','CLT-AL00']
    x = np.arange(7)
    y = [10.25839793,10.29078695,10.21222769,8.501470588,27.56896552,16.0681074,19.01037165]
    plot.figure(figsize=(14,8))
    plot.bar(x, y,width=0.8,color = 'gold', edgecolor = 'white',align='center')
    plot.xlabel('Type', fontdict={'size': 18, 'color': 'b'})
    plot.ylabel("Aver Dl(k)", fontdict={'size': 18, 'color': 'b'})
    plot.title('The average dl of different types ', fontdict={'size': 20, 'color': 'b'})
    plot.xticks(x,labels)
    plot.grid()
    plot.savefig('p11.png')
    plot.show()


def plotP12():
    y = [21000,190,97,64]
    plot.figure(figsize=(10,8))
    plot.pie(y, colors=['gold', 'skyblue','g','r'], labels=['Wifi(count)', 'Cmnet(count)','Ctnet(Count)','3Gnet(Count)'],
             autopct='%1.2f%%', explode=[0, 0,0,0],shadow=False, labeldistance=1.2,
             startangle=0, pctdistance=1.1,)
    plot.axis('equal')
    plot.title('The download count(K) of MLA-AL10 in different ways ', fontdict={'size': 20, 'color': 'b'})
    plot.savefig('p12.png')
    plot.show()

def plotP13():
    y = [20000,511,266,238]
    plot.figure(figsize=(10,8))
    plot.pie(y, colors=['skyblue', 'gold','lightgreen','r'], labels=['Wifi(count)', 'Cmnet(count)','Ctnet(Count)','3Gnet(Count)'],
             autopct='%1.2f%%', explode=[0, 0.08,0,0],shadow=False, labeldistance=1.2,
             startangle=0, pctdistance=1.1,)
    plot.axis('equal')
    plot.title('The download count(K) of CLT-AL00 in different ways ', fontdict={'size': 20, 'color': 'b'})
    plot.savefig('p13.png')
    plot.show()
plotP13()
