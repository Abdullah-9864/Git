import pandas as pd

# ==========================
# CONFIGURATION
# ==========================

input_file = "tb.xlsx"   # weekly file
degree_section = "BSIT-6th-M2"               # student input
output_file = "Filtered_Timetable.xlsx"

# ==========================
# LOAD FILE
# ==========================

df = pd.read_excel(input_file)

# Rename first two columns properly
df.rename(columns={
    df.columns[0]: "Day",
    df.columns[1]: "Room"
}, inplace=True)

# ==========================
# CONVERT WIDE → LONG
# ==========================

df_long = df.melt(
    id_vars=["Day", "Room"],
    var_name="Time Slot",
    value_name="Lecture Info"
)

# Remove empty cells
df_long = df_long.dropna(subset=["Lecture Info"])

# Convert everything to string (important for search)
df_long["Lecture Info"] = df_long["Lecture Info"].astype(str)

# ==========================
# FILTER BY DEGREE/SECTION
# ==========================

filtered = df_long[
    df_long["Lecture Info"].str.contains(degree_section, case=False)
]

# ==========================
# CLEAN OUTPUT (optional)
# ==========================

filtered = filtered.sort_values(by=["Day", "Time Slot"])

# ==========================
# EXPORT RESULT
# ==========================

filtered.to_excel(output_file, index=False)

print("Filtered timetable saved as:", output_file)
