# Salary Calculator

gross_salary = float(input("Gross Salay: "))  
    
match gross_salary:
    case _ if gross_salary >= 0:
        pension = round(gross_salary * 0.07,2)
        match gross_salary:
            case _ if gross_salary < 600:
                tax = 0
            case _ if gross_salary < 1650:
                tax = gross_salary * 0.1 - 60
            case _ if gross_salary < 3200:
                tax = gross_salary * 0.15 - 142.5
            case _ if gross_salary < 5250:
                tax = gross_salary * 0.2 - 302.5
            case _ if gross_salary < 7800:
                tax = gross_salary * 0.25 - 565
            case _ if gross_salary < 10900:
                tax = gross_salary * 0.3 - 950
            case _:
                tax = gross_salary * 0.35 - 1500
        deduction = round(tax + pension,2)
        net_salary = round(gross_salary - deduction,2)   
        print(F"Gross Salary: {gross_salary}")
        print(F"Tax: ${round(tax,2)}")
        print(f"Pension: ${pension}")
        print(f"Deduction: ${deduction}")
        print(f"Net Salary: ${net_salary}")
    case _:
        print("Gross salary cannot be negative!")
    
    

# if gross_salary >= 0:    
#     pension = round(gross_salary * 0.07,2)
    
#     if gross_salary < 600:
#         tax = 0
#     elif  gross_salary < 1650:
#         tax = gross_salary * 0.1 - 60
#     elif  gross_salary < 3200:
#         tax = gross_salary * 0.15 - 142.5
#     elif gross_salary < 5250:
#         tax = gross_salary * 0.2 - 302.5
#     elif gross_salary < 7800:
#         tax = gross_salary * 0.25 - 565
#     elif gross_salary < 10900:
#         tax = gross_salary * 0.3 - 950
#     else:
#         tax = gross_salary * 0.35 - 1500
#     deduction = round(tax + pension,2)
#     net_salary = round(gross_salary - deduction,2)

#     print(F"Gross Salary: {gross_salary}")
#     print(F"Tax: ${round(tax,2)}")
#     print(f"Pension: ${pension}")
#     print(f"Deduction: ${deduction}")
#     print(f"Net Salary: ${net_salary}")
# else:
#     print("Gross salary cannot be negative!")
    