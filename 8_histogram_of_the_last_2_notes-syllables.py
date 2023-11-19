import matplotlib.pyplot as plt
# Assuming you have a DataFrame named sorted_pivot_table
LastTwoNumbers_values = sorted_pivot_table.head(10)

plt.bar(range(len(LastTwoNumbers_values)), LastTwoNumbers_values['Count'], color='#4c72b0')

# Label the x-axis
plt.xlabel('Rhythmic model of final figures')

# Label the y-axis
plt.ylabel('Count')

# Set the x-ticks and labels to match 'LastTwoNumbers'
plt.xticks(range(len(LastTwoNumbers_values)), LastTwoNumbers_values['LastTwoNumbers'], rotation=80)

# Set a title for the histogram
plt.title('Histogram of the Last Two Syllables-Notes')

# Annotate the bars with their counts
for i, count in enumerate(LastTwoNumbers_values['Count']):
    plt.text(i, count, str(count), ha='center', va='bottom')

# Display the histogram
plt.show()
