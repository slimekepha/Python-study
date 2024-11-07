# Write a program that takes input of someone's basic salary and benefits, adds them to fin
# d the gross salary then uses  the gross salary to find the NHIF. 
# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate  using 6% of the Gross Salary. BUT ONLY A MINIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF. 
# Continue with the same program and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015
# Calculate the taxable income.
# i.e taxable_income = gross salary - (NSSF + NHDF + NHIF) 
# Continue with the same program and find the person's PAYEE using the taxable income above.
# Continue with the same program and calculate an individual’s Net Salary using:
#  net_salary = gross_salary - (nhif + nhdf +  nssf + payee)







def calc_gross(basic_salary, benefits):
    gross = basic_salary + benefits
    return gross

basic_salary = float(input("Enter the basic salary: "))
benefits = float(input("Enter the benefits: "))
gross_salary = calc_gross(basic_salary, benefits)
print("Gross Salary:", gross_salary)

def calc_nhif(gross):
    if gross <= 5999:
        nhif = 150
    elif gross <= 7999:
        nhif = 300
    elif gross <= 11999:
        nhif = 400
    elif gross <= 14999:
        nhif = 500
    elif gross <= 19999:
        nhif = 600
    elif gross <= 24999:
        nhif = 750
    elif gross <= 29999:
        nhif = 850
    elif gross <= 34999:
        nhif = 900
    elif gross <= 39999:
        nhif = 950
    elif gross <= 44999:
        nhif = 1000
    elif gross <= 49999:
        nhif = 1100
    elif gross <= 59999:
        nhif = 1200
    elif gross <= 69999:
        nhif = 1300
    elif gross <= 79999:
        nhif = 1400
    elif gross <= 89999:
        nhif = 1500
    elif gross <= 99999:
        nhif = 1600
    else:
        nhif = 1700
    return nhif

nhif_con = calc_nhif(gross_salary)
print("NHIF Contribution:", nhif_con)


def calc_nssf(gross):
    if gross>18000:
        nssf=18000*0.06
    else:
        nssf=gross*0.06
    return nssf

nssf_con=calc_nssf(gross_salary)
print(f"NSSF contribution is: {nssf_con}")


def calc_nhdf(gross):
    nhdf=gross_salary*0.015
    return nhdf

nhdf_con=calc_nhdf(gross_salary)
print(f"NHDF contribution is: {nhdf_con}")

def calc_taxable_income(tax):
    taxincome=gross_salary-(nhif_con+nssf_con+nhdf_con)
    return taxincome
taxable_income=calc_taxable_income(gross_salary)
print(taxable_income)