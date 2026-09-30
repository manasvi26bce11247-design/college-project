import pandas as pd
import csv
df=pd.read_csv("movies_dataset.csv",index_col=0)
def genrefinder(name,moviedata):
    data=[name]+moviedata
    f=open("genrefound.csv","a",newline="")
    w=csv.writer(f)
    w.writerow(data)
    f.close()
def storerecords(name,genres):
    data=[name,genres]
    f=open("records.csv","a",newline="")
    w=csv.writer(f)
    w.writerow(data)
    f.close()
def storerates(name,rate):
    data=[name,rate]
    f=open("rates.csv","a",newline="")
    w=csv.writer(f)
    w.writerow(data)
    f.close()
def movierecgenre():
    name=input("enter your name : ")
    g1=input("enter the first genre : ")
    check=df['Genre'].str.contains(g1,case=False,na=False)
    ch=input("do you want to add second genre (y/n)? ")
    i=2
    genres=[g1]
    while (ch=="y"):
        if i==2:
            g2=input("enter the second genre : ")
            check=check & df['Genre'].str.contains(g2,case=False,na=False)
            genres.append(g2)
        else:
            g3=input("enter the third genre : ")
            check=check & df['Genre'].str.contains(g3,case=False,na=False)
            genres.append(g3)
        if i==3:
            break
        i+=1
        ch=input("do you want to add third genre (y/n)? ")
    filtered=df[check]
    if filtered.empty:
        print("no movie found sorry")
    else:
        print("RECCOMENDATIONS")
        r=filtered['Movie_Name'].unique()[:30]
        for movie in r:
            print(movie)
    storerecords(name,genres)
    print("THANK YOU")
    
def genratefinder():
    name=input("enter your name : ")
    movie=input("enter movie name: ")
    check=df['Movie_Name'].str.contains(movie,case=False,na=False)
    filtered=df[check]
    if filtered.empty:
        print("sorry no movie found")
    else:
        print("MOVIE FOUND")
        print("GENRES")
        gen=filtered['Genre'].iloc[0]
        print(gen)
        r=filtered['Rating'].mean()
        print(round(r,1))
        moviedata=filtered.values.tolist()
        genrefinder(name,moviedata)
    print("THANK YOU")
def movierecrate():
    name=input("enter your name : ")
    rate=float(input("enter rating: "))
    check=df['Rating']==rate
    filtered=df[check]
    r=filtered['Movie_Name'].unique()[:30]
    for movie in r:
        print(movie)
    storerates(name,rate)
    print("THANK YOU")   
print("     WELCOME TO WATCH MY MOVIE!    ")
print("      How Can I Help You Today?       ")
print("       1:recommend movies based on genres       ")
print("       2:more about this movie        ")
print("       3:recommend movies based on ratings      ")
try:
    ch=int(input("     PLEASE ENTER YOUR CHOICE (1/2/3): "))
    if ch==1:
        movierecgenre()
    elif ch==2:
        genratefinder()
    elif ch==3:
        movierecrate()
except ValueError:
    print("sorry invalid value please enter a valid value")

