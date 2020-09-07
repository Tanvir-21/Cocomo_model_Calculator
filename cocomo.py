from array import *
def calculate(table,mode,size):
    #check the mode according to size
    if size >= 2 and size <= 50:
        model = 0 #organic

    elif size>50 and size <= 300:
        model = 1 #semi-detached

    elif size > 300:
        model = 2 #embedded

    print("The mode is ",mode[model])

    #calculate effort
    effort = table[model][0]* pow(size, table[model][1])

    #calculate time
    time = table[model][2] * pow(effort, table[model][3])

    #calculate persons required
    staff = effort/time

    print("\nEffort = ",effort," person-month")
    print("\nDevelopment Time = ",time," Months")
    print("\nAverage staff required = ",round(staff)," Persons")

table = [[2.4,1.05,2.5,0.38],[3.0,1.12,2.5,0.35],[3.6,1.20,2.5,0.32]]
mode = [["organic"],["Semi-Detached"],["Embedded"]]
size = input("Enter your software size in KLOC: ")
calculate(table,mode,int(size))
