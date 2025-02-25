import librosa
import pretty_midi
import random
import subprocess
from pydub import AudioSegment

# Step 1: 소고.wav 파일을 MIDI로 변환하기
def convert_sogo_to_midi(audio_path, midi_output_path):
    # 소고.wav 파일 불러오기
    y, sr = librosa.load(audio_path)

    # 타격 시점 감지
    onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)

    # MIDI 파일 생성
    midi = pretty_midi.PrettyMIDI()
    drum = pretty_midi.Instrument(program=0)

    # 감지된 타격 시점을 MIDI 노트로 변환
    for onset in onset_times:
        note = pretty_midi.Note(velocity=100, pitch=60, start=onset, end=onset + 0.1)
        drum.notes.append(note)

    midi.instruments.append(drum)
    midi.write(midi_output_path)
    print(f'Sogo rhythm MIDI saved to {midi_output_path}')

# Step 2: 소고 리듬을 기반으로 기타 MIDI 생성하기 (소고와 조화를 이루도록 설정)
def generate_guitar_midi(sogo_midi_path, guitar_midi_output_path):
    # MIDI 불러오기
    sogo_midi = pretty_midi.PrettyMIDI(sogo_midi_path)
    guitar = pretty_midi.Instrument(program=24)  # 24: 기타 어쿠스틱

    # 코드 진행 설정 (일관성 있는 코드 진행 사용)
    chord_progression = [
        [48, 52, 55, 60, 64, 67],  # C major
        [55, 59, 62, 67],  # G major
        [45, 48, 52, 57],  # A minor
        [53, 57, 60, 65]  # F major
    ]

    # 소고의 리듬을 참고하면서 조화롭게 기타 연주 생성
    chord_index = 0
    previous_end = 0
    for note in sogo_midi.instruments[0].notes:
        # 현재 코드 선택
        current_chord = chord_progression[chord_index % len(chord_progression)]
        chord_index += 1

        # 소고 리듬을 참고하여 하모니 형성 (스트로크와 아르페지오 패턴 추가, 연주자 느낌 반영)
        start_time = max(previous_end, note.start)
        duration = (note.end - note.start) * random.uniform(0.8, 1.2)  # 소고 리듬을 참고하되 약간 변형
        end_time = start_time + duration

        # 스트로크나 아르페지오 패턴으로 기타 노트 추가 (각 음이 이어지도록 설정)
        if random.random() < 0.5:  # 50% 확률로 스트로크 추가
            # 코드 스트로크: 모든 음을 동시에 연주 (길게 이어지도록 설정)
            for pitch in current_chord:
                guitar_note = pretty_midi.Note(velocity=random.randint(70, 100), pitch=pitch,
                                               start=start_time, end=end_time + 0.5)
                guitar.notes.append(guitar_note)
        else:
            # 아르페지오: 음을 순차적으로 연주 (음 사이가 끊기지 않도록 설정)
            arpeggio_duration = duration / len(current_chord)
            for i, pitch in enumerate(current_chord):
                arpeggio_start = start_time + i * arpeggio_duration
                arpeggio_end = arpeggio_start + arpeggio_duration * random.uniform(0.8, 1.2)
                guitar_note = pretty_midi.Note(velocity=random.randint(70, 100), pitch=pitch,
                                               start=arpeggio_start, end=arpeggio_end + 0.3)
                guitar.notes.append(guitar_note)

        # 쉬는 타이밍 추가 (더 의미 있는 쉬는 타이밍 설정)
        if random.random() < 0.3:  # 30% 확률로 쉬는 타이밍 추가
            rest_duration = duration * random.uniform(0.2, 0.5)
            previous_end = end_time + rest_duration
        else:
            previous_end = end_time

        # 추가적인 대위적 음을 삽입하여 소고와 대화하는 느낌 제공 (음이 이어지도록 설정)
        if random.random() < 0.5:  # 50% 확률로 추가 음 삽입
            counter_pitch = random.choice(current_chord)
            counter_start = start_time + duration * random.uniform(0.1, 0.3)  # 약간의 지연을 주어 대위적 느낌
            counter_end = counter_start + duration * random.uniform(0.5, 0.8) + 0.3
            guitar_note = pretty_midi.Note(velocity=random.randint(60, 90), pitch=counter_pitch,
                                           start=counter_start, end=counter_end)
            guitar.notes.append(guitar_note)

    # 기타 트랙을 새 MIDI에 추가
    ensemble_midi = pretty_midi.PrettyMIDI()
    ensemble_midi.instruments.append(guitar)
    ensemble_midi.write(guitar_midi_output_path)
    print(f'Guitar accompaniment MIDI saved to {guitar_midi_output_path}')

# Step 4: 소고 리듬을 기반으로 바이올린 MIDI 생성하기 (소고와 조화를 이루도록 설정)
def generate_violin_midi(sogo_midi_path, violin_midi_output_path):
    # MIDI 불러오기
    sogo_midi = pretty_midi.PrettyMIDI(sogo_midi_path)
    violin = pretty_midi.Instrument(program=40)  # 40: 바이올린

    # 코드 진행 설정 (일관성 있는 코드 진행 사용)
    chord_progression = [
        [60, 64, 67],  # C major
        [67, 71, 74],  # G major
        [57, 60, 64],  # A minor
        [65, 69, 72]  # F major
    ]

    # 소고의 리듬을 참고하면서 조화롭게 바이올린 연주 생성
    chord_index = 0
    previous_end = 0
    for note in sogo_midi.instruments[0].notes:
        # 현재 코드 선택
        current_chord = chord_progression[chord_index % len(chord_progression)]
        chord_index += 1

        # 소고 리듬을 참고하여 하모니 형성 (멜로디 라인 추가, 연주자 느낌 반영, 음이 이어지도록 설정)
        start_time = max(previous_end, note.start)
        duration = (note.end - note.start) * random.uniform(0.8, 1.2)  # 소고 리듬을 참고하되 약간 변형
        end_time = start_time + duration

        # 멜로디 음을 순차적으로 연주하여 바이올린 노트 추가 (음이 끊기지 않도록 설정)
        melody_pitch = random.choice(current_chord)  # 코드 내에서 멜로디 음 선택
        violin_note = pretty_midi.Note(velocity=random.randint(70, 100), pitch=melody_pitch,
                                       start=start_time, end=end_time + 0.5)
        violin.notes.append(violin_note)

        # 쉬는 타이밍 추가 (더 의미 있는 쉬는 타이밍 설정)
        if random.random() < 0.3:  # 30% 확률로 쉬는 타이밍 추가
            rest_duration = duration * random.uniform(0.2, 0.5)
            previous_end = end_time + rest_duration
        else:
            previous_end = end_time

        # 추가적인 대위적 음을 삽입하여 소고와 대화하는 느낌 제공 (음이 이어지도록 설정)
        if random.random() < 0.5:  # 50% 확률로 추가 음 삽입
            counter_pitch = random.choice(current_chord)
            counter_start = start_time + duration * random.uniform(0.1, 0.3)  # 약간의 지연을 주어 대위적 느낌
            counter_end = counter_start + duration * random.uniform(0.5, 0.8) + 0.3
            violin_note = pretty_midi.Note(velocity=random.randint(60, 90), pitch=counter_pitch,
                                           start=counter_start, end=counter_end)
            violin.notes.append(violin_note)

    # 바이올린 트랙을 새 MIDI에 추가
    ensemble_midi = pretty_midi.PrettyMIDI()
    ensemble_midi.instruments.append(violin)
    ensemble_midi.write(violin_midi_output_path)
    print(f'Violin accompaniment MIDI saved to {violin_midi_output_path}')

# Step 5: MIDI 파일을 WAV로 변환하는 함수 (fluidsynth 사용)
def render_midi_to_wav(midi_path, output_wav_path, soundfont_path):
    # Fluidsynth를 사용하여 MIDI를 WAV로 변환
    subprocess.run(['fluidsynth', '-ni', soundfont_path, midi_path, '-F', output_wav_path])
    print(f'{output_wav_path} saved.')

# Step 6: 여러 WAV 파일을 동시에 재생하도록 병합하고 볼륨을 조정하는 함수
def merge_multiple_wavs_with_volume(wav_files, output_file, background_volume_db=-6, volume_db=-3):
    # 원본 WAV 파일의 볼륨을 background_volume_db만큼 낮추기
    combined = AudioSegment.from_wav(wav_files[0]).apply_gain(background_volume_db)
    
    # 나머지 WAV 파일들을 volume_db로 설정하여 오버레이
    for wav_file in wav_files[1:]:
        next_wav = AudioSegment.from_wav(wav_file).apply_gain(volume_db)
        combined = combined.overlay(next_wav)
    
    # 병합된 오디오 파일을 저장
    combined.export(output_file, format="wav")
    print(f'Merged WAV saved to {output_file}')

# Step 3: 소고 리듬을 기반으로 드럼 MIDI 생성하기 (리듬 강화)
def generate_drum_midi(sogo_midi_path, drum_midi_output_path):
    # MIDI 불러오기
    sogo_midi = pretty_midi.PrettyMIDI(sogo_midi_path)
    drum = pretty_midi.Instrument(program=0, is_drum=True)  # 드럼 채널

    # 소고 리듬을 참고하여 드럼 패턴 생성
    for note in sogo_midi.instruments[0].notes:
        # 킥 드럼 (MIDI pitch 36)과 스네어 드럼 (MIDI pitch 38)을 번갈아가며 추가
        drum_pitch = 36 if random.random() < 0.5 else 38
        drum_note = pretty_midi.Note(velocity=random.randint(80, 120), pitch=drum_pitch,
                                     start=note.start, end=note.end + 0.1)
        drum.notes.append(drum_note)

    # 드럼 트랙을 새 MIDI에 추가
    ensemble_midi = pretty_midi.PrettyMIDI()
    ensemble_midi.instruments.append(drum)
    ensemble_midi.write(drum_midi_output_path)
    print(f'Drum accompaniment MIDI saved to {drum_midi_output_path}')

# Step 5: 패드/신디사이저 패드 MIDI 생성하기 (지속적인 코드 패드 추가)
def generate_pad_midi(sogo_midi_path, pad_midi_output_path):
    # MIDI 불러오기
    sogo_midi = pretty_midi.PrettyMIDI(sogo_midi_path)
    pad = pretty_midi.Instrument(program=88)  # 88: Pad 1 (new age)

    # 코드 진행 설정 (일관성 있는 코드 진행 사용)
    chord_progression = [
        [60, 64, 67],  # C major
        [67, 71, 74],  # G major
        [57, 60, 64],  # A minor
        [65, 69, 72]  # F major
    ]

    # 지속적인 코드 패드 생성
    chord_index = 0
    for i in range(4):  # 각 코드당 일정 길이 유지 (4마디 반복)
        current_chord = chord_progression[chord_index % len(chord_progression)]
        chord_index += 1

        # 코드의 각 음을 패드로 추가 (지속적인 배경음을 위한 설정)
        start_time = i * 4.0  # 각 코드의 시작 시간 (4마디 간격)
        end_time = start_time + 4.0  # 각 코드의 길이 (4초)
        for pitch in current_chord:
            pad_note = pretty_midi.Note(velocity=80, pitch=pitch, start=start_time, end=end_time)
            pad.notes.append(pad_note)

    # 패드 트랙을 새 MIDI에 추가
    ensemble_midi = pretty_midi.PrettyMIDI()
    ensemble_midi.instruments.append(pad)
    ensemble_midi.write(pad_midi_output_path)
    print(f'Pad accompaniment MIDI saved to {pad_midi_output_path}')

# Step 6: 소고 리듬을 기반으로 첼로 MIDI 생성하기 (국악 분위기 반영)
def generate_cello_midi(sogo_midi_path, cello_midi_output_path):
    # MIDI 불러오기
    sogo_midi = pretty_midi.PrettyMIDI(sogo_midi_path)
    cello = pretty_midi.Instrument(program=42)  # 42: 첼로

    # 코드 진행 설정 (일관성 있는 코드 진행 사용)
    chord_progression = [
        [48, 52, 55],  # C major (저음)
        [43, 47, 50],  # G major (저음)
        [45, 48, 52],  # A minor (저음)
        [41, 45, 48]  # F major (저음)
    ]

    # 소고 리듬을 참고하면서 조화롭게 첼로 연주 생성
    chord_index = 0
    previous_end = 0
    for note in sogo_midi.instruments[0].notes:
        # 현재 코드 선택
        current_chord = chord_progression[chord_index % len(chord_progression)]
        chord_index += 1

        # 소고 리듬을 참고하여 하모니 형성 (지속적인 저음 연주 추가)
        start_time = max(previous_end, note.start)
        duration = (note.end - note.start) * random.uniform(1.5, 2.0)  # 음을 더 길게 유지하여 부드럽게 연결
        end_time = start_time + duration

        # 코드의 각 음을 첼로 노트로 추가
        for pitch in current_chord:
            cello_note = pretty_midi.Note(velocity=random.randint(60, 90), pitch=pitch,
                                         start=start_time, end=end_time)
            cello.notes.append(cello_note)

        previous_end = end_time

    # 첼로 트랙을 새 MIDI에 추가
    ensemble_midi = pretty_midi.PrettyMIDI()
    ensemble_midi.instruments.append(cello)
    ensemble_midi.write(cello_midi_output_path)
    print(f'Cello accompaniment MIDI saved to {cello_midi_output_path}')

# Step 7: 소고 리듬을 기반으로 플루트 MIDI 생성하기 (국악 분위기 반영)
def generate_flute_midi(sogo_midi_path, flute_midi_output_path):
    # MIDI 불러오기
    sogo_midi = pretty_midi.PrettyMIDI(sogo_midi_path)
    flute = pretty_midi.Instrument(program=73)  # 73: 플루트

    # 코드 진행 설정 (일관성 있는 코드 진행 사용)
    chord_progression = [
        [72, 76, 79],  # C major (고음)
        [74, 78, 81],  # G major (고음)
        [69, 72, 76],  # A minor (고음)
        [71, 74, 77]  # F major (고음)
    ]

    # 소고 리듬을 참고하면서 조화롭게 플루트 연주 생성
    chord_index = 0
    previous_end = 0
    for note in sogo_midi.instruments[0].notes:
        # 현재 코드 선택
        current_chord = chord_progression[chord_index % len(chord_progression)]
        chord_index += 1

        # 소고 리듬을 참고하여 멜로디 형성 (고음 멜로디 추가)
        start_time = max(previous_end, note.start)
        duration = (note.end - note.start) * random.uniform(1.5, 2.0)  # 음을 더 길게 유지하여 부드럽게 연결
        end_time = start_time + duration

        # 코드 내에서 멜로디 음 선택하여 플루트 노트로 추가
        melody_pitch = random.choice(current_chord)
        flute_note = pretty_midi.Note(velocity=random.randint(70, 100), pitch=melody_pitch,
                                     start=start_time, end=end_time)
        flute.notes.append(flute_note)

        previous_end = end_time

    # 플루트 트랙을 새 MIDI에 추가
    ensemble_midi = pretty_midi.PrettyMIDI()
    ensemble_midi.instruments.append(flute)
    ensemble_midi.write(flute_midi_output_path)
    print(f'Flute accompaniment MIDI saved to {flute_midi_output_path}')

# Step 8: 소고 리듬을 기반으로 오보에 MIDI 생성하기 (국악 분위기 반영)
def generate_oboe_midi(sogo_midi_path, oboe_midi_output_path):
    # MIDI 불러오기
    sogo_midi = pretty_midi.PrettyMIDI(sogo_midi_path)
    oboe = pretty_midi.Instrument(program=68)  # 68: 오보에

    # 코드 진행 설정 (일관성 있는 코드 진행 사용)
    chord_progression = [
        [60, 64, 67],  # C major
        [62, 65, 69],  # D minor
        [67, 71, 74],  # G major
        [65, 69, 72]  # F major
    ]

    # 소고 리듬을 참고하면서 조화롭게 오보에 연주 생성
    chord_index = 0
    previous_end = 0
    for note in sogo_midi.instruments[0].notes:
        # 현재 코드 선택
        current_chord = chord_progression[chord_index % len(chord_progression)]
        chord_index += 1

        # 소고 리듬을 참고하여 멜로디 형성 (고음 멜로디 추가)
        start_time = max(previous_end, note.start)
        duration = (note.end - note.start) * random.uniform(1.5, 2.0)  # 음을 더 길게 유지하여 부드럽게 연결
        end_time = start_time + duration

        # 코드 내에서 멜로디 음 선택하여 오보에 노트로 추가
        melody_pitch = random.choice(current_chord)
        oboe_note = pretty_midi.Note(velocity=random.randint(70, 100), pitch=melody_pitch,
                                     start=start_time, end=end_time)
        oboe.notes.append(oboe_note)

        previous_end = end_time

    # 오보에 트랙을 새 MIDI에 추가
    ensemble_midi = pretty_midi.PrettyMIDI()
    ensemble_midi.instruments.append(oboe)
    ensemble_midi.write(oboe_midi_output_path)
    print(f'Oboe accompaniment MIDI saved to {oboe_midi_output_path}')

# 사용자 선택에 따라 병합할 WAV 파일 선택 및 병합 실행
def merge_selected_wavs(selected_wav_paths, output_file, background_volume_db=-25, volume_db=0):
    # 여러 WAV 파일을 병합하고 볼륨을 조정하는 함수
    combined = AudioSegment.from_wav(selected_wav_paths[0]).apply_gain(background_volume_db)
    for wav_file in selected_wav_paths[1:]:
        next_wav = AudioSegment.from_wav(wav_file).apply_gain(volume_db)
        combined = combined.overlay(next_wav)
    combined.export(output_file, format="wav")
    print(f'Merged WAV saved to {output_file}')

# 파일 경로 설정
sogo_audio_path = 'static/uploads/recorded_audio_clean.wav'  # 소고 오디오 파일 경로
sogo_midi_path = 'static/uploads/sogo_rhythm.mid'  # 소고 리듬 MIDI 출력 경로
guitar_midi_path = 'static/uploads/guitar_accompaniment.mid'  # 기타 반주 MIDI 출력 경로
guitar_wav_path = 'static/uploads/guitar_accompaniment.wav'  # 기타 반주 WAV 출력 경로
violin_midi_path = 'static/uploads/violin_accompaniment.mid'  # 바이올린 반주 MIDI 출력 경로
violin_wav_path = 'static/uploads/violin_accompaniment.wav'  # 바이올린 반주 WAV 출력 경로
drum_midi_path = 'static/uploads/drum_accompaniment.mid'  # 드럼 반주 MIDI 출력 경로
drum_wav_path = 'static/uploads/drum_accompaniment.wav'  # 드럼 반주 WAV 출력 경로
pad_midi_path = 'static/uploads/pad_accompaniment.mid'  # 패드 반주 MIDI 출력 경로
pad_wav_path = 'static/uploads/pad_accompaniment.wav'  # 패드 반주 WAV 출력 경로
cello_midi_path = 'static/uploads/cello_accompaniment.mid'  # 첼로 반주 MIDI 출력 경로
cello_wav_path = 'static/uploads/cello_accompaniment.wav'  # 첼로 반주 WAV 출력 경로
flute_midi_path = 'static/uploads/flute_accompaniment.mid'  # 플루트 반주 MIDI 출력 경로
flute_wav_path = 'static/uploads/flute_accompaniment.wav'  # 플루트 반주 WAV 출력 경로
soundfont_path = 'static/uploads/GeneralUser-GS.sf2'  # 기타 및 바이올린 음색을 위한 SoundFont 파일 경로
final_output = 'static/uploads/final_output.wav'  # 최종 병합된 WAV 파일 경로

guitar_midi_path = 'static/uploads/guitar_accompaniment.mid'  # 기타 반주 MIDI 출력 경로
guitar_wav_path = 'static/uploads/guitar_accompaniment.wav'  # 기타 반주 WAV 출력 경로
violin_midi_path = 'static/uploads/violin_accompaniment.mid'  # 바이올린 반주 MIDI 출력 경로
violin_wav_path = 'static/uploads/violin_accompaniment.wav'  # 바이올린 반주 WAV 출력 경로
drum_midi_path = 'static/uploads/drum_accompaniment.mid'  # 드럼 반주 MIDI 출력 경로
drum_wav_path = 'static/uploads/drum_accompaniment.wav'  # 드럼 반주 WAV 출력 경로
pad_midi_path = 'static/uploads/pad_accompaniment.mid'  # 패드 반주 MIDI 출력 경로
pad_wav_path = 'static/uploads/pad_accompaniment.wav'  # 패드 반주 WAV 출력 경로
cello_midi_path = 'static/uploads/cello_accompaniment.mid'  # 첼로 반주 MIDI 출력 경로
cello_wav_path = 'static/uploads/cello_accompaniment.wav'  # 첼로 반주 WAV 출력 경로
flute_midi_path = 'static/uploads/flute_accompaniment.mid'  # 플루트 반주 MIDI 출력 경로
flute_wav_path = 'static/uploads/flute_accompaniment.wav'  # 플루트 반주 WAV 출력 경로
oboe_midi_path = 'static/uploads/oboe_accompaniment.mid'  # 오보에 반주 MIDI 출력 경로
oboe_wav_path = 'static/uploads/oboe_accompaniment.wav'  # 오보에 반주 WAV 출력 경로
soundfont_path = 'static/uploads/GeneralUser-GS.sf2'  # 기타 및 바이올린 음색을 위한 SoundFont 파일 경로
final_output = 'static/uploads/final_output.wav'  # 최종 병합된 WAV 파일 경로

if __name__ == "__main__":
    # 전체 실행
    convert_sogo_to_midi(sogo_audio_path, sogo_midi_path)
    generate_guitar_midi(sogo_midi_path, guitar_midi_path)
    render_midi_to_wav(guitar_midi_path, guitar_wav_path, soundfont_path)
    generate_violin_midi(sogo_midi_path, violin_midi_path)
    render_midi_to_wav(violin_midi_path, violin_wav_path, soundfont_path)
    generate_drum_midi(sogo_midi_path, drum_midi_path)
    render_midi_to_wav(drum_midi_path, drum_wav_path, soundfont_path)
    generate_pad_midi(sogo_midi_path, pad_midi_path)
    render_midi_to_wav(pad_midi_path, pad_wav_path, soundfont_path)
    generate_cello_midi(sogo_midi_path, cello_midi_path)
    render_midi_to_wav(cello_midi_path, cello_wav_path, soundfont_path)
    generate_flute_midi(sogo_midi_path, flute_midi_path)
    render_midi_to_wav(flute_midi_path, flute_wav_path, soundfont_path)
    generate_oboe_midi(sogo_midi_path, oboe_midi_path)
    render_midi_to_wav(oboe_midi_path, oboe_wav_path, soundfont_path)



    # 사용자에게 추천 목록 제공
    print("추천 병합 목록:")
    print("1: 소고 + 기타 + 첼로 + 플루트")
    print("2: 소고 + 드럼 + 패드 + 오보에")
    print("3: 소고 + 바이올린 + 첼로 + 기타")
    print("4: 소고 + 드럼 + 기타 + 패드 + 플루트")
    print("5: 소고 + 첼로 + 플루트 + 오보에")

    # 사용자 선택 받기
    user_choice = random.randint(1,5)#int(input("추천 조합 번호를 선택해주세요 (1-5): "))

    # 추천 조합에 따라 선택된 파일 설정
    recommended_combinations = {
        1: [sogo_audio_path, guitar_wav_path, cello_wav_path, flute_wav_path],
        2: [sogo_audio_path, drum_wav_path, pad_wav_path, oboe_wav_path],
        3: [sogo_audio_path, violin_wav_path, cello_wav_path, guitar_wav_path],
        4: [sogo_audio_path, drum_wav_path, guitar_wav_path, pad_wav_path, flute_wav_path],
        5: [sogo_audio_path, cello_wav_path, flute_wav_path, oboe_wav_path]
    }



    # 선택한 파일들로 병합 수행
    selected_wav_paths = recommended_combinations.get(user_choice, [])
    if selected_wav_paths:
        merge_selected_wavs(selected_wav_paths, final_output, background_volume_db=0, volume_db=0)
    else:
        print("올바른 번호를 선택하지 않았습니다. 프로그램을 종료합니다.")
