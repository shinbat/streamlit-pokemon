import streamlit as st

st.set_page_config(
    page_title='포켓몬 도감'
)
st.markdown("""
<style>
img {
    max-height: 300px;    
}
.stExpanderDetails div {
    display: flex;
    justify-content: center;            
}
# [data-testid='stIconMaterial'] {
#     visibility: hidden;            
#             }
# .st-emotion-cache-19iic4h {
#     pointer-events: none;            
#             }    
# [data-testid="stElementToolbarButtonContainer"]  {
#     visibility: hidden;            
#             }                                 
</style> 
""", unsafe_allow_html=True)

st.title('Streamlit 포켓몬 도감')
st.markdown('**포켓몬**을 하나씩 추가해서 도감을 채워보세요')

pages = {
    # '네비게이션1': [
    #     st.Page('pages/page2.py', title='page2'), 
    #     st.Page('pages/page4.py', title='page4'), 
    # ],
    'Streamlit 로 구현한 포켓몬':  [
        st.Page('pages/03_wedget.py', title='03_wedget'),
        st.Page('pages/04_columns.py', title='04_columns'),
        st.Page('pages/05_form.py', title='05_form'),
        st.Page('pages/06_session_state.py', title='06_session_state'),
        st.Page('pages/07_toggle.py', title='07_toggle로 자동폼'),
        st.Page('pages/08_delete.py', title='08_delete'),
        st.Page('pages/09_css.py', title='09_css'),
     ],
}

pg = st.navigation(pages)
pg.run()

st.divider() 
col1, col2, col3 = st.columns(3)
col1.link_button('youtube', 'https://youtu.be/F8a-0JFHfOo?si=kHzusCwLH1K-iWMU')
col2.link_button('github', 'https://github.com/shinbat/streamlit-pokemon.git')
col3.link_button('streamlit', 'https://docs.streamlit.io/')
####################################
# python, streamlit 설치 (pip hello)
# streamlit run app.py 로 실행한다
####################################