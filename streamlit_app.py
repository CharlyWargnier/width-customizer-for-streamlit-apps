import streamlit as st

st.set_page_config(page_title="Width Customizer", page_icon="🎈")

st.image(
    # "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/285/recycling-symbol_267b-fe0f.png"
    "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/285/balloon_1f388.png",
    width=100,
)

st.title("Width customizer for Streamlit Apps")

with st.expander("How to use this app", expanded=True):

    st.write(
        """
        1. Set width for your app
        2. Choose the number of columns
        3. Choose width for each column
        4. Copy the code below and paste it in your app!
        """
    )
    st.write("")

st.title("")

c1, c2, c3 = st.columns([0.9, 0.1, 1])

with c1:

    number = st.slider("Choose app width (in pixels)", 500, 780, 1400, key="c1Width")

with c3:

    columnSelection = st.selectbox("How many columns would you like?", [1, 2, 3])


def _max_width_():
    max_width_str = f"max-width: " + str(number) + "px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>
    """,
        unsafe_allow_html=True,
    )


_max_width_()

code = (
    """

import streamlit as st

def _max_width_():
    max_width_str = f'max-width: """
    + str(number)
    + '''px';

    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>
    """,
        unsafe_allow_html=True,
    ) 
   
_max_width_()

'''
)

if columnSelection is 1:

    st.title("#1")
    st.write(
        """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    """
    )

elif columnSelection is 2:

    c1, c2 = st.columns([1, 1])

    with c1:
        c1Width = st.number_input(
            "Column #1 width", min_value=0.1, value=0.5, step=0.1, key="c1Width"
        )

    with c2:
        c2Width = st.number_input(
            "Column #2 width", min_value=0.1, value=0.5, step=0.1, key="c2Width"
        )

    c1, c2 = st.columns([c1Width, c2Width])

    with c1:
        st.title("#1")
        st.write(
            """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
        """
        )
    with c2:
        st.title("#2")
        st.write(
            """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
        """
        )

elif columnSelection is 3:

    c1, c2, c3 = st.columns([1, 1, 1])

    with c1:
        c1Width = st.number_input(
            "Column #1 width", min_value=0.1, value=0.5, step=0.1, key="c1Width"
        )

    with c2:
        c2Width = st.number_input(
            "Column #2 width", min_value=0.1, value=0.5, step=0.1, key="c2Width"
        )

    with c3:
        c3Width = st.number_input(
            "Column #3 width", min_value=0.1, value=0.5, step=0.1, key="c3Width"
        )

    c1, c2, c3 = st.columns([c1Width, c2Width, c3Width])

    with c1:
        st.title("#1")
        st.write(
            """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
        """
        )
    with c2:
        st.title("#2")
        st.write(
            """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
        """
        )
    with c3:
        st.title("#3")
        st.write(
            """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
        """
        )

if columnSelection is 2:

    code2 = (
        """

c1, c2 = st.columns(["""
        + str(c1Width)
        + """, """
        + str(c2Width)
        + """])

with c1:
    st.title("#1")
    st.write(
        '''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    '''
    )
with c2:
    st.title("#2")
    st.write(
        '''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    '''
    )

 """
    )

    st.write("")
    st.write("")
    st.write("")

    with st.expander("⚙️  Get the code", expanded=True):

        st.code(code + code2, language="python")

elif columnSelection is 3:

    code2 = (
        """

c1, c2, c3 = st.columns(["""
        + str(c1Width)
        + """, """
        + str(c2Width)
        + """, """
        + str(c3Width)
        + """])

with c1:
    st.title("#1")
    st.write(
        '''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    '''
    )
with c2:
    st.title("#2")
    st.write(
        '''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    '''
    )
with c3:
    st.title("#3")
    st.write(
        '''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    '''
    )

 """
    )

    st.write("")
    st.write("")
    st.write("")

    with st.expander("🎁 Get the code", expanded=True):

        st.code(code + code2, language="python")

if columnSelection is 1:

    code2 = """
st.title("#1")
st.write(
    '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
'''
)

 """

    st.write("")
    st.write("")
    st.write("")

    with st.expander("🎁 Get the code", expanded=True):

        st.code(code + code2, language="python")
