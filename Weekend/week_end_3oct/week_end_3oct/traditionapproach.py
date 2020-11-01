from week_end_3oct.sample import getemployess_list
emplist = getemployess_list(5)
print(emplist)


def apply_bonus():
    for emp in emplist:
        if emp.empAge>50:
            emp.bonus = emp.empSal*1.10


apply_bonus()


print(emplist)