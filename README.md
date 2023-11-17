# ERA-melody-analysis
Code written for melody analysis in Estonian Literary Museum. All code is written to be used in Google Colaboratory using music scores in XML files as the source data and it was developed for scores of Ukrainian ballads which contain repetition and both single-voiced scores and multiple-voiced scores.

1_counting_the_total_number_of_notes.py
counts the number of notes in the corpus for all voices, as well as if there are chord notes.
2_histogram_counting_the_total_number_of_notes_largest_7.py
visualization of the most frequently repeated notes in the corpus

The following codes is based on the code at the address https://github.com/susmet/ERA-melody-analysis/blob/main/notes_durations_custom.py
We use it as block 3

4_Rhythmic_modeling_the_first_6_last_3_notes-syllables.py
The code creates a columns of the first 6 and the last 3 note-syllables.
5_table_of_the_first_6_notes_of_the_most_10.py
the result displays a table of the most used first 6 notes
6_horizontal_histogram_of_the_first_6_notes_of_the_most_frequent_10.ry
the code creates a histogram to the previous code
7_table_of_repetitions_of_the_last_3_notes_of_the_highest_10.py
the result displays a table of the last 3 most used notes
8_histogram_of_repetitions_of_the_last_3_notes_of_the_highest_10.py
the code creates a histogram to the previous code
