from csv import DictReader
from matplotlib import pyplot as plt


def calculate(mh_data):
    '''to calculate'''
    years = []
    companyid = []
    justyear = ''
    for details in mh_data:
        fullyear = details['DATE_OF_REGISTRATION']
        if fullyear != 'NA':
            justyear = fullyear[-2:]
            if int(justyear) in range(0, 22):
                years.append(int(justyear)+2000)
            else:
                years.append(int(justyear)+1900)
            companyid.append(details['CORPORATE_IDENTIFICATION_NUMBER'])
    # print(combined)
    yearsforplotting = list(set(years))
    print(yearsforplotting)
    companiescount = []
    del yearsforplotting[-1]
    for particularyear in yearsforplotting:
        noofcompanies = years.count(particularyear)
        companiescount.append(noofcompanies)
    print(yearsforplotting)
    print(companiescount)
    return [yearsforplotting, companiescount]


def plot(yearsforplotting, companiescount):
    '''to plot'''

    _, ax = plt.subplots()
    blabels = yearsforplotting
    ax.bar(blabels, companiescount, label=blabels, color='red')
    ax.set_ylabel('Total Companies')
    ax.set_title('Bar Plot of company registration by year')
    plt.show()


mhdata = []
file = open("Maharashtra.csv", "r", encoding="latin-1")
maharastradata = DictReader(file)

for Authorized_Cap_values in maharastradata:
    mhdata.append(Authorized_Cap_values)

company_registration_by_year = calculate(mhdata)
print(company_registration_by_year)
plot(company_registration_by_year[0], company_registration_by_year[1])
