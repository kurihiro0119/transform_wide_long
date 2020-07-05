import pandas as pd
import csv

csv_file = open("sample.csv", "r",
                encoding="ms932", errors="", newline="")
f = csv.reader(csv_file, delimiter=",", doublequote=True,
               lineterminator="\r\n", quotechar='"', skipinitialspace=True)
columns = next(f)
data = []

for row in f:
    data.append(row)

df = pd.DataFrame(data, columns=columns)
df_t = df.pivot_table(values=[columns[1]], index=[columns[0]], columns=[
                      columns[2]], aggfunc='sum', fill_value='N/A')
print(df_t)
