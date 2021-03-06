"""
There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]

https://leetcode.com/problems/course-schedule-ii/
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        same as 207
        BFS approch and reverse at the end to get the topological order
        > create graph to have the index list with the prerequisites items in it.
        > create indegree to have the indexes having the indegree details.
        > create stack with all the indgree as 0 in it.
        """
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        
        # make graph relations
        for i, j in prerequisites:
            graph[i].append(j)
            indegree[j] += 1
        
        stack = []
        
        # for i in range(numCourses):
        #     if indegree[i]==0: stack.append(i)
        stack = [i for i in range(numCourses) if not indegree[i]]
            
        for i in stack:
            for j in graph[i]:
                indegree[j] -= 1
                if indegree[j] == 0: stack.append(j)

        return stack[::-1] if len(stack) == numCourses else []
