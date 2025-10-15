import streamlit as st

st.set_page_config(
    page_title='포켓몬 도감'
)

pages = {
    "네비게이션1": [
        # st.Page("01_write.py", title="01_write"),
        # st.Page("02_table_metric.py", title="02_table_metric"),
        # st.Page("03_input_widget.py", title="03_input_widget"),
        # st.Page("04_layout_cache.py", title="04_layout_cache"),
    ],
    "네비게이션2": [
        st.Page("pages/03_기본위젯.py", title="03_기본위젯 사용법"),
        st.Page("pages/04_columns.py", title="04_columns"),
        # st.Page("pages/page4.py", title="page4"),
     ],
}

pg = st.navigation(pages)
pg.run()