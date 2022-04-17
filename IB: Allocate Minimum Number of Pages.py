"""
  Approach: 
            
            1. Using Binary Search: TC: O( n log n)   SC: O(1)
                
                Intution: The minimum number of pages must lie b/w max(arr) and sum(arr)
                          so we will find mid by using above to values, If by using
                          mid as max amount of pages that can be allocated to stud
                          we can allocate books to all stud than its probabal ans so will 
                          shift r = mid-1 else l = mid+1
                         
                   a. l, r = max(arr), sum(arr)
                   b. while l <= r:
                   c. if canAllocate(mid, std) ie, we can allocate books to all studs by taking upper bound as mid
                   d. than res = mid and r = mid-1
                   e. Else: l = mid + 1
                   
                   for canAllocate:
                        a. take initial student stud = 1 and pages = 0
                        b. for p in arr: if ele > mid: return False
                        c. if pages + ele > mid: stud += 1, pages = ele
                        d. else: pages += ele
                        
                        return stud > std
                        
IB: https://www.interviewbit.com/problems/allocate-books/
YT: https://www.youtube.com/watch?v=gYmWHvRHu-s
"""

def books(self, arr, std):

		def canAllocate(mid, std):
			stud, pages = 1, 0
			for i in arr:
				if i > mid: return False
				if pages + i > mid:
					stud += 1
					pages = i
				else:
					pages += i

			return stud <= std


		res = -1
		n = (len(arr))
		if std > n: return -1

		l, r = max(arr), sum(arr)
		while l <= r:

			mid = (l+r) >> 1

			if canAllocate(mid, std):
				res = mid
				r = mid-1
			else: 
				l = mid+1

		return res
    
    
