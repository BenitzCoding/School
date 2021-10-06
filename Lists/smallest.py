def smallest():
	number_list = []
	count = []
	for i in range(5):
		count.append(i)

	for i in count:
		try:
			number = int(input("Number: "))
		except:
			print("Please enter a number.")
			count.append(len(count) + 1)
			continue
		number_list.append(number)

	largest_numbers = min(number_list)
	print(f"The smallest number is: {largest_numbers}")

smallest()