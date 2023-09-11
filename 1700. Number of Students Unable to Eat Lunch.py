class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        while students:
            student = students[0]
            if student == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                # If no student can be satisfied, break the loop
                if all(s != sandwiches[0] for s in students):
                    break
                students.append(students.pop(0))
        return len(students)
