
# 2. **Interactive Table Filtering**:
#    ```python
#    st.markdown("## Sales Data")
#    sales_data = load_data()  # Assuming a function to load data
#    product = st.selectbox("Select a product:", products_list)
#    filtered_data = sales_data[sales_data['product'] == product]
#    st.write(filtered_data)
#    ```

import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta


st.title("Filter Table")
st.write(" ")
# Function to generate random sales data
def generate_sales_data(num_rows=10):
    # List of products
    products = ['Product A', 'Product B', 'Product C']
    
    # Start date for data generation
    start_date = datetime(2023, 1, 1)
    
    # End date for data generation
    end_date = datetime(2023, 12, 31)
    
    # Creating random sales data
    data = {
        'product': [random.choice(products) for _ in range(num_rows)],
        'date': [start_date + timedelta(days=random.randint(0, (end_date - start_date).days)) for _ in range(num_rows)],
        'sales': [random.randint(100, 1000) for _ in range(num_rows)]
    }

    # Creating a pandas DataFrame from the generated data
    return pd.DataFrame(data)

# Generate sales data
sales_data = generate_sales_data()

# Save the generated data to a CSV file
sales_data.to_csv('sales_data.csv', index=False)

# Display the generated data
st.markdown("## Generated Sales Data")
st.write(sales_data)

# Streamlit app to display sales data based on selected product
st.markdown("## Sales Data")

# Load data function
def load_data():
    # Replace 'sales_data.csv' with your actual data source
    data_path = 'sales_data.csv'
    
    # Assuming the data has columns like 'product', 'date', 'sales', etc.
    # Adjust column names accordingly based on your actual data
    columns = ['product', 'date', 'sales']

    # Read the CSV file into a pandas DataFrame
    sales_data = pd.read_csv(data_path, usecols=columns)

    # Returning the loaded data
    return sales_data



# Load data
sales_data = load_data()

# Dropdown for selecting a product
product = st.selectbox("Select a product", sales_data['product'].unique())

# Filter data based on selected product
filtered_data = sales_data[sales_data['product'] == product]

# Display filtered data
st.write(filtered_data)
