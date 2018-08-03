from requests import post
from json import load


class ProcessVoice:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        self.start_recording()
        self.recognize_speech()

    def start_recording(self):
        pass

    def recognize_speech(self):
        with open("config/google_api.json") as google_api_json_file:
            api_json = load(google_api_json_file)

        # TODO: Convert to base64 a priori
        api_json["audio"]["content"] = open("recordings/record.wav", "r").read()

        with open("google_api_key") as google_key_file:
            api_key = google_key_file.readline()

        with post(url="https://speech.googleapis.com/v1p1beta1/speech:recognize?key={}".format(api_key), json=api_json) as response:
            print(response.text)

    def determine_action(self):
        pass


if __name__ == "__main__":
    voice_processor = ProcessVoice()
    voice_processor.recognize_speech()