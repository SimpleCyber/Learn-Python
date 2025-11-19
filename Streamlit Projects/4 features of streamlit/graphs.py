# 7. **Dynamic Graphs Based on Selection**:
#    ```python
#    st.markdown("## Sales Graph")
#    product = st.selectbox("Choose a product", product_list)
#    graph = generate_graph(product)  # Assuming a function to generate graph
#    st.pyplot(graph)
# #    ```


import streamlit as st 


# Import necessary libraries
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Assuming product_list is a list of products
product_list = ["Product A", "Product B", "Product C"]

# Function to generate a sample sales graph
def generate_graph(product):
    # Generating sample data
    days = np.arange(1, 11)
    sales = np.random.randint(50, 100, size=(10,))
    
    # Plotting the graph
    plt.figure(figsize=(8, 6))
    plt.plot(days, sales, marker='o')
    plt.title(f"Sales Graph for {product}")
    plt.xlabel("Days")
    plt.ylabel("Sales")
    plt.grid(True)
    
    return plt

# Streamlit code
# Set the title for the Streamlit app
st.markdown("## Sales Graph")

# Create a selectbox for choosing a product from the product list
product = st.selectbox("Choose a product", product_list)

# Call the generate_graph function to create a graph for the selected product
graph = generate_graph(product)

# Display the generated graph using st.pyplot
st.pyplot(graph)


# Import necessary libraries
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Assuming product_list is a list of products
product_list = ["Product A", "Product B", "Product C"]

# Function to generate a sample sales graph
def generate_graph(product):
    # Generating sample data
    days = np.arange(1, 11)
    sales = np.random.randint(50, 100, size=(10,))
    
    # Plotting the graph
    plt.figure(figsize=(8, 6))
    plt.plot(days, sales, marker='o')
    plt.title(f"Sales Graph for {product}")
    plt.xlabel("Days")
    plt.ylabel("Sales")
    plt.grid(True)
    
    return plt

# Streamlit code
# Set the title for the Streamlit app
st.markdown("## Sales Graph")

# Create a selectbox for choosing a product from the product list
product = st.selectbox("Choose a product", product_list)

# Call the generate_graph function to create a graph for the selected product
graph = generate_graph(product)

# Display the generated graph using st.pyplot
st.pyplot(graph)

# Explanation:

# 1. `import streamlit as st`: Import the Streamlit library.

# 2. `import matplotlib.pyplot as plt`: Import the Matplotlib library for plotting graphs.

# 3. `import numpy as np`: Import NumPy for numerical operations.

# 4. `product_list = ["Product A", "Product B", "Product C"]`: Define a list of product names.

# 5. `def generate_graph(product):`: Define a function to generate a sample sales graph for a given product.


# 6. Inside `generate_graph` function:
#    - `days = np.arange(1, 11)`: Create an array representing days.
#    - `sales = np.random.randint(50, 100, size=(10,))`: Generate random sales data.
#    - `plt.figure(figsize=(8, 6))`: Set the figure size for the plot.
#    - `plt.plot(days, sales, marker='o')`: Plot the sales data.
#    - `plt.title(f"Sales Graph for {product}")`: Set the title of the graph based on the selected product.
#    - `plt.xlabel("Days")` and `plt.ylabel("Sales")`: Set the labels for the x and y axes.
#    - `plt.grid(True)`: Add a grid to the plot.
#    - `return plt`: Return the Matplotlib figure.


# 7. `st.markdown("## Sales Graph")`: Set the title for the Streamlit app section.

# 8. `product = st.selectbox("Choose a product", product_list)`: Create a selectbox for choosing a product.

# 9. `graph = generate_graph(product)`: Generate a graph for the selected product.

# 10. `st.pyplot(graph)`: Display the generated graph using the `st.pyplot` function.