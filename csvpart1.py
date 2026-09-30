def genrefinder(moviedata):
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
    
    

    
