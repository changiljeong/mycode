#!/usr/bin/python3

import csv

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def parsecsvdata():
    """returns a list. [0] is LAN and [1] WAN data"""
    summary = [] 

    
    with open("/home/student/mycode/graphing/2018summary.csv",\
     "r") as downtime:
        downdata = csv.reader(downtime, delimiter=",")
        for row in downdata:
            rowdat = (int(row[0]), int(row[1]), int(row[2]), int(row[3]))
            summary.append(rowdat) 
    return summary

def main():
    N = 4
    
    summary = parsecsvdata() 
    localnetMeans = summary[0] 
    wanMeans = summary[1] 

    ind = np.arange(N)

    width = 0.35

    p1 = plt.bar(ind, localnetMeans, width)
    p2 = plt.bar(ind, wanMeans, width, bottom=localnetMeans)

    plt.ylabel("Length of Outage (mins)")
    plt.title("2018 Network Summary")
    plt.xticks(ind, ("Q1", "Q2", "Q3", "Q4"))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ("LAN", "WAN"))

    plt.savefig("/home/student/mycode/graphing/2018summaryv2.png")
    plt.savefig("/home/student/static/2018summaryv2.png")       
    print("Graph created.")

if __name__ == "__main__":
    main()

