"""Problem 2

Problem 2: Kth Largest Element in a Stream
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums): Initializes the object with the integer k and the stream of integers nums.
int add(int val): Appends the integer val to the stream and returns the element representing the kth largest element in the stream.


Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

UMPIRE

U: 
- Are there any time/space constraints 
- Are we allowed to use inbuilt sorting methods from python 


M: 
- Stack 

P: 
- Make object class 
- initialize it with int element k and list nums
- adding method: 
    adds element to top of stack, sorts the stack 
    and returns kth largest element 
    
I:
Coded 

R:
Works good 

E:

O(nlog(n))

O(1)



"""
 

class MySolution:
    
    def __init__(self, k:int, nums: list[int]): 
        self.k = k 
        self.nums = nums 
        
    def add(self, val:int) -> int:
        self.nums.append(val)
        sorted_nums = sorted(self.nums, reverse=True)
        return sorted_nums[self.k-1]
    
    
solution = MySolution(k=3, nums=[4, 5, 8, 2])
print(solution.add(val=3))
print(solution.add(val=5))
print(solution.add(val=10))
print(solution.add(val=9))
print(solution.add(val=4))
    
    

### Better solution we came up with
class KthLargest:

  def __init__(self, k: int, nums: list[int]):
    self.k = k
    self.min_heap = []
    for num in nums:
      self.add(num)

  def add(self, val: int) -> int:
    heapq.heappush(self.min_heap, val)
    if len(self.min_heap) > self.k:
      heapq.heappop(self.min_heap)
    return self.min_heap[0]


"""
Problem 3: Number of Recent Calls
You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds 
(including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

Example 1:

Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3

UMPIRE

U:

"""

class RecentCounter:

    def __init__(self):
      self.stack = []

    def ping(self, t: int) -> int:
      self.stack.append(t)
      slicing_idx = 0 
      while self.stack[slicing_idx] < t - 3000: 
        slicing_idx+=1 
      return len(self.stack[slicing_idx:])

rc = RecentCounter()


print(rc.ping(1))
print(rc.ping(100))
print(rc.ping(3001))
print(rc.ping(3002))