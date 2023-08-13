import pandas as pd
dict={"regno":['sjc24cs067','sjc24cs068','sjc24cs069'],
      'name':['Rahul','Hari','Christy'],
      'physics':[78,90,66],
      'chemistry':[67,88,88],
      'maths':[95,77,55]}
df=pd.DataFrame(dict)
df.to_csv('mark.csv')