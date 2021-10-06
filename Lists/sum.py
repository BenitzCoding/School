def sum_list():
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

	sum_of_total_numbers = sum(number_list)
	print(f"The sum of all the number is: {sum_of_total_numbers}")

sum_list()