#FOCP TASK 2

#creating empty dictionary 
data_values = {}

print("Park Runner Time")
print("~~~~~~~~~~~~~~~~~~")
print("\n")
print("Let's go!")

while True:
    v = input("> ")
#condition to check the variable v 
    if v == "END":
            break
#condition to check if the string is present    
    if '::' in v:
        try:
#use of split to split the value of v
            run1 = v.split('::')
#checks if the list contains empty string 
            if "" in run1:
                raise Exception()
            data_values[run1[0]]=int(run1[1])

        except Exception:
            print("Error in data stream. Ignorning. Carry on.")

#condition if the string does not contain '::'
    else:
        print("No data found. Nothing to do. What a pity.")


if data_values:
    print("\nTotal runners: {}".format(len(data_values)))

    a = data_values.values()

#average 
    avg =  sum(a) // len(data_values)
    m = avg //60
    s = avg %60
    if m <=1:
        print("Average Time: {} minute, {} seconds".format(m,s))
    else:   
        print("Average Time: {} minutes, {} seconds".format(m,s))

#fastest
    fastest = max(a)
    mi = fastest//60
    se = fastest%60
    if mi<=1:
        print("Fastest Time: {} minute, {} seconds".format(mi,se))
    else:
        print("Fastest Time: {} minutes, {} seconds".format(mi,se))

#slowest
    slowest = min(a)
    mins = slowest//60
    sec = slowest%60
    if mins<=1:
        print("Slowest Time: {} minute, {} seconds" .format(mins,sec))
    else: 
        print("Slowest Time: {} minutes, {} seconds" .format(mins,sec))

#creates list of keys from dictionary
    key_list = list(data_values.keys())
#creates list of values form dictionary
    values_list = list(data_values.values())
#finds the index of slowest time 
    best_time = values_list.index(slowest)

    print("Best Time Here: Runner # {}".format(key_list[best_time]))
#condition if there is no data 
else:
    print("No data found. Nothing to do. What a pity.")




