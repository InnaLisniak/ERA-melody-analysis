# Function to extract the start six floating-point numbers from a list
def extract_start_six_numbers(duration_list):
    return duration_list[:6]

# Apply the function to create a new column 'StartSixNumbers'
df['StartSixNumbers'] = df['Durations'].apply(lambda x: extract_start_six_numbers(x))

# Function to extract the last two floating-point numbers from a list
def extract_last_two_numbers(duration_list):
    return duration_list[-2:]

# Apply the function to create a new column 'LastTwoNumbers'
df['LastTwoNumbers'] = df['Durations'].apply(lambda x: extract_last_two_numbers(x))

# Display the updated DataFrame
df
