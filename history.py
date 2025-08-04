import streamlit as st

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "What is the Romansh language?",
        "2",
        "3",
        "4"
    ]
)
with tab1:
    st.markdown("""
    Romansh is a romance language spoken in grisons, in Switzerland
    
    It's creation story is pretty much the same as all other romance languages: There are some celtic tribes, then the romans came and introduced Latin. After the roman empire falls, the germanic tribes come and the languages mix together to form new languages
    Unlike other romance languages, the Rhaeto-romance languages (of which Romansh is one) are distinct from other languages because of isolation due to geographical features and exposure to other languages.""")
with tab2:
    st.write(2)
with tab3:
    st.write(3)
with tab4:
    st.write(4)
