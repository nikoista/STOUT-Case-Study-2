#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
"""
@author: Nikolaos Istatiadis
"""
 
# Basic Numpy , Pandas , Matplotlib Libraries
import numpy as np
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import seaborn as sns


warnings.filterwarnings('ignore')


# PUT YOUR FILE PATH HERE
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
path = 'C:/Users/__________'
dataset_path = 'C:/Users/__________'
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
 

path = 'C:/Users/nikos/DIPLOMATIKI/Case_2/'
dataset_path = 'C:/Users/nikos/DIPLOMATIKI/Case_2/Dataset/'

###############################################################################


#########################  Information About our Data #########################
def data_Info (data):
    data.info()
    data.head()
    # Statistics for each column
    data.describe()
    feature_names = [i for i in data.columns ]
    #print('Statistical View of our Data: \n' ,data.describe().T)
    return feature_names
###############################################################################


###############################################################################
def data_Visualization(df ):
    
    
######################## Line plot of total revenue over time #################
    # Total revenue over time , line plot
    plt.figure(figsize=(10,10))
    
    # Group the data by year and calculate the total revenue for each year
    yearly_revenue = df.groupby('year')['net_revenue'].sum().reset_index()
    
    # Get the years and total revenue values
    years = yearly_revenue['year']
    revenue = yearly_revenue['net_revenue']

    # Create the plot
    plt.plot(years, revenue)

    # Add a title and labels
    plt.title('Total Revenue Over Time')
    plt.xlabel('Year')
    plt.ylabel('Total Revenue')

    # Show the plot
    plt.show()

    
############ Bar plot of revenue by customer type (new or existing) ###########
 
    # Group the data by customer email and year, and calculate the total revenue for each customer in each year
    customer_revenue_by_year = df.groupby(['customer_email', 'year'])['net_revenue'].sum().reset_index()

    # Calculate the difference in revenue between consecutive years for each customer
    customer_revenue_by_year['revenue_diff'] = customer_revenue_by_year.groupby('customer_email')['net_revenue'].diff()

    # Create a new column called 'customer_type' and set it to 'new' if the revenue difference is positive, and 'existing' if the revenue difference is negative or zero
    customer_revenue_by_year['customer_type'] = np.where(customer_revenue_by_year['revenue_diff'] > 0, 'new', 'existing')

    # Drop the 'revenue_diff' column
    customer_revenue_by_year = customer_revenue_by_year.drop(columns=['revenue_diff'])

    # Group the data by customer type (new or existing) and year, and calculate the total revenue for each group
    customer_type_revenue = customer_revenue_by_year.groupby(['customer_type', 'year'])['net_revenue'].sum().reset_index()
        
 
    # Get the years and total revenue values for new customers
    new_customer_revenue = customer_type_revenue[customer_type_revenue['customer_type'] == 'new']
    new_customer_years = new_customer_revenue['year']
    new_customer_revenue = new_customer_revenue['net_revenue']

    # Get the years and total revenue values for existing customers
    existing_customer_revenue = customer_type_revenue[customer_type_revenue['customer_type'] == 'existing']
    existing_customer_years = existing_customer_revenue['year']
    existing_customer_revenue = existing_customer_revenue['net_revenue']
 

    # Set the figure size
    plt.figure(figsize=(15, 15))

    # Create the figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(20,20))
    
    # Create the first plot
    ax1.bar(new_customer_years, new_customer_revenue)

    # Create the second plot
    ax2.bar(existing_customer_years, existing_customer_revenue)
    
    # Add a title and labels
    plt.suptitle('Revenue by Customer Type')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Total Revenue')
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Total Revenue')
    
    #Add a legend
    plt.legend()


    # Rotate the x-axis labels to make them easier to read
    plt.xticks(rotation=90)

    # Show the plot
    plt.show()
    
 
    
################ Line plot of the number of customers over time ###############
    plt.figure(figsize=(10,10))
    # Group the data by year and count the number of unique customer emails for each year
    customer_count_by_year = df.groupby('year')['customer_email'].nunique().reset_index()

    # Get the years and customer count values
    years = customer_count_by_year['year']
    customer_count = customer_count_by_year['customer_email']

    # Create the plot
    plt.plot(years, customer_count)

    # Add a title and labels
    plt.title('Number of Customers Over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Customers')

    # Show the plot
    plt.show()
    
################ Bar plot of revenue by customer email ########################   
    plt.figure(figsize=(15,15))
    ## Group the data by customer email and calculate the total revenue for each customer
    customer_revenue = df.groupby('customer_email')['net_revenue'].sum().reset_index()
    
    ## Get the customer emails and total revenue values
    customer_emails = customer_revenue['customer_email']
    revenue = customer_revenue['net_revenue']
    
    # Create the plot
    plt.scatter(range(0,len(customer_emails)), revenue)
    
    # Add a title and labels
    plt.title('Revenue by Customer Email')
    plt.xlabel('Customers')
    plt.ylabel('Total Revenue')
    
    # Rotate the x-axis labels to make them easier to read
    #plt.xticks(rotation=90)
        
    # Show the plot
    plt.show()
        
    
""" # TAKES A LOT OF TIME   
#   Pairplot of the relationship between customer revenue, year,customer email#

    # Create a pairplot of the relationship between customer revenue, year, and customer email
    sns.pairplot(df, x_vars=["customer_email", "year"], y_vars=["net_revenue"])

    # Set the plot style to "darkgrid"
    sns.set_style("darkgrid")

    # Set the plot context to "poster"
    sns.set_context("poster")

    # Customize the plot
    plt.title("Relationship between Customer Revenue, Year, and Customer Email")
    plt.xlabel("Customer Email and Year")
    plt.ylabel("Net Revenue")

    # Show the plot
    plt.show()
"""
    
    
########################## Entry point for the program ########################
if __name__ == '__main__':
    
########################### Import Real Dataset ################################
     data = pd.read_csv(dataset_path+ 'casestudy.csv') #sep=';')
     feature_names = data_Info(data)
 
     df = data.copy()
 


     # Get the unique years in the dataset
     years = df['year'].unique()
     
     # Sort the years in ascending order
     years.sort()

     # Get the current year from the sorted list of years
     current_year = years[-1]

     print('\nThe current year of the dataset is',current_year)

##################### Total revenue for the current year ######################
     
     # Group the data by year and calculate the total revenue for each year
     total_revenue_by_year = df.groupby('year')['net_revenue'].sum()

     # Print the total revenue for each year
     for year, total_revenue in total_revenue_by_year.items():
        print(f'Total revenue for {year}:  {total_revenue:.2f} $')
        
     df = data.copy()  
     
     
############################# New Customer Revenue #############################
     
     # Initialize an empty dictionary to store the new customer revenue for each year
     new_customer_revenue = {}

     # Iterate over the years in the dataset
     for year in years:
        # Calculate the previous year
        previous_year = year - 1
    
        # Get the customer emails for the current year
        customer_emails_current_year = df[df['year'] == year]['customer_email'].unique()
    
        # Get the customer emails for the previous year
        customer_emails_previous_year = df[df['year'] == previous_year]['customer_email'].unique()
    
        # Filter the data to include only those customers that are not present in the previous year
        new_customers = df[(df['year'] == year) & (~df['customer_email'].isin(customer_emails_previous_year))]
    
        # Group the data by customer email and sum the revenue for the new customers
        new_customer_revenue[year] = new_customers.groupby('customer_email')['net_revenue'].sum()

     # Print the new customer revenue for each year
     print('\nNew costumer revenue for 2015:',new_customer_revenue[2015].sum())
     print('\nNew costumer revenue for 2016:',new_customer_revenue[2016].sum())
     print('\nNew costumer revenue for 2017:',new_customer_revenue[2017].sum())

     df = data.copy()
     
     
########################### Revenue lost from attrition #######################

     previous_year = 2016
     current_year = 2017
     # Select the customer emails and net revenue in the previous year
     customer_revenue_previous_year = df[df['year'] == previous_year][['customer_email', 'net_revenue']]

     # Group the data by customer email and sum the net revenue
     customer_revenue_previous_year = customer_revenue_previous_year.groupby('customer_email').sum()

     # Select the customer emails and net revenue in the current year
     customer_revenue_current_year = df[df['year'] == current_year][['customer_email', 'net_revenue']]

     # Group the data by customer email and sum the net revenue
     customer_revenue_current_year = customer_revenue_current_year.groupby('customer_email').sum()

     # Calculate the revenue lost from attrition
     attrition_revenue = customer_revenue_previous_year['net_revenue'] - customer_revenue_current_year['net_revenue']

     # Sum the attrition revenue
     attrition_revenue = attrition_revenue.sum()

     print('\nRevenue lost from attrition for years  2016-2017 ',attrition_revenue)
     
     
     previous_year = 2015
     current_year = 2016
     # Select the customer emails and net revenue in the previous year
     customer_revenue_previous_year = df[df['year'] == previous_year][['customer_email', 'net_revenue']]

     # Group the data by customer email and sum the net revenue
     customer_revenue_previous_year = customer_revenue_previous_year.groupby('customer_email').sum()

     # Select the customer emails and net revenue in the current year
     customer_revenue_current_year = df[df['year'] == current_year][['customer_email', 'net_revenue']]

     # Group the data by customer email and sum the net revenue
     customer_revenue_current_year = customer_revenue_current_year.groupby('customer_email').sum()

     # Calculate the revenue lost from attrition
     attrition_revenue = customer_revenue_previous_year['net_revenue'] - customer_revenue_current_year['net_revenue']

     # Sum the attrition revenue
     attrition_revenue = attrition_revenue.sum()

     print('\nRevenue lost from attrition for years  2015-2016 ',attrition_revenue)

############################# Existing Customers ##############################

     # Initialize an empty list to store the resulting DataFrames
     df_existing_customers_list = []

     # Iterate through the years
     for year in years:
         # Filter the data to include only the current year and the prior year
         df_current_year = df[df['year'] == year]
         df_prior_year = df[df['year'] == year - 1]
         
         # Group the data by customer email and sum the revenue for each customer
         customer_revenue = df_current_year.groupby('customer_email')['net_revenue'].sum()
         
         # Filter the data to include only the existing customers (i.e. those that are not new customers)
         existing_customers = customer_revenue[customer_revenue.index.isin(df_prior_year['customer_email'])]
         
         # Create a DataFrame with the existing customers and add the year as a column
         df_existing_customers = pd.DataFrame(existing_customers).reset_index()
         df_existing_customers['year'] = year
         
         # Add the DataFrame to the list
         df_existing_customers_list.append(df_existing_customers)



#################### Existing Customer Revenue Current Year ###################

     df_existing_customers_current_year = pd.DataFrame(df_existing_customers_list[2])
     print('\nExisting customer rvenue current year : ',df_existing_customers_current_year['net_revenue'].sum())

#################### Existing Customer Revenue prior Year ###################

     df_existing_customers_prior_year =  pd.DataFrame(df_existing_customers_list[1])
     print('\nExisting customer revenue prior year : ',df_existing_customers_prior_year['net_revenue'].sum())

    
    
    
########################### Existing Customer Growth ##########################
 
    
     # Merge the two DataFrames on the customer email column
     df_existing_customers_growth = pd.merge(df_existing_customers_current_year, df_existing_customers_prior_year, on='customer_email', suffixes=('_current_year', '_prior_year'))

     # Calculate the growth by subtracting the revenue from the prior year from the revenue in the current year
     df_existing_customers_growth['growth'] = df_existing_customers_growth['net_revenue_current_year'] - df_existing_customers_growth['net_revenue_prior_year']

     print('\nExisting customer growth : ',df_existing_customers_growth['growth'].sum())
    
    
########################### Total Customers Current Year ######################

     # Select the unique customer emails in the current year
     customer_emails_current_year = df[df['year'] == 2017]['customer_email'].unique()

     # Calculate the total number of customers in the current year
     total_customers_current_year = len(customer_emails_current_year)

     print('\n Total customers in 2017 is :',total_customers_current_year)
     total_customers_2017 = total_customers_current_year
     
     
########################### Total Customers Previous Year #####################

     # Calculate the previous year so in year 2016
 
     # Select the unique customer emails in the current year
     customer_emails_prior_year = df[df['year'] == 2016]['customer_email'].unique()

     # Calculate the total number of customers in the current year
     total_customers_prior_year = len(customer_emails_prior_year)
     total_customers_2016 = total_customers_prior_year

     print('\n Total customers in 2016 is :',total_customers_2016)
 


     # Calculate the previous year so in year 2015
 

     # Select the unique customer emails in the current year
     customer_emails_prior_year = df[df['year'] == 2015]['customer_email'].unique()

     # Calculate the total number of customers in the current year
     total_customers_prior_year = len(customer_emails_prior_year)
     total_customers_2015 = total_customers_prior_year

     print('\n Total customers in 2015 is :',total_customers_2015)
 


################################## New Customers ##############################

     # Calculate the number of new customers
     new_customers_2017 = total_customers_2017 - total_customers_2016
    
     new_customers_2016 = total_customers_2016 - total_customers_2015
     
     new_customers_2015 = total_customers_2015
     
     print('\n New customers in 2017 is :',new_customers_2017)
     print('\n New customers in 2016 is :',new_customers_2016)
     print('\n We can"t find the new customers in 2015  because we dont have previous data')



################################# Lost Customers ##############################

     # Calculate the number of lost customers
     lost_customers_2017 = total_customers_2016 - total_customers_2017
   
     lost_customers_2016 = total_customers_2015 - total_customers_2016
    
     lost_customers_2015 = total_customers_2015
    
     print('\n New customers in 2017 is :',lost_customers_2017)
     print('\n New customers in 2016 is :',lost_customers_2016)
     print('\n We can"t find the lost customers in 2015  because we dont have previous data')

 
############################ Some Visualizations ##############################

data_Visualization(df )