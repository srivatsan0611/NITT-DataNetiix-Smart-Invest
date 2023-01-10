import streamlit as st
import pickle
#import xgboost
import pandas as pd
import numpy as np
from PIL import Image
import time
from datetime import datetime, timedelta

st.set_page_config(page_title='Smart Invest',page_icon=":tada:",layout="wide")

st.title('Smart Invest')
st.sidebar.header('Stock Return Prediction')
#image = Image.open('stock.webp')
#st.image(image, '')
#
sec={'IT':'IT_Sector.csv','CHEMICAL':'Chem_sector.csv','IRON AND STEEL':'Iron_And_Steel_Sector.csv','TEXTILE':'textile_sector.csv','CONSTRUCTION':'const_sector.csv'}

def load_data(sector):
    d=pd.read_csv(sector)
    return d


def main():

    text=st.sidebar.number_input('Enter Budget Per Stock',min_value=100)
    print(text)
    budget=float(text)

    sectors = ('IT', 'CHEMICAL', 'IRON AND STEEL', 'TEXTILE','CONSTRUCTION')
    selected_stock = st.sidebar.selectbox('Sector', sectors)


    data=load_data(sec[selected_stock])

    data['Best Selling Date Approx']=(pd.to_datetime(data['Best Selling Date Approx']))

    data_budget=data[(data.Close<budget) & (data['Best Selling Date Approx']>datetime.today())]

    sorted_data=data_budget.sort_values(by=['ROI'],ascending=False)
    #st.write(data.head(5))

    #sorted_data['Best Selling Date Approx']=sorted_data['Best Selling Date Approx']

    #st.dataframe(sorted_data.head(5))

    st.markdown("You can invest in these companies- ")

    n=len(sorted_data.head())
    print(n)

    for i in range(0,n):
      st.markdown(f" :blue[{sorted_data.iloc[i,1]}]")
      st.markdown(f"  -   with :green[{np.round(sorted_data.iloc[i,4],2)}%] ROI")
      st.markdown(f"  -   Check around :green[{sorted_data.iloc[i,5].date()}] to sell your stocks")


if __name__ == '__main__':
    main()