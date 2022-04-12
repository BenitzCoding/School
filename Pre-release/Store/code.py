
PRODUCTS = {
	"101": {
		"name": "Rubber",
		"price": 1.00,
		"stock": 50
	},
	"102": {
		"name": "Ruler",
		"price": 1.50,
		"stock": 100
	},
	"103": {
		"name": "Pencil",
		"price": 2.50,
		"stock": 100
	},
	"104": {
		"name": "Pen",
		"price": 3.00,
		"stock": 200
	},
	"105": {
		"name": "Markers",
		"price": 5.00,
		"stock": 50
	},
	"106": {
		"name": "Notebook",
		"price": 6.00,
		"stock": 100
	},
	"107": {
		"name": "Compass",
		"price": 2.50,
		"stock": 20
	},
	"108": {
		"name": "Folder",
		"price": 15.00,
		"stock": 20
	},
	"109": {
		"name": "Stapler",
		"price": 25.00,
		"stock": 100
	},
	"110": {
		"name": "Calculator",
		"price": 40.00,
		"stock": 10
	}
}

def display_products():
	print("\nProducts:\n")
	print(f"#{34 * '-'}#\n| ID: | Name:            | Price:  |\n|{34 * '-'}|")
	for key, value in PRODUCTS.items():
		if value["stock"] > 10:
			print(f"| {key} | {value['name']} {(15 - len(value['name'])) * ' '} | ${value['price']}0{(5 - len(str(value['price']))) * ' '} |")
	print(f"#{34 * '-'}#")

def get_user_products():
	user_products = {}
	while True:
		user_input = input("\nEnter product ID or 'q' to quit [>] ")
		if user_input == "q":
			break
		ids = []
		for key, value in PRODUCTS.items():
			ids.append(key)
		if user_input in ids:
			amount = int(input("Enter amount [>] "))
			if amount >= PRODUCTS[user_input]['stock'] or PRODUCTS[user_input]['stock'] <= 10:
				print(f"\nNot enough stock. (0-{PRODUCTS[user_input]['stock']})\n")
				continue
			user_products.update({user_input: amount})
			payload = PRODUCTS[user_input]
			payload.update({"stock": payload["stock"] - amount})
			PRODUCTS.update({user_input: payload})
		else:
			print("\nInvalid product ID.\n")
	return user_products

def calculate_price(products: dict):
	total_price = 0.0
	for product_id, amount in products.items():
		try:
			total_price = float(total_price) + PRODUCTS[product_id]["price"] * float(amount)
		except:
			total_price = PRODUCTS[product_id]["price"] * float(amount)
	print(f"\nTotal price: ${total_price:.2f}")

def main(a=False):
	if a:
		while True:
			products = get_user_products()
			calculate_price(products)
	display_products()
	products = get_user_products()
	calculate_price(products)
	return main(True)

main()