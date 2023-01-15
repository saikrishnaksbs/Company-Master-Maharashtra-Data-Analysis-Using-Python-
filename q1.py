from decimal import Decimal
from csv import DictReader
from matplotlib import pyplot as plt


def calculate(mhdata):
    '''to calculate'''
    cap_values = []
    for company in mhdata:
        temp = int(Decimal(company["AUTHORIZED_CAP"]))
        # print(type(temp))
        cap_values.append(temp)
    return cap_values


def plot(cap_values):
    '''to plot'''
    max_value = max(cap_values)
    bins_value = [0, 100001, 1000001, 10000001,
                  100000001, max_value+1]
    labels = ['<1L', '1L-10L', '10L-1Cr', '1Cr-10Cr', '>10cr']
    xtics_value = [7e+4, 3e+5, 3e+6, 3e+7, 1e+10]
    plt.hist(cap_values, bins_value, ec='black')
    plt.xscale('log')
    plt.xticks(xtics_value, labels)
    plt.xlabel("Cap Amount")
    plt.ylabel("Number of Companies")
    plt.title("Cap Values")
    plt.tight_layout()
    plt.show()


m_h_data = []
file = open("Maharashtra.csv", "r", encoding="latin-1")
maharastradata = DictReader(file)

for Authorized_Cap_values in maharastradata:
    m_h_data.append(Authorized_Cap_values)

Authorized_cap_values = calculate(m_h_data)
plot(Authorized_cap_values)
