import streamlit as st

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

with st.expander(label=pokemon['name'], expanded=True):
    st.image(pokemon['image_url'], caption='누오')
    emoji_types = [f'{type_emoji_dict[x]} {x}' for x in pokemon['types']]
    st.subheader(' / '.join(emoji_types))