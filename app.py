import streamlit as st

st.set_page_config(
    page_title='포켓몬 도감'
)

type_emoji_dict = {
    '노말': '⚪',
    '격투': '👊',
    '비행': '🦅',
    '독': '💀',
    '땅': '⛰️',
    '바위': '🪨',
    '벌레': '🐛',
    '고스트': '👻',
    '강철': '🛡️',
    '불꽃': '🔥',
    '물': '💧',
    '풀': '🌿',
    '전기': '⚡',
    '에스퍼': '🧠',
    '얼음': '❄️',
    '드래곤': '🐉',
    '악': '⚫',
    '페어리': '✨'
}

pokemon = {
    'name': '누오',
    'types': ['물', '땅'],
    'image_url': 'https://i.namu.wiki/i/cDs6f1XZ8NqV0ieTNWrvDYxlOAqbAyM6cFwwMzdfckacs80Q7e0OrX7UYqlGOe8a-okHmHyFSRDJxJXcUgEjHTeTOAIfwazRyVdFYse5SgMl1Lrz66i2Ykkk4VFFbvvhTr-3tjzZg5TfxyML4iRCzQ.webp'
}

st.subheader(pokemon['name'])
st.image(pokemon['image_url'], caption='누오')
emoji_types = [f'{type_emoji_dict[x]} {x}' for x in pokemon['types']]
st.subheader(' / '.join(emoji_types))

pages = {
    "네비게이션1": [
        # st.Page("01_write.py", title="01_write"),
        # st.Page("02_table_metric.py", title="02_table_metric"),
        # st.Page("03_input_widget.py", title="03_input_widget"),
        # st.Page("04_layout_cache.py", title="04_layout_cache"),
    ],
    "네비게이션2": [
        st.Page("pages/page1.py", title="page1"),
        st.Page("pages/page2.py", title="page2"),
        # st.Page("pages/page4.py", title="page4"),
     ],
}

pg = st.navigation(pages)
pg.run()