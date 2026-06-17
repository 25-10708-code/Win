import streamlit as st
import pandas as pd
import random

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="나만의 밴드 노래 추천소",
    page_icon="🎸",
    layout="centered"
)

# 2. 밴드 노래 데이터베이스 (줄바꿈/복사 오류 방지를 위해 주소를 안전하게 쪼갰습니다)
@st.cache_data
def load_data():
    data = [
        # 오아시스 (Oasis)
        {"band": "오아시스 (Oasis)", "song": "Don't Look Back In Anger", "mood": "희망찬/떼창", 
         "link": "https://www.youtube.com/" "watch?v=cmpRLQZkTb8"},
        {"band": "오아시스 (Oasis)", "song": "Champagne Supernova", "mood": "몽환적인", 
         "link": "https://www.youtube.com/" "watch?v=tI-5uv4wryI"},
        {"band": "오아시스 (Oasis)", "song": "Wonderwall", "mood": "아련한/감성적", 
         "link": "https://www.youtube.com/" "watch?v=bx1Bh8Yba1M"},
        
        # 콜드플레이 (Coldplay)
        {"band": "콜드플레이 (Coldplay)", "song": "Viva La Vida", "mood": "웅장한", 
         "link": "https://www.youtube.com/" "watch?v=dvgZkm1xWPE"},
        {"band": "콜드플레이 (Coldplay)", "song": "Fix You", "mood": "위로/감동", 
         "link": "https://www.youtube.com/" "watch?v=k4V3Mo61fJM"},
        {"band": "콜드플레이 (Coldplay)", "song": "Yellow", "mood": "아련한/감성적", 
         "link": "https://www.youtube.com/" "watch?v=yKNxeF4KMsY"},
        
        # 데이식스 (DAY6)
        {"band": "데이식스 (DAY6)", "song": "한 페이지가 될 수 있게", "mood": "청량한/신나는", 
         "link": "https://www.youtube.com/" "watch?v=vnS_gJg9560"},
        {"band": "데이식스 (DAY6)", "song": "예뻤어", "mood": "아련한/감성적", 
         "link": "https://www.youtube.com/" "watch?v=BS7tz2rAOMS"},
        {"band": "데이식스 (DAY6)", "song": "Welcome to the Show", "mood": "희망찬/떼창", 
         "link": "https://www.youtube.com/" "watch?v=stI2bZof_y0"},
        
        # 루시 (LUCY)
        {"band": "루시 (LUCY)", "song": "개화 (Flowering)", "mood": "청량한/신나는", 
         "link": "https://www.youtube.com/" "watch?v=QqZ9bH_yI8g"},
        {"band": "루시 (LUCY)", "song": "아지랑이", "mood": "위로/감동", 
         "link": "https://www.youtube.com/" "watch?v=TAsY_VwIenU"},
        
        # 실리카겔 (Silica Gel)
        {"band": "실리카겔 (Silica Gel)", "song": "No Pain", "mood": "사이케델릭/강렬한", 
         "link": "https://www.youtube.com/" "watch?v=eE77mR_Gg_Y"},
        {"band": "실리카겔 (Silica Gel)", "song": "Tik Tak Tok (feat. So!YoON!)", "mood": "사이케델릭/강렬한", 
         "link": "https://www.youtube.com/" "watch?v=YwL069GIn9E"},
        
        # 잔나비
        {"band": "잔나비", "song": "주저하는 연인들을 위해", "mood": "레트로/감성적", 
         "link": "https://www.youtube.com/" "watch?v=GwlshZ_6w-k"},
        {"band": "잔나비", "song": "투게더!", "mood": "청량한/신나는", 
         "link": "https://www.youtube.com/" "watch?v=8V_fB9T6oio"},
        
        # 퀸 (Queen) - [오류 수정 완료!]
        {"band": "퀸 (Queen)", "song": "Bohemian Rhapsody", "mood": "웅장한", 
         "link": "https://www.youtube.com/" "watch?v=fJ9rUzIMcZQ"},
        {"band": "퀸 (Queen)", "song": "Don't Stop Me Now", "mood": "청량한/신나는", 
         "link": "https://www.youtube.com/" "watch?v=HgzGwKwLmgM"},
        
        # 라디오헤드 (Radiohead)
        {"band": "라디오헤드 (Radiohead)", "song": "Creep", "mood": "아련한/감성적", 
         "link": "https://www.youtube.com/" "watch?v=XFkzRNyygfk"},
        {"band": "라디오헤드 (Radiohead)", "song": "No Surprises", "mood": "몽환적인", 
         "link": "https://www.youtube.com/" "watch?v=u5CVsCnxyXg"},
        
        # 요아소비 (YOASOBI)
        {"band": "요아소비 (YOASOBI)", "song": "Idol (アイドル)", "mood": "청량한/신나는", 
         "link": "https://www.youtube.com/" "watch?v=ZRtdQ81jCUs"},
        {"band": "요아소비 (YOASOBI)", "song": "Monster (怪物)", "mood": "사이케델릭/강렬한", 
         "link": "https://www.youtube.com/" "watch?v=C7nG4uHdf_M"}
    ]
    return pd.DataFrame(data)

df = load_data()

# 3. 웹 페이지 헤더
st.title("🎸 My Favorite Band Song Recommender")
st.markdown("내가 좋아하는 밴드들의 명곡을 추천해주는 공간입니다. 취향껏 골라보세요!")
st.write("---")

# 4. 사이드바 검색 필터 UI
st.sidebar.header("🎵 취향 필터")

all_bands = ["전체"] + sorted(list(df["band"].unique()))
selected_band = st.sidebar.selectbox("좋아하는 밴드", all_bands)

all_moods = ["전체"] + sorted(list(df["mood"].unique()))
selected_mood = st.sidebar.selectbox("지금 당기는 분위기", all_moods)


# 5. 데이터 필터링 로직
filtered_df = df.copy()

if selected_band != "전체":
    filtered_df = filtered_df[filtered_df["band"] == selected_band]
if selected_mood != "전체":
    filtered_df = filtered_df[filtered_df["mood"] == selected_mood]


# 6. 추천 결과 화면 표시
st.subheader("🎧 추천 음악 리스트")

if not filtered_df.empty:
    
    # 6-1. 랜덤 추천 버튼 기능
    if st.button("🎲 이 조건에서 한 곡만 랜덤 추천받기"):
        random_pick = filtered_df.sample(n=1).iloc[0]
        st.balloons()
        
        st.success("🎉 오늘의 랜덤 추천 곡을 찾았습니다!")
        
        # 랜덤 추천 결과 카드
        with st.container(border=True):
            st.markdown(f"### 🎵 {random_pick['song']}")
            st.markdown(f"**아티스트:** {random_pick['band']}")
            st.markdown(f"**태그:** #{random_pick['mood']}")
            st.write("")
            st.link_button("📺 유튜브에서 음악 감상하기", random_pick['link'], type="primary", use_container_width=True)
    
    st.write("") 
    st.markdown("#### 📋 조건에 맞는 모든 곡")
    
    # 6-2. 필터링된 모든 곡 목록 보여주기 (카드 형태)
    for index, row in filtered_df.iterrows():
        with st.container(border=True):
            col1, col2 = st.columns([3, 1.2])
            with col1:
                st.markdown(f"##### {row['song']}")
                st.caption(f"{row['band']} | 분위기: {row['mood']}")
            with col2:
                st.write("") # 세로 여백 맞추기
                st.link_button("▶️ 유튜브 링크", row['link'], use_container_width=True)
else:
    st.warning("선택하신 조건에 맞는 노래가 없습니다. 다른 필터를 선택해 보세요! 😭")

# 7. 하단 정보
st.caption("Made with ❤️ using Streamlit & GitHub")
