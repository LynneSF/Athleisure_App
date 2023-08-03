import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Zena\'s Amazing Athleisure Catalog')

#Snowflake-related functions
def get_color_list():
  with my_cnx.cursor() as my_cur:
       my_cur.execute("select sweatsuit_color_or_style from upsell_mapping")
       return my_cur.fetchall()
