import pandas as pd
data = {
"Calories":[420,380,390],
"Durations":[50,40,45]
}
df = pd.DataFrame(data,index= ["day1","day2","day3"])
print(df)
print(df.loc["day2']
