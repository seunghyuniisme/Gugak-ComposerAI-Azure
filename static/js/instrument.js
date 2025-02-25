// 악기 데이터
const instruments = {
    sogo: {
        name: "소고",
        description: `소고는 한국의 전통 악기로, 작고 둥근 북 모양을 하고 있으며, 나무 손잡이와 나무로 만든 채를 사용해 연주합니다.
        주로 농악이라는 전통 음악에서 쓰이며, 북의 지름은 약 20cm 정도로 작은 편입니다. 
        소리는 북의 가죽 면을 두드려서 내지만, 소리 자체는 크지 않으며, 주로 춤이나 퍼포먼스에서 많이 사용됩니다.
        소고는 지역마다 크기나 모양에 차이가 있을 수 있고, 일부 지역에서는 손잡이 대신 끈을 사용해 고정시켜 연주하기도 합니다. 
        현재는 다양한 형태에서 표준화된 형태로 많이 통일되었습니다. 
        이 악기는 음향보다는 춤과 동작에 더 많이 사용되며, 소고를 들고 추는 전통 춤 양식도 따로 발달해 있습니다.`,
        image1: "static/img/sogo1.png",
        image2: "static/img/sogo2_dance.jpg",
        sound: "static/audios/sogo.mp3"
    },
    gayageum: {
        name: "가야금",
        description: `가야금은 한국의 전통적인 현악기입니다. 
        긴 평평한 몸체에 열두 개의 명주실 줄이 걸려 있으며, 각 줄은 움직일 수 있는 다리(안족)에 올려져 있습니다. 
        줄의 장력은 몸통 머리 부분의 돌괘와 꼬리 부분의 줄을 당겨 조절합니다. 
        가야금에는 풍류 가야금과 산조 가야금 두 종류가 있으며, 풍류 가야금이 더 크고, 주로 앉아서 연주합니다. 
        오동나무로 만들어졌으며, 손으로 줄을 뜯어 소리를 냅니다. 
        전통적으로 바닥에 앉아 연주하지만, 의자에 앉거나 서서도 연주할 수 있습니다.`,
        image1: "static/img/gayageum1.jpg",
        image2: "static/img/gayageum2.jpg",
        sound: "static/audios/산조가야금.mp3"
    },
    jing: {
        name: "징",
        description: `징은 한국의 전통 타악기 중 하나입니다. 
        놋쇠로 만든 둥근 쟁반 모양의 악기를 왼손에 들거나 틀에 매달아 놓고 둥근 채로 치는 방식으로 연주합니다. 
        농악, 무속음악, 불교음악, 군악 등에 두루 사용되며, 악기의 여운이 길고 울림이 깊습니다. 
        징채의 채 끝에 헝겊을 감아치기 때문에 부드러운 음색을 냅니다.`,
        image1: "static/img/jing1.jpg",
        image2: "static/img/jing2.jpg",
        sound: "static/audios/jing.mp3"
    },
    haegeum: {
        name: "해금",
        description: `
        해금은 한국 전통 현악기 중 하나입니다. 
        속이 빈 둥근 나무에 오동나무로 만든 앞판을 붙이고, 긴 나무 막대를 꽂아 줄을 활 모양으로 걸어 연주합니다. 
        오른손으로 활대를 이용해 두 줄을 문질러 소리를 내며, 왼손으로는 두 줄을 동시에 잡거나 떼면서 음높이를 조절합니다. 
        해금은 고려시대에 한국에 전해진 이후, 궁중음악부터 민속음악까지 다양한 분야에서 널리 사용되고 있습니다.
        `,
        image1: "static/img/haegeum1.jpg",
        image2: "static/img/haegeum2.png",
        sound: "static/audios/haegeum.mp3"
    },
    kkwaenggwari: {
        name: "꽹과리",
        description: `꽹과리는 한국의 전통 타악기로, 작은 크기의 놋쇠로 만들어졌습니다. 
        본래 서민들이 주로 사용했으나, 종묘제례악에서도 사용됩니다. 
        징보다 크기는 작지만, 소리가 매우 강하고 뚜렷하여 사물놀이에서 가장 두드러진 소리를 냅니다. 
        꽹과리는 농악이나 무속 음악에서 빠르고 변화무쌍한 장단을 이끌어가는 역할을 합니다. 
        둥글고 납작한 나뭇조각을 끝에 달아 만든 채로 연주하며, 손가락을 꽹과리 뒤쪽에 넣어 소리의 여운을 조절할 수 있습니다.`,
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


///////////
// 녹음 일시정지 또는 정지 함수
// 녹음 시작 함수
function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            mediaRecorder = new MediaRecorder(stream);
            audioChunks = []; // 녹음 시작 시 기존 녹음 데이터 초기화
            
            mediaRecorder.ondataavailable = event => {
                audioChunks.push(event.data);
            };

            mediaRecorder.onstop = () => {
                const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
                audioUrl = URL.createObjectURL(audioBlob);
                
                // 서버에 업로드하는 함수 호출
                uploadAudio(audioBlob);
            };

            mediaRecorder.start();
            console.log('녹음 시작');
            recordingTimeout = setTimeout(pauseOrStopRecording, 30000); // 30초 후 자동 정지

            // UI 상태 업데이트
            smoothTransition('.record-button', '.pause-button');
            document.querySelector('.title').style.display = 'none';
            document.querySelector('.recording-message').style.display = 'block';
            document.querySelector('.next-button').style.display = 'none';
            document.getElementById('beatSample').style.display = 'none';
            document.querySelector('.trigger-image').style.display = 'none';
            document.querySelector('.back-button').style.display = 'none';
        })
        .catch(error => console.error('마이크를 사용할 수 없습니다.', error));
}

// 녹음 일시정지 또는 정지 함수
function pauseOrStopRecording() {
    if (mediaRecorder.state === "recording") {
        mediaRecorder.stop();
        clearTimeout(recordingTimeout);
        console.log('녹음 중지');

        // UI 상태 업데이트
        document.querySelector('.pause-button').style.display = 'none';
        document.querySelector('.play-button').style.display = 'block';
        document.querySelector('.recording-message').style.display = 'none';
        const title = document.querySelector('.title');
        title.innerText = '녹음된 악기 소리를 클릭해서 들어보세요';
        document.querySelector('.next-button').style.display = 'block';
        title.classList.add('fade-in');
        title.style.display = 'block';
        document.getElementById('beatSample').style.display = 'none';
        document.querySelector('.trigger-image').style.display = 'none';
        document.getElementById('recordingInfo').style.display = 'none';

        // 리셋 버튼과 메시지 보이기
        document.querySelector('.reset-button').style.display = 'block';
        document.querySelector('.reset-message').style.display = 'block';
        document.querySelector('.back-button').style.display = 'none';
    }
}

// 오디오 파일 서버 업로드 함수
function uploadAudio(blob) {
    const formData = new FormData();
    formData.append('file', blob, 'recorded_audio.wav');

    fetch('/upload_audio', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        if (data.message) {
            console.log("Audio uploaded successfully");
        } else {
            console.error("Audio upload failed:", data.error);
        }
    })
    .catch(error => console.error('Error:', error));
}
