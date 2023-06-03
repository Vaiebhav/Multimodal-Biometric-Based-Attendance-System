# import pandas as pd

# # Read the attendance Excel sheet into a pandas dataframe
# df = pd.read_excel("attendance.xlsx",sheet_name=None)

# # Prompt the user to enter the student name
# student_name = input("Enter the student name: ")

# # Filter the dataframe to include only rows where the student name matches
# student_attendance = df[df["Name"] == student_name]

# # Calculate the total number of classes attended by the student
# classes_attended = student_attendance.shape[0]

# # Calculate the total number of classes held (assuming one entry per class)
# classes_held = len(df.keys())

# # Calculate the attendance percentage
# attendance_percentage = (classes_attended / classes_held) * 100

# # Print the attendance percentage
# print(f"{student_name} attended {classes_attended} out of {classes_held} classes ({attendance_percentage:.2f}% attendance)")


# import pandas as pd
# import openpyxl

# # Read the attendance Excel sheet into a pandas dataframe
# df = pd.read_excel("attendance.xlsx", sheet_name=None)

# # Count the number of sheets in the file to get the total number of classes held
# classes_held = len(df.keys())

# # Prompt the user to enter the student name
# student_name = input("Enter the student name: ")

# # Filter the dataframe to include only rows where the student name matches
# student_attendance = df[df["Name"] == student_name]

# # Calculate the total number of classes attended by the student
# classes_attended = student_attendance.shape[0]

# # Calculate the attendance percentage
# attendance_percentage = (classes_attended / classes_held) * 100

# # Print the attendance percentage
# print(f"{student_name} attended {classes_attended} out of {classes_held} classes ({attendance_percentage:.2f}% attendance)")


import pandas as pd

# Read the attendance Excel sheet into a pandas dataframe
df = pd.read_excel("attendance.xlsx", sheet_name=None)

# Prompt the user to enter the student name
student_name = input("Enter the student name: ")

# Filter the dataframe to include only rows where the student name matches
attendance_count = 0
for sheet_name in df.keys():
    sheet_attendance = df[sheet_name][df[sheet_name]["Name"] == student_name]
    attendance_count += sheet_attendance.shape[0]

# Calculate the total number of classes held (assuming one sheet per class)
classes_held = len(df.keys())

# Calculate the attendance percentage
attendance_percentage = (attendance_count / classes_held) * 100

# Print the attendance percentage
print(f"{student_name} attended {attendance_count} out of {classes_held} classes ({attendance_percentage:.2f}% attendance)")
