# Entertainer Data Analysis

<h5>
 This is Analysis of Entertainer Data in which the Key columns are include Entertainer(Name), Gender, Birth Year, Year of Breakthrough/#1 Hit/Award Nomination, Breakthrough Name, Year of First Oscar/Grammy/Emmy, Year of Last Major Work (arguable), Year of Death, Award Won from Breakthrough, Total Awards won, Total Nominees, Profession, Oscar won, Grammy won, Emmy won, and Other Awards.
  
<!-- ![image](https://github.com/shashikant190/Entertainer-Data-Analysis/assets/114300191/8b43bb06-f916-49f8-9ea2-ab382f072c00) -->

 </h5>
<h4>
Let's start from Jupyter Notebook -
  <br>
  <br>
  <p>to import python libraries</p> 
</h4>

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
