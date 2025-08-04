import streamlit as st

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "What is the Romansh language?",
        "Why is it a national language?",
        "Rumantsch Grischun",
        "4"
    ]
)
with tab1:
    st.markdown("""
    Romansh is a romance language spoken in grisons, in Switzerland
    
    It's creation story is pretty much the same as all other romance languages: There are some celtic tribes, then the romans came and introduced Latin. After the roman empire falls, the germanic tribes come and the languages mix together to form new languages.
    Unlike other romance languages, the Rhaeto-romance languages (of which Romansh is one) are distinct from other languages because of isolation due to geographical features and exposure to other languages.""")
with tab2:
    st.markdown("""Despite less than 1% of Switzerlamd speaking Romansh, it is still a national language. But why?

There are a few things, however the main factor was that in the lead up to the 2nd world war, Hitler was saying that he wanted to get all the German speaking countries back together. The swiss people were (unsurprisingly) not very keen on this idea. To try and diffrentiate themselves from Germany, in 1938, Romansh became a national language."")
with tab3:
    st.write(3)
with tab4:
    st.write(4)
