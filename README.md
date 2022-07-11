# Seng309Assignment5
Machine Learning app to predict software developer Salary
A. The Idea was to predict a software developers salary based on country, education level, and experience coding.

B. I used the data set from stacker over flows yearly Developer survey.
https://insights.stackoverflow.com/survey/
Data originally 48 different gollum’s to features. I cut it down to 5 columns. Originally 83438 entries after removing entries that contain null values I  still had 47183 entries. There are 5 data types being used Country, education level, years code pro, employment and salary. I then only kept data where the subject was employed full time. Dropping my entries to 40399 and removing employment at a column. Then I got rid of countries that only had a small number of entries like Somalia only had one entry. I ended up combining those countries into an other category. Originally there were 64 countries.I have 25 named countries and other is the 26 category. All named countries have at least 400 data points. Moved on to clean Years of coding and education by finding unique values and combining a few of the outliers.
To find best parameters for ML algorithms I used and imported Grid SearchCV  with cross validation

C. I used python. I am still fine tuning the Gun, I attempted to use streamline.io but was having problems. I am now trying to use Tinkiter,

D. Demo will be presented in class 7/6 or upload to teams.

E.) I tried three algorithms linear regression, Decision tree Regression, and random forrest regressor. Below you can see the error in Salary ranges. The lowest error came from decision tree regressor.
Error
Linear Regression error $47921.674961757024
Decision Tree Regressor error = $$34,369.73
Random Forrest Regression error = $$34,731.21


Current problems are having the inputs be saved for the test model.
Displaying the results on the app and not the terminal
