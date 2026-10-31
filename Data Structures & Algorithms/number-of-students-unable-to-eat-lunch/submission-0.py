class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        while sandwiches:
            if students[0] == sandwiches[0]:
                count = 0
                sandwiches.pop(0)
                students.pop(0)

            #if all the students have been seen without any matching a sandwhich preference
            count += 1
            if count > len(students):
                break
            students.append(students.pop(0))
            
        return len(students)
            

        