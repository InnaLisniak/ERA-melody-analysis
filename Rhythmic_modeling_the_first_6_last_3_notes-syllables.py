# Function to extract the start six floating-point numbers from a list
def extract_start_six_numbers(duration_list):
    return duration_list[:6]

# Apply the function to create a new column 'StartSixNumbers'
df['StartSixNumbers'] = df['Durations'].apply(lambda x: extract_start_six_numbers(x))

# Function to extract the last three floating-point numbers from a list
def extract_last_three_numbers(duration_list):
    return duration_list[-3:]

# Apply the function to create a new column 'LastThreeNumbers'
df['LastThreeNumbers'] = df['Durations'].apply(lambda x: extract_last_three_numbers(x))

# Display the updated DataFrame
df