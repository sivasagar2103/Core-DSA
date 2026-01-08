'''
Problem:


Approach:
- Sort students and cookies to pair smallest requirements first.
- Use two pointers to iterate through students and cookies.
- Assign cookies greedily whenever possible.
- Return total number of satisfied students.

Time: O(n log n + m log m)
Space: O(1)

'''

def assign_cookies(student, cookie):
    student.sort()
    cookie.sort()
    i, j = 0, 0 #i -- student, j == cookie
    assigned = 0

    while i < len(student) and j < len(cookie):
        if cookie[j] >= student[i]:
            #Assign cookie j to student i
            assigned += 1
            i += 1
            j += 1
        else:
            j+=1 #Current cookie too small, try next bigger cookie
    
    return assigned


student = [1, 2]
cookie = [1, 2, 3]
res = assign_cookies(student, cookie)
print(res)
