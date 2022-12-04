import random, os
from colorama import init, Fore
init(autoreset=True)

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
        print("Times: "+ str(RollTimes) +"\nItems: "+ str(len(list)))
        todo = input("""What to do next?
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
    elif todo == 2:
        showlist(RollTimes)
    elif todo == 3:
        removeItems(RollTimes)
    elif todo == 4:
        run(RollTimes)
    elif todo == 5:
        main()
    
def run(RollTimes):
    clear()
    print("Times: "+ str(RollTimes) +"\nItems: "+ str(len(list)))
    
    if len(list) <= 1:
        print(Fore.RED+"You need more items!")
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
    print(Fore.GREEN+"\nWinner: \""+max(won, key=won.get)+"\" with " + "{:.2f}".format(rate) + "%")
    
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
        x = dict( sorted(won.items(), key=lambda x: x[0].lower()) )
        for key,value in x.items():
            print('{} : {:.2f}%'.format(key,value))
        
        
    input("\nPress Enter to continue...")
    won.clear()
    cm(RollTimes)
        
        
    
def addItems(RollTimes):
    clear()
    while True:
        addNew = input("""Enter something to add into list(or):
    Back. to Cancel/Save
""")
        if addNew == "":
            clear()
            print(Fore.RED+"Item can't be empty!\n")
        elif addNew.lower() == "back":
            cm(RollTimes)
            break
        elif addNew.lower() == "all":
            clear()
            print(Fore.RED+"\"All\" is not allowed\n")
        elif addNew in list:
            clear()
            print(Fore.YELLOW+"Item already exist!\n")
        else:
            list.append(str(addNew))
            clear()
            print(Fore.GREEN+"\""+addNew+"\" Added into list\n")


def showlist(RollTimes):
    clear()
    if len(list) == 0:
        print(Fore.RED+"List is empty")
        input("\nPress Enter to continue...")
        cm(RollTimes)
    else:
        newList = sorted(list)
        print(*newList, sep=", ")
        input("\nPress Enter to continue...")
        cm(RollTimes)

def removeItems(RollTimes):
    clear()
    print("Items: "+ str(len(list)))
    while len(list) >= 1:
        itemToR = str(input("""Enter item to remove (or): 
    All. To remove everything
    Back. to Cancel/Save
""")).lower()
        if itemToR.lower() == "back":
            cm(RollTimes)
        elif itemToR.lower() == "all":
            list.clear()
            clear()
            print(Fore.RED+"Everything removed")
            input("\nPress Enter to continue...")
            cm(RollTimes)
        else:
            if itemToR in list:
                list.remove(itemToR)
                clear()
                print(Fore.RED+"\""+itemToR+"\" Removed from list\n")
            elif itemToR == "":
                clear()
                print(Fore.YELLOW+"Can't be empty!\n")
            else:
                clear()
                print(Fore.YELLOW+"Item not exist!\n")
    if len(list) == 0:
        print(Fore.YELLOW + 'There is nothing to remove')
        input("\nPress Enter to continue...")
        cm(RollTimes)

def clear():
    os.system('cls' if os.name=='nt' else 'clear')
    print(Fore.CYAN+"""
 __                            __               
|__)_  _  _| _  _ \_/  |_     |  \ _ _ | _| _ _ 
| \(_|| )(_|(_)|||/ \  |_)\/  |__/| (_||(_|(-|  
                          /                     
""")

__author__ = "Dralder"
__version__ = "0.1.1"

if __name__ == '__main__':
    main()
    