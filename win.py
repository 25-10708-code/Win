import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="나의 최애 노래 추천소",
    page_icon="🎵",
    layout="wide"
)

# 2. 스타일링 (디자인 보완)
st.markdown("""
    <style>
    .main-title {
        color: #ff4757;
        text-align: center;
        font-size: 2.7rem;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .sub-title {
        text-align: center;
        color: #666666;
        font-size: 1.1rem;
        margin-bottom: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 헤더 표시
st.markdown('<p class="main-title">🎵 My Playlist</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">오늘의 기분에 맞는 노래를 선택해 보세요!</p>', unsafe_allow_html=True)

# 4. 넉넉하게 추가된 15개의 노래 데이터 리스트
songs = [
    # --- 💃 신나는 노래 ---
    {"title": "Dynamite", "artist": "BTS", "mood": "💃 신나는", "emoji": "✨", "url": "https://www.youtube.com/results?search_query=BTS+Dynamite"},
    {"title": "Hype Boy", "artist": "NewJeans", "mood": "💃 신나는", "emoji": "👖", "url": "https://www.youtube.com/results?search_query=NewJeans+Hype+Boy"},
    {"title": "Super Shy", "artist": "NewJeans", "mood": "💃 신나는", "emoji": "🐰", "url": "https://www.youtube.com/results?search_query=NewJeans+Super+Shy"},
    {"title": "LOVE DIVE", "artist": "IVE (아이브)", "mood": "💃 신나는", "emoji": "💘", "url": "https://www.youtube.com/results?search_query=IVE+LOVE+DIVE"},
    {"title": "Next Level", "artist": "aespa", "mood": "💃 신나는", "emoji": "🚀", "url": "https://www.youtube.com/results?search_query=aespa+Next+Level"},
    
    # --- ☕ 잔잔한 노래 ---
    {"title": "밤편지", "artist": "아이유 (IU)", "mood": "☕ 잔잔한", "emoji": "💌", "url": "https://www.youtube.com/results?search_query=아이유+밤편지"},
    {"title": "모든 날, 모든 순간", "artist": "폴킴", "mood": "☕ 잔잔한", "emoji": "🌅", "url": "https://www.youtube.com/results?search_query=폴킴+모든날모든순간"},
    {"title": "주저하는 연인들을 위해", "artist": "잔나비", "mood": "☕ 잔잔한", "emoji": "🎸", "url": "https://www.youtube.com/results?search_query=잔나비+주저하는+연인들을+위해"},
    {"title": "취기를 빌려", "artist": "산들", "mood": "☕ 잔잔한", "emoji": "🌙", "url": "https://www.youtube.com/results?search_query=산들+취기를+빌려"},
    {"title": "비도 오고 그래서", "artist": "헤이즈 (Heize)", "mood": "☕ 잔잔한", "
