"""
Idea:

Scenario [1]: Can take course because If I start the course now at t=time I will be able to finish it before its deadline
              append the course to the heap
              increment timer

Scenario [2]: Cannot take course because If I start the course now at t=time I will NOT be able to finish it before its deadline
              We need to revisit the courses we've decided we're gonna take so far and check the course with the longest duration
              Compare the curr course against that course and swap if the duration of curr course is greater than the course with longest duration so far

                Why are we doing this you ask? Because this means that there is a course that we decided previously we could take but in reality its affecting
                our ability to take more shorter courses. And since the priority is to take more courses -> we sacrifice the long course when we
                encounter a course that is shorter in duration in hopes we can maximize the number of courses we can take.

                The test upon which we base our decision is simple : Is the curr course shorter than the longest course we are planning to take so far?

                if yes: -> we swap for the reasons explained above
                if no: -> we do nothing and skip the iteration becuz the cur course is either as long as the (longest course so far) or even longer
                which means doing any modification is not gonna help us take more courses

        TC: 2NlogN      SC: N
   
   LeetCode 630: https://leetcode.com/problems/course-schedule-iii/
   Sol: https://leetcode.com/problems/course-schedule-iii/discuss/953918/Python-Max-Heap-Solution-with-detailed-explanation-and-comments
"""

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        courses.sort(key = lambda x: x[1])
        h = []
        totdur = 0
        
        for c in courses:
            
            if c[1] >= totdur + c[0]:
                totdur += c[0]
                heappush(h, -c[0])
            
            elif h and c[0] < -h[0]:
                totdur -= -heappop(h)
                totdur += c[0]
                heappush(h, -c[0])
                

        return len(h)
            
            
