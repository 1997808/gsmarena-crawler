import csv

def format_device_name(device_name):
    formatted_name = device_name.lower().replace(" ", "_")
    return formatted_name


input_file = "devices.csv"
output_file = "formatted_devices.csv"

with open(input_file, "r", newline="") as infile, open(output_file, "w", newline="") as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        row["name"] = format_device_name(row["name"])
        writer.writerow(row)

print("Formatting completed. Output written to", output_file)
