# bigdata-aggregating-python

## Dataset
The data that represent the amount of money for every account in a bank. The data is in multiple CSV files with 2 columns:
1.	account_id: string represent the account holder. Single account_id may appear multiple times in different CSV file but it is unique in a single CSV file.
2.	account_balance: integer represent the amount of money in the account.
size of the data is roughly 4GB

## Code Overview
1.	Task 1: Calculate the sum of money from all accounts.
2.	Task 2: Group the account based on the first two character on the account_id, then calculate the sum of money for each group.
3.	Task 3: Get the top 1000000 richest accounts (have biggest amount of money).
4.	Task 4: Calculate the sum of their money (for the top 1000000 richest account) and the ratio compared to the total sum on no 1.

This implementation will not use more than 1GB of memory/RAM and all tasks will finish under 15 minutes
