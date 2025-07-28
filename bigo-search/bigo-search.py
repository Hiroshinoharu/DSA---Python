def checkStudent(student_list):
    for student in student_list:
        if student == 'Alice':
            return True
    return False


student_list1 = ['Bob', 'Charlie', 'Alice']
student_list2 = ['Bob', 'Charlie', 'David']

# Test cases
print(checkStudent(student_list1))  # Expected output: True
print(checkStudent(student_list2))  # Expected output: False