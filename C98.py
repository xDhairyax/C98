def count():
    fileName=input("Enter the file name:")
    n=0
    file=open(fileName,"r")
    for line in file:
        w=line.split()
        n=n+len(w)
        print("Number of Words:")
        print(n)
count()

        
        

