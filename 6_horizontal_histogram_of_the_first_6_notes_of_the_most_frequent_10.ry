import seaborn as sns
plt.title('Histogram of the First Six Syllables')
ax = sns.barplot(eight_largest_values, x="Count", y="StartSixNumbers", orient="h")
# Add counts as annotations to the right of the bars
for p in ax.patches:
    width = p.get_width()
    plt.text(width, p.get_y() + p.get_height() / 2, f'{width:.0f}', ha="left")
