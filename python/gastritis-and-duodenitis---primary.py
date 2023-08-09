# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"J153.00","system":"readv2"},{"code":"J154000","system":"readv2"},{"code":"J154100","system":"readv2"},{"code":"J154200","system":"readv2"},{"code":"J154300","system":"readv2"},{"code":"J15z.00","system":"readv2"},{"code":"J4z0.00","system":"readv2"},{"code":"ZV65316","system":"readv2"},{"code":"10906.0","system":"med"},{"code":"1138.0","system":"med"},{"code":"11497.0","system":"med"},{"code":"11519.0","system":"med"},{"code":"14787.0","system":"med"},{"code":"14928.0","system":"med"},{"code":"15025.0","system":"med"},{"code":"15348.0","system":"med"},{"code":"18260.0","system":"med"},{"code":"18596.0","system":"med"},{"code":"19190.0","system":"med"},{"code":"25544.0","system":"med"},{"code":"27763.0","system":"med"},{"code":"2877.0","system":"med"},{"code":"2936.0","system":"med"},{"code":"29492.0","system":"med"},{"code":"3341.0","system":"med"},{"code":"33820.0","system":"med"},{"code":"3462.0","system":"med"},{"code":"376.0","system":"med"},{"code":"38638.0","system":"med"},{"code":"4506.0","system":"med"},{"code":"45769.0","system":"med"},{"code":"5635.0","system":"med"},{"code":"5858.0","system":"med"},{"code":"6420.0","system":"med"},{"code":"73154.0","system":"med"},{"code":"9731.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('gastritis-and-duodenitis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["gastritis-and-duodenitis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["gastritis-and-duodenitis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["gastritis-and-duodenitis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
