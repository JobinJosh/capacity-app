import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Constants and initial data
total_capacity = 120000  # Maximum capacity of Poruba
existing_population = 100000
water_per_person_per_day_litres = 107
electricity_per_person_per_year_kwh = 5370
people_per_sqkm = 136

# Function to calculate water capacity based on population
def calculate_water_capacity(population):
    return population * water_per_person_per_day_litres * 365 / 1000  # Convert litres to cubic meters

# Function to calculate electricity capacity based on population
def calculate_electricity_capacity(population):
    return population * electricity_per_person_per_year_kwh / 1000  # Convert kWh to MWh

# Function to calculate land coverage based on population
def calculate_land_coverage(population):
    land_sqkm = population / people_per_sqkm
    return land_sqkm

# Main title
st.title('Poruba Population Data')

# Sidebar with population input
new_population = st.sidebar.number_input('Enter New Population', min_value=0, max_value=total_capacity, value=existing_population, step=1000)

# Calculate capacities based on the input population
water_current_capacity = calculate_water_capacity(existing_population)
electricity_current_capacity = calculate_electricity_capacity(existing_population)
land_coverage_current = calculate_land_coverage(existing_population)

water_new_capacity = calculate_water_capacity(new_population)
electricity_new_capacity = calculate_electricity_capacity(new_population)
land_coverage_new = calculate_land_coverage(new_population)

# Calculate additional percentage needed for water and electricity
water_additional_percentage = ((water_new_capacity - water_current_capacity) / water_current_capacity) * 100
electricity_additional_percentage = ((electricity_new_capacity - electricity_current_capacity) / electricity_current_capacity) * 100

# Create a DataFrame for displaying capacities with units and additional percentage
capacities_data = {
    'Capacity Type': ['Water', 'Electricity', 'Land Coverage'],
    'Current Capacity': [water_current_capacity, electricity_current_capacity, land_coverage_current],
    'Current Units': ['million litres/day', 'MWh/year', 'sqkm'],
    'New Capacity': [water_new_capacity, electricity_new_capacity, land_coverage_new],
    'Additional Percentage Needed': ['{:.2f}%'.format(water_additional_percentage), '{:.2f}%'.format(electricity_additional_percentage), 'N/A']
}
capacities_df = pd.DataFrame(capacities_data)

# Display capacities in table format
st.header('Capacities')
st.table(capacities_df)

# Create larger, separate plots for water, electricity, and land coverage capacities
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 18))

# Water capacity plot
ax1.bar(['Current', 'New'], [water_current_capacity, water_new_capacity], color=['blue', 'blue'], alpha=0.7)
ax1.set_title('Water Capacity')
ax1.set_ylabel('Capacity (million litres/day)')

# Electricity capacity plot
ax2.bar(['Current', 'New'], [electricity_current_capacity, electricity_new_capacity], color=['red', 'red'], alpha=0.7)
ax2.set_title('Electricity Capacity')
ax2.set_ylabel('Capacity (MWh/year)')

# Land coverage plot
ax3.bar(['Current', 'New'], [land_coverage_current, land_coverage_new], color=['green', 'green'], alpha=0.7)
ax3.set_title('Land Coverage')
ax3.set_ylabel('Coverage (sqkm)')

# Adjust layout
plt.tight_layout()

# Display plots in Streamlit
st.header('Capacity Graphs')
st.pyplot(fig)
