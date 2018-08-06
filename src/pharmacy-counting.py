import sys
import csv

#Function to concatenate first and last names as LastFirst
def cleanName(names):
    for name in names:
        if name is not '':
            name = str.upper(name[0]) + str.lower(name[1:])
    return names[0]+names[1]

def main():
    #Dictionary to hold data as {Medicine: SET(Names),totalAmount}
    pharm = {}
    
    #Read in data
    with open(data_file,'r+') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        reader.next()
        for row in reader:
            med = str.upper(row[3])
            if med not in pharm:
                user_set = set()
                if row[4] is not '':
                    cost = float(row[4])
                else:
                    cost = 0
                val = [user_set,cost]
                pharm[med] = val
                user_set.add(cleanName([row[1],row[2]]))
            else:
                val = pharm[med]
                val[0].add(cleanName([row[1],row[2]]))
                if row[4] is not '':
                    val[1] += float(row[4])
    
    #Write out data to output file
    with open(output_file,'w+') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['drug_name','num_prescriber','total_cost'])
        for rx,record in pharm.items():
            
            writer.writerow([rx,len(record[0]),'{:.2f}'.format(record[1])])
        
if __name__ == "__main__":
    global data_file
    global output_file
    data_file = sys.argv[1]
    output_file = sys.argv[2]
    main()