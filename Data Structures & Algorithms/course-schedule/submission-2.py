class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_graph = defaultdict(list)
        for c,pre in prerequisites:
            course_graph[c].append(pre)
        
        seen = set()

        def dfs(course):
            if course in seen:
                return False
            if course_graph[course] == []:
                return True
            
            seen.add(course)
            for p in course_graph[course]:
                if not dfs(p):
                    return False
            seen.remove(course)
            course_graph[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
