# Elevate_Labs_Task1
This is my Elevate Labs Task 1 where I cleaned and prepared a raw data named Fleet Data.
Here are some changes I made to transform the fleet dataset.
1. First I read the csv file and named the dataset as df.
2. Getting overall information of data by- df.info() .
3. Renaming the columns having space and improper naming styles.
4. Removing some characters like ($ and ,) from the cost columns.
5. Checking the null values and replacing numeric values by their mean and drop the null values from the columns having less than 5% null values.
6. Chnging the of cost columns from object to int.
7. Dropping the duplicates values by df.drop_duplicates().
