import streamlit as st

st.title('st.form')

#Full example of using the with notation
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine **OUT OF ORDER**')

with st.form('my_form'):
    st.subheader('**Order your coffee**')

    #Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta', 'Carcinogenica'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Raw', 'Light', 'Medium', 'Dark', 'Burnt'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'All milk...keep the coffee'])
    owncup_val = st.checkbox('Bring own cup')

    #Every form must have a submit button
    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write(':point_up: Place your order!')

st.header("2. Example with object notation")

form = st.form('my_object_form')
form.subheader('**Order your HOT CHOCOLATE**')
chocolate_type = form.selectbox('Chocolate bean', ['Belgian', 'French', 'Aztec'])
chocolate_blend = form.selectbox('Blend', ['Single origin', 'House blend', '1:2:3'])
chocolate_brew = form.selectbox('Brewing method', ['Microwave', 'Stovetop'])
chocolate_milk = form.select_slider('Milk intensity', ['Water', 'One percent', 'Half and Half', 'Cream'])
candy_cane = form.checkbox('Candy cane')
own_cup = form.checkbox('Bring own cup')
chocolate_submitted = form.form_submit_button('Submit')

if chocolate_submitted:
    st.markdown(f'''
        You have ordered:
        - Chocolate origin: `{chocolate_type}`
        - Chocolate blend: `{chocolate_blend}`
        - Brewing: `{chocolate_brew}`
        - Base: `{chocolate_milk}`
        - Candy cane: `{candy_cane}`
        - Bring own cup: `{own_cup}`
        ''')
else:
    st.write(':point_up: Place your order!')