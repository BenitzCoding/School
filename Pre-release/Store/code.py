PRODUCTS = {
	101: {
		"name": "Rubber",
		"price": 1.00,
		"stock": 50
	},
	102: {
		"name": "Ruler",
		"price": 1.50,
		"stock": 100
	},
	103: {
		"name": "Pencil",
		"price": 2.50,
		"stock": 100
	},
	104: {
		"name": "Pen",
		"price": 3.00,
		"stock": 200
	},
	105: {
		"name": "Markers",
		"price": 5.00,
		"stock": 50
	},
	106: {
		"name": "Notebook",
		"price": 6.00,
		"stock": 100
	},
	107: {
		"name": "Compass",
		"price": 2.50,
		"stock": 20
	},
	108: {
		"name": "Folder",
		"price": 15.00,
		"stock": 20
	},
	109: {
		"name": "Stapler",
		"price": 25.00,
		"stock": 100
	},
	110: {
		"name": "Calculator",
		"price": 40.00,
		"stock": 10
	}
}

def display_products():
	print("\nProducts:\n")
	print(f"#{34 * '-'}#\n| ID: | Name:            | Price:  |\n|{34 * '-'}|")
	for key, value in PRODUCTS.items():
		if value["stock"] != 0:
			print(f"| {key} | {value['name']} {(15 - len(value['name'])) * ' '} | ${value['price']}0{(5 - len(str(value['price']))) * ' '} |")
	print(f"#{34 * '-'}#")

display_products()