from os import name
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df = pd.read_csv("medium_data.csv")

data = df["reading_time"].tolist()

pmean = statistics.mean(data)
pstdev = statistics.stdev(data)

print("mean :",pmean)
print("stdev :",pstdev)

def samplingmean() :
    sample = []
    for i in range(0,30) :
        rindex = random.randint(0,len(data)-1)
        value = data[rindex]
        sample.append(value)
    mean = statistics.mean(sample)
    return mean

meanlist = []
for i in range(0,100) :
    setofmeans = samplingmean()
    meanlist.append(setofmeans)
meane = statistics.mean(meanlist)
stdevv = statistics.stdev(meanlist)

print("sampling mean :",meane)
print("sampling stdev :",stdevv)

fstds,fstde = meane-stdevv,meane+stdevv
sstds,sstde = meane-(2*stdevv),meane+(2*stdevv)
tstds,tstde = meane-(3*stdevv),meane+(3*stdevv)

mean1 = samplingmean()

fig = ff.create_distplot([meanlist],["sampling mean distribution or some shortform of that"],show_hist = False)
fig.add_trace(go.Scatter(x = [meane,meane],y = [0.005,0.8], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [fstde,fstde], y = [0,0.8], mode = "lines" , name = "standard deviations 1"))
fig.add_trace(go.Scatter(x = [sstde,sstde], y = [0,0.8], mode = "lines" , name = "standard deviations 2"))
fig.add_trace(go.Scatter(x = [tstde,tstde], y = [0,0.8], mode = "lines" , name = "standard deviations 3"))
fig.add_trace(go.Scatter(x = [mean1,mean1],y = [0.005,0.8], mode = "lines", name = "mean1"))

fig.show()

zscore1 = (meane-mean1)/stdevv
print("the zscore of data 1 is ",zscore1)



