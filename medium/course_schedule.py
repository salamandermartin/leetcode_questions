class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i : 0 for i in range(numCourses)}
        into = {i : [] for i in range(numCourses)}
        
        for course, pre in prerequisites:
            prereqs[course] += 1
            into[pre].append(course)
            
        queue = deque([c for c in prereqs if prereqs[c] == 0])
        count = 0
        
        while queue:
            curr = queue.popleft()
            count += 1
            
            for next_course in into[curr]:
                prereqs[next_course] -= 1
                
                if prereqs[next_course] == 0:
                    queue.append(next_course)
                    
        return count == numCourses