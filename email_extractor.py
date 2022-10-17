import re
mystr =""""
TATA PAKISTAN is an industry leader in Textile since the last five decades
and also making its mark in Foods and Energy business.
It all started with one textile mill and now several decades later,
Email: atifsalam78@outlook.com
we are one of the leaders in the textile industry of PAKISTAN.
CORPORATE OFFICE
+(92) 213 – 2426740
+(92) 213 – 2426745
+(92) 213 – 2426750
+(92) 213 – 2412955
+(92) 213 – 2417710
Email: info@tatapakistan.com
( For General queries)
exports@tatapakistan.com
( For International customers queries)
sales@tatapakistan.com
( For Local/ domestic customers queries)
Email: tbflms@tatapakistan.com
( For Local/ International Meat queries)
6th Floor, Textile Plaza, M. A. Jinnah Road, Karachi - 74000, Pakistan.
Email: atif.salam@gmail.com
"""

def email_extract(str):
    """Extract emails from given string as an argument"""
    pat = re.compile(r'[\w.]+[@][\w.]+')
    matches = pat.findall(str)
    for index, string in enumerate(matches):
        email_text = f"{index+1}: {string}\n"
        with open("email_extractor.txt","a") as f:
            f.write(email_text)

tata = email_extract(mystr)
