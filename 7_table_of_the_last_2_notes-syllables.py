# Convert lists to tuples
df['LastTwoNumbers'] = df['LastTwoNumbers'].apply(tuple)

# Create a pivot table-like result using groupby and count
pivot_table = df.groupby('LastTwoNumbers').size().reset_index(name='Count')
sorted_pivot_table = pivot_table.sort_values(by='Count', ascending=False)

# Display the sorted pivot table
#print(sorted_pivot_table)

LastTwoNumbers_values = sorted_pivot_table.head(10)

# Display the ten largest values
LastTwoNumbers_values.head(10)
