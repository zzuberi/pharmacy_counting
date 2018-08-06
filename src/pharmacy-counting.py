import sys
import csv
from record import Record as Rec

def main():
    #Dictionary to hold data as {Medicine: SET(Names),totalAmount}
    pharm = {}
    
    #Read in data
    with open(data_file,'r+b') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        reader.next()
        for row in reader:
            med = str.upper(row[3])
            if med not in pharm:
                record = Rec(med,[row[1],row[2]],row[4])
                pharm[med] = record
            else:
                rec = pharm[med]
                rec.addName([row[1],row[2]])
                rec.addVal(row[4])
    pharm = pharm.values()
    pharm.sort(reverse=True)
    
    #Write out data to output file
    with open(output_file,'w+b') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['drug_name','num_prescriber','total_cost'])
        for record in pharm:
            writer.writerow([record.med,record.nameCount(),record.totVal()])
        
        
if __name__ == "__main__":
    global data_file
    global output_file
    data_file = sys.argv[1]
    output_file = sys.argv[2]
    main()
