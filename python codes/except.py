try:
    age=int(input("Age: "))
    print(age)
    income=100000
    Avg_Salary = income/age
    print(Avg_Salary)
except ValueError:
    print("invalid value")
except ZeroDivisionError:
    print("age can't be 0.")