#Collects number and makes list
def CollectNumbers(totalNumber):
    print("Enter the numbers to be calculated and taken avaerage")
    for i in range(0,totalNumber):
        ele = float(input())
        mylist.append(ele)


#Calculate the average
def calculateAverage():
    total=0
    for i in range(len(mylist)):
        total = total + mylist[i]
    avg = total/totalNumber
    return avg

mylist= []
totalNumber = int(input("Average of how many numbers"))
CollectNumbers(totalNumber)
avg=calculateAverage()
print(avg)




    