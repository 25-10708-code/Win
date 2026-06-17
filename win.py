import streamlit as st
import pandas as pd
import random

# 1. 페이지 기본 설정 (웹 브라우저 탭에 표시될 정보)
st.set_page_config(
    page_title="나만의 밴드 노래 추천소",
    page_icon="🎸",
    layout="centered"
)

# 2. 추천할 밴드 및 노래 데이터베이스 (자유롭게 추가/수정 가능!)
@st.cache_data
def load_data():
    data = [
        {"band": "오아시스 (Oasis)", "song": "Don't Look Back In Anger", "mood": "희망찬/떼창", "tempo": "미디엄템포", "link": "https://www.youtube.com/watch?v=cmpRLQZkTb8"},
        {"band": "오아시스 (Oasis)", "song": "Champagne Supernova", "mood": "몽환적인", "tempo": "느림", "link": "https://www.youtube.com/watch?v=tI-5uv4wryI"},
        {"band": "콜드플레이 (Coldplay)", "song": "Viva La Vida", "mood": "웅장한", "tempo": "빠름", "link": "https://www.youtube.com/watch?v=dvgZkm1xWPE"},
        {"band": "콜드플레이 (Coldplay)", "song": "Fix You", "mood": "위로/감동", "tempo": "느림", "link": "https://www.youtube.com/watch?v=k4V3Mo61fJM"},
        {"band": "데이식스 (DAY6)", "song": "한 페이지가 될 수 있게", "mood": "청량한/신나는", "tempo": "빠름", "link": "https://www.youtube.com/watch?v=vnS_gJg9560"},
        {"band": "데이식스 (DAY6)", "song": "예뻤어", "mood": "아련한/감성적", "tempo": "미디엄템포", "link": "https://www.youtube.com/watch?v=BS7tz2rAOMS"},
        {"band": "실리카겔 (Silica Gel)", "song": "No Pain", "mood": "사이케델릭/강렬한", "tempo": "빠름", "link": "https://www.youtube.com/watch?v=eE77mR_Gg_Y"},
        {"band": "잔나비", "song": "주저하는 연인들을 위해", "mood": "레트로/감성적", "tempo": "느림", "link": "https://www.youtube.com/watch?v=GwlshZ_6w-k"},
    ]
    return pd.DataFrame(data)

df = load_data()

# 3. 웹 페이지 헤더 및 타이틀
st.title("🎸 My Favorite Band Song Recommender")
st.markdown("내가 좋아하는 밴드들의 명곡을 추천해주는 공간입니다. 취향껏 골라보세요!")
st.write("---")

# 4. 사이드바 검색 필터 UI
st.sidebar.header("🎵 취향 필터")

# 밴드 선택 (기본값: 전체)
all_bands = ["전체"] + list(df["band"].unique())
selected_band = st.sidebar.selectbox("좋아하는 밴드", all_bands)

# 분위기 선택 (기본값: 전체)
all_moods = ["전체"] + list(df["mood"].unique())
selected_mood = st.sidebar.selectbox("지금 당기는 분위기", all_moods)

# 템포 선택 (기본값: 전체)
all_tempos = ["전체"] + list(df["tempo"].unique())
selected_tempo = st.sidebar.selectbox("선호하는 템포", all_tempos)


# 5. 사용자가 선택한 필터에 따라 데이터 필터링
filtered_df = df.copy()

if selected_band != "전체":
    filtered_df = filtered_df[filtered_df["band"] == selected_band]

if selected_mood != "전체":
    filtered_df = filtered_df[filtered_df["mood"] == selected_mood]

if selected_tempo != "전체":
    filtered_df = filtered_df[filtered_df["tempo"] == selected_tempo]


# 6. 추천 결과 화면 표시
st.subheader("🎧 추천 음악 리스트")

if not filtered_df.empty:
    # 6-1. 랜덤 추천 버튼 기능
    if st.button("🎲 이 조건에서 한 곡만 랜덤 추천받기"):
        random_pick = filtered_df.sample(n=1).iloc[0]
        st.balloons() # 화면에 풍선 애니메이션 효과
        st.success(f"오늘의 추천: **{random_pick['band']}** - **{random_pick['song']}**")
        st.video(random_pick['link']) # 유튜브 플레이어 띄우기
    
    st.write("") # 레이아웃 공백용
    
    # 6-2. 필터링된 모든 곡 목록 보여주기
    for index, row in filtered_df.iterrows():
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"### {row['song']}")
                st.caption(f"아티스트: {row['band']} | 분위기: {row['mood']} | 템포: {row['tempo']}")
            with col2:
                st.write("") # 세로 위치 맞추기용 공백
                st.markdown(f"[▶️ 유튜브로 열기]({row['link']})")
            st.write("---")
else:
    # 조건에 맞는 곡이 없는 경우 예외 처리
    st.warning("선택하신 조건에 맞는 노래가 없습니다. 다른 필터를 선택해 보세요! 😭")

# 7. 하단 카피라이트 정보
st.caption("Made with ❤️ using Streamlit & GitHub")
