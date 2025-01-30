# 1° Challenge de Dados -  Alura
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

<center>
  <img src="https://i.imgur.com/jn7km8o.png">
</center>

Alura Voz is a telecommunications company that hired us to work as data scientists on the sales team. In the very first week, the leadership informed us that it is essential to conduct a study on the company's churn. It was explained that churn indicates whether a customer has canceled their contract with the company, and that, in cases of customer loss, the company also loses revenue, which results in financial losses to the final income.

Thus, our leadership informed us that we have 4 weeks to find an alternative to minimize customer attrition and provided us with a dataset from Alura Voz containing various customer information, as well as indicating whether they left the company or not.

We know that before considering any alternatives, it is necessary to understand the information we received. After a brief meeting, we concluded that during the first week, we would dedicate ourselves to understanding the database, identifying the types of data, checking for inconsistent values, and correcting them if necessary.

## Disclaimer

Aside from the introduction above, I have not reviewed the material in the `made_by_alura` folder. The objective of this repository is to perform my own data cleaning, analysis, modeling, and fine-tuning of the Alura Voz case independently, following the steps provided on the challenge site and Trello.

## Project Structure 

- The `made_by_alura` directory contains the notebooks created by the challenge organizers.
- The `Dados` directory contains the raw data used in the project.
- The `1 - Cleaning Data` directory contains the notebook used for cleaning the raw data.
- The `2 - Data Analysis` directory contains the notebook used for analyzing the data.
- The `3 - Modeling` directory contains the notebooks used for creating the model and selecting variables.
- The `4 - Fine Tuning` directory contains the notebook used for fine-tuning the selected model.
- The `conda_env` directory contains the Conda virtual environment used in this project. To replicate the environment on your machine, use the following command:

```bash
conda env create -f environment.yml
```

## Step 1 - Data Cleaning and Initial Steps

The notebook referenced in these steps is [this one](https://github.com/leorlik/alura-voz/blob/main/1%20-%20Cleaning%20Data/cleaning-data-notebook.ipynb). 

The JSON data provided includes, besides the customerID and the binary "Churn" field, four different dataframes. Here's a summary of each dataframe and its columns:

- The "customer" dataframe provides information about the service contractor:

  - The field gender indicates whether the client is male or female.
  - The field SeniorCitizen indicates whether the client is over 65 years old.
  - The field Partner indicates whether the client has a partner.
  - The field Dependents indicates whether the client has dependents.
  - The field tenure provides information about the duration of the client's contract with Alura Voz.

- The "phone" dataframe provides information about the client's phone service:
  - The field PhoneService indicates whether the customer has a phone service in their contract.

  - The field MultipleLines indicates whether the customer has multiple phone lines.

- The "internet" dataframe provides information about the client's internet services:

  - The field InternetService indicates the subscription to an internet provider.
  - The field OnlineSecurity indicates an additional subscription for online security.
  - The field OnlineBackup indicates an additional subscription for online backup.
  - The field DeviceProtection indicates an additional subscription for device protection.
  - The field TechSupport indicates an additional subscription for technical support, with reduced waiting times.
  - The field StreamingTV indicates a subscription for cable TV.
  - The field StreamingMovies indicates a subscription for movie streaming services.

- The "account" dataframe provides information about the client's account details:

  - The field Contract specifies the type of contract.
  - The field PaperlessBilling indicates whether the client prefers to receive their bill online.
  - The field PaymentMethod specifies the payment method used by the client.
  - The field Charges.Monthly indicates the total cost of all services for the client per month.
  - The field Charges.Total indicates the total amount spent by the client.

These datasets were separated into the SOT layer, along with a unified dataframe containing all the information, available in [this folder](https://github.com/leorlik/alura-voz/tree/main/data/SOT). The initial data treatments were as follows:

- Rows with null values in the Churn field were deleted.
- Rows with a tenure value of 0 were also deleted.

## Step 2 - Data Analysis

The notebook referenced in these steps is [this one](https://github.com/leorlik/alura-voz/blob/main/2%20-%20Data%20Analysis/data_analysis.ipynb).

In this step, an analysis of the data and its correlations was conducted, primarily focusing on the Churn variable but not limited to it. Since most of the data consists of categorical variables, chi-squared tests were performed to assess their significance, using the p-value as a reference.

### Numerical Variables (Continuous and Discrete)

There are only three numerical variables in the dataset: tenure, Charges.Monthly, and Charges.Total. To begin the analysis, let's describe them:

| Statistic | Tenure  | Charges Monthly | Charges Total |
|-----------|--------|----------------|--------------|
| Count     | 7032.000000 | 7032.000000 | 7032.000000 |
| Mean      | 32.421786  | 64.798208    | 2283.300441 |
| Std       | 24.545260  | 30.085974    | 2266.771362 |
| Min       | 1.000000   | 18.250000    | 18.800000   |
| 25%       | 9.000000   | 35.587500    | 401.450000  |
| 50%       | 29.000000  | 70.350000    | 1397.475000 |
| 75%       | 55.000000  | 89.862500    | 3794.737500 |
| Max       | 72.000000  | 118.750000   | 8684.800000 |

We can already see that these variables have a wide range, as indicated by their high standard deviations and the large differences between their minimum and maximum values. Additionally, except for Charges.Total, the median is relatively close to the mean.

Another notable relationship is that when we multiply the mean values of tenure and Charges.Monthly, the result is, as expected, close to the mean of Charges.Total.

Looking at the mean, median, and mode of these variables:

| Statistic         | Mean        | Median   | Mode  |
|------------------|------------|---------|------|
| Tenure          | 32.421786   | 29.000  | 1.00  |
| Charges Monthly | 64.798208   | 70.350  | 20.05 |
| Charges Total   | 2283.300441 | 1397.475 | 20.20 |

It's clear that Charges.Total and tenure follow a right-skewed distribution, possibly indicating the presence of outliers that could be removed in future preprocessing steps.

Histograms can help confirm this assumption and provide further insights into the Charges.Monthly variable.

#### Tenure Histogram

![Histogram of Tenure]("../charts/tenure_hist.png")

The tenure variable shows spikes at the lowest and highest values, confirming a right-skewed distribution. If customers in these extreme groups have high churn rates, they could be considered critical segments.

#### Charges.Monthly Histogram

![Histogram of Monthly Charges]("../charts/Charges.Monthly_hist.png")

Many customers have low monthly charges, and bills between 26 and 43 BRL are quite unusual.

#### Charges.Total Histogram

![Histogram of Total Charges]("../charts/Charges.Total_hist.png")

The Charges.Total variable is a textbook example of a right-skewed distribution. If this variable is included in the model, it may indicate the presence of outliers that should be addressed.

## Step 3 - Modeling

## Step 4 - Fine Tuning