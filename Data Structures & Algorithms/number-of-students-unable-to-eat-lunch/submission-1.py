from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        #[1100] student stack
        #[0101] sandwhcih stack
        rem = len(students)
        cnt = Counter(students)
        for sand in sandwiches:
            if cnt[sand] == 0:
                return rem
            cnt[sand] -= 1 
            rem -= 1
        return 0






        
        
        