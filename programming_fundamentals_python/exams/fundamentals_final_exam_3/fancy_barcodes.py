import re

barcodes_number = int(input())
pattern = r"\@\#{1,}[A-Z][a-zA-Z0-9]{4,}[A-Z]\@\#{1,}"
for i in range(barcodes_number):
    barcode = input()
    group = ""
    match = re.search(pattern, barcode)
    if match:
        for ch in match.group():
            if ch.isdigit():
                group += ch
        if len(group) == 0:
            group = "00"
        print(f"Product group: {group}")
    elif not match:
        print("Invalid barcode")