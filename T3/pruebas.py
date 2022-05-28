import re
from datetime import datetime


inicio = "2022-05-05 22:55"    
inicio2 = "2022-05-05"

regexFecha = r"\d{4}/\d{2}/\d{2}\s+\d{2}:\d{2}:\d{2}"
regex2 = r"\d{4}/([1][0-2]|[0][0-9])/([3][0-1]|[1-2][0-9]|[0][1-9]|[1-9])"
regex3 = "^([0-2][0-9]{3})\-(0[1-9]|1[0-2])\-([0-2][0-9]|3[0-1]) ([0-1][0-9]|2[0-3]):([0-5][0-9])\:([0-5][0-9])( ([\-\+]([0-1][0-9])\:00))?$"
regex4 = "^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
f = re.fullmatch(regex3,inicio)

if f:
    print("si mach")
else:
    print("no mach")


x = inicio.split()

print(x)




try:
    datetime.strptime(inicio, '%Y-%m-%d %H:%M')
    # or date_object = datetime.strptime(DATE, '%Y-%m-%d %H:%M:%S')
    # if you need the actual date object later
except ValueError:
    pass  # handle invalid date
    print("mal")

print("paso")