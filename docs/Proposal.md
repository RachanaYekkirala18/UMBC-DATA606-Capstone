## 1. Predictive Analysis Of Article Virality Based On Titles

- Predictive Analysis of Article Virality based on Titles
- Prepared for UMBC Data Science Master Degree Capstone by Rachana Yekkirala under the guidance of Dr Chaojie (Jay) Wang
- Author Name: Venkata Rachana Yekkirala
- Linked In : [Linked In](www.linkedin.com/in/yekkirala-venkata-rachana-4150881a9)
- Github : [Github](https://github.com/RachanaYekkirala18)
- PowerPoint presentation:

## 2. Background

-What is it about?
-The project is about using machine learning to predict the virality of articles based on their titles. It examines how certain features of a title, such as sentiment, length, and specific keywords, correlate with the article's engagement on social media platforms like Twitter and Medium.

-Why does it matter?
-Understanding what makes an article go viral can significantly impact content creation strategies, enabling writers and publishers to craft titles that are more likely to attract attention and engagement. This can lead to increased readership, improved brand visibility, and higher content dissemination efficiency.

-Research Questions
-What title features correlate with higher retweets and likes? This question aims to identify specific characteristics of article titles that are associated with greater social media engagement.

-Can machine learning models accurately predict the engagement level (retweets and likes) of an article based on its title? This question explores the feasibility of applying predictive analytics to forecast how well an article will perform on social platforms based solely on its title.

## 3. Data

-Data Sources: The dataset is sourced from Twitter and Medium, focusing on FreeCodeCamp's articles shared on Twitter along with their corresponding engagement metrics and categories on Medium.

-Data Size: Approximately 0.35 MB.

-Data Shape: The dataset contains 717 rows and 8 columns.

-Time Period: The dataset covers the period from November 26, 2017, to August 7, 2018.

-Row Representation: Each row represents a tweet related to an article published by FreeCodeCamp, including engagement metrics and article information.

-Data Dictionary
id (int64): Unique identifier for each tweet.
retweet_count (int64): Number of retweets the tweet received.
favorite_count (int64): Number of likes (favorites) the tweet received.
text (object): The text of the tweet, typically including the title of the article and a URL.
created_at (datetime64[ns]): Timestamp when the tweet was posted.
url (object): URL of the article on Medium (not displayed in the provided output but inferred from context).
medium_claps (int64): Number of claps the article received on Medium.
medium_categories (object): Categories of the article on Medium, listed in an array format.

-Target/Label Variable
For a machine learning model focusing on predicting the virality of an article based on its title, the target variables could be either:

retweet_count: To predict the number of retweets, or
favorite_count: To predict the number of likes.
Additionally, you could derive a categorical variable indicating virality levels (e.g., "High", "Medium", "Low") based on these metrics.

-Feature/Predictor Variables
text (Title): The main feature for predicting engagement would be the article title extracted from the text column. You might need to preprocess this text to extract only the title.
medium_categories: Categories could serve as additional features, assuming there might be correlations between certain topics and engagement levels.

