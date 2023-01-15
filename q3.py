from csv import DictReader
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('TkAgg')


def calculate(mhdata, allpincodes):
    '''to calculate'''
    address = []
    for details in mhdata:
        fullyear = details['DATE_OF_REGISTRATION']
        if (fullyear[-2:]) == '15':
            address.append(details['Registered_Office_Address'][-6:])

    pincodes = []
    districts = []
    for pincode in allpincodes:
        pincodes.append(pincode['pincode'])
        districts.append(pincode['district'])
    print(pincodes)
    count = [0]*len(pincodes)

    for pincode in mhdata:
        fullyear = pincode['DATE_OF_REGISTRATION']
        if ((fullyear[-2:]) == '15' and
                pincode['Registered_Office_Address'][-6:] in pincodes):
            pin = pincode['Registered_Office_Address'][-6:]
            index = pincodes.index(pin)
            value = count[index]
            value = value+1
            count[index] = value

    print(count)
    pincode_count = dict(zip(pincodes, count))

    print(pincode_count)
    registration_count_distictwise = [0]*len(districts)

    districts_and_registration_count = dict(
        zip(districts, registration_count_distictwise))

    print(districts_and_registration_count)

    for pincode in pincodes:
        index = pincodes.index(pincode)
        value = count[index]
        district = districts[index]
        print(district)
        count_each_district = districts_and_registration_count.get(
            district)
        count_each_district += value
        districts_and_registration_count[district] = count_each_district
    print(districts_and_registration_count)
    return districts_and_registration_count


def plot(uniquedistricts, finalcountofregistrations):
    '''to plot'''

    _, aux = plt.subplots()

    blabels = uniquedistricts

    aux.bar(blabels, finalcountofregistrations, label=blabels, color='green')

    aux.set_ylabel('No of registration')

    aux.set_title('Years')

    plt.show()


if __name__ == "__main__":
    mh_data = []
    overall_pincodes = []
    file = open("Maharashtra.csv", "r", encoding="latin-1")
    maharastradata = DictReader(file)

    for Authorized_Cap_values in maharastradata:
        mh_data.append(Authorized_Cap_values)

    file1 = open("pincodes.csv", "r", encoding="latin-1")
    all_pincodes = DictReader(file1)

    for pins in all_pincodes:
        overall_pincodes.append(pins)

    districts_and_regist_count = calculate(mh_data, overall_pincodes)
    print(districts_and_regist_count)
    plot(districts_and_regist_count.keys(),
         districts_and_regist_count.values())
