def average(*numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def make_course(code, **details):
    return {"code": code, **details}


print(average(70, 80, 90))  
print(average(100))         
print(average())           

print(make_course("CE101", title="Fundamentals of Programming", credits=6))
