import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Zena\'s Amazing Athleisure Catalog')

streamlit.header("View Our color List")

#Snowflake-related functions
def get_color_list():
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  with my_cnx.cursor() as my_cur:
       my_cur.execute("select sweatsuit_color_or_style from upsell_mapping")
       return my_cur.fetchall()

#import colors
my_color_list = get_color_list()

#add a pick list
colors_to_show = my_color_list.loc[fruits_selected]


