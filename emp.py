print("Welcome to the Employee Performance Evaluation System!")

employee_name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")
department = input("Enter employee department: ")

print("\nEmployee Information:")
print("Name:", employee_name)
print("ID:", employee_id)
print("Department:", department)

print("\nEvaluation Criteria:")
print("1. Communication Skills")
print("2. Teamwork")
print("3. Problem Solving")
print("4. Punctuality")
print("5. Overall Performance")

communication_skills = int(input("\nEnter rating (1-5) for Communication Skills: "))
teamwork = int(input("Enter rating (1-5) for Teamwork: "))
problem_solving = int(input("Enter rating (1-5) for Problem Solving: "))
punctuality = int(input("Enter rating (1-5) for Punctuality: "))

overall_performance = (communication_skills + teamwork + problem_solving + punctuality) / 4

print("\nEmployee Performance Summary:")
print("Name:", employee_name)
print("ID:", employee_id)
print("Department:", department)
print("Communication Skills:", communication_skills)
print("Teamwork:", teamwork)
print("Problem Solving:", problem_solving)
print("Punctuality:", punctuality)
print("Overall Performance:", overall_performance)

if overall_performance >= 4.0:
    print("Excellent performance! Keep up the good work!")
elif overall_performance >= 3.0:
    print("Good performance. There is room for improvement.")
elif overall_performance >= 2.0:
    print("Average performance. Work on enhancing your skills.")
else:
    print("Below average performance. Immediate action needed to improve.")
