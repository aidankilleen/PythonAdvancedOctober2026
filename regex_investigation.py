# regex_investigation.py

import re


#PPS_RE = re.compile("0-9]{7,8}[A-Z]{1,2}\s")
pps_pattern = "[0-9]{7,8}[A-Z]{1,2}\\s"

text = """
this is some text
it contains an email aidan.killeen@gmail.com
aidan_killeen@gmail.com
fre27@homail.co.uk
ABC_def-123@somewhere.com
and it also has some pps numbers
1234
1234567A
12345678AA
1234567
aidan
021-8412345
087 1234567
(021)1234567
01
025
+353 21 87654321
"""

matches = re.findall(pps_pattern, text)

print (matches)
email_pattern = "([A-Za-z0-9._%+-])([A-Za-z0-9._%+-]*)(@[\\w.-]+\\.[A-Za-z]{2,})"
emails = re.findall(email_pattern, text)
print (emails)

# search and replace
# lambda takes the matches and returns the changed text
result = re.sub(email_pattern, lambda m: m.group(1)+ "*"*len(m.group(2)) + m.group(3), text)

print (result)




