// let currentAudio = null;

document.getElementById("ttsModalButton").addEventListener("click", () => {
  const title = document.getElementById("instrumentTitle").innerText;
  const description = document.getElementById(
    "instrumentDescription"
  ).innerText;
  const text = `${title}. ${description}`; // 제목과 설명을 결합

  getSpeechAudio(text);
});

function speakDescription() {
  const title = document.getElementById("instrumentTitle").innerText;
  const description = document.getElementById("instrumentDescription").innerText;
  const text = `${title}. ${description}`; // 제목과 설명을 결합


  // 기존 오디오가 재생 중이라면 중단
  if (currentAudio) {
    currentAudio.pause();
    currentAudio.currentTime = 0; 
  }
  getSpeechAudio(text);

}

async function getSpeechAudio(text) {
  const subscriptionKey = "516cb868c787467581b7189d5ab4bbbd"; // 구독 키
  const region = "eastus"; // 지역

  const tokenResponse = await fetch(
    `https://${region}.api.cognitive.microsoft.com/sts/v1.0/issueToken`,
    {
      method: "POST",
      headers: {
        "Ocp-Apim-Subscription-Key": subscriptionKey,
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "0",
      },
    }
  );

  const accessToken = await tokenResponse.text();

  const ssml = `<speak version='1.0' xml:lang='en-US'>
        <voice xml:lang='en-US' xml:gender='Female' name='en-US-AvaMultilingualNeural'>
            ${text}
        </voice>
    </speak>`;

  const response = await fetch(
    `https://${region}.tts.speech.microsoft.com/cognitiveservices/v1`,
    {
      method: "POST",
      headers: {
        Authorization: `Bearer ${accessToken}`,
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "audio-24khz-48kbitrate-mono-mp3",
      },
      body: ssml,
    }
  );

  if (response.ok) {
    const audioBlob = await response.blob();
    const audioUrl = URL.createObjectURL(audioBlob);

    // 기존 오디오가 재생 중이라면 중단
  if (currentAudio) {
    currentAudio.pause();
    currentAudio.currentTime = 0; 
  }

    // const audio = new Audio(audioUrl);
    // audio.play();
    currentAudio = new Audio(audioUrl);
    currentAudio.play();

  } else {
    console.error("TTS 요청 실패:", response.statusText);
  }
}



// 모달을 닫을 때 음성을 정지
function closeModal() {
  // 모달 닫기
  document.getElementById('instrumentModal').style.display = 'none';

  // 오디오 정지
  const audioElement = document.getElementById('instrumentAudio');
  audioElement.pause();  // 오디오 일시정지
  audioElement.currentTime = 0;  // 오디오 재생 위치 초기화

  // 음성 정지
  if (currentAudio) {
    currentAudio.pause(); // 음성 정지
    currentAudio.currentTime = 0; // 음성 재생 위치 초기화
    currentAudio = null; // 현재 오디오 초기화
  }
}








// async function getSpeechAudio(text) {
//   const subscriptionKey = "516cb868c787467581b7189d5ab4bbbd"; // 구독 키
//   const region = "eastus"; // 지역

//   const tokenResponse = await fetch(
//     `https://${region}.api.cognitive.microsoft.com/sts/v1.0/issueToken`,
//     {
//       method: "POST",
//       headers: {
//         "Ocp-Apim-Subscription-Key": subscriptionKey,
//         "Content-Type": "application/x-www-form-urlencoded",
//         "Content-Length": "0",
//       },
//     }
//   );

//   const accessToken = await tokenResponse.text();

//   const ssml = `<speak version='1.0' xml:lang='ko-KR'>
//         <voice xml:lang='ko-KR' xml:gender='Female' name='ko-KR-SunHiNeural'>
//             ${text}
//         </voice>
//     </speak>`;

//   const response = await fetch(
//     `https://${region}.tts.speech.microsoft.com/cognitiveservices/v1`,
//     {
//       method: "POST",
//       headers: {
//         Authorization: `Bearer ${accessToken}`,
//         "Content-Type": "application/ssml+xml",
//         "X-Microsoft-OutputFormat": "audio-24khz-48kbitrate-mono-mp3",
//       },
//       body: ssml,
//     }
//   );

//   if (response.ok) {
//     const audioBlob = await response.blob();
//     const audioUrl = URL.createObjectURL(audioBlob);

//     // 현재 오디오가 재생 중이라면 정지
//     if (currentAudio) {
//       currentAudio.pause();
//     }


//     const audio = new Audio(audioUrl);
//     audio.play();
//   } else {
//     console.error("TTS 요청 실패:", response.statusText);
//   }
// }
