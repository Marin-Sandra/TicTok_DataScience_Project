#!/usr/bin/env python
# coding: utf-8

# # **TikTok Project**
# **Course 3 - Go Beyond the Numbers: Translate Data into Insights**

# Your TikTok data team is still in the early stages of their latest project. So far, you’ve completed a project proposal and used Python to inspect and organize the TikTok dataset.
# 
# Orion Rainier, a Data Scientist at TikTok, is pleased with the work you have already completed and is requesting your assistance with some Exploratory Data Analysis (EDA) and data visualization. The management team asked to see a Python notebook showing data structuring and cleaning, as well as any matplotlib/seaborn visualizations plotted to help us understand the data. At the very least, include a graph comparing claim counts to opinion counts, as well as boxplots of the most important variables (like “video duration,” “video like count,” “video comment count,” and “video view count”) to check for outliers. Also, include a breakdown of “author ban status” counts.
# 
# Additionally, the management team has recently asked all EDA to include Tableau visualizations. Tableau visualizations are particularly helpful in status reports to the client and board members. For this data, create a Tableau dashboard showing a simple claims versus opinions count, as well as stacked bar charts of claims versus opinions for variables like video view counts, video like counts, video share counts, and video download counts. Make sure it is easy to understand to someone who isn’t data savvy, and remember that the assistant director is a person with visual impairments.
# 
# You also notice a follow-up email from the Data Science Lead, Willow Jaffey. Willow suggests including an executive summary of your analysis to share with teammates.
# 
# A notebook was structured and prepared to help you in this project. Please complete the following questions.

# # **Course 3 End-of-course project: Exploratory data analysis**
# 
# In this activity, you will examine data provided and prepare it for analysis. You will also design a professional data visualization that tells a story, and will help data-driven decisions for business needs.
# 
# Please note that the Tableau visualization activity is optional, and will not affect your completion of the course. Completing the Tableau activity will help you practice planning out and plotting a data visualization based on a specific business need. The structure of this activity is designed to emulate the proposals you will likely be assigned in your career as a data professional. Completing this activity will help prepare you for those career moments.
# <br/>
# 
# **The purpose** of this project is to conduct exploratory data analysis on a provided data set. Your mission is to continue the investigation you began in C2 and perform further EDA on this data with the aim of learning more about the variables. Of particular interest is information related to what distinguishes claim videos from opinion videos.
# 
# **The goal** is to explore the dataset and create visualizations.
# <br/>
# *This activity has 4 parts:*
# 
# **Part 1:** Imports, links, and loading
# 
# **Part 2:** Data Exploration
# *   Data cleaning
# 
# 
# **Part 3:** Build visualizations
# 
# **Part 4:** Evaluate and share results

# Follow the instructions and answer the question below to complete the activity. Then, you will complete an executive summary using the questions listed on the PACE Strategy Document.
# 
# Be sure to complete this activity before moving on. The next course item will provide you with a completed exemplar to compare to your own work.

# # **Visualize a story in Tableau and Python**

# <img src="images/Pace.png" width="100" height="100" align=left>
# 
# # **PACE stages**

# Throughout these project notebooks, you'll see references to the problem-solving framework PACE. The following notebook components are labeled with the respective PACE stage: Plan, Analyze, Construct, and Execute.

# <img src="images/Plan.png" width="100" height="100" align=left>
# 
# 
# ## **PACE: Plan**
# 
# Consider the questions in your PACE Strategy Document and those below where applicable to craft your response:
# 1. Identify any outliers:
# 
# 
# *   What methods are best for identifying outliers?
# *   How do you make the decision to keep or exclude outliers from any future models?
# 
# 

# 1.Numpy functions can be used to identify the range of values and observe any outliers.
# Visualization can be used to identify outlier values.
# 2.Outliers can either be deleted, reassigned or kept as it is based on business objectives or dataset.

# ### **Task 1. Imports, links, and loading**
# Go to Tableau Public
# The following link will help you complete this activity. Keep Tableau Public open as you proceed to the next steps.
# 
# Link to supporting materials:
# Public Tableau: https://public.tableau.com/s/. Note that the TikTok dataset can be downloaded directly from this notebook by going to "Lab Files" in the menu bar at the top of the page, clicking into the "/home/jovyan/work" folder, selecting `tiktok_dataset.csv`, and clicking "Download" above the list of files. 
# 
# For EDA of the data, import the packages that would be most helpful, such as `pandas`, `numpy`, `matplotlib.pyplot`, and `seaborn`.
# 

# In[13]:


# Import packages for data manipulation
import pandas as pd
import numpy as np


# Import packages for data visualization
import matplotlib.pyplot as plt
import seaborn as sns


# Then, load the dataset into a dataframe. Read in the data and store it as a dataframe object.
# 
# **Note:** As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.
# 

# In[2]:


# Load dataset into dataframe
data = pd.read_csv("tiktok_dataset.csv")


# <img src="images/Analyze.png" width="100" height="100" align=left>
# 
# ## **PACE: Analyze**
# 
# Consider the questions in your PACE Strategy Document and those below where applicable to complete your code.

# ### **Task 2a: Data exploration and cleaning**
# 
# The first step is to assess your data. Check the Data Source page on Tableau Public to get a sense of the size, shape and makeup of the data set.
# 
# Consider functions that help you understand and structure the data.
# 
# *    `.head()`
# *    `.info()`
# *    `.describe()`
# *    `.groupby()`
# *    `.sort_values()`
# 
# Consider the following questions as you work:
# 
# What do you do about missing data (if any)?
# 
# Are there data outliers?

# Start by discovering, using `.head()`, `.size`, and `.shape`.

# In[3]:


# Display and examine the first few rows of the dataframe
data.head()


# In[5]:


# Get the size of the data
data.size


# In[6]:


# Get the shape of the data
data.shape


# Get basic information about the data, using `.info()`.

# In[7]:


# Get basic information about the data
data.info()


# Generate a table of descriptive statistics, using `.describe()`.

# In[8]:


# Generate a table of descriptive statistics
data.describe()


# ### **Task 2b. Assess data types**

# In Tableau, staying on the data source page, double check the data types of the columns in the dataset. Refer to the dimensions and measures in Tableau.
# 

# Review the instructions linked in the previous Activity document to create the required Tableau visualization.

# ### **Task 2c. Select visualization type(s)**

# Select data visualization types that will help you understand and explain the data.
# 
# Now that you know which data columns you’ll use, it is time to decide which data visualization makes the most sense for EDA of the TikTok dataset. What type of data visualization(s) would be most helpful? Consider the distribution of the data.
# 
# * Line graph
# * Bar chart
# * Box plot
# * Histogram
# * Heat map
# * Scatter plot
# * A geographic map
# 

# Box plot and Histogram

# <img src="images/Construct.png" width="100" height="100" align=left>
# 
# ## **PACE: Construct**
# 
# Consider the questions in your PACE Strategy Document to reflect on the Construct stage.

# ### **Task 3. Build visualizations**
# 
# Now that you have assessed your data, it’s time to plot your visualization(s).

# #### **video_duration_sec**
# 
# Create a box plot to examine the spread of values in the `video_duration_sec` column.

# In[15]:


# Create a boxplot to visualize distribution of `video_duration_sec`
plt.figure(figsize=(5,1))
plt.title('Video Duration')
sns.boxplot(x=data['video_duration_sec']);


# Create a histogram of the values in the `video_duration_sec` column to further explore the distribution of this variable.

# In[16]:


# Create a histogram
plt.figure(figsize=(5,3))
sns.histplot(data['video_duration_sec'],bins=range(0,61,5));


# **Question:** What do you notice about the duration and distribution of the videos?

#     All videos are about 5 to 60 seconds duration.

# #### **video_view_count**
# 
# Create a box plot to examine the spread of values in the `video_view_count` column.

# In[17]:


# Create a boxplot to visualize distribution of `video_view_count`
plt.figure(figsize=(5,1))
plt.title('video_view_count')
sns.boxplot(x=data['video_view_count']);


# Create a histogram of the values in the `video_view_count` column to further explore the distribution of this variable.

# In[18]:


# Create a histogram
plt.figure(figsize=(5,3))
sns.histplot(data['video_view_count'],bins=range(0,10**6+1,10**5));


# **Question:** What do you notice about the distribution of this variable?

# #### **video_like_count**
# 
# Create a box plot to examine the spread of values in the `video_like_count` column.

# In[21]:


# Create a boxplot to visualize distribution of `video_like_count`
plt.figure(figsize=(10,1))
plt.title('video_like_count')
sns.boxplot(x=data['video_like_count']);


# Create a histogram of the values in the `video_like_count` column to further explore the distribution of this variable.

# In[22]:


# Create a histogram
ax = sns.histplot(data['video_like_count'], bins=range(0,(7*10**5+1),10**5))
labels = [0] + [str(i) + 'k' for i in range(100, 701, 100)]
ax.set_xticks(range(0,7*10**5+1,10**5), labels=labels)
plt.title('Video like count histogram');


# **Question:** What do you notice about the distribution of this variable?

# #### **video_comment_count**
# 
# Create a box plot to examine the spread of values in the `video_comment_count` column.

# In[23]:


# Create a boxplot to visualize distribution of `video_comment_count`
plt.figure(figsize=(5,1))
plt.title('video_comment_count')
sns.boxplot(x=data['video_comment_count']);


# Create a histogram of the values in the `video_comment_count` column to further explore the distribution of this variable.

# In[24]:


# Create a histogram
plt.figure(figsize=(5,3))
sns.histplot(data['video_comment_count'], bins=range(0,(3001),100))
plt.title('Video comment count histogram');


# **Question:** What do you notice about the distribution of this variable?

# #### **video_share_count**
# 
# Create a box plot to examine the spread of values in the `video_share_count` column.

# In[25]:


# Create a boxplot to visualize distribution of `video_share_count`
plt.figure(figsize=(5,1))
plt.title('video_share_count')
sns.boxplot(x=data['video_share_count']);


# *Create* a histogram of the values in the `video_share_count` column to further explore the distribution of this variable.

# In[26]:


# Create a histogram
plt.figure(figsize=(5,3))
sns.histplot(data['video_share_count'], bins=range(0,(270001),10000))
plt.title('Video share count histogram');


# **Question:** What do you notice about the distribution of this variable?

# #### **video_download_count**
# 
# Create a box plot to examine the spread of values in the `video_download_count` column.

# In[27]:


# Create a boxplot to visualize distribution of `video_download_count`
plt.figure(figsize=(5,1))
plt.title('video_download_count')
sns.boxplot(x=data['video_download_count']);


# Create a histogram of the values in the `video_download_count` column to further explore the distribution of this variable.

# In[28]:


# Create a histogram
plt.figure(figsize=(5,3))
sns.histplot(data['video_download_count'], bins=range(0,(15001),500))
plt.title('Video download count histogram');


# **Question:** What do you notice about the distribution of this variable?

# #### **Claim status by verification status**
# 
# Now, create a histogram with four bars: one for each combination of claim status and verification status.

# In[29]:


# Create a histogram
plt.figure(figsize=(7,4))
sns.histplot(data=data,
             x='claim_status',
             hue='verified_status',
             multiple='dodge',
             shrink=0.9)
plt.title('Claims by verification status histogram');


# **Question:** What do you notice about the number of verified users compared to unverified? And how does that affect their likelihood to post opinions?

# #### **Claim status by author ban status**
# 
# The previous course used a `groupby()` statement to examine the count of each claim status for each author ban status. Now, use a histogram to communicate the same information.

# In[30]:


# Create a histogram
fig = plt.figure(figsize=(7,4))
sns.histplot(data, x='claim_status', hue='author_ban_status',
             multiple='dodge',
             hue_order=['active', 'under review', 'banned'],
             shrink=0.9,
             palette={'active':'green', 'under review':'orange', 'banned':'red'},
             alpha=0.5)
plt.title('Claim status by author ban status - counts');


# **Question:** What do you notice about the number of active authors compared to banned authors for both claims and opinions?

# #### **Median view counts by ban status**
# 
# Create a bar plot with three bars: one for each author ban status. The height of each bar should correspond with the median number of views for all videos with that author ban status.

# In[31]:


# Create a bar plot
ban_status_counts = data.groupby(['author_ban_status']).median(
    numeric_only=True).reset_index()

fig = plt.figure(figsize=(5,3))
sns.barplot(data=ban_status_counts,
            x='author_ban_status',
            y='video_view_count',
            order=['active', 'under review', 'banned'],
            palette={'active':'green', 'under review':'orange', 'banned':'red'},
            alpha=0.5)
plt.title('Median view count by ban status');


# **Question:** What do you notice about the median view counts for non-active authors compared to that of active authors? Based on that insight, what variable might be a good indicator of claim status?

# In[32]:


# Calculate the median view count for claim status.
data.groupby('claim_status')['video_view_count'].median()


# In[ ]:


### YOUR CODE HERE ###


# #### **Total views by claim status**
# 
# Create a pie graph that depicts the proportions of total views for claim videos and total views for opinion videos.

# In[33]:


# Create a pie graph
fig = plt.figure(figsize=(3,3))
plt.pie(data.groupby('claim_status')['video_view_count'].sum(), labels=['claim', 'opinion'])
plt.title('Total views by video claim status');


# **Question:** What do you notice about the overall view count for claim status?

# ### **Task 4. Determine outliers**
# 
# When building predictive models, the presence of outliers can be problematic. For example, if you were trying to predict the view count of a particular video, videos with extremely high view counts might introduce bias to a model. Also, some outliers might indicate problems with how data was captured or recorded.
# 
# The ultimate objective of the TikTok project is to build a model that predicts whether a video is a claim or opinion. The analysis you've performed indicates that a video's engagement level is strongly correlated with its claim status. There's no reason to believe that any of the values in the TikTok data are erroneously captured, and they align with expectation of how social media works: a very small proportion of videos get super high engagement levels. That's the nature of viral content.
# 
# Nonetheless, it's good practice to get a sense of just how many of your data points could be considered outliers. The definition of an outlier can change based on the details of your project, and it helps to have domain expertise to decide a threshold. You've learned that a common way to determine outliers in a normal distribution is to calculate the interquartile range (IQR) and set a threshold that is 1.5 * IQR above the 3rd quartile.
# 
# In this TikTok dataset, the values for the count variables are not normally distributed. They are heavily skewed to the right. One way of modifying the outlier threshold is by calculating the **median** value for each variable and then adding 1.5 * IQR. This results in a threshold that is, in this case, much lower than it would be if you used the 3rd quartile.
# 
# Write a for loop that iterates over the column names of each count variable. For each iteration:
# 1. Calculate the IQR of the column
# 2. Calculate the median of the column
# 3. Calculate the outlier threshold (median + 1.5 * IQR)
# 4. Calculate the numer of videos with a count in that column that exceeds the outlier threshold
# 5. Print "Number of outliers, {column name}: {outlier count}"
# 
# ```
# Example:
# Number of outliers, video_view_count: ___
# Number of outliers, video_like_count: ___
# Number of outliers, video_share_count: ___
# Number of outliers, video_download_count: ___
# Number of outliers, video_comment_count: ___
# ```

# In[34]:


count_cols = ['video_view_count',
              'video_like_count',
              'video_share_count',
              'video_download_count',
              'video_comment_count',
              ]

for column in count_cols:
    q1 = data[column].quantile(0.25)
    q3 = data[column].quantile(0.75)
    iqr = q3 - q1
    median = data[column].median()
    outlier_threshold = median + 1.5*iqr

    # Count the number of values that exceed the outlier threshold
    outlier_count = (data[column] > outlier_threshold).sum()
    print(f'Number of outliers, {column}:', outlier_count)


# #### **Scatterplot**

# In[35]:


# Create a scatterplot of `video_view_count` versus `video_like_count` according to 'claim_status'
sns.scatterplot(x=data["video_view_count"], y=data["video_like_count"],
                hue=data["claim_status"], s=10, alpha=.3)
plt.show()


# In[36]:


# Create a scatterplot of ``video_view_count` versus `video_like_count` for opinions only
opinion = data[data['claim_status']=='opinion']
sns.scatterplot(x=opinion["video_view_count"], y=opinion["video_like_count"],
                 s=10, alpha=.3)
plt.show()


# You can do a scatterplot in Tableau Public as well, which can be easier to manipulate and present. If you'd like step by step instructions, you can review the instructions linked in the previous Activity page.

# <img src="images/Execute.png" width="100" height="100" align=left>
# 
# ## **PACE: Execute**
# 
# Consider the questions in your PACE Strategy Document to reflect on the Execute stage.

# ### **Task 5a. Results and evaluation**
# 
# Having built visualizations in Tableau and in Python, what have you learned about the dataset? What other questions have your visualizations uncovered that you should pursue?
# 
# ***Pro tip:*** Put yourself in your client's perspective, what would they want to know?
# 
# Use the following code cells to pursue any additional EDA. Also use the space to make sure your visualizations are clean, easily understandable, and accessible.
# 
# ***Ask yourself:*** Did you consider color, contrast, emphasis, and labeling?
# 

# ==> ENTER YOUR RESPONSE HERE
# 
# I have learned ....
# 
# My other questions are ....
# 
# My client would likely want to know ...
# 
# 

# ### **Task 5b. Conclusion**
# *Make it professional and presentable*
# 
# You have visualized the data you need to share with the director now. Remember, the goal of a data visualization is for an audience member to glean the information on the chart in mere seconds.
# 
# *Questions to ask yourself for reflection:*
# Why is it important to conduct Exploratory Data Analysis? What other visuals could you create?
# 

# EDA is important because ...
# 
# ==> ENTER YOUR RESPONSES HERE
# 
# Visualizations helped me understand ..
# 
# ==> ENTER YOUR RESPONSES HERE
# 

# You’ve now completed a professional data visualization according to a business need. Well done! Be sure to save your work as a reference for later work in Tableau.

# **Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged.
