import math

# Current Monetary Information request
def financialInfoRequest(): 
    print("Enter your annual salary:")
    salary = float(input())
    print("Enter the percent of your salary to save, as a decimal:")
    portion = float(input())
    print("Enter the cost of your dream home:")
    cost = float(input())
    print("Enter the semi-annual raise, as a decimal")
    percentRaise = float(input())
    return salary, portion, cost, percentRaise
    
def calcSavingTime(salary, portion, cost, annualReturn, percentRaise):
    savingsBal = 0
    monthsReq = 0
    portion = cost * 0.25 # Present Value
    while(savingsBal <= portion):
        savingsBal += (savingsBal * annualReturn / 12)
        savingsBal += (salary / 12 * portion)
        monthsReq += 1
        if(monthsReq % 6 == 0):
            salary += (salary * percentRaise)
    return monthsReq

# def calcBestSavingRate(salary, portion, cost, annualReturn, percentRaise):
#     recommendSavPortion = 0.0


#     return recommendSavPortion


annualSalary, portionSaved, totalHouseCost, semiAnnualRaise = financialInfoRequest();
monthsReq4DownPayment = calcSavingTime(annualSalary, portionSaved, totalHouseCost, 0.04, semiAnnualRaise)
print("You need to save for " + str(monthsReq4DownPayment) + " months to meet your downpayment.")

# def futureValueLumpSum(r, n , pv):
#     fv = pv * (1 + r) ** n
#     print(fv) 

# def presentValueLumpSum(r, n, fv):
#     pv = fv / ((1 + r) ** n)
#     print(pv)

