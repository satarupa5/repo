import numpy as np
import pandas as pd
# creating a test dataframe
s = pd.Series([1,3,5,np.nan,6,8])
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df2 = pd.DataFrame({ 'A' : 1.,
                       'B' : pd.Timestamp('20130102'),
                         'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                         'D' : np.array([3] * 4,dtype='int32'),
                         'E' : pd.Categorical(["test","train","test","train"]),
                         'F' : 'foo' })
#variable type of each columns-- use attribute dtypes
df2.dtypes
#head and tail of the dataset
df2.head()
df2.tail()
#column headings
df2.columns
#quick summary
df2.describe()
#shows the numpy data in the same order
df2.values
#the column headings are sorted in ascending/descending order
df2.sort_index(axis = 1, ascending = False)
#sorting by values
df2.sort_values(by = 'B')
#selecting cols as a series, both codes are equivaent
df2.A
df2['A']
#slicing cols-- shows first 4 cols including index cols
df2[0:3]
#shows all the rows between the mentioned index values. Endpoints are included.
df['20130102' : '20130104']


