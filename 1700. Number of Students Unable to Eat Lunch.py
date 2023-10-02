from collections import deque


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


# using queue package


class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        students_queue = deque(students)
        sandwiches_queue = deque(sandwiches)

        while students_queue:
            student = students_queue.popleft()  # popleft means from the front
            sandwich = sandwiches_queue[0]

            if student == sandwich:
                sandwiches_queue.popleft()
            else:
                # If no student can be satisfied, break the loop
                if all(s != sandwich for s in students_queue):
                    break
                students_queue.append(student)

        return len(students_queue)
