function solution(genres, plays) {
    const genreTotalMap = new Map(); // 장르별 총 재생 횟수
    const songMap = new Map();       // 장르별 곡 정보 (index, plays)

    // 1. 데이터 해싱 (Map 활용)
    genres.forEach((genre, i) => {
        const play = plays[i];
        genreTotalMap.set(genre, (genreTotalMap.get(genre) || 0) + play);
        
        const songs = songMap.get(genre) || [];
        songs.push({ id: i, play });
        songMap.set(genre, songs);
    });

    // 2. 장르 정렬 (총 재생 횟수 내림차순)
    const sortedGenres = [...genreTotalMap.entries()]
        .sort((a, b) => b[1] - a[1])
        .map(entry => entry[0]);

    // 3. 결과 도출 (장르별 최대 2곡씩)
    const result = [];
    for (const genre of sortedGenres) {
        const songs = songMap.get(genre);
        
        // 곡 정렬: 재생수 내림차순 -> 같으면 index 오름차순
        songs.sort((a, b) => b.play - a.play || a.id - b.id);
        
        // 최대 2개만 추출
        result.push(...songs.slice(0, 2).map(s => s.id));
    }

    return result;
}