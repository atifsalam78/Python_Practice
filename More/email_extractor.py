import re

mystr1 = """"
TATA PAKISTAN is an industry leader in Textile since the last five decades
and also making its mark in Foods and Energy business.
It all started with one textile mill and now several decades later,
atifsalam78@outlook.com
we are one of the leaders in the textile industry of PAKISTAN.
CORPORATE OFFICE
+(92) 213 – 2426740
+(92) 213 – 2426745
+(92) 213 – 2426750
+(92) 213 – 2412955
+(92) 213 – 2417710
info@tatapakistan.com
( For General queries)
exports@tatapakistan.com
( For International customers queries)
sales@tatapakistan.com
( For Local/ domestic customers queries)
tbflms@tatapakistan.com
( For Local/ International Meat queries)
6th Floor, Textile Plaza, M. A. Jinnah Road, Karachi - 74000, Pakistan.
atif.salam@gmail.com
"""


mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii
'''
#
# pat = re.compile()
# matches = re.findall(r"(\b.*@.*)", mystr)
# for index, string in enumerate(matches):
#     email_text = f"{index+1}: {string}\n"
#     print(email_text)
    # with open("email_collector.txt","a") as f:
    #     f.write(email_text)

print(re.findall(re.split('(\bE[a-z]*)', mystr)re.findall(r"\b.*@.*")))
