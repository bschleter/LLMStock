import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_pandas_profiling import st_profile_report
import matplotlib.pyplot as plt
from motor import financial_analyst
from pandas import pandas as pd
def main(): 
    st.title("Brandon's ALora Analyst")

    company_name = st.text_input("Company Name:")
    analyze_button = st.button("Analyze")

    if analyze_button:
        if company_name:
            st. write("Thinking...JUST a moment")
            investment_thesis, hist = financial_analyst(company_name)

            #Select 'Open' and 'Close' columns from the hist dataframe
            hist_selected = hist["Close"]

            #Create a new figure in matplotlib
            #fig, ax = plt.subplots()

            # Calculate the 50-day simple moving average
            sma_50 = hist_selected.rolling(window=50).mean()

            # Plot the 'Close' column and the 50-day SMA on the same chart
            fig, ax = plt.subplots()
            hist_selected.plot(kind='line', ax=ax)
            sma_50.plot(kind='line', ax=ax, label='50 Day SMA')

            #Plot the selected data
            #hist_selected.plot(kind='line', ax=ax)

            #Set the title and axis labels
            ax.set_title(f"{company_name} Stock Price")
            ax.set_xlabel("Date")
            ax.set_ylabel("Price")

            #Add a legend to the plot
            ax.legend()
            #Display the plot in Streamlit
            st.pyplot(fig)

            st.write("Investment Thesis:")

            st.markdown(investment_thesis, unsafe_allow_html=True)
        else:
            st.write("Please enter a company name")

if __name__ == "__main__":
    main()



        

