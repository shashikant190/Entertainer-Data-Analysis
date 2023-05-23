import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel(r'C:\Users\mshas\Data Analytics Dashboard\Entertainers Data Analysis\Entertainer - Final.xlsx')
data.head()

# 1. How many male and female entertainers are there ?

print(data.columns)

genders = data['Gender (traditional)'].to_numpy()
unique_genders, gender_counts = np.unique(genders, return_counts=True)
gender_count_dict = dict(zip(unique_genders, gender_counts))
for gender, count in gender_count_dict.items():
    print(f"Number of {gender} entertainers: {count}")

# 2. How many Entertainers had a Breakthrough in the year 2000 or later ?

entertainer_names = data['Entertainer'].to_numpy()
breakthrough_years = data['Year of Breakthrough/#1 Hit/Award Nomination'].to_numpy()
indices = np.where(breakthrough_years >= 2000)[0]
for i in range(4):
    index = indices[i]
    name = entertainer_names[index]
    year = breakthrough_years[index]
    print(f"Entertainer: {name}, Breakthrough Year: {year}")

# 3. who is the oldest Entertainer in the dataset ?

birth_years = data['Birth Year'].to_numpy()
oldest_index = np.argmin(birth_years)
oldest_entertainer = data.loc[oldest_index, 'Entertainer']
print("Oldest Entertainer:", oldest_entertainer)

# 4. How many Entertainers have won an Oscar ?

entertainer_names = data['Entertainer'].to_numpy()
oscar_won = data['Oscar Won'].to_numpy()
indices = np.where(oscar_won > 0)[0]
print("Entertainers who have won an Oscar:")
for index in indices:
    name = entertainer_names[index]
    print(name)
num_oscar_winners = np.sum(oscar_won > 0)
print("Number of entertainers who have won an Oscar:", num_oscar_winners)

# 5. How many Entertainers have won awards other than Oscar, Grammy or Emmy ?

other_awards = data['Other Awards '].to_numpy()
num_other_award_winners = np.sum(other_awards > 0)
print("Number of entertainers who have won other awards:", num_other_award_winners)

# 6. What is the average number of awards won by Entertainers ?

awards_won = data['Total Awards won'].to_numpy()
average_awards_won = np.mean(awards_won)
average_awards_won = int(average_awards_won)
print("Average number of awards won by entertainers:", average_awards_won)

# 7. How many entertainers have received an Oscar, a Grammy, and an Emmy?

oscar_won = data['Oscar Won'].to_numpy()
grammy_won = data['Grammy Won'].to_numpy()
emmy_won = data['Emmy Won'].to_numpy()
indices = np.where((oscar_won > 0) & (grammy_won > 0) & (emmy_won > 0))
num_entertainers = len(indices[0])
print("Numer of Entertainers with an Oscar, a Grammy and an Emmy :", num_entertainers)

# 8. What is the percentage of Entertainers who have won an Award from their Breakthrough ?

award_won_from_breakthrough = data['Award Won from Breakthrough'].to_numpy()
num_entertainers_with_award = np.count_nonzero(award_won_from_breakthrough)
total_entertainers = data.shape[0]
percentage = (num_entertainers_with_award / total_entertainers) * 100
print("Percentage of entertainers who have won an award from their breakthrough:", percentage)

# 9. How many Entertainers have received a total of more than 50 awards ?

total_awards = data['Total Awards won'].to_numpy()
indices = np.where(total_awards > 50)
num_entertainers = len(indices[0])
print("Number of entertainers with more than 50 awards:", num_entertainers)

# 10. Determine the number of Entertainers who have not received awards in the dataset ?

total_awards = data['Total Awards won'].to_numpy()
indices = np.where(total_awards == 0)
num_entertainers = len(indices[0])
print("Number of entertainers with no awards:", num_entertainers)

# 11. How many entertainers are there in each gender category ?

genders = data['Gender (traditional)'].to_numpy()
unique_genders, gender_counts = np.unique(genders, return_counts=True)
plt.bar(unique_genders, gender_counts)
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Number of Entertainers by Gender')
plt.show()

# 12. What are the top 10 entertainers with the most awards?

sorted_data = data.sort_values(by='Total Awards won', ascending=False)
top_10 = sorted_data.head(10)
entertainer_names = top_10['Entertainer'].to_numpy()
awards_counts = top_10['Total Awards won'].to_numpy()
plt.barh(entertainer_names, awards_counts)
plt.xlabel('Total Awards')
plt.ylabel('Entertainer Name')
plt.title('Top 10 Entertainers with the Most Awards')
plt.show()

# 13 How many entertainers belong to each profession category?

professions = data['Profession'].to_numpy()
unique_professions, profession_counts = np.unique(professions, return_counts=True)
plt.bar(unique_professions, profession_counts)
plt.xlabel('Profession')
plt.ylabel('Count')
plt.title('Number of Entertainers by Profession')
plt.xticks(rotation=90)
plt.show()
