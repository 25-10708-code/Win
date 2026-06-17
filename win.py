import streamlit as st
import pandas as pd
import random
import urllib.parse

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="국내 밴드 노래 추천소",
    page_icon="🎸",
    layout="centered"
)

# 2. 한국 밴드 대형 데이터베이스 (★캔트비블루 "진짜 공식 곡" 반영 완료!)
@st.cache_data
def load_data():
    data = [
        # 데이식스 (DAY6)
        {"band": "데이식스 (DAY6)", "song": "한 페이지가 될 수 있게", "mood": "청량한/신나는"},
        {"band": "데이식스 (DAY6)", "song": "예뻤어", "mood": "아련한/감성적"},
        {"band": "데이식스 (DAY6)", "song": "Welcome to the Show", "mood": "희망찬/떼창"},
        {"band": "데이식스 (DAY6)", "song": "Happy", "mood": "위로/감동"},
        {"band": "데이식스 (DAY6)", "song": "녹아내려요", "mood": "청량한/신나는"},
        
        # 루시 (LUCY)
        {"band": "루시 (LUCY)", "song": "개화 (Flowering)", "mood": "청량한/신나는"},
        {"band": "루시 (LUCY)", "song": "아지랑이", "mood": "위로/감동"},
        {"band": "루시 (LUCY)", "song": "아니 근데 진짜", "mood": "청량한/신나는"},
        {"band": "루시 (LUCY)", "song": "조깅", "mood": "청량한/신나는"},
        
        # 실리카겔 (Silica Gel)
        {"band": "실리카겔 (Silica Gel)", "song": "No Pain", "mood": "사이케델릭/강렬한"},
        {"band": "실리카겔 (Silica Gel)", "song": "Tik Tak Tok (feat. So!YoON!)", "mood": "사이케델릭/강렬한"},
        {"band": "실리카겔 (Silica Gel)", "song": "APEX", "mood": "사이케델릭/강렬한"},
        
        # 캔트비블루 (Can't be blue) - [진짜 공식 발매곡으로 최종 정정!]
        {"band": "캔트비블루 (Can't be blue)", "song": "사랑이라 했던 말 속에서", "mood": "아련한/감성적"},
        {"band": "캔트비블루 (Can't be blue)", "song": "can't love (feat. HAN of Stray Kids)", "mood": "청량한/신나는"},
        
        # 잔나비
        {"band": "잔나비", "song": "주저하는 연인들을 위해", "mood": "레트로/감성적"},
        {"band": "잔나비", "song": "투게더!", "mood": "청량한/신나는"},
        {"band": "잔나비", "song": "뜨거운 여름밤은 가고 남은 것은 볼품없지만", "mood": "아련한/감성적"},
        
        # 넬 (NELL)
        {"band": "넬 (NELL)", "song": "기억을 걷는 시간", "mood": "아련한/감성적"},
        {"band": "넬 (NELL)", "song": "Stay", "mood": "몽환적인"},
        {"band": "넬 (NELL)", "song": "지구가 태양을 네 번 감싸는 동안", "mood": "웅장한"},

        # 쏜애플 (Thornapple)
        {"band": "쏜애플 (Thornapple)", "song": "시퍼런 봄", "mood": "사이케델릭/강렬한"},
        {"band": "쏜애플 (Thornapple)", "song": "남극", "mood": "몽환적인"},
        
        # 검정치마 (The Black Skirts)
        {"band": "검정치마", "song": "EVERYTHING", "mood": "아련한/감성적"},
        {"band": "검정치마", "song": "안티프리즈 (Antifreeze)", "mood": "레트로/감성적"},
        
        # 터치드 (TOUCHED)
        {"band": "터치드 (TOUCHED)", "song": "Highlight", "mood": "사이케델릭/강렬한"},
        {"band": "터치드 (TOUCHED)", "song": "야라바 (Alive)", "mood": "희망찬/떼창"},

        # QWER
        {"band": "QWER", "song": "고민중독", "mood": "청량한/신나는"},
        {"band": "QWER", "song": "내 이름 맑음", "mood": "위로/감동"},
        {"band": "QWER", "song": "가짜 아이돌", "mood": "청량한/신나는"},
        
        # 페퍼톤스 (Peppertones)
        {"band": "페퍼톤스", "song": "행운을 빌어요", "mood": "희망찬/떼창"},
        {"band": "페퍼톤스", "song": "공원여행", "mood": "청량한/신나는"},
        
        # 소란 (SORAN)
        {"band": "소란 (SORAN)", "song": "가을목이", "mood": "희망찬/떼창"},
        {"band": "소란 (SORAN)", "song": "리코타 치즈 샐러드", "mood": "레트로/감성적"}
    ]
    
    # 안전한 유튜브 검색 URL 자동 생성 로직
    for item in data:
        search_keyword = f"{item['band']} {item['song']}"
        encoded_keyword = urllib.parse.quote(search_keyword)
        item["link"] = f"https://www.youtube.com/results?search_query={encoded_keyword}"
        
    return pd.DataFrame(data)

df = load_data()

# 3. 웹 페이지 헤더
st.title("🎸 국대 밴드 명곡 추천소 v2.3")
st.markdown("내가 좋아하는 대한민국 대표 밴드들의 명곡을 추천하는 공간입니다. 취향껏 골라보세요!")
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
        
        st.success("🎉 오늘의 랜덤 추천 국내 곡을 찾았습니다!")
        
        # 랜덤 추천 결과 카드
        with st.container(border=True):
            st.markdown(f"### 🎵 {random_pick['song']}")
            st.markdown(f"**아티스트:** {random_pick['band']}")
            st.markdown(f"**태그:** #{random_pick['mood']}")
            st.write("")
            st.link_button("📺 유튜브에서 검색 결과 보기", random_pick['link'], type="primary", use_container_width=True)
    
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
                st.link_button("🔍 유튜브 검색", row['link'], use_container_width=True)
else:
    st.warning("선택하신 조건에 맞는 노래가 없습니다. 다른 필터를 선택해 보세요! 😭")

# 7. 하단 정보
st.caption("Made with ❤️ using Streamlit & GitHub")
