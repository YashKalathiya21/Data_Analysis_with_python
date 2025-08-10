import pandas as pd

def demographic_data:

	df = pd.read_csv('/Users/yashkalathiya/Downloads/Yash/Data Analyst Portfolio Projects/census+income/Census.csv')
	df.columns = ['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','salary']

	# How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
	raceGrp = df.groupby('race')[['race']].count()  #or using value_count --- raceGrp = df['race'].value_count()
	print(raceGrp)

	# What is the average age of men?
	averageAge = df[['sex','age']].copy().groupby('sex').mean()
	print(round(averageAge.iloc[1],1))

	# What is the percentage of people who have a Bachelor's degree?
	bachelorDegreeHolders = df.groupby('education')[['education']].count()
	bachelorDegreeHolders = bachelorDegreeHolders.iloc[9]
	bachelorDegreeHolderPercentage = round (bachelorDegreeHolders/df.shape[0] * 100,1)
	print(bachelorDegreeHolderPercentage)

	# What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K
	df2 = df.copy()
	df2 = df2[df2['education'].isin([' Bachelors', ' Masters', ' Doctorate'])]
	advancedPeopleCount = df2[df2['salary'] == ' >50K'].count()
	totalPeople = df2.shape[0]
	percentageValue = round((advancedPeopleCount / totalPeople) * 100,1)
	print(percentageValue)

	# What percentage of people without advanced education make more than 50K?
	df2 = df[['education','salary']].copy()
	df2 = df[~df['education'].isin([' Bachelors', ' Masters', ' Doctorate'])]
	notAdvancedPeopleCount = df2[df2['salary'] == ' >50K'].count()
	percentageValue = round((notAdvancedPeopleCount/totalPeople) * 100,1)
	print(percentageValue)

	# What is the minimum number of hours a person works per week?
	min_work_hr = df['hours-per-week'].min()
	print(min_work_hr)

	# What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
	df2 = df[['hours-per-week','salary']].copy()
	df2 = df2[df2['salary'] == ' >50K']
	peopleWithMoreSalary = len(df2)
	peopleWithMinHr = df2[df2['hours-per-week'] == min_work_hr].count()
	percentage = round((peopleWithMinHr / peopleWithMoreSalary) * 100, 1)
	print(percentage)

	# What country has the highest percentage of people that earn >50K and what is that percentage?

	df2 = df.copy()
	highest_earning_country = None
	highest_earning_country_percentage = 0
	for country, data in df2.groupby('native-country'):
    percentage = (df2['salary'] == ' >50K').sum() / df2['salary'].count()
    if highest_earning_country_percentage < percentage :
        highest_earning_country_percentage = percentage
        highest_earning_country = country

	highest_earning_country_percentage = round(highest_earning_country_percentage,1)
	print(highest_earning_country_percentage)

	# Identify the most popular occupation for those who earn >50K in India.
	topOccupationInIndia = df2[(df2['salary'] == ' >50K') & (df2['native-country'] == ' India')]['occupation'].value_counts().keys()[0]



