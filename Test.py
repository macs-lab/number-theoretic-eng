import streamlit as st
from st_pages import Page, show_pages

# Specify what pages should be shown in the sidebar, and what their titles
# and icons should be

# Icons Link - https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/

show_pages(
    [
        Page("Test.py", "Welcome", ":house:"),
        Page("pages/Shapes.py", "Simple Shapes", ":large_green_circle:"),
        Page("pages/Lissajous.py", "Lissajous", ":curly_loop:"),
        Page("pages/Koch_Snowflake.py", "Koch Snowflake", ":snowflake:"),
        Page("pages/The_Chaos_Game.py", "Chaos Game", ":space_invader:"),
        Page("pages/Brownian_Motion.py", "Brownian", ":floppy_disk:"),
        Page("pages/Voronoi_script.py", "Voronoi", ":world_map:"),
        Page("pages/Meanders.py", "Meanders", ":desert_island:"),
        Page("pages/Fractals.py", "Fractals", ":herb:"),
        Page("pages/Chaos.py", "Chaos", ":milky_way:"),
        Page("pages/Fibonacci.py", "Fibonacci", ":shell:"),
        Page("pages/Modulo_Graphics.py", "Modulo Graphics", ":cyclone:"),
        Page("pages/Golden_Spiral.py", "Golden Spiral", ":sunflower:")
    ]
)


st.title('Welcome to the Number-theoretic Control and Engineering Demonstration Wesbite')
st.image('Images/Capstone_Poster_JPEG.jpg')
st.write('We demonstrate a library of intriguing patterns in nature and engineering. The patterns are based on various number theory concepts and can be customized with different parameters to create unique designs.')
st.write('The web-based application can additionally be interfaced with a mobile robot to draw the patterns physically.')
st.header('Team')
st.write('Boris Popov | Garrett Porter | Alejandro Martin-Villa | Xu Chen (advisor)')
st.header('Acknowledgement')
st.write('This project is supported in part by NSF Award No. 2141293 and Award No. 1953155.')
st.write('---')
st.subheader("_Note: printing only works if app is run locally_")
st.write('''In order to be able to print:
1) Clone the [github repository](https://github.com/macs-lab/number-theoretic-eng) to your local machine
2) Install the required Python packages by running `pip install -r requirements.txt`.
3) Run the app using the command `streamlit run Test.py` or `python -m streamlit run Test.py`.
4) Connect your Raspberry Pi to your computer via Bluetooth.
5) Open the `Backend/SendData.py` file and change line 19/20 to the MAC address of your Raspberry Pi.
6) Open your web browser and navigate to `http://localhost:8501` to view the app.
7) On your Raspberry Pi, uncomment and run the `RPI/Movement.py` file.
8) Once you have chosen a pattern, press the print button to send the data to the robot.
9) On the robot, click the button to start the print!

Note: You can adjust the size of the print by scaling the points in the Transform function in `Backend/SendData.py`
''')

#Page("pages/Tree.py", "Tree", ":maple_leaf:"),
