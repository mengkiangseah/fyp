#!/usr/bin/python3

import string

# Call danger metric
def callMetric(wordsSpoken):
	# Catelogy A words
	alist = ["invest", "invests", "shares", "share", "property", "properties", "estate", "estates", "opportunity", "opportunities", "investment", "investments", "stock", "stocks", "equity", "equities", "pension", "pensions", "scheme", "schemes", "apple", "microsoft", "tech", "support", "computer", "computers", "account", "accounts", "detail", "details", "pin", "code", "codes", "debit", "credit", "deposit", "deposits", "accident", "accidents", "compensation", "compensations", "entitled", "entitlement", "entitlements", "compensate", "incident", "incidents", "scam", "scams", "anti", "prevent", "fee", "fees"]

	# Category B words
	blist = ["real", "market", "markets", "return", "hedge", "interest", "trust", "returns", "fund", "funds", "income", "benefit", "benefits", "payment", "payments", "retirement", "infected", "virus", "software", "windows", "machine", "bank", "number", "card", "cards", "miss", "mister", "madam", "missus", "insurance", "damages", "damage", "fake", "pay", "phony", "protect", "protection", "money"]

	wordsA = [word for word in wordsSpoken.lower().split() if word in alist]

	wordsB = [word for word in wordsSpoken.lower().split() if word in blist]

	numA = len(wordsA)
	numB = len(wordsB)

	# No keywords, no risk.
	if numA == 0 and numB == 0:
		return 6
	# Only possible keywords, some risk.
	elif numA == 0 and numB != 0:
		return 7
	# Only probably keywords, high risk.
	elif numA != 0 and numB == 0:
		return 8
	# Both types
	else:
		# More probable than possible, some.
		if numA > numB:
			return 8
		# Otherwise medium
		else:
			return 7

	# If it gets this far, it's an error!
	return 9

def main():
	scamList = []
	with open('scams.txt', 'r') as f:
		scamList = f.readlines()

	translator = str.maketrans('', '', string.punctuation)
	editedScamList = [l.translate(translator).rstrip() for l in scamList]

	metric = [callMetric(l) for l in editedScamList]
	print(metric)

if __name__ == '__main__':
	main()
