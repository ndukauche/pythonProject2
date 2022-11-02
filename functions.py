# students_scores = {
#     "harry": 81,
#     "ron": 78,
#     "herm": 99,
#     "draco": 74,
#     "nev": 62,
# }
# students_grade = {}
# for students in students_scores:
#     score = students_scores[students]
#     if score > 90:
#         students_grade[students] = "outstanding"
#     elif score > 80:
#         students_grade[students] = "exceed expectation"
#     elif score > 70:
#         students_grade[students] = "acceptable"
#     else:
#         students_grade[students] = "fail"
# print(students_grade)
print(f"welcome to the secret auction")
more_bidders = True
bidders = {}
while more_bidders:
    name = input(f"what is your name?\n")
    bid = int(input(f"how much are u willing to bid?\n$"))
    bidders[name] = bid
    hh = input("any more bidders? tyype 'y' for yes and 'n' for no\n")
    if hh == 'n':
         more_bidders = False
n = 0
for bidd in bidders:
    highest = bidders[bidd]
    if highest > n:
        n = highest
        winner = bidd
print(bidders)
print("thank you for participating in this auction")
print(f"The winner goes to {winner} with a bid of ${n} ")