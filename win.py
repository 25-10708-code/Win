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

# 4. 15개의 노래 데이터 리스트 (따옴표 에러 완전 수정 완료)
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
    {"title": "비도 오고 그래서", "artist": "헤이즈 (Heize)", "mood": "☕ 잔잔한", "emoji": "☔", "url": "https://www.youtube.com/results?search_query=헤이즈+비도+오고+그래서"},

    # --- 🌙 위로되는 노래 ---
    {"title": "수고했어 오늘도", "artist": "옥상달빛", "mood": "🌙 위로되는", "emoji": "🌳", "url": "https://www.youtube.com/results?search_query=옥상달빛+수고했어+오늘도"},
    {"title": "숨", "artist": "박효신", "mood": "🌙 위로되는", "emoji": "🌬️", "url": "https://www.youtube.com/results?search_query=박효신+숨"},
    {"title": "서른 즈음에", "artist": "김광석", "mood": "🌙 위로되는", "emoji": "🍂", "url": "https://www.youtube.com/results?search_query=김광석+서른즈음에"},
    {"title": "달리기", "artist": "옥상달빛 (or SES)", "mood": "🌙 위로되는", "emoji": "🏃", "url": "https://www.youtube.com/results?search_query=옥상달빛+달리기"},
    {"title": "나의 옛날이야기", "artist": "아이유 (IU)", "mood": "🌙 위로되는", "emoji": "📻", "url": "https://www.youtube.com/results?search_query=아이유+나의옛날이야기"}
]

# 5. 상단 필터 선택창
mood_options = ["전체보기", "💃 신나는", "☕ 잔잔한", "🌙 위로되는"]
selected_mood = st.selectbox("👉 지금 기분이 어떠신가요? 필터를 선택해보세요!", mood_options)

# 6. 필터링 로직
if selected_mood == "전체보기":
    filtered_songs = songs
else:
    filtered_songs = [song for song in songs if song["mood"] == selected_mood]

st.write(f"총 **{len(filtered_songs)}**개의 추천 곡이 있습니다.")
st.write("---")

# 7. 노래 목록을 3열(Grid) 카드로 배치
cols = st.columns(3)

for idx, song in enumerate(filtered_songs):
    with cols[idx % 3]:
        with st.container(border=True):
            st.markdown(f"### {song['emoji']} {song['title']}")
            st.caption(f"**아티스트:** {song['artist']}")
            st.markdown(f"`#{song['mood'].split()[-1]}`")
            
            # 들어보기 버튼
            st.link_button("🎧 들어보기", song["url"], use_container_width=True)
