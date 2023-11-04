def job_sequencing(job_list):
    # Sort the job list in descending order of profits.
    job_list.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job_list, key=lambda x: x[1])[1]
    schedule = [-1] * (max_deadline + 1)

    total_profit = 0

    for job in job_list:
        deadline = job[1]
        for i in range(deadline, 0, -1):
            if schedule[i] == -1:
                total_profit += job[2]
                break

    return total_profit


# Example usage:
jobs = [(1, 9, 15), (2, 2, 2), (3, 5, 18), (4, 7, 1), (5, 4, 25)]
total_profit = job_sequencing(jobs)

print("Total Profit:", total_profit)
