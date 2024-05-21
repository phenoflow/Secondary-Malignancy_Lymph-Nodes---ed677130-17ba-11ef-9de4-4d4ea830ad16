# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"B56y.00","system":"readv2"},{"code":"B560300","system":"readv2"},{"code":"B564100","system":"readv2"},{"code":"B562000","system":"readv2"},{"code":"B560400","system":"readv2"},{"code":"B563000","system":"readv2"},{"code":"B560.00","system":"readv2"},{"code":"B563200","system":"readv2"},{"code":"B562200","system":"readv2"},{"code":"B561200","system":"readv2"},{"code":"B561800","system":"readv2"},{"code":"B561100","system":"readv2"},{"code":"B565z00","system":"readv2"},{"code":"B560700","system":"readv2"},{"code":"B561700","system":"readv2"},{"code":"B561300","system":"readv2"},{"code":"B560100","system":"readv2"},{"code":"B560600","system":"readv2"},{"code":"B560200","system":"readv2"},{"code":"B565200","system":"readv2"},{"code":"B563z00","system":"readv2"},{"code":"B562400","system":"readv2"},{"code":"B562300","system":"readv2"},{"code":"B562z00","system":"readv2"},{"code":"B561500","system":"readv2"},{"code":"B561.00","system":"readv2"},{"code":"B56..00","system":"readv2"},{"code":"B563100","system":"readv2"},{"code":"B561400","system":"readv2"},{"code":"B563300","system":"readv2"},{"code":"B561600","system":"readv2"},{"code":"B564000","system":"readv2"},{"code":"B562100","system":"readv2"},{"code":"B564.00","system":"readv2"},{"code":"B564z00","system":"readv2"},{"code":"B560900","system":"readv2"},{"code":"B565300","system":"readv2"},{"code":"B561900","system":"readv2"},{"code":"B560000","system":"readv2"},{"code":"B563.00","system":"readv2"},{"code":"B565.00","system":"readv2"},{"code":"B561z00","system":"readv2"},{"code":"B560800","system":"readv2"},{"code":"B562.00","system":"readv2"},{"code":"B560z00","system":"readv2"},{"code":"B560500","system":"readv2"},{"code":"B56z.00","system":"readv2"},{"code":"C77","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('secondary-malignancy_lymph-nodes-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["secondary-malignancy_lymph-nodes-unspecified---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["secondary-malignancy_lymph-nodes-unspecified---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["secondary-malignancy_lymph-nodes-unspecified---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
