import re
import csv
import sys
from pathlib import Path

def parse_top_output(file_path):
    """Parses a top output file and returns a list of dictionaries."""
    print("Parsing top output file named " + file_path)
    file_name_without_extn = Path(file_path).stem
    csv_file = file_name_without_extn+".csv"
    print("Creating a csv file named " + csv_file)
    with open (csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['TIME', 'PID', '%CPU', '%MEM', 'COMMAND'])

    with open(file_path, 'r') as f:
        lines = f.readlines()

    process_started = False
    time_string = ''
    for line in lines:
        line = line.lstrip()
        if line.startswith('top'):
            match = re.match(r''
                             '(\w+)\s+'
                             '(\S+)\s+'
                             '(\S+)\s+',
                             line)
            if match:
                if match.group(1) == 'top':
                    time_string = match.group(3)

        if line.startswith('PID'):
            process_started = True
            continue

        if process_started:
            match = re.match(
                r'(\d+)\s+'
                '(\w+)\s+'
                '(\d+)\s+'
                '(\d+)\s+'
                '(\d+)\s+'
                '(\S+)\s+'
                '(\d+)\s+'
                '(\w+)\s+'
                '([0-9.]+)\s+'
                '([0-9.]+)\s+'
                '([0-9.:]+)\s+'
                '(.*$)\s+',
                line)
            if match:
                with open(csv_file, 'a', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([time_string, match.group(1), match.group(9),match.group(10), match.group(12)])
    return

if __name__ == '__main__':
    file_path = sys.argv[1]
    parse_top_output(file_path)
