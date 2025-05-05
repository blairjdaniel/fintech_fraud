# Bitcoin Price Prediction

This project aims to analyze the relationship between Bitcoin price movements and major US market events. In the first phase, I completed an exploratory data analysis (EDA) that shows the correlation—even potential causation—between Bitcoin and other US market indicators. Interactive charts highlight these comparisons, laying the foundation for a predictive model.

## Data Sources

- **Federal Reserve Economic Data:**  
  - [CPIAUCSL](https://fred.stlouisfed.org/series/CPIAUCSL) – Consumer Price Index for All Urban Consumers (Seasonally Adjusted)  
  - [CPIENGSL](https://fred.stlouisfed.org/series/CPIENGSL) – Energy Component of the CPI

- **Investing.com:**  
  - Historical Bitcoin prices

## Project Structure

- **Data Ingestion & Cleaning:**  
  Scripts and notebooks that read, clean, and preprocess the raw CSV data.

- **Exploratory Data Analysis:**  
  Notebooks (e.g. [data_import.ipynb](notebooks/data_import.ipynb) and [EDA.ipynb](notebooks/EDA.ipynb)) with interactive visualizations showing the relationships between Bitcoin and key economic indicators.

- **Future Work – Price Prediction Model:**  
  Planned development of a model to predict Bitcoin prices that will incorporate major events such as Bitcoin halving and presidential elections. Tuned models and hyperparameter search will be detailed in upcoming notebooks (e.g. [hypertuning.ipynb](notebooks/hypertuning.ipynb)).

- **Dashboarding:**  
  Future plans include integrating the analysis and model outputs into an interactive dashboard (e.g., Tableau) for live insights.

## Insights So Far

- The initial analysis revealed significant correlations between Bitcoin price and several economic indicators.
- Comparisons are visualized through an array of interactive charts.
- These findings provide a strong foundation for the next phase: developing a price prediction model that factors in major events.

## Next Steps

- **Develop a Predictive Model:**  
  Build and tune a machine learning model to forecast Bitcoin prices using historical trends and major events like Bitcoin halving and presidential elections.

- **Deploy Interactive Dashboards:**  
  Present live, interactive visualizations and predictions via a dashboard.

## How to Run

1. **Data Ingestion:**  
   Run the scripts in the `scripts/` directory to load your CSV files into the PostgreSQL database.

2. **Exploratory Analysis:**  
   Open the notebooks in the `notebooks/` folder to view data cleaning, EDA, and visualization processes.

3. **Model Training:**  
   (Upcoming) Develop and hyperparameter-tune the Bitcoin price prediction model in the designated notebook.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more details.