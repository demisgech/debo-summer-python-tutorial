# Strings

# Slicing

course = "python programming"
        # 

print(course[0:3]) 
print(course[:3]) 
print(course[0])

print(course[3:])

# string methods
result = course.capitalize()
print(result)

count = course.count('m',1)
print(count)

result = course.replace('p','J')
result = course.find('p',1)

result = len(course)

result = course.endswith('G')
print(result)