"""
Question:
	Program a system that takes as inputs: 
		• The average speed of a car over the length of a journey. 
		• The distance that the car has to travel. 
	The system should output, in minutes, the length of time the journey will take. 
"""
def output(content):
	print(content)

def get_data():
	try:
		speed = int(input("Avarage Speed (in Meters/Minute): "))
	except:
		print("Please enter a whole number as your value.")
	try:
		distance = int(input("Distance (in Meters): "))
	except:
		print("Please enter a whole number as your value.")
	return { "Speed": speed, "Distance": distance } # Returning the information as JSON.

def calculate(data):
	speed = data["Speed"] # Getting values from the dictionary.
	distance = data["Distance"]
	time = (distance/speed)
	if f"{time}".startswith(".0"):
		time = int(time)
	return f"Time Taken: {time} Minutes"

def main():
	data = get_data() # Getting data by asking the user for information.
	value = calculate(data=data) # Calculating the time taken with the given data.
	return output(content=value)

main()