# noisereduce 설치
# pip install noisereduce

import noisereduce as nr
import librosa
import soundfile as sf

def reduce_noise(input_file, output_file):
    # 오디오 파일 로드
    audio_data, sr = librosa.load(input_file, sr=None)

    # Noise reduction 적용
    reduced_noise = nr.reduce_noise(y=audio_data, sr=sr)

    # 결과 저장
    sf.write(output_file, reduced_noise, sr)
    print(f"Noise reduced file saved at: {output_file}")

# 사용 예시
# input_file = 'sogo.wav'
# output_file = 'sogo_clean.wav'

# reduce_noise(input_file, output_file)
