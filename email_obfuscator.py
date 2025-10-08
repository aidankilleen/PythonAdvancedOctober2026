# email_obfuscator.py
import re
import sys
from pathlib import Path

usage = """
usage:
python email_obfuscator.py [file]
obfuscate all email addresses in the text file
"""
if len(sys.argv)< 2:
    print (usage)
    exit(1)

filename = sys.argv[1]

input_path = Path(filename)

if not input_path.exists():
    print ("File not found")
    exit(1)

output_path = input_path.stem + "_obfuscated" + input_path.suffix

print (output_path)

email_pattern = "([A-Za-z0-9._%+-])([A-Za-z0-9._%+-]*)(@[\\w.-]+\\.[A-Za-z]{2,})"

with open(input_path, "r") as f:
    text = f.read()
    result = re.sub(email_pattern, lambda m: m.group(1)+ "*"*len(m.group(2)) + m.group(3), text)
    print (result)

with open(output_path, "w") as fo:
    fo.write(result)

print(f"file saved to {output_path}")




