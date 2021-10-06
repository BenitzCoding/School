def multiply():
	number_list = []
	count = []
	for i in range(6):
		count.append(i)

	for i in count:
		try:
			number = int(input("Number: "))
		except:
			print("Please enter a number.")
			count.append(len(count) + 1)
			continue
		number_list.append(number)

	sum_of_total_numbers = 0
	count = 5
	for number in number_list:
		if count == 0:
			break
		sum_of_total_numbers = number + sum_of_total_numbers

	number = sum(number_list)/number_list[-1]
	print(f"The number is: {number}")

multiply()