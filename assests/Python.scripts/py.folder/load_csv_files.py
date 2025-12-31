
import pandas as pd
from sqlalchemy import create_engine

conn_string = 'postgresql://postgres:admin@localhost/painting'
db = create_engine(conn_string)
conn = db.connect()

df = pd.read_csv(r'C:\Users\HP\Videos\Painting_dataset\artist.csv')
df.to_sql('artist',con=conn,if_exists='replace',index=False)

df = pd.read_csv(r'C:\Users\HP\Videos\Painting_dataset\canvas_size.csv')
df.to_sql('canvas_size',con=conn,if_exists='replace',index=False)

df = pd.read_csv(r'C:\Users\HP\Videos\Painting_dataset\image_link.csv')
df.to_sql('image_link',con=conn,if_exists='replace',index=False)

df = pd.read_csv(r'C:\Users\HP\Videos\Painting_dataset\museum.csv')
df.to_sql('museum',con=conn,if_exists='replace',index=False)

df = pd.read_csv(r'C:\Users\HP\Videos\Painting_dataset\museum_hours.csv')
df.to_sql('museum_hours',con=conn,if_exists='replace',index=False)

df = pd.read_csv(r'C:\Users\HP\Videos\Painting_dataset\product_size.csv')
df.to_sql('product_size',con=conn,if_exists='replace',index=False)

df = pd.read_csv(r'C:\Users\HP\Videos\Painting_dataset\subject.csv')
df.to_sql('subject',con=conn,if_exists='replace',index=False)

df = pd.read_csv(r'C:\Users\HP\Videos\Painting_dataset\work.csv')
df.to_sql('work',con=conn,if_exists='replace',index=False)