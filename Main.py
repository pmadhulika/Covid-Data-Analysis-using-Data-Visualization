import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Fun():
    print("\n*** COVID Data Visualization Menu ***")
    print("1. Check the data")
    print("2. Read file without index")
    print("3. Line Chart")
    print("4. Bar Graph")
    print("5. Scatter Plot")
    print("6. Exit")

def Read_CSV():
    df = pd.read_csv("Covid_data_kerala1.csv")
    print(df)

def No_Index():
    df = pd.read_csv("Covid_data_kerala1.csv", index_col=0)
    print(df)

def line_plot():
    df = pd.read_csv("Covid_data_kerala1.csv")
    df['Districts'] = ['EKM','PTA','KTM','TSR','KKD','MPM','KLM','PKD','ALP','KNR','TVM','IDK','WYD','KGD']
    District = df["Districts"]
    Confirmed, Recovered, Deaths, Active = df["Confirmed"], df["Recovered"], df["Deaths"], df["Active"]

    print("Line Chart Options:\n1. Confirmed\n2. Recovered\n3. Deaths\n4. Active\n5. All")
    CC = int(input("Enter your choice: "))
    plt.xlabel("Districts")

    if CC == 1:
        plt.ylabel("Confirmed Cases")
        plt.title("Confirmed Cases by District")
        plt.plot(District, Confirmed, color='blue')
    elif CC == 2:
        plt.ylabel("Recovered Cases")
        plt.title("Recovered Cases by District")
        plt.plot(District, Recovered, color='green')
    elif CC == 3:
        plt.ylabel("Deaths")
        plt.title("Deaths by District")
        plt.plot(District, Deaths, color='red')
    elif CC == 4:
        plt.ylabel("Active Cases")
        plt.title("Active Cases by District")
        plt.plot(District, Active, color='cyan')
    elif CC == 5:
        plt.plot(District, Confirmed, color='blue', label='Confirmed')
        plt.plot(District, Recovered, color='green', label='Recovered')
        plt.plot(District, Deaths, color='red', label='Deaths')
        plt.plot(District, Active, color='cyan', label='Active')
        plt.ylabel("Cases")
        plt.title("All Cases by District")
        plt.legend()
    else:
        print("Invalid Input")
        return
    plt.show()

def bar_plot():
    df = pd.read_csv("Covid_data_kerala1.csv")
    df['Districts'] = ['EKM','PTA','KTM','TSR','KKD','MPM','KLM','PKD','ALP','KNR','TVM','IDK','WYD','KGD']
    District = df["Districts"]
    Confirmed, Recovered, Deaths, Active = df["Confirmed"], df["Recovered"], df["Deaths"], df["Active"]

    print("Bar Graph Options:\n1. Confirmed\n2. Recovered\n3. Deaths\n4. Active\n5. Stacked\n6. Multi Bar")
    CC = int(input("Enter your choice: "))
    plt.xlabel("Districts")

    if CC == 1:
        plt.bar(District, Confirmed, color='blue')
        plt.ylabel("Confirmed Cases")
    elif CC == 2:
        plt.bar(District, Recovered, color='green')
        plt.ylabel("Recovered Cases")
    elif CC == 3:
        plt.bar(District, Deaths, color='red')
        plt.ylabel("Deaths")
    elif CC == 4:
        plt.bar(District, Active, color='cyan')
        plt.ylabel("Active Cases")
    elif CC == 5:
        plt.bar(District, Confirmed, color='blue', label='Confirmed')
        plt.bar(District, Recovered, color='green', label='Recovered')
        plt.bar(District, Deaths, color='red', label='Deaths')
        plt.bar(District, Active, color='cyan', label='Active')
        plt.legend()
    elif CC == 6:
        D = np.arange(len(District))
        width = 0.2
        plt.bar(D, Confirmed, width, color='blue', label='Confirmed')
        plt.bar(D+width, Recovered, width, color='green', label='Recovered')
        plt.bar(D+2*width, Deaths, width, color='red', label='Deaths')
        plt.bar(D+3*width, Active, width, color='cyan', label='Active')
        plt.xticks(D+1.5*width, District)
        plt.legend()
    else:
        print("Invalid Input")
        return
    plt.title("Bar Chart")
    plt.show()

def scatter_chart():
    df = pd.read_csv("Covid_data_kerala1.csv")
    df['Districts'] = ['EKM','PTA','KTM','TSR','KKD','MPM','KLM','PKD','ALP','KNR','TVM','IDK','WYD','KGD']
    District = df["Districts"]
    plt.scatter(District, df["Confirmed"], color='blue', label='Confirmed')
    plt.scatter(District, df["Recovered"], color='green', label='Recovered')
    plt.scatter(District, df["Deaths"], color='red', label='Deaths')
    plt.scatter(District, df["Active"], color='cyan', label='Active')
    plt.xlabel("Districts")
    plt.ylabel("Cases")
    plt.title("Scatter Plot of All Cases")
    plt.legend()
    plt.show()

# Main
Fun()
CC = int(input("Enter Your Choice: "))
while CC in [1, 2, 3, 4, 5, 6]:
    if CC == 1:
        Read_CSV()
    elif CC == 2:
        No_Index()
    elif CC == 3:
        line_plot()
    elif CC == 4:
        bar_plot()
    elif CC == 5:
        scatter_chart()
    elif CC == 6:
        print("Thank You!")
        break
    else:
        print("Invalid Input")
    print("\n")
    Fun()
    CC = int(input("Enter Your Choice: "))
