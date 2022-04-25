import pandas as pd
import statistics as stc
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
claplist = df["claps"].tolist()
clapsmean = stc.mean(claplist)

def show_figure(meanlist) :
    df = meanlist
    mean = stc.mean(df)
    fig = ff.create_distplot([df],["claps"], show_hist=False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = "lines", name = "MEAN"))
    fig.show()

def randommeans(counter) :
    dataset = []
    for i in range(0,counter):
        randomin = random.randint(0,len(claplist)-1)
        value = claplist[randomin]
        dataset.append(value)
    mean = stc.mean(dataset)
    return mean

def main():
    meanlist = []
    for i in range(0,100):
        setofmeans = randommeans(30)
        meanlist.append(setofmeans)
    show_figure(meanlist)