#!/usr/bin/python3
import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_code_counts = {code: 0 for code in status_codes}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        data = line.split()
        if len(data) == 9:
            status_code = int(data[7])
            file_size = int(data[8])
            if status_code in status_codes:
                status_code_counts[status_code] += 1
            total_size += file_size
        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_codes):
                if status_code_counts[code] > 0:
                    print("{}: {}".format(code, status_code_counts[code]))
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))

