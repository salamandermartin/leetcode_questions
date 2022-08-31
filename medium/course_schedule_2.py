class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = {i : set() for i in range(numCourses)}
        into = {i : [] for i in range(numCourses)}
        
        for course, pre in prerequisites:
            prereqs[course].add(pre)
            into[pre].append(course)
        
        output = []
        queue = deque([c for c in prereqs if len(prereqs[c]) == 0])
        
        
        while queue:
            curr = queue.popleft()
            
            output.append(curr)
            
                
            for next_course in into[curr]:
                if curr in prereqs[next_course]:
                    prereqs[next_course].remove(curr)
                    if len(prereqs[next_course]) == 0:
                        queue.append(next_course)
        
        if len(output) < numCourses:
            return []
        return output