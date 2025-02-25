// 악기 데이터
const instruments = {
    sogo: {
        name: "小鼓(소고)",
        description: `小鼓是韩国的传统乐器，形状像一个小的圆形鼓，演奏时使用木质手柄和木质的敲棒。
        主要用于名为农乐的传统音乐，鼓的直径约为20厘米，属于较小的类型。
        声音是通过敲击鼓面的皮革发出，但声音本身并不大，主要用于舞蹈或表演中。
        小鼓的大小和形状可能因地区而异，在一些地区，演奏时会用绳子代替手柄进行固定。
        如今，经过各种形式的发展，小鼓的形态已经较为统一。
        这种乐器更多用于舞蹈和动作而非音效，并且拿着小鼓跳的传统舞蹈形式也有独自的发展。`,
        image1: "static/img/sogo1.png",
        image2: "static/img/sogo2_dance.jpg",
        sound: "static/audios/sogo.mp3"
    },
    gayageum: {
        name: "伽倻琴(가야금)",
        description: `伽倻琴(gayageum)是韩国的传统弦乐器。
        长而平的琴身上有十二根丝线弦，每根弦都放置在可移动的桥（安足）上。
        弦的张力通过琴身头部的旋钮和尾部的拉绳来调节。伽倻琴有风流伽倻琴和散调伽倻琴两种类型，风流伽倻琴更大，通常坐着演奏。
        伽倻琴由梧桐木制成，用手拨弦发声。传统上是坐在地上演奏，但也可以坐在椅子上或站着演奏。

`,
        image1: "static/img/gayageum1.jpg",
        image2: "static/img/gayageum2.jpg",
        sound: "static/audios/산조가야금.mp3"
    },
    jing: {
        name: "锣(징)",
        description: `锣(jing)是韩国的传统打击乐器之一。
        用黄铜制成的圆形托盘状乐器，演奏时用左手拿着或悬挂在框架上，用圆形的槌子敲打。
        锣广泛用于农乐、巫俗音乐、佛教音乐和军乐中，其余音悠长，回响深沉。
        因为槌子的末端包裹着布料，所以发出柔和的音色。`,
        image1: "static/img/jing1.jpg",
        image2: "static/img/jing2.jpg",
        sound: "static/audios/jing.mp3"
    },
    haegeum: {
        name: "奚琴(해금)",
        description: `奚琴(haegeum)是韩国传统弦乐器之一。
        它由中空的圆形木质琴体和由梧桐木制成的前面板组成，琴体上插着一根长木杆，琴弦呈弓形挂在上面演奏。
        演奏时，右手使用弓杆摩擦两根弦发声，左手通过同时按压或放开两根弦来调节音高。自高丽时期传入韩国以来，
        奚琴广泛应用于从宫廷音乐到民间音乐的各种领域。`,
        image1: "static/img/haegeum1.jpg",
        image2: "static/img/haegeum2.png",
        sound: "static/audios/haegeum.mp3"
    },
    kkwaenggwari: {
        name: "小锣(꽹과리)",
        description: `小锣(kkwaeinggwari)是韩国的传统打击乐器，使用小型的黄铜制成。
        最初主要由平民使用，但在宗庙祭礼乐中也有使用。
        虽然小锣的尺寸比锣小，但声音非常强烈而清晰，因此在四物游戏中发出最为突出的声音。
        小锣在农乐或巫俗音乐中，起着引领快速且多变节奏的作用。
        演奏时使用末端挂着圆形扁平木片的槌子，并通过将手指放在小锣的背面来调节声音的余韵。`,
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
