import streamlit as st
import pandas as pd
import time

df = ""
Q1 = ""
score = 0

st.markdown(
    """
    <style>
        .stProgress > div > div > div > div {
            height: 600px;
        }
    </style>""",
    unsafe_allow_html=True,
)

progress_colour = st.sidebar.selectbox(
    "Which colour for progress bars",
    ["green", "blue", "orange", "red", "purple", "yellow"]
)

if progress_colour == "green":
    st.markdown(
    """
    <style>
        .stProgress > div > div > div > div {
            background-color: green;
        }
    </style>""",
    unsafe_allow_html=True,
)
elif progress_colour == "orange":
    st.markdown(
    """
    <style>
        .stProgress > div > div > div > div {
            background-color: orange;
        }
    </style>""",
    unsafe_allow_html=True,
)
elif progress_colour == "red":
    st.markdown(
    """
    <style>
        .stProgress > div > div > div > div {
            background-color: red;
        }
    </style>""",
    unsafe_allow_html=True,
)
elif progress_colour == "purple":
    st.markdown(
    """
    <style>
        .stProgress > div > div > div > div {
            background-color: purple;
        }
    </style>""",
    unsafe_allow_html=True,
)
elif progress_colour == "blue":
    st.markdown(
    """
    <style>
        .stProgress > div > div > div > div {
            background-color: blue;
        }
    </style>""",
    unsafe_allow_html=True,
)
elif progress_colour == "yellow":
    st.markdown(
    """
    <style>
        .stProgress > div > div > div > div {
            background-color: yellow;
        }
    </style>""",
    unsafe_allow_html=True,
)

st.set_page_config(
    page_title="Learn Romansh! (Still in progress)", page_icon="🇨🇭", initial_sidebar_state="expanded"
)

st.sidebar.title("Which lesson")
st.sidebar.write("Choose which lesson you're on")
page = st.sidebar.radio(
        "Go to",
        ["Welcome", "Lesson 1", "Lesson 2", "Chat 1", "Lesson 3", "Lesson 4", "Lesson 5"]
    )

if page == "Lesson 1":
    if st.button("Start"):
        df = pd.DataFrame({
        'English': ["Hello", "Good morning", "Good afternoon", "How"],
        'Romansh': ["Allegra", "Bun di", "Buna saira", "Co"]
        })

        df
        st.markdown("---")
        st.markdown("---")
        
    
    Q1 = st.text_area("What is 'Hello'?")
    if Q1 == "Allegra":
        score = score + 1
        Q2 = st.text_area("What is 'How'?")
        if Q2 == "Co":
            score = score + 1
            Q3 = st.text_area("What is 'Hello, how?'?")
            if Q3 == "Allegra, co?":
                score = score + 1    
                Q4 = st.text_area("What is 'Good afternoon'?")
                if Q4 == "Buna saira":
                    placeholder = st.empty()
                    placeholder.progress(50, "Half way there!")    
                    score = score + 1    
                    Q5 = st.text_area("What is 'Good morning'?")
                    if Q5 == "Bun di":
                        score = score + 1    
                        Q6 = st.text_area("What is 'Hello, good morning'?")
                        if Q6 == "Allegra, bun di":
                            score = score + 1    
                            Q7 = st.text_area("What is 'Good afternoon, how?'?")
                            if Q7 == "Buna saira, co?":
                                score = score + 1    
                                Q8 = st.text_area("What is 'Good afternoon, good morning'?")
                                if Q8 == "Buna saira, bun di":
                                    score = score + 1    
                                    st.balloons() 
                                        
if page == "Welcome":
    st.title("Romansh for you")
    st.caption("This web app is still being made. currently the content is limited")
    st.markdown("""
    **Romansh for you** is a :rainbow[completely free] way to learn Romansh for everyone.
    The way it works is that at the beginning of every lesson there is a button like this:""")
    st.button("Start")
    st.markdown("That reveals a table like this:")
    df = pd.DataFrame({
        'English': ["Hello", "Good morning", "Good afternoon", "How"],
        'Romansh': ["Allegra", "Bun di", "Buna saira", "Co"]
    })

    df
    st.markdown("This table shows your vocabulary for that lesson. Once you have memorised those words, you can start answering the questions. When you have finished all the questions, you will see balloons go across the screen")
    if st.button("Show example balloons"):
        st.balloons()
    st.markdown("""The questions in this course are **case sensitive**, so if nothing happens when you enter your answer check you have mirrored the punctuation in the question.""")
    
    st.markdown("To enter you answer press **ctrl+enter**, or on a phone **tap the bottom right corner** of the text input area")
    st.title("Chats")
    st.markdown("""
    In this course, there are multiple chats. When you enter a chat lesson, type in the given starting word **in Romansh**. The bot will write its response back, and what you should write next will appear under that. **If you do not write the correct response, or miss capital letters or punctuation (except for full stops when the english text doesn't have them), the chat will not work!** You repeat that until you are told the chat has finished. **You only write things in Romansh in a chat lesson**. """)
    st.write("Learning another language can be hard, and we suggest you check out [our notes](https://romansh-notes-el9msjjcuqzbtijzp6z6iu.streamlit.app/) about things that are slightly different than english") 

answer = 1

if page == "Chat 1":
    answer = st.chat_input("")
    st.title("Chat 1")
    st.caption("You can start by saying 'hello'")
    
    if answer == "Allegra":
        placeholder = st.empty()
        placeholder.progress(0)
        with st.chat_message("assistant"):
            st.markdown("Bun di")
        st.write("Respond with 'How are you?'")
    elif answer == "Co vai?":
        placeholder = st.empty()
        placeholder.progress(50)
        with st.chat_message("Assistant"):
            st.markdown("Bain grazia, e ti?")
        st.write("Respond with 'Well'")
    elif answer == "Bain":
        placeholder = st.empty()
        placeholder.progress(75)
        with st.chat_message("assistant"):
            st.markdown("Bun")
        st.write("Respond with 'Goodbye'")
    elif answer == "A revair":
        placeholder = st.empty()
        placeholder.progress(100)
        with st.chat_message("assistant"):
            st.markdown("A revair!")
        st.success("You just completed your first chat!")
        st.balloons()

if page == "Lesson 2":
    if st.button("Start"):
        df = pd.DataFrame({
            'English': ["How are you?", "Good", "Goodbye", "Well", "Thank you", "And you?"],
            'Romansh': ["Co vai?", "Bun", "A revair", "Bain", "Grazia", "E ti?"]
            })

    df
    st.markdown("---")
    st.markdown("---")

    score = 0    
    L2Q1 = st.text_area("What is 'How are you?'")
    if L2Q1 == "Co vai?": 
        score = score + 1
        L2Q2 = st.text_area("What is 'Good afternoon, how are you? Well'")
        if L2Q2 == "Buna saira, co vai? Bain":
            score = score + 1
            L2Q3 = st.text_area("What is 'Good bye, thank you'")
            if L2Q3 == "A revair, grazia":
                score = score + 1    
                L2Q4 = st.text_area("What is 'Good, and you?'")
                if L2Q4 == "Bun, e ti?":
                    placeholder = st.empty    
                    placeholder.progress(50, "Half way there!")    
                    score = score + 1    
                    L2Q5 = st.text_area("What is 'Thank you, how are you?'")
                    if L2Q5 == "Grazia, co vai?":
                        score = score + 1    
                        L2Q6 = st.text_area("What is 'Well, thank you. Goodbye'")
                        if L2Q6 == "Bain, grazia. A revair":
                                L2Q8 = st.text_area("What is 'Good morning, how are you?'")
                                if L2Q8 == "Bun di, co vai?":
                                    st.balloons()
if page == "Lesson 3":
    if st.button("Start"):
        df = pd.DataFrame({
        'English': ["I am called ...", "Please", "Nice to meet you", "Yes", "No"],
        'Romansh': ["Jau hai num ...", "Per plaschair", "Fa plaschair", "Gea", "Na"]
        })

        df
        st.markdown("---")
        st.markdown("---")
    L3Q1 = st.text_area("What is 'I am called Simon' in Romansh?")
    if L3Q1 == "Jau hai num Simon":
        L3Q2 = st.text_area("What is 'Hello, nice to meet you' in Romansh?")
        if L3Q2 == "Allegra, fa plaschair":
            L3Q3 = st.text_area("What is 'Yes, please' in Romansh?")
            if L3Q3 == "Gea, per plaschair":
                L3Q4 = st.text_area("What is 'No, thank you' in Romansh?")
                if L3Q4 == "Na, grazia":
                    placeholder = st.empty()
                    placeholder.progress(50, "You're half way there!")
                    L3Q5 = st.text_area("What is 'Yes, I am called James, nice to meet you'in Romansh?")
                    if L3Q5 == "Gea, jau hai num James, fa plaschair":
                        L3Q6 = st.text_area("What is 'I am called Nando, and you?' in Romansh")
                        if L3Q6 == "Jau hai num Nando, e ti?":
                            L3Q7 = st.text_area("What is 'Good morning, nice to meet you'in Romansh")
                            if L3Q7 == "Bun di, fa plaschair":
                                L3Q8 = st.text_area("What is 'No, good afternoon' in Romansh?")
                                if L3Q8 == "Na, buna saira":
                                    st.balloons()
                                    placeholder2 = st.empty()
                                    placeholder2.progress(100, "**Done!**")

if page == "Lesson 4":
    if st.button("Start"):
        df = pd.DataFrame({
        'English': ["I am", "You are", "And", "If"],
        'Romansh': ["Jau sun", "Ti es", "E", "Sche"]
        })

        df
        st.markdown("---")
        st.markdown("---")
    L4 = st.text_area("What is 'I am well, thank you' in Romansh")
    if L4 == "Jau sun bain, grazia":
        L4 = st.text_area("What is 'You are Simon, yes?' in Romansh")
        if L4 == "Ti es Simon, gea?":
            L4 = st.text_area("What is 'If you are well, hello' in Romansh")
            if L4 == "Sche ti es bain, allegra":
                L4 = st.text_area("What is 'You are well, and I am well' in Romansh")
                if L4 == "Ti es bain, e jau sun bain":
                    placeholder = st.empty()
                    placeholder.progress(50, "You're half way there!")
                    st.markdown("**Did you know you can make questions by switching the verb and noun around?**")
                    L4 = st.text_area("What is 'Are you well?' in romansh")
                    if L4 == "Es ti bain?":
                        L4 = st.text_area("What is 'Am I well? If I am, you are well' in Romansh")
                        if L4 == "Sun jau bain? Sche jau sun, ti es bain":
                            L4 = st.text_area("What is 'Good morning and good afternoon' in romansh")
                            if L4 == "Bun di e buna saira":
                                L4 = st.text_area("What is 'Please, I am well' in Romansh")
                                if L4 == "Per plaschair, jau sun bain":
                                    st.balloons()
                                    placeholder = st.empty()
                                    placeholder.progress(100, "**Done!**")

if page == "Lesson 5":
    st.caption("Still making this one ...")
    
