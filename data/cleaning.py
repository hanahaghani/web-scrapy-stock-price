from pathlib import Path
import pandas as pd

base_dir=Path(__file__).resolve().parent
data=pd.read_csv(base_dir/"raw"/"price.csv")
data.info()

price_columns = ["ons_gold","silver","coin","gold_18k"]

for column in price_columns:
    data[column]=pd.to_numeric(data[column],errors='coerce')
    print(data.info())

data['timestamp']=pd.to_datetime(data['timestamp'],errors='coerce')

data.info()

output_path=base_dir/"processed"/'price-final.csv'
data.to_csv(output_path,index=False)
