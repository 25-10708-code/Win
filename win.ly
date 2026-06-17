<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🎵 나의 최애 노래 추천소</title>
    <style>
        :root {
            --bg-color: #f8f9fa;
            --card-bg: #ffffff;
            --text-color: #333333;
            --primary-color: #ff4757;
        }

        body {
            font-family: 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        header {
            text-align: center;
            margin-bottom: 30px;
        }

        h1 {
            color: var(--primary-color);
            font-size: 2.5rem;
            margin-bottom: 10px;
        }

        .filter-buttons {
            margin-bottom: 30px;
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            justify-content: center;
        }

        .btn {
            background-color: white;
            border: 2px solid var(--primary-color);
            color: var(--primary-color);
            padding: 10px 20px;
            border-radius: 20px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
        }

        .btn:hover, .btn.active {
            background-color: var(--primary-color);
            color: white;
        }

        .playlist-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            width: 100%;
            max-width: 1200px;
        }

        .card {
            background: var(--card-bg);
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            padding: 20px;
            text-align: center;
            transition: transform 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        .album-art {
            width: 120px;
            height: 120px;
            background-color: #ddd;
            border-radius: 50%;
            margin: 0 auto 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3rem;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }

        .song-title {
            font-size: 1.2rem;
            font-weight: bold;
            margin: 10px 0 5px;
        }

        .artist {
            color: #666;
            margin-bottom: 15px;
            font-size: 0.95rem;
        }

        .mood-tag {
            display: inline-block;
            background-color: #f1f2f6;
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.8rem;
            color: #57606f;
            margin-bottom: 15px;
        }

        .listen-btn {
            display: inline-block;
            background-color: #ff4757;
            color: white;
            text-decoration: none;
            padding: 8px 15px;
            border-radius: 8px;
            font-size: 0.9rem;
            font-weight: bold;
        }

        .listen-btn:hover {
            background-color: #e84118;
        }
    </style>
</head>
<body>

    <header>
        <h1>🎵 My Playlist</h1>
        <p>오늘의 기분에 맞는 노래를 들어보세요!</p>
    </header>

    <div class="filter-buttons">
        <button class="btn active" onclick="filterSongs('all')">전체보기</button>
        <button class="btn" onclick="filterSongs('신나는')">💃 신나는</button>
        <button class="btn" onclick="filterSongs('잔잔한')">☕ 잔잔한</button>
        <button class="btn" onclick="filterSongs('위로되는')">🌙 위로되는</button>
    </div>

    <div class="playlist-container" id="playlist">
        </div>

    <script>
        // 💡 여기에 본인이 추천하고 싶은 노래 데이터를 마음껏 추가하세요!
        const songs = [
            {
                title: "Dynamite",
                artist: "BTS",
                mood: "신나는",
                emoji: "✨",
                url: "https://www.youtube.com/results?search_query=BTS+Dynamite"
            },
            {
                title: "밤편지",
                artist: "아이유 (IU)",
                mood: "잔잔한",
                emoji: "💌",
                url: "https://www.youtube.com/results?search_query=아이유+밤편지"
            },
            {
                title: "수고했어 오늘도",
                artist: "옥상달빛",
                mood: "위로되는",
                emoji: "🌳",
                url: "https://www.youtube.com/results?search_query=옥상달빛+수고했어+오늘도"
            },
            {
                title: "Hype Boy",
                artist: "NewJeans",
                mood: "신나는",
                emoji: "👖",
                url: "https://www.youtube.com/results?search_query=NewJeans+Hype+Boy"
            },
            {
                title: "모든 날, 모든 순간",
                artist: "폴킴",
                mood: "잔잔한",
                emoji: "🌅",
                url: "https://www.youtube.com/results?search_query=폴킴+모든날모든순간"
            }
        ];

        // 노래 카드를 화면에 그리는 함수
        function displaySongs(songList) {
            const playlistContainer = document.getElementById('playlist');
            playlistContainer.innerHTML = ''; // 기존 카드 초기화

            songList.forEach(song => {
                const card = document.createElement('div');
                card.className = 'card';
                card.innerHTML = `
                    <div class="album-art">${song.emoji}</div>
                    <div class="song-title">${song.title}</div>
                    <div class="artist">${song.artist}</div>
                    <span class="mood-tag">#${song.mood}</span><br>
                    <a href="${song.url}" target="_blank" class
