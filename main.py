import pandas as pd

# Load simulated data into a DataFrame
simulated_data = simulate_starbucks()
df = pd.DataFrame(simulated_data)

# Display the first few rows of the DataFrame
print(df.head())
# Calculate average wait times by drink type
avg_wait_time_by_drink = df.groupby('drink_type')['wait_time'].mean()

# Average wait time for mobile vs. in-store orders
avg_wait_time_by_order_type = df.groupby('is_mobile')['wait_time'].mean()

# Wait times during different hours of the day
df['order_time'] = pd.to_datetime(df['order_time'])
df['hour'] = df['order_time'].dt.hour
avg_wait_time_by_hour = df.groupby('hour')['wait_time'].mean()

# Output results
print("Average Wait Time by Drink Type:\n", avg_wait_time_by_drink)
print("Average Wait Time by Order Type:\n", avg_wait_time_by_order_type)
print("Average Wait Time by Hour:\n", avg_wait_time_by_hour)
# Count the number of orders by hour
orders_by_hour = df.groupby('hour').size()

# Output results
print("Orders by Hour:\n", orders_by_hour)
# Calculate total revenue by drink type and by hour
total_revenue_by_drink = df.groupby('drink_type')['price'].sum()
total_revenue_by_hour = df.groupby('hour')['price'].sum()

# Output results
print("Total Revenue by Drink Type:\n", total_revenue_by_drink)
print("Total Revenue by Hour:\n", total_revenue_by_hour)
