"""
Approach: Greedy: Eg array: [[1, 2], [3, 4], [0, 6], [5, 7], [8, 9], [5, 9]]
      TC:O(nlogn) SC:O(n)
      
      a. Sort the array in order of endtime ie, 2nd element. We will get [[1, 2], [3, 4], [0, 6], [5, 7], [8, 9], [5, 9]]
      b. Initialize Count = 1 and endTime = times[0][1]
      c. Loop from 1 to n and check if strt time of any meet is greater than endtime ie, times[i][0] > endtime
      d. If yes than endtime = times[i][1] count += 1
      
  GFG: https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1#
  YT: https://www.youtube.com/watch?v=II6ziNnub1Q
"""

 def maximumMeetings(self,n,start,end):
        times = []
        for i in range(n):
            times.append([start[i], end[i]])
            
        times.sort(key=lambda x: x[1])
        
        c = 1
        endtime = times[0][1]
        for i in range(1, n):
            if endtime < times[i][0]:
                endtime = times[i][1]
                c += 1
        return c
      
      
