starts = {"users": 450, "sales": 50000, "active_customer": 200}
sales_barchart = {"labels":["Jan","Feb","March","Apr"], 
                  "values":[4500, 5200, 4800, 6100],
                  "title":"Neptasy Company Insights for 2026 Q1"
                }


import streamlit as st 

st.header(f":green[{sales_barchart['title']}]")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
# st.write("* Here the display")
col1, col2, col3 = st.columns(3)

with col1:
    Total_Users = starts["users"]
    st.info(f" :green[**Total Users**] \n\n :yellow[{Total_Users}]", icon=":material/group:")

with col2:
    sales= starts["sales"]
    st.info(f"**Total Sales** \n\n :yellow[{sales}]", icon=":material/analytics:")
    
    
    
with col3:
    active=starts["active_customer"]
    st.info(f"**Active User** \n\n :yellow[{active}]" , icon=":material/paid:")
    
    
# st.info(" **Total Users**", icon=":material/user_attributes:",
#           width="30px")
# st.info(" **Total Sales**", icon=":material/user_attributes:",
#           width="stretch")
# st.info(" **Action Users**", icon=":material/user_attributes:",
#           width="stretch")

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

st.info(f":violet[*Bar Chart Visualization*]")
st.bar_chart(sales_barchart, x="labels",y="values", sort=False, x_label="Months", y_label="Sales")



