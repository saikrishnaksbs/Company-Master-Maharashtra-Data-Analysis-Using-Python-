import csv
import matplotlib.pyplot as plt


def calculate(princi_busi_activitydata):
    '''to calculate'''
    years = list(range(11, 21))
    years_and_activity = {}

    for princi_busi_activity in princi_busi_activitydata:

        if princi_busi_activity['DATE_OF_REGISTRATION'][-2:] != 'NA':

            year = int(princi_busi_activity['DATE_OF_REGISTRATION'][-2:])
            activity_name = princi_busi_activity[
                "PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN"]

        if year in years:

            if year not in years_and_activity:
                years_and_activity[year] = {}
                if activity_name not in years_and_activity[year]:
                    years_and_activity[year][activity_name] = 1
                else:
                    years_and_activity[year][activity_name] += 1
            else:
                if activity_name not in years_and_activity[year]:
                    years_and_activity[year][activity_name] = 1
                else:
                    years_and_activity[year][activity_name] += 1

    for year in years:
        sorted_activity = sorted(
            years_and_activity[year].items(), key=lambda x: x[1], reverse=True)
        print(sorted_activity[:5])
        convert_to_dict = dict(sorted_activity[:5])
        years_and_activity[year] = convert_to_dict

    years_and_activity = dict(sorted(years_and_activity.items()))

    print(years_and_activity)
    return years_and_activity


def tranform(years_and_activity):
    '''to transform'''

    final = list(years_and_activity.values())
    activitylist_count = []
    for year in range(10):
        count = list(final[year].values())
        activitylist_count.append(count)

    print(activitylist_count)
    activitylist_count_final = list(map(list, zip(*activitylist_count)))

    print(activitylist_count_final[0])
    return activitylist_count_final


def plot(years, activilist_count):
    '''for plotting'''
    bar_width = 0.1
    activilist_count_list = [[]]*5
    print(activilist_count_list)
    for i in range(5):
        if i == 0:
            activilist_count_list[i] = years
        else:
            activilist_count_list[i] = [j+bar_width
                                        for j in activilist_count_list[i-1]]

    plt.figure(figsize=(20, 5))
    for k in range(5):
        plt.bar(activilist_count_list[k],
                activilist_count[k],
                width=bar_width)

    plt.xticks(activilist_count_list[0], years)
    plt.legend()
    plt.show()


file = open("Maharashtra.csv", 'r', encoding="ISO-8859-1")
dataforprinciplebusinessactivity = csv.DictReader(file)
princibusiactivitydata = []
for dataforeachrow in dataforprinciplebusinessactivity:
    princibusiactivitydata.append(dataforeachrow)
# print(princibusiactivitydata)

years_and_activity_data = calculate(princibusiactivitydata)
activity_list_count = tranform(years_and_activity_data)
plot(list(years_and_activity_data.keys()), activity_list_count)
