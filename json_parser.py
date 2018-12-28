import json,csv
from pprint import pprint
import sys,time

def main(argv):
    bid=time.strftime('%Y%m%d%H%M%S')
    print(bid)
    with open(argv[0]) as f:
        data = json.load(f)
    #print(data["mam"])
    #pprint(data)
    csvfile= open('json_to_{}.csv'.format(bid),'w',newline='')
    csvwtr=csv.writer(csvfile,delimiter=',')
    for i in range(len(data["maps"])):
        lst=[data["maps"][i]["id"],data["masks"]["id"]]
        csvwtr.writerow(lst)
    csvfile.close()

if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv[1:])