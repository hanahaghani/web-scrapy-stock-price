from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

base_dir=Path(__file__).resolve().parent
data=pd.read_csv(base_dir/"data/raw"/"price.csv")
price_columns = ["ons_gold","silver","coin","gold_18k"]

for column in price_columns:
    data[column]=data[column].str.replace(',','',regex=False)
    data[column]=pd.to_numeric(data[column],errors='coerce')
    print(data.info())


data['timestamp']=data['timestamp'].str.replace(',','',regex=False)
data['timestamp']=pd.to_datetime(data['timestamp'],errors='coerce')


output_path=base_dir/"data/processed"/'price-final.csv'
data.to_csv(output_path,index=False)

engine = create_engine(
    "mysql+pymysql://market_user:Market1234@localhost/market_data"
)

output_path_sql=base_dir/"data/processed"/'price.sql'
data.to_sql("price",con=engine ,if_exists="append",index=False)


