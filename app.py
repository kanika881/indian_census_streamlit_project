# streamlit run your_script.py
import streamlit as st 
import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
df=pd.read_csv("india_data.csv")
list_states=list(df["State name"].unique())
sorted(list_states)
# list_states.insert(0,"All")
st.sidebar.title("please select the options to see the data:")
selected_state=st.sidebar.selectbox("select a state",["ALL","State Vs State","States"])
list_categroy=["population","Literacry","Caste","Workers","Religion","Basic Neccessties","Citizen Age Group","Vehicles Owned","Household with gadjets","Housing Info","Household size","Water supply","Married","Power Parity"]

if "show_landing" not in st.session_state:
    st.session_state.show_landing=True
if st.session_state.show_landing:
    st.title("📊 Indian Census Data Explorer")
    st.write("Welcome! Use the options on the left sidebar to explore census data by state, category, and parameter. You can view comparisons as indian maps or pie charts.")
    col1,=st.columns([1])
    with col1:
        image = Image.open("india.jpg") # Open the image file
        st.image(image, width=500)
if selected_state=="State Vs State":
    selected_options_multiselect=st.sidebar.multiselect("please select more than one states to compare",list_states)
if selected_state=="States":
    state_select=st.sidebar.selectbox("please select a state to compare:",list_states)
if selected_state:
    category=st.sidebar.selectbox("please select a category to compare",list_categroy)

if selected_state:

    if category=="population":
        sub_category=st.sidebar.selectbox("select One parameter",['Population','Male','Female'])
    elif category=="Literacry":
        sub_category=st.sidebar.selectbox("select One parameter",['Literate','Male_Literate','Female_Literate','Below_Primary_Education',
 'Primary_Education',
 'Middle_Education',
 'Secondary_Education',
 'Higher_Education',
 'Graduate_Education',
 'Other_Education',
 'Literate_Education',
 'Illiterate_Education'])
    elif category=="Caste":
        sub_category=st.sidebar.selectbox("select One parameter",['SC','Male_SC','Female_SC','ST','Male_ST','Female_ST'])
    elif category=="Workers":
        sub_category=st.sidebar.selectbox("select One parameter",['Main_Workers','Marginal_Workers','Non_Workers','Cultivator_Workers','Agricultural_Workers','Household_Workers','Other_Workers'])
    elif category=="Religion":
        sub_category=st.sidebar.selectbox("select One parameter",['Hindus',
 'Muslims',
 'Christians',
 'Sikhs',
 'Buddhists',
 'Jains',
 'Others_Religions',
 'Religion_Not_Stated'])
    elif category=="Basic Neccessties":
        sub_category=st.sidebar.selectbox("select One parameter",['LPG_or_PNG_Households',
    'Housholds_with_Electric_Lighting',
    'Households_with_Internet',
    'Households_with_Computer',
    'Rural_Households',
    'Urban_Households',
    'Households'])
    elif category=="Citizen Age Group":
        sub_category=st.sidebar.selectbox("select One parameter",['Age_Group_0_29',
 'Age_Group_30_49',
 'Age_Group_50',
 'Age not stated'])
    elif category=="Vehicles Owned":
        sub_category=st.sidebar.selectbox("select One parameter",['Households_with_Bicycle',
 'Households_with_Car_Jeep_Van',
 'Households_with_Radio_Transistor',
 'Households_with_Scooter_Motorcycle_Moped'])
    elif category=="Household with gadjets":
        sub_category=st.sidebar.selectbox("select One parameter",['Households_with_Telephone_Mobile_Phone_Landline_only',
 'Households_with_Telephone_Mobile_Phone_Mobile_only',
 'Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car',
 'Households_with_Television',
 'Households_with_Telephone_Mobile_Phone',
 'Households_with_Telephone_Mobile_Phone_Both'])
    elif category=="Housing Info":
        sub_category=st.sidebar.selectbox("select One parameter",['Condition_of_occupied_census_houses_Dilapidated_Households',
 'Households_with_separate_kitchen_Cooking_inside_house',
 'Having_bathing_facility_Total_Households',
 'Having_latrine_facility_within_the_premises_Total_Households',
 'Ownership_Owned_Households',
 'Ownership_Rented_Households',
 'Type_of_bathing_facility_Enclosure_without_roof_Households',
 'Type_of_fuel_used_for_cooking_Any_other_Households',
 'Type_of_latrine_facility_Pit_latrine_Households',
 'Type_of_latrine_facility_Other_latrine_Households',
 'Type_of_latrine_facility_Night_soil_disposed_into_open_drain_Households',
 'Type_of_latrine_facility_Flush_pour_flush_latrine_connected_to_other_system_Households',
 'Not_having_bathing_facility_within_the_premises_Total_Households',
 'Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households'])
    elif category=="Household size":
        sub_category=st.sidebar.selectbox("select One parameter",['Household_size_1_person_Households',
 'Household_size_2_persons_Households',
 'Household_size_1_to_2_persons',
 'Household_size_3_persons_Households',
 'Household_size_3_to_5_persons_Households',
 'Household_size_4_persons_Households',
 'Household_size_5_persons_Households',
 'Household_size_6_8_persons_Households',
 'Household_size_9_persons_and_above_Households'])
    elif category=="Water supply":
        sub_category=st.sidebar.selectbox("select One parameter",['Main_source_of_drinking_water_Un_covered_well_Households',
 'Main_source_of_drinking_water_Handpump_Tubewell_Borewell_Households',
 'Main_source_of_drinking_water_Spring_Households',
 'Main_source_of_drinking_water_River_Canal_Households',
 'Main_source_of_drinking_water_Other_sources_Households',
 'Main_source_of_drinking_water_Other_sources_Spring_River_Canal_Tank_Pond_Lake_Other_sources__Households',
 'Location_of_drinking_water_source_Near_the_premises_Households',
 'Location_of_drinking_water_source_Within_the_premises_Households',
 'Main_source_of_drinking_water_Tank_Pond_Lake_Households',
 'Main_source_of_drinking_water_Tapwater_Households',
 'Main_source_of_drinking_water_Tubewell_Borehole_Households','Location_of_drinking_water_source_Away_Households'])
    elif category=="Married":
        sub_category=st.sidebar.selectbox("select One parameter",['Married_couples_1_Households',
 'Married_couples_2_Households',
 'Married_couples_3_Households',
 'Married_couples_3_or_more_Households',
 'Married_couples_4_Households',
 'Married_couples_5__Households',
 'Married_couples_None_Households'])
    elif category=="Power Parity":
        sub_category=st.sidebar.selectbox("select two parameter",['Power_Parity_Less_than_Rs_45000',
 'Power_Parity_Rs_45000_90000',
 'Power_Parity_Rs_90000_150000',
 'Power_Parity_Rs_45000_150000',
 'Power_Parity_Rs_150000_240000',
 'Power_Parity_Rs_240000_330000',
 'Power_Parity_Rs_150000_330000',
 'Power_Parity_Rs_330000_425000',
 'Power_Parity_Rs_425000_545000',
 'Power_Parity_Rs_330000_545000',
 'Power_Parity_Above_Rs_545000',
 'Total_Power_Parity'])
        
if selected_state != "All" or category != "Population" or  sub_category!= "Urban_Households":
    st.session_state.show_landing = False
button1=st.sidebar.button("plot on map")
button2=st.sidebar.button("plot a pie chart")
button3=st.sidebar.button("Home")

if button1:
    if selected_state=="State Vs State":
        if selected_options_multiselect:
            cols=st.columns(len(selected_options_multiselect))
            
            for idx,state in enumerate(selected_options_multiselect):
                with cols[idx]:
                    data=df[df["State name"]==state]
                    data=data[["District code","State name","District name",sub_category,"Latitude","Longitude"]]
                    st.subheader(f"Top 5 districts with highest {sub_category} in {state}")
                    st.dataframe(data.sort_values(by=sub_category,ascending=False,ignore_index=True)[["State name","District name",sub_category]].head())
                    fig=px.scatter_mapbox(data,lat="Latitude",lon="Longitude",size=sub_category,color="District name",zoom=6,mapbox_style="carto-positron",size_max=10,width=500,title=f"Size of marker depends on the count of {sub_category} in {state}'s each district")
                    st.plotly_chart(fig,use_container_width=True)
            
if button2:
    if selected_state=="State Vs State":
       if selected_options_multiselect:
           st.subheader("Data is based on 2011 census")
           cols=st.columns(len(selected_options_multiselect))
           for idx,state in enumerate(selected_options_multiselect):
               with cols[idx]:
                   data=df[df["State name"]==state][["District code","District name","State name",sub_category]]
                   fig=px.sunburst(data,path=["State name","District name"],values=sub_category,color_discrete_map="vividis",title=f"sunburst graph for {sub_category}",subtitle=f"{state.lower()} and its Districts")
                   st.plotly_chart(fig, use_container_width=True)
                   data1=data.sort_values(by=sub_category,ascending=False,ignore_index=True)[["District name",sub_category]].head(1)
                   data2=data.sort_values(by=sub_category,ignore_index=True)[["District name",sub_category]].head(1).head(1)
                   st.write(f"Districts with highest and lowest **{sub_category}** for the city **{state}**")
                   st.subheader("Highest:")
                   st.dataframe(data1)
                   st.subheader("Lowest:")
                   st.dataframe(data2)
if button3:
    st.session_state.show_landing = True
if button1:
    
    if selected_state=="ALL":
        st.subheader("Data is based on 2011 census")
        data=df.groupby(["State name", "District name", "District code", "Latitude", "Longitude"])[sub_category].sum().reset_index()
        # data=data.merge(df,on=["District name",sub_category])[["State name","District name",sub_category,"District code","Latitude","Longitude"]]
        st.subheader(f"Top 5 districts with highest {sub_category}")
        st.dataframe(data.sort_values(by=sub_category,ascending=False).head())
        # st.dataframe(data)
        fig=px.scatter_mapbox(data,lat="Latitude",lon="Longitude",size=sub_category,color="State name",zoom=3,mapbox_style="open-street-map",width=1000,hover_name="District name",title=f"Size of marker depends on the count of {sub_category} in each districts")
        st.plotly_chart(fig,use_container_width=True)
        # st.write(f"****")
    elif selected_state=="States":
        data=df[df["State name"]==state_select]
        data=data[["District code","State name","District name",sub_category,"Latitude","Longitude"]]
        st.subheader(f"Top 5 districts with highest {sub_category}")
        st.dataframe(data.sort_values(by=sub_category,ascending=False).head())
        
        
        fig=px.scatter_mapbox(data,lat="Latitude",lon="Longitude",size=sub_category,color="District name",zoom=6,mapbox_style="carto-positron",size_max=35,width=1000,title=f"Size of marker depends on the count of {sub_category} in {state_select}'s each district")
        st.plotly_chart(fig,use_container_width=True)
        # st.write(f"****")
if button2:
    if selected_state=="ALL":
        st.subheader("Data is based on 2011 census")
        temp=df.groupby(["State name","District name"])[sub_category].sum().reset_index()

       
        col1,col2=st.columns(2)
     
        
        with col2:
            st.subheader("sunburst graph: with path as states and districts ")
            state_level = temp.groupby("State name", as_index=False)[sub_category].sum()
            state_level["parent"] = ""   # states have no parent

            # District-level data
            district_level = temp.rename(columns={"District name": "label", "State name": "parent"})
            district_level = district_level[["label", "parent", sub_category]]

            # Rename state-level columns
            state_level = state_level.rename(columns={"State name": "label", sub_category: sub_category})

            # Combine states + districts
            all_nodes = pd.concat([state_level[["label","parent",sub_category]],
                                district_level[["label","parent",sub_category]]])

            # Sunburst chart
            fig = go.Figure(go.Sunburst(
                labels=all_nodes["label"],
                parents=all_nodes["parent"],
                values=all_nodes[sub_category],
                insidetextorientation='radial',
                maxdepth=2,
                marker=dict(
            colors=temp["State name"],    # use values as color
            # colorscale="cividis",          # choose scale: Viridis, Blues, Reds, Rainbow etc.
            # showscale=True 
            )
                ))

            fig.update_layout(
                autosize=False,
                width=400,
                height=400,
                # text=sub_category,
                
                margin = dict(t=0, l=0, r=0, b=0)
            )
            st.plotly_chart(fig, use_container_width=True) 
            st.subheader("for better visiblity of each states and their respective districts:")
            st.markdown("-click and unclick on the states")
            
        with col1:
            
            
            st.subheader(f"highest {sub_category} in each state")
            show=df.groupby(["State name","District name"])[sub_category].sum().reset_index().sort_values(by=[sub_category],ascending=False).drop_duplicates(subset=["State name"],ignore_index=True)
            st.dataframe(show)
           
            # st.markdown(f"-color on the district closer to color scale shows increase in  {sub_category}")
    elif selected_state=="States":
        st.title("Data is based on 2011 Census")
        col1,col2=st.columns([1,2])
        data=df[df["State name"]==state_select][["District code","District name","State name",sub_category,]]
        with col1:
            
            fig=px.sunburst(data,path=["State name","District name"],values=sub_category,color_discrete_map="vividis",title=f"sunburst graph for {sub_category}",subtitle=f"{selected_state.lower()} and its Districts")
            st.plotly_chart(fig, use_container_width=True)
            # st.write()
            
        with col2:
            data1=data.sort_values(by=sub_category,ascending=False).head(1)
            data2=data.sort_values(by=sub_category).head(1)
            st.write(f"Districts with highest and lowest **{sub_category}** for the city **{state_select}**")
            st.subheader("Highest:")
            st.dataframe(data1)
            st.subheader("Lowest:")
            st.dataframe(data2)
        
            




        