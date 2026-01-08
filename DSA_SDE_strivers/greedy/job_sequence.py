'''
Problem:
You are given a set of N jobs where each job comes with a deadline and profit.
The profit can only be earned upon completing the job within its deadline. 
Find the number of jobs done and the maximum profit that can be obtained. 
Each job takes a single unit of time and only one job can be performed at a time.

Core Idea:
- Schedule jobs with highest profit first.
- Assign each job to the latest available time slot on or before its deadline.
- This ensures maximum profit while meeting deadlines without overlapping jobs.

Approach:
- Sort jobs by profit in descending order — prioritize the most profitable jobs.
- Find the maximum deadline among all jobs — determines the maximum number of slots.
- Create an array of slots representing time units up to the max deadline, initially all free.
- For each job in sorted order:
  . Scan backward from the job's deadline to the earliest slot (1).
  . Assign the job to the first free slot found in this range.
  . If a slot is assigned, increment count and add profit.
- After processing all jobs, return:
  . Total number of jobs scheduled (count).
  . Total profit from scheduled jobs.


Time: O(N log N) [for sorting ]+ O(N*M) [for slot allocation in worst case
                                        (N = no. of jobs, D = max deadline).]
Space: O(D) [for slots array.]

'''

def job_schedules(jobs):
    jobs.sort(key = lambda x: x[2], reverse=True)
    max_slots = max(job[1] for job in jobs)

    slots = [0] * (max_slots + 1)

    count = 0
    total_profit = 0

    for job_id, deadline, profit in jobs:

        for slot in range(deadline, 0, -1):
            if slots[slot] == 0:
                slots[slot] = job_id
                count += 1
                total_profit += profit
                break
        
    return count, total_profit


#job id, deadline, profit
jobs = [
        (1, 2, 100),
        (2, 1, 19),
        (3, 2, 27),
        (4, 1, 25),
        (5, 1, 15)
]
jobs_done, max_profit = job_schedules(jobs)
print(jobs_done)
print(max_profit)
