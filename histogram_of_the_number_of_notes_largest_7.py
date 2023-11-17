# Assuming you have a DataFrame named sorted_pivot_table
Value_values = note_durations_df.head(7)

plt.bar(range(len(Value_values)), Value_values['Count'], color='#4c72b0')

# Label the x-axis
plt.xlabel('Duration of notes')

# Label the y-axis
plt.ylabel('Count')

# Set the x-ticks and labels to match 'LastThreeNumbers'
plt.xticks(range(len(Value_values)), Value_values['Value'], rotation=80)

# Set a title for the histogram
plt.title('Histogram of the counting notes')

# Annotate the bars with their counts
for i, count in enumerate(Value_values['Count']):
    plt.text(i, count, str(count), ha='center', va='bottom')

# Display the histogram
plt.show()
