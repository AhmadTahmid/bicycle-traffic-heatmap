import pandas as pd

def load_and_process_data(input_file, output_file):
    # Load the dataset
    dataset = pd.read_csv(input_file, sep=';')
    
    # Clean and process the data
    dataset_clean = dataset.dropna(subset=['Geo Point'])

    # Split Geo Point into Latitude and Longitude
    dataset_clean[['Latitude', 'Longitude']] = dataset_clean['Geo Point'].str.split(',', expand=True)
    dataset_clean['Latitude'] = pd.to_numeric(dataset_clean['Latitude'], errors='coerce')
    dataset_clean['Longitude'] = pd.to_numeric(dataset_clean['Longitude'], errors='coerce')

    # Convert 'Data' column to datetime
    dataset_clean['Data'] = pd.to_datetime(dataset_clean['Data'], format='%d/%m/%Y %H:%M')

    # Extract hour from the 'Data' column
    dataset_clean['Hour'] = dataset_clean['Data'].dt.hour

    # Save the cleaned dataset to a new CSV file
    dataset_clean.to_csv(output_file, index=False)
    print(f"Processed data saved to {output_file}")

if __name__ == "__main__":
    # Specify the paths for input and output files
    input_file = 'colonnine-conta-bici.csv'  
    output_file = 'processed_bicycle_data.csv'  
    load_and_process_data(input_file, output_file)


