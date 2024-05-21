# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"15507.0","system":"readv2"},{"code":"93716.0","system":"readv2"},{"code":"61677.0","system":"readv2"},{"code":"64918.0","system":"readv2"},{"code":"50904.0","system":"readv2"},{"code":"44931.0","system":"readv2"},{"code":"33395.0","system":"readv2"},{"code":"65253.0","system":"readv2"},{"code":"98626.0","system":"readv2"},{"code":"69132.0","system":"readv2"},{"code":"52736.0","system":"readv2"},{"code":"55463.0","system":"readv2"},{"code":"61289.0","system":"readv2"},{"code":"95378.0","system":"readv2"},{"code":"52190.0","system":"readv2"},{"code":"47366.0","system":"readv2"},{"code":"73538.0","system":"readv2"},{"code":"64116.0","system":"readv2"},{"code":"69392.0","system":"readv2"},{"code":"67129.0","system":"readv2"},{"code":"50199.0","system":"readv2"},{"code":"6701.0","system":"readv2"},{"code":"66775.0","system":"readv2"},{"code":"20159.0","system":"readv2"},{"code":"9618.0","system":"readv2"},{"code":"70747.0","system":"readv2"},{"code":"7830.0","system":"readv2"},{"code":"63915.0","system":"readv2"},{"code":"92703.0","system":"readv2"},{"code":"84368.0","system":"readv2"},{"code":"25366.0","system":"readv2"},{"code":"68611.0","system":"readv2"},{"code":"37919.0","system":"readv2"},{"code":"105953.0","system":"readv2"},{"code":"28059.0","system":"readv2"},{"code":"72713.0","system":"readv2"},{"code":"18658.0","system":"readv2"},{"code":"41691.0","system":"readv2"},{"code":"67797.0","system":"readv2"},{"code":"37540.0","system":"readv2"},{"code":"58692.0","system":"readv2"},{"code":"38343.0","system":"readv2"},{"code":"72803.0","system":"readv2"},{"code":"66163.0","system":"readv2"},{"code":"49214.0","system":"readv2"},{"code":"54278.0","system":"readv2"},{"code":"46409.0","system":"readv2"},{"code":"62124.0","system":"readv2"},{"code":"44627.0","system":"readv2"},{"code":"101662.0","system":"readv2"},{"code":"39433.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('secondary-malignancy_lymph-nodes-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["lymph---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["lymph---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["lymph---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
