#!/usr/bin/env python3
# -*- coding: utf-8 -*- https://gist.github.com/chromefinch/6d5b6f3af44a8c7f978c4d6f897feaec

lines = ouilist.text.splitlines()

# Open the CSV file and write the data
with open("oui.csv", "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["OUI", "Company Name", "Address 1", "Address 2", "Country"])

    # Iterate through each line in the 'lines' list and get the index and value simultaneously
    for idx, line in enumerate(lines):
        if "(hex)" in line:
            if not "Private" in line:
                split_line = line.split()
                oui = split_line[0]
                company_name = " ".join(split_line[2:])
                
                # Extract the address and country from the next three lines
                address1 = lines[idx+2].strip()
                address2 = lines[idx+3].strip()
                country = lines[idx+4].strip()
                # Write the data to the CSV file
                csv_writer.writerow([oui, company_name, address1, address2, country])
