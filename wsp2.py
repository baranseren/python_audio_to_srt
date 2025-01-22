import whisper
import os

def seconds_to_srt_timestamp(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

def generate_srt(audio_path, output_srt_path, language=None):
    model = whisper.load_model("base")
    # language parametresi None ise otomatik algıla, 'tr' ise Türkçe olarak çalış
    if language:
        result = model.transcribe(audio_path, language=language)
    else:
        result = model.transcribe(audio_path)
        
    segments = result["segments"]

    with open(output_srt_path, "w", encoding="utf-8") as srt_file:
        for i, seg in enumerate(segments, start=1):
            start = seconds_to_srt_timestamp(seg["start"])
            end = seconds_to_srt_timestamp(seg["end"])
            text = seg["text"].strip()
            srt_file.write(f"{i}\n{start} --> {end}\n{text}\n\n")

if __name__ == "__main__":
    # Mutlak yol (absolute path) kullanarak örnek veriyoruz
    audio_path = r"C:\Users\baranseren\Desktop\python_whisper\ses_klasoru\Allah.mp3"
    output_srt_path = r"C:\Users\baranseren\Desktop\python_whisper\cikti.srt"
    
    # Türkçe (tr) parametresini vererek çağırabilirsiniz; 
    # Dilerseniz None verip otomatik algılamayı kullanabilirsiniz.
    generate_srt(audio_path, output_srt_path, language="tr")
    print("SRT dosyası oluşturuldu.")
