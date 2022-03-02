
# Place code below to do the munging part of this assignment.
# Group: Laura Lourenco, Maryam Khalili, Yinlong Dai, Yong Liao

raw = open("data.txt", "r")
# cleaned = open("clean_data.csv", "w")

# skipping over the first few lines and saving the header file
for i in range(7):
    raw.readline()
header = raw.readline()
header = header.split()[:-1]

# saving all the rows as lists (inside an array)
lines = raw.readlines()

#close data file
raw.close()
data = []
curr = 1
for line in lines:
    if (line[0].isnumeric()):
        sepData = line.split()
        
        # filter through rows that contain missing values
        if('***' not in sepData):
            
            # convert to F within one decimal place
            for value in sepData[1:19]:
                convertedValue = float((int(value)/100)*(9/5))
                sepData[curr] = str("{:.1f}".format(convertedValue))
                curr += 1
                
                # reset current index to first value of year
                if(curr == 19):
                    curr = 1
            data.append(sepData[0:19])


# create the cleaned csv file
clean = open("clean_data.csv","w")

#write the header
clean.write(",".join(header)+"\n")

#write the data
for i in data:
    clean.write(",".join(i)+"\n")
clean.close()

