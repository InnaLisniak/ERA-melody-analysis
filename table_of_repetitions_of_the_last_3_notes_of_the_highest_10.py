# Convert lists to tuples
df['LastThreeNumbers'] = df['LastThreeNumbers'].apply(tuple)

# Create a pivot table-like result using groupby and count
pivot_table = df.groupby('LastThreeNumbers').size().reset_index(name='Count')
sorted_pivot_table = pivot_table.sort_values(by='Count', ascending=False)

# Display the sorted pivot table
#print(sorted_pivot_table)

LastThreeNumbers_values = sorted_pivot_table.head(10)

# Display the eight largest values
LastThreeNumbers_values.head(10)
