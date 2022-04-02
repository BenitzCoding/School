PRICES = {
	1: {
		"adult": 20.00,
		"children": 12.00,
		"senior": 16.00,
		"family-ticket": 60.00,
		"group": 15.00
	},
	2: {
		"adult": 30.00,
		"children": 18.00,
		"senior": 24.00,
		"family-ticket": 90.00,
		"group": 22.50
	},
	"attractions": {
		"lion-feeding": 2.50,
		"penguin-feeding": 2.00,
		"evening-barbecue": 5.00
	}
}

def display_information():
	message = (
"""
Welcome to Wildlife Park!

This is a program that calculates the ammout you would be paying for your stay at Wild Life Park.
Here are the Attraction Prices:

Single Day:
 - Adult: $20.00
 - Children: $12.00
 - Senior: $16.00
 - Family Ticket: $60.00
 - Group: $15.00

2 Day:
 - Adult: $30.00
 - Children: $18.00
 - Senior: $24.00
 - Family Ticket: $90.00
 - Group: $22.50

Attractions:
 - Lion Feeding: $2.50
 - Penguin Feeding: $2.00
 - Evening Barbecue: $5.00

Please state how many people and attraction who will be joining you below!
"""
	)
	print(message)
	return

def calculate_prices(
	entries: dict
):
	days = entries["days"]
	group = entries["group"]
	group_number = entries["group_number"]
	adults = entries["adults"]
	children = entries["children"]
	seniors = entries["seniors"]
	family_ticket = entries["family_ticket"]
	lion_feeding = entries["lion_feeding"]
	penguin_feeding = entries["penguin_feeding"]
	evening_barbecue = entries["evening_barbecue"]
	price = 0
	if group:
		price = PRICES[days]["group"] * float(group_number)

	elif not group:
		price = price + PRICES[days]["adult"] * float(adults)
		price = price + PRICES[days]["children"] * float(children)
		price = price + PRICES[days]["senior"] * float(seniors)
		price = price + PRICES[days]["family-ticket"] * float(family_ticket)

	if lion_feeding == True:
		price = price + PRICES["attractions"]["lion-feeding"]

	elif penguin_feeding == True:
		price = price + PRICES["attractions"]["penguin-feeding"]

	elif evening_barbecue == True:
		price = price + PRICES["attractions"]["evening-barbecue"]
	return price

def prompt_user():
	days, group, group_number, family_ticket, adults, children, seniors = 0, 0, 0, 0, 0, 0, 0
	days = int(input("\nAre you here for 1 or 2 days? (1/2) "))
	if days > 2:
		return prompt_user()
	group = input("\nAre you going in a group of 6 or more? (y/n) ")
	if group == "y":
		group_number = int(input("\nHow many people are in your group? "))
		lion_feeding = input("\nDo you want to see the lion feeding? (y/n) ")
		penguin_feeding = input("\nDo you want to see the penguin feeding? (y/n) ")
		if days == 2:
			evening_barbecue = input("\nDo you want to see the evening barbecue? (y/n) ")
		if lion_feeding == "y":
			lion_feeding = True
		else:
			lion_feeding = False
		if penguin_feeding == "y":
			penguin_feeding = True
		else:
			penguin_feeding = False
		try:
			if evening_barbecue == "y":
				evening_barbecue = True
		except:
			evening_barbecue = False
		group = True
		return {
			"days": days,
			"group": group,
			"group_number": group_number,
			"lion_feeding": lion_feeding,
			"penguin_feeding": penguin_feeding,
			"evening_barbecue": evening_barbecue,
			"family_ticket": family_ticket,
			"adults": adults,
			"children": children,
			"seniors": seniors
		}

	else:
		group = False

	if group == False:
		family_ticket = int(input("\nHow many family tickets? "))
		adults = int(input("\nHow many adults? "))
		children = int(input("\nHow many children? "))
		seniors = int(input("\nHow many seniors? "))
		lion_feeding = input("\nDo you want to see the lion feeding? (y/n) ")
		penguin_feeding = input("\nDo you want to see the penguin feeding? (y/n) ")
		if days == 2:
			evening_barbecue = input("\nDo you want to see the evening barbecue? (y/n) ")
		if lion_feeding == "y":
			lion_feeding = True
		else:
			lion_feeding = False
		if penguin_feeding == "y":
			penguin_feeding = True
		else:
			penguin_feeding = False
		try:
			if evening_barbecue == "y":
				evening_barbecue = True
		except:
			evening_barbecue = False

	return {
		"days": days,
		"group": group,
		"group_number": group_number,
		"lion_feeding": lion_feeding,
		"penguin_feeding": penguin_feeding,
		"evening_barbecue": evening_barbecue,
		"family_ticket": family_ticket,
		"adults": adults,
		"children": children,
		"seniors": seniors
	}

def main():
	display_information()
	payload = prompt_user()
	print("Your total is: " + f"${calculate_prices(payload)}")

main()
