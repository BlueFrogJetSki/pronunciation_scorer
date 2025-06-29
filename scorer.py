import Levenshtein, pronouncing, speech_recognition as sr
def phones(w):  # ARPAbet phones for a word
    lst = pronouncing.phones_for_word(w.lower())
    return lst[0].split() if lst else []


def calculate_score(expected, target):
    dist = Levenshtein.distance(expected, target)
    return max(0, 1 - dist / max(len(expected), 1))


def score(audio_path, target):
    recog, twords = sr.Recognizer(), target.lower().split()
    with sr.AudioFile(audio_path) as src:
        transcript = recog.recognize_google(recog.record(src)).lower()

    ph_tr = sum(map(phones, transcript.split()), [])
    ph_tgt = sum(map(phones, twords), [])
    print(ph_tr)
    print(ph_tgt)
    return calculate_score("".join(ph_tgt), "".join(ph_tr)), transcript
