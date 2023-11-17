import os
from music21 import converter, note, chord
import pandas as pd

def count_note_durations_in_folder(folder_path):
    note_durations = {}

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.xml'):
            file_path = os.path.join(folder_path, file_name)
            s = converter.parse(file_path)

            for element in s.recurse().getElementsByClass([note.Note, chord.Chord]):
                if hasattr(element, 'duration'):
                    if isinstance(element, note.Note):
                        duration = element.duration.quarterLength
                        add_to_note_durations(note_durations, duration)
                    elif isinstance(element, chord.Chord):
                        # For chords, consider the maximum duration of its individual notes
                        for n in element.notes:
                            duration = n.duration.quarterLength
                            add_to_note_durations(note_durations, duration)

    return note_durations

def add_to_note_durations(note_durations, duration):
    if duration in note_durations:
        note_durations[duration] += 1
    else:
        note_durations[duration] = 1

def create_note_durations_dataframe(folder_path):
    note_durations = count_note_durations_in_folder(folder_path)

    total_count = sum(note_durations.values())
    data = {
        'Value': list(note_durations.keys()),
        'Count': list(note_durations.values()),
        'Percentage': [(count / total_count) * 100 for count in note_durations.values()]
    }

    df = pd.DataFrame(data)
    df = df.sort_values(by='Value')

    return df

if __name__ == "__main__":
    folder_path = '/content/drive/MyDrive/balads'  # Update with your folder path
    note_durations_df = create_note_durations_dataframe(folder_path)

    # Sort the DataFrame by the 'Count' column in descending order
    note_durations_df = note_durations_df.sort_values(by='Count', ascending=False)

    # Reset the index to have sequential row numbers
    note_durations_df = note_durations_df.reset_index(drop=True)

    # Print the sorted DataFrame
    print(note_durations_df)
    total_notes = note_durations_df['Count'].sum()
    print("Total number of notes:", total_notes)
