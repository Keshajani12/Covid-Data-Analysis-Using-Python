import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Get data from csv file
df= pd.read_csv('Covid/covid_19_india.csv')
print(df.head())
print(df.tail())
print(df.shape)
print(df.describe())
print(df.info)
df=df.fillna(0)
print(df)

# Drop columns which are not required
df.drop(['Sno','Time','ConfirmedIndianNational','ConfirmedForeignNational'],axis=1,inplace=True)
print(df.head())

# Find active cases from data
df['ActiveCases']= df['Confirmed']-(df['Cured']+df['Deaths'])
print(df.head())

df['DeathRate']= df['Deaths']* 100/ df['Confirmed']
df['CuredRate']=df['Cured']* 100/ df['Confirmed']
print(df.head())
print(df.sort_values(by='Confirmed',ascending=False))

#  Create Lineplot using Seaborn
sns.lineplot(data=df,x=df['Deaths'] ,y=df['DeathRate'] ,errorbar=None)
plt.show()

sns.lineplot(data=df,x='Cured',y='CuredRate',errorbar=None)
plt.show()


sns.lineplot(data=df,x='Deaths',y='Cured',errorbar=None)
plt.show()

tenActiveCases= df.groupby(by='State/UnionTerritory').max()[['ActiveCases','Date']]\
    .sort_values(by=['ActiveCases'],ascending=False).reset_index()
print(tenActiveCases)

#  Create Barplot 

fig= plt.figure(figsize=(10,15))
plt.title('Top 10 Most Active Cases Statewise')
ax= sns.barplot(data=tenActiveCases.iloc[:10],x='State/UnionTerritory',y='ActiveCases',edgecolor='black',linewidth=2)
plt.xlabel('State/UnionTerritory')
plt.ylabel('ActiveCases')
plt.show()

x=df['Cured']
y1=df['CuredRate']
y2=df['Confirmed']
plt.bar(x,y1,color='r')
plt.bar(x,y2,bottom=y1,color='b')
plt.show()


sns.barplot(data=df,x='State/UnionTerritory',y='Deaths')
plt.show()

#  Create Scatterplot using Seaborn
sns.scatterplot(data=df,x='Cured',y='Confirmed')
plt.show()

# Split data into X (deaths) and y (cured)
x=df[['Deaths']]
y=df['Cured']

# Split data into X (cured) and y (confirmed)
# x=df[['Cured']]
# y=df[['Confirmed']]

x_train,x_test,y_train,y_test= train_test_split(x, y, train_size=0.3)
print(x_train.head())
print(x_test.head())

lr=LinearRegression()
lr.fit(x_train,y_train)
y_predict= lr.predict(x_test)
print(y_test.head())
print(y_predict[:5])

# Find mean value using prediction and test value
mse=mean_squared_error(y_test,y_predict)
print(mse)


# Create a DataFrame to hold the actual and predicted Cured data
record = pd.DataFrame({
    'Actual Cured': y_test,
    'Predicted Cured': y_predict
})

# Create a line plot using Seaborn
sns.lineplot(data=record)
plt.show()
