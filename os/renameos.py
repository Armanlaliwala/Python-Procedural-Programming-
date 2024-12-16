import os 

for i in range(100):# Loop to create 100 directories named 'day1', 'day2', ..., 'day100' inside the 'os\data' directory

    os.rename(f"os\data\ day{i + 1}", f"os\data\ tutorial{i + 1}" )
