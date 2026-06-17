import streamlit as st
import pandas as pd
import random

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="나만의 밴드 노래 추천소",
    page_icon="🎸",
    layout="centered"
)

# 2. 밴드 노래 데이터베이스 (줄바꿈 오류가 나지 않도록 주소를 확실히 닫았습니다)
@st.cache_data
def load_data():
    data = [
        # 오아시스 (Oasis)
        {"band": "오아시스 (Oasis)", "song": "Don't Look Back In Anger", "mood": "희망찬/떼창", "link": "https://www.youtube.com/watch?v=cmpRLQZkTb8"},
        {"band": "오아시스 (Oasis)", "song": "Champagne Supernova", "mood": "몽환적인", "link": "https://www.youtube.com/watch?v=tI-5uv4wryI"},
        {"band": "오아시스 (Oasis)", "song": "Wonderwall", "mood": "아련한/감성적", "link": "https://www.youtube.com/watch?v=bx1Bh8Yba1M"},
        
        # 콜드플레이 (Coldplay)
        {"band": "콜드플레이 (Coldplay)", "song": "Viva La Vida", "mood": "웅장한", "link": "https://www.youtube.com/watch?v=dvgZkm1xWPE"},
        {"band": "콜드플레이 (Coldplay)", "song": "Fix You", "mood": "위로/감동", "link": "https://www.youtube.com/watch?v=k4V3Mo61fJM"},
        {"band": "콜드플레이 (Coldplay)", "song": "Yellow", "mood": "아련한/감성적", "link": "https://www.youtube.com/watch?v=yKNxeF4KMsY"},
        
        # 데이식스 (DAY6)
        {"band": "데이식스 (DAY6)", "song": "한 페이지가 될 수 있게", "mood": "청량한/신나는", "link": "https://www.youtube.com/watch?v=vnS_gJg9560"},
        {"band": "데이식스 (DAY6)", "song": "예뻤어", "mood": "아련한/감성적", "link": "https://www.youtube.com/watch?v=BS7tz2rAOMS"},
        {"band": "데이식스 (DAY6)", "song": "Welcome to the Show", "mood": "희망찬/떼창", "link": "https://www.youtube.com/watch?v=stI2bZof_y0"},
        
        # 루시 (LUCY)
        {"band": "루시 (LUCY)", "song": "개화 (Flowering)", "mood": "청량한/신나는", "link": "https://www.youtube.com/watch?v=QqZ9bH_yI8g"},
        {"band": "루시 (LUCY)", "song": "아지랑이", "mood": "위로/감동", "link": "https://www.youtube.com/watch?v=TAsY_VwIenU"},
        
        # 실리카겔 (Silica Gel) - [오류 수정 완료!]
        {"band": "실리카겔 (Silica Gel)", "song": "No Pain", "mood": "사이케델릭/강렬한", "link": "https://www.youtube.com/watch?v=eE77mR_Gg_Y"},
        {"band": "실리카겔 (Silica Gel)", "song": "Tik Tak Tok (feat. So!YoON!)", "mood": "사이케델릭/강렬한", "link": "https://www.youtube.com/watch?v=YwL069GIn9E"},
        
        # 잔나비
        {"band": "잔나비", "song": "주저하는 연인들을 위해", "mood": "레트로/감성적", "link": "https://www.youtube.com/watch?v=GwlshZ_6w-k"},
        {"band": "잔나비", "song": "투게더!", "mood": "청량한/신나는", "link": "https://www.youtube.com/watch?v=8V_fB9T6oio"},
        
        # 퀸 (Queen)
        {"band": "퀸 (Queen)", "song": "Bohemian Rhapsody", "mood": "웅장한", "link": "https://www.youtube.com/watch?v=fJ9rUzIMcZQ"},
        {"band": "퀸 (Queen)", "song": "Don't Stop Me Now", "mood": "청량한/신나는", "link": "
