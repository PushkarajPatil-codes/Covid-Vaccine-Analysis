import pandas as pd

# Define path to the CSV file
CSV_PATH = "Data/covid_vaccine_statewise.csv"

def run_vaccination_analysis():
    print("=== COVID-19 VACCINATION DATA ANALYSIS ===")
    
    # Load dataset
    df = pd.read_csv(CSV_PATH)
    
    # Clean column names by removing extra spaces
    df.columns = df.columns.str.strip()
    
    # --- a. Describe the dataset ---
    print("\n--- a. Dataset Description ---")
    print(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print("\nColumns in the dataset:")
    print(list(df.columns))
    print("\nBasic Summary Statistics:")
    print(df.describe())
    
    # Separate statewise data (exclude rows representing national totals 'India')
    states_df = df[df['State'] != 'India']
    
    # --- b. Number of persons statewise vaccinated for first dose ---
    print("\n--- b. Top 10 States - First Dose Administered ---")
    statewise_first = states_df.groupby('State')['First Dose Administered'].max().sort_values(ascending=False)
    for state, val in statewise_first.head(10).items():
        print(f"{state}: {int(val):,}")
        
    # --- c. Number of persons statewise vaccinated for second dose ---
    print("\n--- c. Top 10 States - Second Dose Administered ---")
    statewise_second = states_df.groupby('State')['Second Dose Administered'].max().sort_values(ascending=False)
    for state, val in statewise_second.head(10).items():
        print(f"{state}: {int(val):,}")
        
    # --- d. Number of Males and Females vaccinated ---
    print("\n--- d/e. Gender Vaccination Numbers (National) ---")
    india_df = df[df['State'] == 'India']
    
    total_male = int(india_df['Male(Individuals Vaccinated)'].max())
    total_female = int(india_df['Female(Individuals Vaccinated)'].max())
    
    print(f"Males Vaccinated: {total_male:,}")
    print(f"Females Vaccinated: {total_female:,}")
    print(f"Total Doses (First + Second) for India: {int(india_df['First Dose Administered'].max() + india_df['Second Dose Administered'].max()):,}")

if __name__ == "__main__":
    run_vaccination_analysis()
