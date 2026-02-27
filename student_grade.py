
def score_card (num):
  if num >= 75:
    return "A"
  elif num >= 60:
    return "B"
  elif num >= 40:
    return "C"
  else:
    return "F"


student_name = input("Enter student Name: ")
Physics = int(input("Enter Physics marks: "))
Chemistry = int(input("Enter Chemistry marks: "))
Maths = int(input("Enter Maths marks: "))

total = (Physics + Chemistry + Maths) / 300
percentage = (total) * 100

print(f"Name: {student_name}\nPercentage: {percentage}%")
print("Grade:", score_card(percentage))
