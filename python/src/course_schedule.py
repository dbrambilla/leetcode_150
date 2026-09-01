from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # 1. Build adjacency list and indegree tracker
        adj = defaultdict(list)
        indegrees = [0] * numCourses
        
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegrees[course] += 1
            
        # 2. Push all courses with 0 prerequisites into the queue
        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
        courses_taken = 0
        
        # 3. Process the queue
        while queue:
            current = queue.popleft()
            courses_taken += 1
            
            # Decrement neighbor indegrees
            for neighbor in adj[current]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
                    
        # 4. If we successfully took all courses, no cycle exists
        return courses_taken == numCourses
