# 🔈 하모예 (HARMO-YEAH)

<div align="center">
  <img src="https://github.com/user-attachments/assets/6fb9e564-05de-431b-9946-62d84e520e85" width="400" alt="설명">
</div>


## 📌 프로젝트 정보 (Project Info)
> **프로젝트 (Project):** MS AI School 4기 최종 팀 프로젝트   
> **개발기간 (Development Period):** September 2024 – October 2024  
> 팀원 : 민정, 서진, 수정, 승현, 재홍, 예연


## 📌 프로젝트 소개 (Project Description)
**하모예는 외국인 관광객을 위한 퓨전 국악 합주 생성 플랫폼입니다.**  
한국 전통 음악은 외국인 관광객에게 친숙하지 않아 쉽게 접하기 어려운 경우가 많습니다. 하모예를 통해 관광객은 직접 한국의 전통 악기를 연주하며 자신만의 멜로디를 만들고, AI가 이를 분석하여 적절한 음악적 요소를 보완해 더욱 풍성한 합주를 완성합니다. 이를 통해 국악을 단순히 감상하는 것을 넘어, 직접 연주하고 창작하는 새로운 경험을 제공합니다. 저희 프로젝트는 전통 문화 관광지를 방문하는 외국인 관광객을 대상으로 국악의 매력을 보다 쉽게 전달하고, 국악을 더욱 친근하게 즐길 수 있도록 하는 것을 목표로 합니다.    

**Harmo-Yeah is a fusion Korean traditional music ensemble platform for foreign tourists.**  
Tourists can play traditional Korean instruments and create their own melodies, while **AI enhances the ensemble by analyzing and complementing their performance**. This provides an interactive experience beyond simply listening to traditional music.  



## 📌 기술 스택 (Tech Stack)
### AI Model 
- **Automated Transcription Model:** Omnizart libsora, PrettyMIDI 
- **Audio Processing:** pydub 

### Cloud & AI Services 
- **Microsoft Azure:** TTS, Chatbot(gpt-4o) 

### Web Development 
- **Frontend:** HTML, CSS, JavaScript 
- **Backend:** Python 3.9 (Flask) 
- **Deployment:** Render  

### Collaboration Tool
- Microsoft Teams, Notion


## 📌 데이터 출처 (Data Sources)
### AI-Hub (https://www.aihub.or.kr/) 
  - **국악 음원 및 악보 데이터 (Korean Traditional Music Audio & Score Dataset)** 
  - **한국 대중음악 루프 사운드 데이터 (Korean Popular Music Loop Sound Dataset)**  


## 📌 실행 화면 (Final Output)
| 메인 페이지 (Main Page) | 헤더2 |
|---|---|
| 값1 | 값2 |
| 값4 | 값5 |


## 📌 주요 기능 (Key Features)
### 1️⃣ 전통 악기 녹음 및 분석
- 사용자가 직접 전통 악기 연주 녹음 가능  
- 배경 소음 제거 및 특정 악기 소리 분리  

### 2️⃣ 채보 (악보) 생성
- 녹음된 WAV 파일을 MIDI로 변환  
- 자동으로 악보 데이터 생성  

### 3️⃣ AI 기반 반주 생성
- MIDI 파일을 기반으로 자동 반주 생성  
- 한국 전통 악기(소고)와 조화로운 퓨전 음악 제작  

### 4️⃣ 최종 합주 음원 제공
- MIDI + 반주를 병합하여 WAV 파일로 변환  
- 완성된 퓨전 국악 합주를 감상 가능   

### 5️⃣ AI 챗봇 및 음성 안내 (TTS)
- 국악 악기 설명 및 사용법 안내  
- 다국어 지원 가능한 TTS 서비스

### 6️⃣ 관광객을 위한 언어별 페이지
- 한국어, 영어, 일본어, 중국어


## 📌 기타 추가 사항 (Notes)
 이 서비스는 **Microsoft Azure**가 활용되었습니다.   
 **Azure**의 **API 키**와 **Endpoint** 값이 필요합니다.

 This service utilizes **Microsoft Azure**.  
 **Azure API Key** and **Endpoint** are required for proper functionality.
