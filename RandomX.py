import random, os

list = []
won = {}

def main():
    list.clear()
    won.clear()
    clear()
    try:
        RollTimes = int(input("How many times to roll a dice? "))
    except:
        main()
    cm(RollTimes)

def cm(RollTimes):
    clear()
    try:
        todo = input("Times: "+ str(RollTimes) +"""
Items: """+ str(len(list)) +"""
    What to do next?
    1. Add to list
    2. Show list
    3. Remove from list
    4. Run
    5. Restart
""")
        todo = int(todo)
    except:
       cm(RollTimes)
        
    if todo == 1:
        addItems(RollTimes)
    if todo == 2:
        showlist(RollTimes)
    if todo == 3:
        removeItems(RollTimes)
    if todo == 4:
        run(RollTimes)
    if todo == 5:
        main()
    
def run(RollTimes):
    clear()
    print("Times: "+ str(RollTimes) +"\nItems: "+ str(len(list)))
    
    if len(list) <= 1:
        print("You need more items!")
        input("\nPress Enter to continue...")
        cm(RollTimes)
    
    for i in range(RollTimes):
        num = random.randint(1,len(list))
        item = list[num-1]
        if item in won:
            won[item] = won[item] + 1
        else:
            won[item] = 1
    rate = (int(max(won.values())) * 100)/int(RollTimes)
    print("\nWinner: \""+max(won, key=won.get)+"\" with " + "{:.2f}".format(rate) + "%")
    
    inp = input("""
    1. Show results
    [~]. Back
    """)
    
    if inp == "1":
        clear()
        print("Times: "+ str(RollTimes) +"\nItems: "+ str(len(list)))
        print("\nWinner: \""+max(won, key=won.get)+"\" with " + "{:.2f}".format(rate) + "%\n")
        for key, value in won.items():
            won[key] = (int(value) * 100)/int(RollTimes)
            print(key, ':', "{:.2f}".format(won[key])+"%")
        
    input("\nPress Enter to continue...")
    won.clear()
    cm(RollTimes)
        
        
    
    
def addItems(RollTimes):
    clear()
    try:
        itemCount = input("""How many Items to add?
    !1. Back
""")
        if itemCount == "!1":
            cm(RollTimes)
        itemCount = int(itemCount)
        if itemCount <= 0:
            addItems(RollTimes)
    except:
        addItems(RollTimes)
    while itemCount >= 1:
        addNew = input("Enter something to add into list:\n")
        if addNew == "":
            print("Item can't be empty!")
        elif addNew in list:
            print("Item already exist!")
        else:
            itemCount += -1
            list.append(str(addNew))
    print("All items added into list")
    input("\nPress Enter to continue...")
    cm(RollTimes)
  
def showlist(RollTimes):
    clear()
    if len(list) == 0:
        print("List is empty")
        input("\nPress Enter to continue...")
        cm(RollTimes)
    else:
        print(*list, sep=", ")
        input("\nPress Enter to continue...")
        cm(RollTimes)

def removeItems(RollTimes):
    clear()
    print("Items: "+ str(len(list)))
    while len(list) >= 1:
        itemToR = str(input("""Enter item to remove (or): 
    !1. To remove everything
    !2. Back
""")).lower()
        if itemToR == "!2":
            cm(RollTimes)
        elif itemToR == "!1":
            list.clear()
            print("Everything removed")
            input("\nPress Enter to continue...")
            cm(RollTimes)
        else:
            if itemToR in list:
                list.remove(itemToR)
                print(itemToR+" Removed from list")
                input("\nPress Enter to continue...")
                removeItems(RollTimes)
            else:
                print("Item not exist!")
    if len(list) == 0:
        print("There is nothing to remove")
        input("\nPress Enter to continue...")
        cm(RollTimes)

def clear():
    os.system('cls' if os.name=='nt' else 'clear')
    print("""
 __                            __               
|__)_  _  _| _  _ \_/  |_     |  \ _ _ | _| _ _ 
| \(_|| )(_|(_)|||/ \  |_)\/  |__/| (_||(_|(-|  
                          /                     
""")

if __name__ == '__main__':
    main()