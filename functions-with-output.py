# def format_name(f_name, l_name):
#     print(f_name.title())
#     print(l_name.title())
# # format_name("uchenna", "nduka")
# year = int(input('enter a year:'))
# month = int(input("enter a month:"))
# def is_leap_year(year) :
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                  return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
# def days_in_month(year,month):
#     month_days = [31,28,31,30,31,30,31,31,31,31,30,31]
#     if is_leap_year(year) and month == 2:
#         return 29
#     return month_days[month-1]
# days = days_in_month(year, month)
# print(days)

print("calculator app")
def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def divid(n1,n2):
    return n1 / n2

def multiply(n1,n2):
    return n1 * n2

operators = {
    "+": add,
    "-": sub,
    "/": divid,
    "*": multiply,

}
n1 = int(input("whats ur first number?"))
n2 = int(input("whats ur second number?"))
for operation in operators:
    print(operation)
opp = input("pick a sysmbol")
bet = operators[opp]
answer = bet(n1,n2)
print(f"{n1} {opp} {n2} = {answer}")