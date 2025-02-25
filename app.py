from flask import Flask, request, jsonify, render_template
import os
from process_audio import reduce_noise
from g_midi import (
    convert_sogo_to_midi,
    generate_guitar_midi,
    render_midi_to_wav,
    generate_violin_midi,
    generate_drum_midi,
    generate_pad_midi,
    generate_cello_midi,
    generate_flute_midi,
    generate_oboe_midi,
    merge_selected_wavs
)

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], 'recorded_audio.wav')
    file.save(input_path)
    
    return jsonify({'message': 'File uploaded successfully', 'file_path': input_path}), 200


# 2. 노이즈 감소와 합주 생성 처리
@app.route('/process_audio', methods=['POST'])
def process_audio():
    # 클라이언트로부터 파일 경로 수신
    input_path = request.json.get('file_path')
    if not input_path:
        return jsonify({'error': 'No audio file path provided'}), 400

    # Step 1: 노이즈 감소
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'recorded_audio_clean.wav')
    reduce_noise(input_path, output_path)

    # Step 2: MIDI 변환 및 반주 생성
    sogo_midi_path = os.path.join(app.config['UPLOAD_FOLDER'], 'sogo_rhythm.mid')
    convert_sogo_to_midi(output_path, sogo_midi_path)

    # 반주 파일 생성
    paths = {
        "guitar": ("guitar_accompaniment", generate_guitar_midi),
        "violin": ("violin_accompaniment", generate_violin_midi),
        "drum": ("drum_accompaniment", generate_drum_midi),
        "pad": ("pad_accompaniment", generate_pad_midi),
        "cello": ("cello_accompaniment", generate_cello_midi),
        "flute": ("flute_accompaniment", generate_flute_midi),
        "oboe": ("oboe_accompaniment", generate_oboe_midi),
    }

    soundfont_path = os.path.join(app.config['UPLOAD_FOLDER'], 'GeneralUser-GS.sf2')
    wav_files = []

    for name, (base_filename, midi_function) in paths.items():
        midi_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{base_filename}.mid")
        wav_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{base_filename}.wav")
        midi_function(sogo_midi_path, midi_path)
        render_midi_to_wav(midi_path, wav_path, soundfont_path)
        wav_files.append(wav_path)

    # Step 4: 병합 수행
    final_output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'final_output.wav')
    merge_selected_wavs([output_path] + wav_files[:3], final_output_path)

    return jsonify({'message': 'Audio processing complete, ensemble generated.', 'ensemble_path': final_output_path}), 200

##############################

###
# 메인 페이지
@app.route('/')
def home():
    return render_template('kor/main.html') 

# 튜토리얼 페이지
@app.route('/tutorial')
def tutorial():
    return render_template('kor/tutorial.html')  

# 악기 소개 페이지
@app.route('/instrument')
def instrument():
    return render_template('kor/instrument.html')  

# 합주 시작 페이지
@app.route('/compose_start')
def compose_start():
    return render_template('kor/Compose_Start.html')  

# 합주 완료 페이지
@app.route('/compose_finish')
def compose_finish():
    return render_template('kor/Compose_Finish.html')  

# 에러 페이지
@app.route('/error')
def error():
    return render_template('kor/error.html')  


############### 중국어 ###############
# 메인 페이지
@app.route('/zh_main')
def zh_home():
    return render_template('chs/zh_main.html') 

# 튜토리얼 페이지
@app.route('/zh_tutorial')
def zh_tutorial():
    return render_template('chs/zh_tutorial.html')  

# 악기 소개 페이지
@app.route('/zh_instrument')
def zh_instrument():
    return render_template('chs/zh_instrument.html')  

# 합주 시작 페이지
@app.route('/zh_compose_start')
def zh_compose_start():
    return render_template('chs/zh_Compose_Start.html')  

# 합주 완료 페이지
@app.route('/zh_compose_finish')
def zh_compose_finish():
    return render_template('chs/zh_Compose_Finish.html')  

# 에러 페이지
@app.route('/zh_error')
def zh_error():
    return render_template('chs/zh_error.html')  
#####################################################


############### 영어 ###############
# 메인 페이지
@app.route('/en_main')
def en_home():
    return render_template('eng/en_main.html') 

# 튜토리얼 페이지
@app.route('/en_tutorial')
def en_tutorial():
    return render_template('eng/en_tutorial.html')  

# 악기 소개 페이지
@app.route('/en_instrument')
def en_instrument():
    return render_template('eng/en_instrument.html')  

# 합주 시작 페이지
@app.route('/en_compose_start')
def en_compose_start():
    return render_template('eng/en_Compose_Start.html')  

# 합주 완료 페이지
@app.route('/en_compose_finish')
def en_compose_finish():
    return render_template('eng/en_Compose_Finish.html')  

# 에러 페이지
@app.route('/en_error')
def en_error():
    return render_template('eng/en_error.html')  

# 구조도 페이지
@app.route('/en_service_structure')
def en_service_structure():
    return render_template('eng/en_service_structure.html')  
#####################################################


############### 일본어 ###############
# 메인 페이지
@app.route('/jpn')
def ja_home():
    return render_template('jpn/ja_main.html') 

# 튜토리얼 페이지
@app.route('/ja_tutorial')
def ja_tutorial():
    return render_template('jpn/ja_tutorial.html')  

# 악기 소개 페이지
@app.route('/ja_instrument')
def ja_instrument():
    return render_template('jpn/ja_instrument.html')  

# 합주 시작 페이지
@app.route('/ja_compose_start')
def ja_compose_start():
    return render_template('jpn/ja_Compose_Start.html')  

# 합주 완료 페이지
@app.route('/ja_compose_finish')
def ja_compose_finish():
    return render_template('jpn/ja_Compose_Finish.html')  

# 에러 페이지
@app.route('/ja_error')
def ja_error():
    return render_template('jpn/ja_error.html')  
#####################################################



# 404 에러 핸들러
@app.errorhandler(404)
def page_not_found(e):
    path = request.path
    if path.startswith('/zh'):
        return render_template('chs/zh_error.html'), 404
    elif path.startswith('/en'):
        return render_template('eng/en_error.html'), 404
    elif path.startswith('/ja'):
        return render_template('jpn/ja_error.html'), 404
    else:
        return render_template('kor/error.html'), 404


# 500 에러 핸들러
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('kor/error.html'), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 7000, debug=True)
# , debug=True
