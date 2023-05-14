import streamlit as st
import plotly.express as px
import backend

# Header for the web page
st.header(body='Weather forecast for the Next Days')

# Text box to entre to place
place = st.text_input(label='Place', value='london')

# Slider to select forecast for no of days
days = st.slider(label="Forecast Days", min_value=1, max_value=5)

# Dropdown list to choose option Temperature or Sky
option = st.selectbox(label='Select data to view', options=('Temperature', 'Sky'), )

# Sub header to display selections
st.subheader(body=f'{option} for next {days} days in {place}')

# Content display as per selection
try:
    if option == "Temperature":
        date, temp = backend.get_data(place=place, forecast_days=days, kind=option)
        figure = px.line(x=date, y=temp, labels={'x': "Days", 'y': 'Temp (c)'})
        st.plotly_chart(figure_or_data=figure)

    else:
        sky_pred, dates = backend.get_data(place=place, forecast_days=days, kind=option)

        repeat = 0
        s_len = len(sky_pred)
        image_path = []
        date_to_display = []

        for index, sky_cond in enumerate(sky_pred):
            image = f'images\{sky_cond.lower()}.png'

            image_path.append(image)
            date_to_display.append(dates[index])
            repeat = repeat + 1

            if repeat == s_len:
                break

        st.image(image=image_path, width=115, caption=date_to_display)
except KeyError:
    st.write('This place does not exist')
    