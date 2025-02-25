// 악기 데이터
const instruments = {
    sogo: {
        name: "sogo(소고)",
        description: `The sogo is a traditional Korean percussion instrument, shaped like a small round drum. 
        It is played using a wooden handle and a wooden stick. It is primarily used in nongak (Korean traditional farmers’ music),
         and the drum's diameter is about 20 cm, making it relatively small. 
         The sound is produced by striking the drum's leather surface, but the sound itself is not very loud. It is often used in performances or dances.
        The size and shape of the sogo can vary by region, and in some areas, instead of a handle, a string is used to secure the drum while playing. 
        Nowadays, the sogo has become more standardized in its form.
        This instrument is used more for dance and movement rather than for its acoustic qualities, 
        and traditional dance styles that involve holding and dancing with the sogo have also developed separately.
.`,
        image1: "static/img/sogo1.png",
        image2: "static/img/sogo2_dance.jpg",
        sound: "static/audios/sogo.mp3"
    },
    gayageum: {
        name: "gayageum(가야금)",
        description: `The gayageum is a traditional Korean string instrument. 
        It has twelve silk strings stretched over its long, flat body, and each string is supported by a movable bridge (anjok). 
        The tension of the strings is adjusted by pulling the strings at the tail and tuning pegs at the head of the instrument.
        There are two types of gayageum: the pungnyu gayageum and the sanjo gayageum. 
        The pungnyu gayageum is larger and is typically played while seated. 
        It is made from paulownia wood, and sound is produced by plucking the strings with the hands.
        Traditionally, the gayageum is played while sitting on the floor, but it can also be played while seated in a chair or even standing.`,
        image1: "static/img/gayageum1.jpg",
        image2: "static/img/gayageum2.jpg",
        sound: "static/audios/산조가야금.mp3"
    },
    jing: {
        name: "jing(징)",
        description: `The jing is one of Korea's traditional percussion instruments. 
        It is a round, brass instrument shaped like a tray, and it is played either by holding it in the left hand or hanging it on a frame while striking it with a round mallet. 
        The jing is widely used in nongak (farmers' music), shamanic music, Buddhist music, and military music. 
        The instrument produces a long-lasting resonance with deep reverberation.
        The mallet used to play the jing is wrapped in cloth at the tip, which produces a soft tone when struck.`,
        image1: "static/img/jing1.jpg",
        image2: "static/img/jing2.jpg",
        sound: "static/audios/jing.mp3"
    },
    haegeum: {
        name: "haegeum(해금)",
        description: `The haegeum is one of Korea's traditional string instruments. 
        It has a hollow, round wooden body with a front plate made of paulownia wood, and a long wooden rod is inserted through the body. 
        Two strings are strung across it in the shape of a bow.
        The instrument is played by rubbing the two strings with a bow using the right hand, 
        while the left hand adjusts the pitch by pressing and releasing the strings. 
        Since its introduction to Korea during the Goryeo Dynasty, the haegeum has been widely used in various musical genres, from court music to folk music.`,
        image1: "static/img/haegeum1.jpg",
        image2: "static/img/haegeum2.png",
        sound: "static/audios/haegeum.mp3"
    },
    kkwaenggwari: {
        name: "kkwaenggwari(꽹과리)",
        description: `The kkwaenggwari is a traditional Korean percussion instrument made of a small brass disc. 
        Originally, it was mainly used by commoners, but it is also used in Jongmyo Jeryeak (royal ancestral ritual music). 
        Although smaller than the jing, it produces a very strong and clear sound, 
        making it the most prominent instrument in samulnori (Korean traditional percussion quartet).
        The kkwaenggwari plays a leading role in guiding fast and dynamic rhythms in nongak (farmers' music) or shamanic music. 
        It is played using a mallet with a round, flat wooden piece attached to the tip, 
        and the player can control the resonance by placing fingers behind the instrument.`,
        image1: "static/img/kkwaenggwari1.jpg",
        image2: "static/img/kkwaenggwari2.png",
        sound: "static/audios/kkwaenggwari.mp3"
    }
};

    // 뒤로가기 버튼
    function goBack() {
        window.history.back();
    }
    
let currentAudio = null;

function showModal(instrumentKey) {
    const instrument = instruments[instrumentKey];
    if (instrument) {
        document.getElementById('instrumentTitle').textContent = instrument.name;
        document.getElementById('instrumentDescription').textContent = instrument.description;
        
        // 여러 개의 이미지를 설정
        document.getElementById('instrumentImage1').src = instrument.image1;  // 첫 번째 이미지
        document.getElementById('instrumentImage2').src = instrument.image2 || instrument.image1;  // 두 번째 이미지, 없으면 첫 번째 이미지로 대체
        
        // 오디오 파일 설정
        const audioElement = document.getElementById('instrumentAudio');
        audioElement.src = instrument.sound;  // 악기 사운드 파일 설정
        audioElement.load();  // 오디오 파일 로드

        // 모달 표시
        document.getElementById('instrumentModal').style.display = 'flex';
    }
}


function closeModal() {
    // 모달 닫기
    document.getElementById('instrumentModal').style.display = 'none';

    // 오디오 정지
    const audioElement = document.getElementById('instrumentAudio');
    audioElement.pause();  // 오디오 일시정지
    audioElement.currentTime = 0;  // 오디오 재생 위치 초기화
}
