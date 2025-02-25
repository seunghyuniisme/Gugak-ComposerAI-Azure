// 악기 데이터
const instruments = {
    sogo: {
        name: "ソゴ(소고)",
        description: `ソゴ(sogo)は韓国の伝統的な楽器で、小さく丸い太鼓の形をしており、木の握り手と木製のバチを使って演奏します。
        主に農楽という伝統音楽で使われ、太鼓の直径は約20cmほどと小さい方です。
        音は太鼓の革の面を叩いて出しますが、音量自体は大きくなく、主に踊りやパフォーマンスでよく使われます。
        ソゴは地域によって大きさや形に違いがあることもあり、一部の地域では握り手の代わりに紐を使って固定し、演奏することもあります。
        今では、様々な形から標準化され、段々統一されています。
        ソゴは音響よりも踊りや動作に多く使用されており、これを持って踊る伝統的な踊りの形式も別に発達しています。`,
        image1: "static/img/sogo1.png",
        image2: "static/img/sogo2_dance.jpg",
        sound: "static/audios/sogo.mp3"
    },
    gayageum: {
        name: "カヤグム(가야금)",
        description: `カヤグム(gayageum)は韓国の伝統的な弦楽器です。
    長く平らな胴体に12本の絹の糸で作られた弦が張られており、各弦は可動式の橋（雁足）の上に置かれています。
    弦の張力は胴体の頭の部分にあるトルケ(軫棵-カヤグムの音を調節する木切れ)と尾の部分の弦を引っ張って調整します。
    カヤグムには風流カヤグムとサンジョカヤグムの2種類があり、風流カヤグムの方が大きく、主に座って演奏します。
    桐の木で作られ、手で弦をはじいて音を出します。伝統的には床に座って演奏しますが、椅子に座ったり立ったりしても演奏できます。`,
        image1: "static/img/gayageum1.jpg",
        image2: "static/img/gayageum2.jpg",
        sound: "static/audios/산조가야금.mp3"
    },
    jing: {
        name: "チン(징)",
        description: `チン(jing)は韓国の伝統的な打楽器の一つです。
        真鍮で作られた丸いお盆の形をした楽器を左手で持ったり、枠に吊るして、丸いバチで叩く方法で演奏します。
        農楽、巫俗音楽、仏教音楽、軍楽などさまざまな音楽に広く使われ、楽器の余韻が長く、響きが深いです。
        先端に布を巻いて叩くため、柔らかい音色を出します。`,
        image1: "static/img/jing1.jpg",
        image2: "static/img/jing2.jpg",
        sound: "static/audios/jing.mp3"
    },
    haegeum: {
        name: "ヘグム(해금)",
        description: `ヘグム(haegeum)は韓国の伝統的な弦楽器の一つです。
        中が空て丸い木に桐の木で作られた前板を取り付け、長い木の棒に弦を弓の形にかけて演奏します。
        右手で弓を使って2本の弦をこすり音を出し、左手で2本の弦を同時に押さえたり離したりして音程を調整します。
        ヘグムは高麗時代に韓国に伝わって以来、宮廷音楽から民俗音楽に至るまで、さまざまな分野で広く使用されています。`,
        image1: "static/img/haegeum1.jpg",
        image2: "static/img/haegeum2.png",
        sound: "static/audios/haegeum.mp3"
    },
    kkwaenggwari: {
        name: "クェンガリ(꽹과리)",
        description: `クェンガリ(kkwaenggwari)は韓国の伝統的な打楽器で、小さな真鍮で作られています。
        元々は庶民が主に使用していましたが、宗廟祭礼楽でも使用されます。
        チンよりもサイズは小さいですが、音が非常に強く、はっきりしているため、サムルノリ(四種の打楽器でいろいろなリズム音楽を合奏する民俗音楽)で最も際立つ音を出します。
        クェンガリは農楽や巫俗音楽で、速くて変化に富んだリズムをリードする役割を果たします。
        丸くて平たい木片を端につけて作ったまま演奏し、指をクェンガリの裏側に入れて音の余韻を調整することができます。`,
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
