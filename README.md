# Blackspot Analysis and Prediction Project

## Project Overview
This project is a data science solution aimed at analyzing and predicting accident-prone areas, known as "Blackspots," for the Victorian government's Department of Transport (DOT). Using data on demographics, road types, environmental conditions, and other factors, we build a logistic regression model to identify patterns and predict potential Blackspots. 

The project provides insights that can be used to:
- Develop awareness campaigns
- Propose legislative changes
- Inform infrastructure improvements, like traffic signals or speed limits

The ultimate goal is to reduce accident hotspots, thereby improving road safety and potentially saving lives.

## Data Description
The dataset used for this project includes 36 features and 5326 rows, covering a range of factors contributing to Blackspots. Key features include:
- **Demographics**: Age distribution, percentage of single parents, couples with or without children.
- **Road Characteristics**: Intersection types, road types, and whether traffic signals are present.
- **Environmental Factors**: Land use types, presence of liquor licenses, proximity to schools, supermarkets, etc.

The data includes both categorical and numerical values. Some features require encoding and scaling before model training.

## Project Workflow
1. **Data Preprocessing**: Data cleaning, handling missing values, encoding categorical features, and scaling numerical features.
2. **Exploratory Data Analysis (EDA)**: Visualizations to understand the relationships between features, including univariate, bivariate, and multivariate analysis.
3. **Modeling**: Building a Logistic Regression model to predict the likelihood of a Blackspot.
4. **Evaluation**: Assessing model performance using metrics such as accuracy, precision, and ROC curve analysis.
5. **Recommendation**: Proposing actionable solutions based on the model's insights for DOT.

## Requirements
To run this project, you'll need the following Python libraries. You can install them using the provided ```requirements.txt``` file:

```bash
pip install -r requirements.txt
```
Key dependencies include:
- ```pandas```: For data manipulation and preprocessing
- ```scikit-learn```: For model training, evaluation, and preprocessing utilities
- ```matplotlib``` and ```seaborn```: For data visualization

## Setup and Usage
**1. Clone the Repository:**

```bash
git clone https://github.com/pradiptadutta63/Blackspot_Prediction-using-LR.git
cd Blackspot_Prediction-using-LR
```
**2. Install Dependencies:**

```bash
pip install -r requirements.txt
```
**3. Data Placement:**
- Place the dataset files in the data/raw folder.

**4. Run the Notebooks:**
- You can run notebooks/Python_script.ipynb to see data preprocessing, EDA, model building, and evaluation in one place.

**5. Run Python Scripts:**
- Alternatively, you can run the individual Python scripts provided in the src/ directory.


## Data Preprocessing
To clean and preprocess data:

```bash
python src/data_preprocessing.py
```

## Exploratory Data Analysis (EDA)
To visualize and analyze relationships in the data:

```bash
python src/eda.py
```

## Model Training
To train the logistic regression model on the preprocessed data:

```bash
python src/model.py
```

## Model Evaluation
To evaluate model performance:

```bash
python src/evaluation.py
```

## Results
The Logistic Regression model achieves:

Accuracy: 91.67%
Precision: 86%

These metrics indicate a reliable model that can help the DOT make informed decisions about where to focus resources to reduce accidents. The final recommendations include adding traffic signals at high-risk intersections, controlling liquor licenses near residential areas, and running safety awareness campaigns targeting high-risk age groups.

## Contributors
Pradipta Dutta - Data Scientist
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pradiptadutta63)
