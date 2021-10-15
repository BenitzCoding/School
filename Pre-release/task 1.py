import os

CANDIDATES = { # This is all capital because it's a constant.
	"1": "George",
	"2": "Matthew",
	"3": "Paul",
	"4": "Mark"
}

VOTE_MESSAGE = (
"""
Please enter the candidate's name or the candidate's number to vote for them.

#----------------------------#
|         CANDIDATES         |
|----------------------------|
|  [1]: George               |
|  [2]: Matthew              |
|  [3]: Paul                 |
|  [4]: Mark                 |
#----------------------------#
"""
)

CANDIDATE_VOTES = {
	"George": 0,
	"Matthew": 0,
	"Paul": 0,
	"Mark": 0
}

def get_data(option=None):
	VALID_OPTIONS = ["1", "2", "3", "4"]
	REVERSED_VALID_OPTIONS = ["George", "Matthew", "Paul", "Mark"]
	if option != "re-enter":
		os.system("cls")
		print(VOTE_MESSAGE)
	candidate_vote = input("> ")
	if candidate_vote in VALID_OPTIONS:
		input("Thank you for voting!\n\n[Please press enter before the next vote.]\n>")
		return { "type": "normal", "vote": candidate_vote }
	elif candidate_vote in REVERSED_VALID_OPTIONS:
		input("Thank you for voting!\n\n[Please press enter before the next vote.]\n>")
		return { "type": "reversed", "vote": candidate_vote }
	else:
		print("Please re-enter with a valid vote.")
		return get_data("re-enter")

def register_vote(type, vote):
	if type == "reversed":
		CANDIDATE_VOTES.update({ vote: CANDIDATE_VOTES[vote] + 1 })
		return True
	elif type == "normal":
		CANDIDATE_VOTES.update({ CANDIDATES[vote]: CANDIDATE_VOTES[CANDIDATES[vote]] + 1 })
		return True
	else:
		print("The code has been tampered with, causing things to break.\nRecieved an unknown vote type.")
		return False

def main():
	vote_data = get_data()
	if register_vote(type=vote_data["type"], vote=vote_data["vote"]) == False:
		print("Vote Unsuccessful.")
		return "VOTE ERROR"
	else:
		return "VOTE SUCCESS"

def output_votes():
	os.system("cls")
	sorted_dict = dict(sorted(CANDIDATE_VOTES.items(), key=lambda item: item[1], reverse=True))
	print(f"Vote Leaderboard:\n\n")
	count = 0
	for name, votes in sorted_dict.items():
		count = count + 1
		print(f"[{count}]: {name} | {votes} Votes")

def run():
	for i in range(30):
		if main() == "VOTE ERROR":
			break
	output_votes()

run()