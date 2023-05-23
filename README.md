# Entertainer Data Analysis

<h5>
 This is Analysis of Entertainer Data in which the Key columns are include Entertainer(Name), Gender, Birth Year, Year of Breakthrough/#1 Hit/Award Nomination, Breakthrough Name, Year of First Oscar/Grammy/Emmy, Year of Last Major Work (arguable), Year of Death, Award Won from Breakthrough, Total Awards won, Total Nominees, Profession, Oscar won, Grammy won, Emmy won, and Other Awards.
 </h5>

<h2>
Let's start from Jupyter Notebook 
  <br>
  <br>
  <p>to import python libraries</p> 
</h2>

```python
import numpy as np
```
```python
import pandas as pd
```
<h4>
To import excel file which consist the dataset
</h4>

```python
data = pd.read_excel(r'C:\Users\mshas\Data Analytics Dashboard\Entertainers Data Analysis\Entertainer - Final.xlsx')
```
<h4>
To see some datas to understand the columns and rows
</h4>

```python
data.head()
```

# Graph data


<h3>
Q. How many entertainers are there in each gender category ?
</h3>

```python
genders = data['Gender (traditional)'].to_numpy()
```
```python
unique_genders, gender_counts = np.unique(genders, return_counts=True)
```
```python
plt.bar(unique_genders, gender_counts)
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Number of Entertainers by Gender')
plt.show()
```
<h3>
OUTPUT 
</h3>

![image](https://github.com/shashikant190/Entertainer-Data-Analysis/blob/main/assets/Graph11.png?raw=true)

<h3>
Q. What are the top 10 entertainers with the most awards?
</h3>

```python
sorted_data = data.sort_values(by='Total Awards won', ascending=False)
```
```python
top_10 = sorted_data.head(10)
```
```python
entertainer_names = top_10['Entertainer'].to_numpy()
```
```python
awards_counts = top_10['Total Awards won'].to_numpy()
```
```python
plt.barh(entertainer_names, awards_counts)
plt.xlabel('Total Awards')
plt.ylabel('Entertainer Name')
plt.title('Top 10 Entertainers with the Most Awards')
plt.show()
```
<h3>
OUTPUT 
</h3>

![image](https://github.com/shashikant190/Entertainer-Data-Analysis/blob/main/assets/Graph12.png?raw=true)

<h3>
Q. How many entertainers belong to each profession category?
</h3>

```python
professions = data['Profession'].to_numpy()
```
```python
unique_professions, profession_counts = np.unique(professions, return_counts=True)
```
```python
plt.bar(unique_professions, profession_counts)
plt.xlabel('Profession')
plt.ylabel('Count')
plt.title('Number of Entertainers by Profession')
plt.xticks(rotation=90)
plt.show()
```

<h3>
OUTPUT 
</h3>

![image](https://github.com/shashikant190/Entertainer-Data-Analysis/blob/main/assets/Graph13.png?raw=true)

<h2>
Now Let's overlook the Power Bi Dashboard -
</h2>

<h3>
Here, The Entertainer Data Analysis data which consists of the following action elements :
<br>
<br>
<ul>
<li>Cards</li>
<li>Slicer</li>
<li>Pie Chart</li>
<li>Stacked Column Chart</li>
<li>Stacked Bar Chart</li>
</ul>

</h3>
<h3>
    Here, We used 8 cards elements which shows us the data about 
    <ol>
    <li>Awards Won</li>
    <li>Total Nominees</li>
    <li>Oscar Won</li>
    <li>Emmy Won</li>
    <li>Profession</li>
    <li>First Award won from Breakthrough</li>
    <li>Entertainer Name</li>
    <li>First Breakthrough Name</li>
    </ol>
</h3>

<p>This is The Entertainer Data of all Entertainers Combined as well as compared.</p>

![image](https://github.com/shashikant190/Entertainer-Data-Analysis/blob/main/assets/FullDashboard.png?raw=true)


<p>This is The Entertainer Data of a single Entertainer. Here we have selected Gene Hackman.</p>

![image](https://github.com/shashikant190/Entertainer-Data-Analysis/blob/main/assets/SigleEntertainerDashboard.png?raw=true)

# The Dashboard file

https://github.com/shashikant190/Entertainer-Data-Analysis/raw/main/Entertainer%20Data%20Analysis.pbix


# The Dashboard Video

https://drive.google.com/file/d/146Lk7DULDmsIhrFbiFFZzcXNVc38PEr-/view?usp=share_link

