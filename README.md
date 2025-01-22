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

The notebook that is referenced in these steps is [this one](https://github.com/leorlik/alura-voz/blob/main/1%20-%20Cleaning%20Data/cleaning-data-notebook.ipynb). 

The json data provided, is, in fact, besides the customerID and the binary "Churn" field, four different dataframes. Here's a summary of each dataframe and it's columns:

- The "customer" dataframe provides information about the service contractor:
  - Field "gender" says if the client is a Male or a Female;
  - Field "SeniorCitzen" says if the client is over 65 years;
  - Field "Partner" says if the client has a partner;
  - Field "Dependents" says if the client has Dependents;
  - Field "tenure" has information about the time the contractor has in the Alura Voz company;
- The "phone" dataframe provides information about the client's phone service

## Step 2 - Data Analysis

## Step 3 - Modeling

## Step 4 - Fine Tuning