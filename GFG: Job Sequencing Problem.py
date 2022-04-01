"""
Approach: eg: {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}

    intution: a job takes 1 unit of time to complete so if the deadline is n 
              than job can be done in any n-1 to 0 timeslot. so we will assign any n-1 to 0
              slot to job if any available and add the profit.
    
    a. sort the array based on profit
    b. create bool array of len max(deadline) initialized with False
    c. for each job if any (job.deadline-1 to 0) slot is available in bool array
       assign that slot to job and add profit
    return profit
    TC:O(N^2) SC:O(N)
    
 GFG: https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1#
 YT: https://www.youtube.com/watch?v=bID397v7ja4
 
 NOTE: each ele in job array is object of class Jobs with vals self.id, deadline, profit
"""
class Solution:
    def JobScheduling(self,jobs,n):
      
        njob = []
        
        maxdead = -1
        for i in jobs:
            maxdead = max(maxdead, i.deadline)
            njob.append([i.id, i.deadline, i.profit])
            
        njob = sorted(njob, key=lambda x: x[2], reverse=True)
        
        dead = [False] * maxdead
        profit = 0
        jb = 0
        for i in njob:
            for j in range(min(n, i[1]-1), -1, -1):
                if not dead[j]:
                   dead[j] = True
                   profit += i[2]
                   jb += 1
                   break
               
        return jb, profit
      
      
