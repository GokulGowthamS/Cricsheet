# *Cricsheet*  
In the Old days, no details and interactive charts could improve the spectator's experience. So, I have devised a plan to interactively check player performance and match details with ease of use.
This project involves scraping, processing, analyzing, and visualizing cricket match data from Cricsheet. The data includes different match formats (ODI, T20, and Test) and is used to generate insights through SQL queries, Python EDA, and a Power BI dashboard.

### *Key Features*
__Data Storage__: Stored structured data in SQL tables for efficient querying.  
__SQL Analysis__: Wrote 20+ SQL queries to analyze performance metrics, player stats, and match outcomes.  
__Exploratory Data Analysis (EDA)__: Used Matplotlib, Seaborn, and Plotly for data visualization.  
__Power BI Dashboard__: Created interactive visualizations to showcase key insights.  

### *Technology Stack*  
__Database__: MySQL  
__Query Language__: SQL  
__Data Analysis & EDA__: Python (Pandas, Matplotlib, Seaborn, Plotly)  
__Data Visualization__: Power BI  

### *Raw json Files*  
This folder has all the files that have been converted into .csv files by using the panda's library.  

### *General Datasets*  
This folder contains all the general information that supports further analysis  

### *Innings Datasets*  
This folder contains all the necessary information used for plotting and for further analysis.  

### *Preprocessed General Datasets*  
This folder contains the preprocessed files that were present in the __General Datasets__ folder that have been processed for the null values and dates.  

### *Proprocessed Innings Datasets*  
This folder contains the preprocessed files that were present in the __Innings Datasets__ folder that have been processed for the null values.  

### *Pages*  
This folder contains the files that contribute to the Streamlit Applications (i.e.) Table View, Query View, and Visualizations.  

### *Scripts*  
This folder contains all the files that were used to extract, convert, and visualize the data from the JSON file.  

### *Cricsheet.pbix*  
This is an interactive dashboard that can be used to spectate and analyze the match data with much more ease than viewing it in a table format.  

### *Conclusion*  
This project successfully transforms raw cricket match data from Cricsheet into meaningful insights through SQL queries, Python-based EDA, and Power BI visualizations.  
By leveraging web scraping, data processing, and interactive dashboards, users can explore player performances, match outcomes, and team statistics in an intuitive way.   
The combination of structured datasets, preprocessed data, and Streamlit applications makes cricket analytics more accessible and engaging.   
This project not only enhances the viewing experience but also provides valuable insights for analysts, fans, and strategists.
