import streamlit as st
print('page reloaded')
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

initial_pokemons = [
  {
    'name': '피카츄',
    'types': ['전기'],
    'image_url': 'https://i.namu.wiki/i/SVMK4eZf-H5dqybpTkReUG_iVr3Q4HXCPAd0lNPldimJlp41N_pCilPiR6QPghJgck28w_GgXdMAMrmnxo8-sUpYXAo1UDzu-daukUlLu22_BK9_sPRAmpgDWKE8QtCpMYFqyPpx1SWRtZlEk11Nfw.webp'
  },
  {
    'name': '누오',
    'types': ['물','땅' ],
    'image_url': 'https://i.namu.wiki/i/cDs6f1XZ8NqV0ieTNWrvDYxlOAqbAyM6cFwwMzdfckacs80Q7e0OrX7UYqlGOe8a-okHmHyFSRDJxJXcUgEjHTeTOAIfwazRyVdFYse5SgMl1Lrz66i2Ykkk4VFFbvvhTr-3tjzZg5TfxyML4iRCzQ.webp'
  },
  {
    'name': '파이리',
    'types': ['불꽃'],
    'image_url': 'https://i.namu.wiki/i/MO6--wWn36H6VEwEIhb9fi3onYkJHQLl_0QoeKGGZTE1hGS-jBUR7MbHW4GkJTF5X0ewOZk2Fs-hVvwtFZOewf2u-vSkCh0PAY_ZCS89M-50_LMAFMc_TEZ422_uzgg26zhx3b1lF0STxO8WUGlaHA.webp'
  },
  {
    'name': '갸라도스',
    'types': ['물', '비행'],
    'image_url': 'https://i.namu.wiki/i/h9WMq1hyKoT5aR1WBmDCQSyGMKk-0UWSFw8GwDXYJyf1SGP7j6eA9txN_qZyzau6rOU4cW49X7Uv13wa6etYydkgvYJfH14KfW8UBgnB6DZUvgxJJzmVQ40RXVf63Lz7oLfSpSinJZkVWPo-K-OWXQ.webp'
  },
  {
    'name': '개굴닌자',
    'types': ['물', '악'],
    'image_url': 'https://i.namu.wiki/i/0fbwxHiaLj3tbVZGUA-YJ8W9pPprpPY0JzAQzCUOkNYx0MBinb-LPQV1PCffVSWth6jNqoIxv5Mw8UB3EyFWpIHAZ0QBCMRZa751QJnofIqVB6oro3aCFOkT_zzFQC46vW3JZTYjI9yikef4isEYQA.webp'
  },
  {
    'name': '루카리오',
    'types': ['격투', '강철'],
    'image_url': 'https://i.namu.wiki/i/_-_1FO_ztYci7Ji1iWJlmmJ15OufdWfEs91pm_fdSMnTUTOIIYFtAaTyKoxv0bXVmLwEXwM2uS_em0EvoPT7ZtLN5QmZvr6VzeS3vGPzDZzEqnimVFM7l671VVysfBsC4YE-P-cwU_xoyVcbnsbCiQ.webp'
  },
  {
    'name': '꼬부기',
    'types': ['물'],
    'image_url': 'https://i.namu.wiki/i/B3KmIwp1KR6W2t_qpxg1KmzN4UBc6KVlwRF3KwuPCfcac5sSWaaRvzx2x-I1b3wa2Kt8jw2Oz2CgGzvR1JcDNPbZ3Y1MZWFW3jIL53DCnvDFlHYZAMEhvHXEVxt3PJVaxmHi4C7BskWJfnXwoB8gBQ.webp'
  },
]

example_pokemon = {
    'name': '알로라 디그다',
    'types': ['땅', '강철'],
    'image_url': 'https://i.namu.wiki/i/ALZtkHTxXSqaowmX8e4ugKm8w8iJ01K0T8fluMwOQW4E2E4lVe_gk60rkE1-XHtmvE0xQ19iorcHQUd1pxR2wFPKFw5JK3ZpsS3zaBPLhNU2kfLK8CQjhrfsooliUv1RgW236pGJBGKqh9iAi8oyhS48xuAd5te7viokTn1umo0.webp'
}

if 'pokemons' not in st.session_state:
   st.session_state.pokemons = initial_pokemons

auto_complete = st.toggle('예시 데이터로 채우기')

with st.form(key='form'):
    col1, col2 = st.columns(2)
    with col1:
      name = st.text_input(
         label='포켓몬 이름',
         value=example_pokemon['name'] if auto_complete else '')
    with col2:
      types = st.multiselect(
          label='포켓몬 속성', 
          options=list(type_emoji_dict.keys()),
          max_selections=2,
          default=example_pokemon['types'] if auto_complete else []
      )
    image_url = st.text_input(
       label='포켓몬 이미지 url',
       value=example_pokemon['image_url'] if auto_complete else '')
    submit = st.form_submit_button(label='Submit')
    if submit:
      if not name:
        st.error('이름을 입력하세요')
      elif not len(types):
        st.error('포켓몬의 속성을 적어도 한개 선택하세요')
      else:
         st.success('포켓몬을 추가할 수 있습니다')
         st.session_state.pokemons.append({
            'name': name,
            'types': types,
            'image_url': image_url if image_url else './images/default.jpg'           
         })

for i in range(0, len(st.session_state.pokemons), 3):
    row_pokemons = st.session_state.pokemons[i:i+3]
    cols = st.columns(3)
    for j in range(len(row_pokemons)):
        with cols[j]:
            pokemon = row_pokemons[j]
            with st.expander(label=f'**{i+j+1}. {pokemon['name']}**', expanded=True):
                st.image(pokemon['image_url'], caption=pokemon['name'])
                emoji_types = [f'{type_emoji_dict[x]} {x}' for x in pokemon['types']]
                st.text(' / '.join(emoji_types))
                delete_button = st.button(label='삭제', key=i+j, use_container_width=True)
                if delete_button:
                   print('delete button clicked')
                   del st.session_state.pokemons[i+j]
                   st.rerun()
                   
