def job_scheduling(jobsList):
    jobsList.sort(key=lambda x: x[2], reverse=True)
    maxDeadline = max(jobsList, key=lambda x: x[1])[1]
    schedule = [-1] * (maxDeadline + 1)
    profit = 0
    for job in jobsList:
        deadline = job[1]
        for i in range(deadline, 0, -1):
            if schedule[i] == -1:
                profit += job[2]
                break

    return profit


jobs = [(1, 9, 15), (2, 2, 2), (3, 5, 18), (4, 7, 1), (5, 4, 25)]
total_profit = job_scheduling(jobs)

print("Total Profit:", total_profit)
