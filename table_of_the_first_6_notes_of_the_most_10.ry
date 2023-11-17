# Convert lists to tuples
df['StartSixNumbers'] = df['StartSixNumbers'].apply(tuple)

# Create a pivot table-like result using groupby and count
pivot_table = df.groupby('StartSixNumbers').size().reset_index(name='Count')
sorted_pivot_table = pivot_table.sort_values(by='Count', ascending=False)

# Display the sorted pivot table
#print(sorted_pivot_table)

eight_largest_values = sorted_pivot_table.head(10)

# Display the eight largest values
eight_largest_values
