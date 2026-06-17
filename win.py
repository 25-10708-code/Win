import streamlit as st

# 1. 페이지 설정 (웹브라우저 탭에 표시될 내용)
st.set_page_config(
    page_title="나의 최애 노래 추천소",
    page_icon="🎵",
    layout="wide"
)

# 2. 스타일링 (스트림릿 내부에 CSS 주입)
st.markdown("""
    <style>
    .main-title {
        color: #ff4757;
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .sub-title {
        text-align: center;
        color: #666666;
        margin-bottom: 30px;
    }
    div[data-testid="stMetric"] {
        background-color: #ffffff;
        border: 1px solid #e6e6e6;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# 3. 헤더 표시
st.markdown('<p class="main-title">🎵 My Playlist</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">오늘의 기분에 맞는 노래를 들어보세요!</p>', unsafe_allow_html=True)

# 4. 노래 데이터 세팅 (원하는 노래를 자유롭게 추가해보세요!)
songs = [
    {"title": "Dynamite", "artist": "BTS", "mood": "💃 신나는", "emoji": "✨", "url": "https://www.youtube.com/results?search_query=BTS+Dynamite"},
    {"title": "밤편지", "artist": "아이유 (IU)", "mood": "☕ 잔잔한", "emoji": "💌", "url": "https://www.youtube.com/results?search_query=아이유+밤편지"},
    {"title": "수고했어 오늘도", "artist": "옥상달빛", "mood": "🌙 위로되는", "emoji": "🌳", "url": "https://www.youtube.com/results?search_query=옥상달빛+수고했어+오늘도"},
    {"title": "Hype Boy", "artist": "NewJeans", "mood": "💃 신나는", "emoji": "👖", "url": "https://www.youtube.com/results?search_query=NewJeans+Hype+Boy"},
    {"title": "모든 날, 모든 순간", "artist": "폴킴", "mood": "☕ 잔잔한", "emoji": "🌅", "url": "https://www.youtube.com/results?search_query=폴킴+모든날모든순간"}
]

# 5. 사이드바 또는 상단에 필터(선택창) 만들기
mood_options = ["전체보기", "💃 신나는", "☕ 잔잔한", "🌙 위로되는"]
selected_mood = st.selectbox("👉 지금 기분이 어떠신가요?", mood_options)

# 6. 필터링된 노래 분류
if selected_mood == "전체보기":
    filtered_songs = songs
else:
    filtered_songs = [song for song in songs if song["mood"] == selected_mood]

st.write("---")

# 7. 노래 목록을 Grid(카드 형태)로 배치하기
# 한 줄에 3개씩 보여주기 위해 컬럼 생성
cols = st.columns(3)

for idx, song in enumerate(filtered_songs):
    # 컬럼 번갈아가며 배치 (0, 1,
