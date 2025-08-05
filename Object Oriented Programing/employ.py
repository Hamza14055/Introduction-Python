class employ :
    def salary(self,daily_wage,working_days):
        salary = daily_wage*working_days
        return salary
Days = employ()
print(Days.salary(700,15))