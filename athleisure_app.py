import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Zena\'s Amazing Athleisure Catalog')

#import pandas
my_color_list = ('Red','Blue','Pink','Yellow','Green')


#add a pick list
colors_selected = streamlit.multiselect("Pick a sweatsuit color or style:", list(my_color_list.index),['Red','Blue'])
colors_to_show = my_color_list.loc[colors_selected]
