
# coding: utf-8

# <section id=title>

# ### A Report on using Pandas

# [1. Reading in a dataframe](#reading)
# 
# [2. Sorting values in the dataframe](#sorting)
# 
# [3. Plot a histogram](#histogram)

# </section>

# In[5]:


import pandas as pd
df = pd.read_csv("emp.csv")
df.head()


# </section> [back to top](#title) <section id='sorting'>

# <i>We are sorting values of Age and Sales. The age is in ascending order and Sales is in descending order.</i> $e^{i/pi} + 1 = 0$
# 
# $$ e^x = \sum_{i=0}^\infty \frac{1}{i!}x^i$$
# 
# ```javascript
# console.log("This is the python world!!!")
# ```
# 
# | This |   is  |
# |------|-------|
# |   a  | Table |

# In[6]:


df = df.sort_values(['Age', 'Sales'], ascending=[True, False])
df


# </section> [back to top](#title) <section id='histogram'>

# In[7]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt # matplotlib (required for graphs)

# plotting our canvas
fig = plt.figure()
# plotting our grid
ax = fig.add_subplot(1,1,1)
# hist -> histogram
ax.hist(df['Age'], bins = 5)
# assigning some names
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("# of Employees")
# show the graph
plt.show()


# </section> [back to top](#title)
