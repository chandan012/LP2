def job_sequencing(jobs):
    # Sort jobs by decreasing order of profits
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(jobs, key=lambda x: x[1])[1]
    slots = [-1] * (max_deadline + 1)  # Slots to track job assignments

    # Assign jobs to slots
    for job in jobs:
        deadline = job[1]
        # Find an available slot for the job
        while deadline > 0:
            if slots[deadline] == -1:
                slots[deadline] = job[0]
                break
            deadline -= 1

    # Get the job sequence
    sequence = [job for job in slots if job != -1]
    return sequence


# Take job input from the user
n = int(input("Enter the number of jobs: "))
jobs = []
for i in range(n):
    name = input("Enter the job name: ")
    duration = int(input("Enter the job duration: "))
    profit = int(input("Enter the job profit: "))
    jobs.append((name, duration, profit))

# Perform job sequencing
job_sequence = job_sequencing(jobs)
print("Job sequence:")
for job in job_sequence:
    print(job[0])
