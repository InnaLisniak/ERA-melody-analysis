import matplotlib.pyplot as plt
# Assuming you have a DataFrame named sorted_pivot_table
LastThreeNumbers_values = sorted_pivot_table.head(10)

plt.bar(range(len(LastThreeNumbers_values)), LastThreeNumbers_values['Count'], color='#4c72b0')

# Label the x-axis
plt.xlabel('Rhythmic modeling of final figures')

# Label the y-axis
plt.ylabel('Count')

# Set the x-ticks and labels to match 'LastThreeNumbers'
plt.xticks(range(len(LastThreeNumbers_values)), LastThreeNumbers_values['LastThreeNumbers'], rotation=80)

# Set a title for the histogram
plt.title('Histogram of the Last Three Tones')

# Annotate the bars with their counts
for i, count in enumerate(LastThreeNumbers_values['Count']):
    plt.text(i, count, str(count), ha='center', va='bottom')

# Display the histogram
plt.show()
