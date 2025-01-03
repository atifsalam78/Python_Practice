from fuzzywuzzy import fuzz
from fuzzywuzzy import process

x = fuzz.ratio("Catherine M Gitau","Catherine Gitau")
print(f"Fuzzy Ratio {x}")
y = fuzz.partial_ratio("Catherine M. Gitau","Catherine Gitau")
print(f"Fuzzy Partial Ratio {y}")

z = fuzz.token_sort_ratio("Catherine Gitau M.", "Gitau Catherine")
print(f"Fuzzy Token Sort Ratio {z}")

a = fuzz.token_set_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear")
print(f"Fuzzy Token Set Ratio {a}")

choices = ["Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys"]
b = process.extract("new york jets", choices, limit=2)
print(f"Process Extract: {b}")

c = process.extractOne("cowboys", choices)
print(f"Process Extract One: {c}")

d = process.extractOne("System of a down - Hypnotize - Heroin", songs)

