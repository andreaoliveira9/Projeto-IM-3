import json
import xml.etree.ElementTree as ET
import ssl
import websockets
from enums import Type
import time

from utils import *
from youtube_music import YoutubeMusic
from tts import TTS

HOST = "127.0.0.1"
not_quit = True
intent_not_undestand_well_voice = None
gesture_confirmation = None


def process_message(message):
    if message == "OK":
        return message, Type.OK

    commands = ET.fromstring(message).findall(".//command")
    json_command = commands.pop(0).text
    command = json.loads(json_command)
    modality = command["recognized"][0]

    if modality == "SPEECH":
        return json.loads(command["nlu"]), Type.SPEECH
    elif modality == "GESTURES":
        return command["recognized"][1], Type.GESTURE
    elif modality == "FUSION":
        return (command["recognized"][1:], commands), Type.FUSION


async def message_handler(youtube_music: YoutubeMusic, message: str):
    message, typ = process_message(message)

    """ typ = Type.GESTURE
    message = "SEARCHMUSIC" """
    # typ = Type.FUSION
    # message = "LLM"
    if typ == Type.SPEECH:
        speech_control(youtube_music, message)
    elif typ == Type.GESTURE:
        gesture_control(youtube_music, message)
    elif typ == Type.FUSION:
        fusion_control(youtube_music, message)

    elif typ == Type.OK:
        return

    """ time.sleep(3)
    for i in range(3):
        typ = Type.GESTURE
        message = "TESTEDOWN"
        if typ == Type.SPEECH:
            speech_control(youtube_music, message)
        elif typ == Type.GESTURE:
            gesture_control(youtube_music, message)
        elif typ == Type.OK:
            return
        time.sleep(1)

    for i in range(2):
        typ = Type.GESTURE
        message = "TESTEUP"
        if typ == Type.SPEECH:
            speech_control(youtube_music, message)
        elif typ == Type.GESTURE:
            gesture_control(youtube_music, message)
        elif typ == Type.OK:
            return
        time.sleep(1)
    
    typ = Type.GESTURE
    message = "PUSH"
    if typ == Type.SPEECH:
        speech_control(youtube_music, message)
    elif typ == Type.GESTURE:
        gesture_control(youtube_music, message)
    elif typ == Type.OK:
        return
    time.sleep(2) """
    """ time.sleep(3)


    for i in range(2):
        typ = Type.GESTURE
        message = "MOVERIGHTCATEGORY"
        if typ == Type.SPEECH:
            speech_control(youtube_music, message)
        elif typ == Type.GESTURE:
            gesture_control(youtube_music, message)
        elif typ == Type.OK:
            return
        time.sleep(2)

    for i in range(1):
        typ = Type.GESTURE
        message = "MOVELEFTCATEGORY"
        if typ == Type.SPEECH:
            speech_control(youtube_music, message)
        elif typ == Type.GESTURE:
            gesture_control(youtube_music, message)
        elif typ == Type.OK:
            return
        time.sleep(1)

    for i in range(1):
        typ = Type.GESTURE
        message = "SCROLLDOWNCATEGORY"
        if typ == Type.SPEECH:
            speech_control(youtube_music, message)
        elif typ == Type.GESTURE:
            gesture_control(youtube_music, message)
        elif typ == Type.OK:
            return
        time.sleep(2)


    for i in range(2):
        typ = Type.GESTURE
        message = "MOVEDOWNCATEGORY"
        if typ == Type.SPEECH:
            speech_control(youtube_music, message)
        elif typ == Type.GESTURE:
            gesture_control(youtube_music, message)
        elif typ == Type.OK:
            return
        time.sleep(1)

    for i in range(2):
        typ = Type.GESTURE
        message = "MOVERIGHTCATEGORY"
        if typ == Type.SPEECH:
            speech_control(youtube_music, message)
        elif typ == Type.GESTURE:
            gesture_control(youtube_music, message)
        elif typ == Type.OK:
            return
        time.sleep(2)

    for i in range(1):
        typ = Type.GESTURE
        message = "MOVEUPCATEGORY"
        if typ == Type.SPEECH:
            speech_control(youtube_music, message)
        elif typ == Type.GESTURE:
            gesture_control(youtube_music, message)
        elif typ == Type.OK:
            return
        time.sleep(1)

    for i in range(1):
        typ = Type.GESTURE
        message = "SCROLLDOWNCATEGORY"
        if typ == Type.SPEECH:
            speech_control(youtube_music, message)
        elif typ == Type.GESTURE:
            gesture_control(youtube_music, message)
        elif typ == Type.OK:
            return
        time.sleep(2)

    for i in range(2):
        typ = Type.GESTURE
        message = "MOVEDOWNCATEGORY"
        if typ == Type.SPEECH:
            speech_control(youtube_music, message)
        elif typ == Type.GESTURE:
            gesture_control(youtube_music, message)
        elif typ == Type.OK:
            return
        time.sleep(1)

    for i in range(2):
        typ = Type.GESTURE
        message = "MOVERIGHTCATEGORY"
        if typ == Type.SPEECH:
            speech_control(youtube_music, message)
        elif typ == Type.GESTURE:
            gesture_control(youtube_music, message)
        elif typ == Type.OK:
            return
        time.sleep(2)

    for i in range(1):
        typ = Type.GESTURE
        message = "MOVEUPCATEGORY"
        if typ == Type.SPEECH:
            speech_control(youtube_music, message)
        elif typ == Type.GESTURE:
            gesture_control(youtube_music, message)
        elif typ == Type.OK:
            return
        time.sleep(1)    

    for i in range(1):
        typ = Type.GESTURE
        message = "SELECTPAUSE"
        if typ == Type.SPEECH:
            speech_control(youtube_music, message)
        elif typ == Type.GESTURE:
            gesture_control(youtube_music, message)
        elif typ == Type.OK:
            return

        time.sleep(1) """


def speech_control(youtube_music, message):
    global intent_not_undestand_well_voice
    print(f"Speech received: {message}")

    intent = message["intent"]["name"]
    confidence = message["intent"]["confidence"]
    entities = message.get("entities", [])

    if intent == "confirm_action" and confidence > 0.7:
        if intent_not_undestand_well_voice:
            action = next(
                (e["value"] for e in entities if e["entity"] == "action"), None
            )
            if action == "comfirm":
                intent = intent_not_undestand_well_voice.intent
                entities = intent_not_undestand_well_voice.entities
                youtube_music.sendoToTTS("Ok, vou fazer o que pediste.")
            elif action == "cancel":
                youtube_music.sendoToTTS("Ok, não vou fazer nada.")
            else:
                youtube_music.sendoToTTS("Não entendi o que disseste.")
                return
        else:
            youtube_music.sendoToTTS(random_not_understand())
            return

        intent_not_undestand_well_voice = None
        return

    if confidence <= 0.45:
        youtube_music.sendoToTTS(random_not_understand())
        return
    elif confidence > 0.45 and confidence < 0.8:
        intent_not_undestand_well_voice = IntentNotUnderstoodWellVoice(intent, entities)
        youtube_music.sendoToTTS(intent_not_undestand_well_voice.confirmation())
        return

    if intent == "control_music":  # DONE
        # Pausar ou continuar
        action = next((e["value"] for e in entities if e["entity"] == "action"), None)
        if action == "pause":
            youtube_music.pause()
        elif action == "resume":
            youtube_music.resume()
        else:
            youtube_music.sendoToTTS(
                "Não percebi se queres pausar ou continuar a música."
            )

    elif intent == "change_track":  # DONE
        # Mudar para próxima ou anterior
        direction = next(
            (e["value"] for e in entities if e["entity"] == "direction"), None
        )
        if direction == "next":
            youtube_music.next_song()
        elif direction == "previous":
            youtube_music.previous_song()
        elif direction == "same":
            youtube_music.repeat_song()
        else:
            youtube_music.sendoToTTS(
                "Não percebi se queres passar para a póxima música, ir para a anterior ou repetir esta música."
            )

    elif intent == "adjust_volume":  # DONE
        action = next((e["value"] for e in entities if e["entity"] == "action"), None)
        if action == "increase":
            youtube_music.increase_volume_generic(10)
        elif action == "decrease":
            youtube_music.decrease_volume_generic(30)
        elif action == "mute":
            youtube_music.mute()
        elif action == "unmute":
            youtube_music.unmute()
        else:
            youtube_music.sendoToTTS(
                "Não percebi de queres aumentar, diminuir, desloigar ou ligar o som."
            )

    elif intent == "set_mode":  # DONE
        mode = next((e["value"] for e in entities if e["entity"] == "mode"), None)
        if mode == "shuffle_on":
            youtube_music.shuffle_on()
        elif mode == "shuffle_off":
            youtube_music.shuffle_off()
        elif mode == "repeat_one":
            youtube_music.repeat_one()
        elif mode == "repeat_all":
            youtube_music.repeat_all()
        elif mode == "repeat_off":
            youtube_music.repeat_off()
        else:
            youtube_music.sendoToTTS("Não percebi qual o modo queres colocar.")

    elif intent == "add_to_favorites":  # DONE
        youtube_music.like_music()

    elif intent == "search_music":  # DONE
        song = next((e["value"] for e in entities if e["entity"] == "song"), None)
        artist = next((e["value"] for e in entities if e["entity"] == "artist"), None)

        if song and artist:
            youtube_music.search_music_list(song, artist)
            # youtube_music.play_music_searched()
        else:
            if not song and not artist:
                youtube_music.sendoToTTS("Não percebi o nome nem o artista.")
            elif not song:
                youtube_music.sendoToTTS("Não percebi o nome da música.")
            elif not artist:
                youtube_music.sendoToTTS("Não percebi o nome do artista.")

    elif intent == "add_music_to_queue":  # DONE
        song = next((e["value"] for e in entities if e["entity"] == "song"), None)
        artist = next((e["value"] for e in entities if e["entity"] == "artist"), None)

        if song and artist:
            youtube_music.search_music(song, artist)
            youtube_music.add_to_queue()
        else:
            if not song and not artist:
                youtube_music.sendoToTTS("Não percebi o nome nem o artista.")
            elif not song:
                youtube_music.sendoToTTS("Não percebi o nome da música.")
            elif not artist:
                youtube_music.sendoToTTS("Não percebi o nome do artista.")

    elif intent == "wich_music_is_playing":  # DONE
        youtube_music.get_current_music()

    elif intent == "play_playlist":  # DONE
        playlist = next(
            (e["value"] for e in entities if e["entity"] == "playlist"), None
        )

        if playlist:
            youtube_music.play_playlist(playlist)
        else:
            youtube_music.sendoToTTS("Não percebi o nome da playlist.")

    elif intent == "add_music_to_playlist_search":  # DONE
        song = next((e["value"] for e in entities if e["entity"] == "song"), None)
        artist = next((e["value"] for e in entities if e["entity"] == "artist"), None)
        playlist = next(
            (e["value"] for e in entities if e["entity"] == "playlist"), None
        )

        if song and artist and playlist:
            youtube_music.search_music(song, artist)
            youtube_music.add_music_to_playlist_search(playlist)
        else:
            if not song and not artist and not playlist:
                youtube_music.sendoToTTS(
                    "Não percebi o nome da música, do artista e da playlist."
                )
            elif not song and not artist:
                youtube_music.sendoToTTS("Não percebi o nome da música e do artista.")
            elif not song and not playlist:
                youtube_music.sendoToTTS("Não percebi o nome da música e da playlist.")
            elif not artist and not playlist:
                youtube_music.sendoToTTS("Não percebi o nome do artista e da playlist.")
            elif not song:
                youtube_music.sendoToTTS("Não percebi o nome da música.")
            elif not artist:
                youtube_music.sendoToTTS("Não percebi o nome do artista.")
            elif not playlist:
                youtube_music.sendoToTTS("Não percebi o nome da playlist.")

    elif intent == "help":  # DONE
        option = next(
            (e["value"] for e in entities if e["entity"] == "help_option"), None
        )

        if option:
            youtube_music.help(option)
        else:
            youtube_music.help(None)

    elif intent == "goodbye":  # DONE
        youtube_music.sendoToTTS(random_goodbye())
        youtube_music.close()
        global not_quit
        not_quit = False

    else:
        youtube_music.sendoToTTS(random_not_understand())


def gesture_control(youtube_music, message):
    global gesture_confirmation
    from youtube_music import LAST_ACTION

    print(f"Gesture received: {message}")

    is_exploring = (
        LAST_ACTION == "scroll_up_categories"
        or LAST_ACTION == "scroll_down_categories"
        or LAST_ACTION == "move_down_category"
        or LAST_ACTION == "move_left_category"
        or LAST_ACTION == "move_right_category"
        or LAST_ACTION == "move_up_category"
        or LAST_ACTION == "open_explore"
        or LAST_ACTION == "move_down_music_list"
        or LAST_ACTION == "move_up_music_list"
        or LAST_ACTION == "search_music_list"
    )

    can_resume = youtube_music.paused and youtube_music.music_playing

    if gesture_confirmation and message != gesture_confirmation:
        gesture_confirmation = None

    if message == "ARMSX":  # Acenar com a mão para sair
        global not_quit
        if gesture_confirmation == "ARMSX":
            not_quit = False
            youtube_music.sendoToTTS("Até à próxima!")
        else:
            gesture_confirmation = "ARMSX"
            youtube_music.sendoToTTS("Tens a certeza que queres sair?")
    elif message == "MOUTHHAND":  # Fazer gesto de shiu na boca
        youtube_music.mute()
    elif message == "EARHAND":  # Apontar para a boca
        youtube_music.unmute()
    elif message == "SCRATCHHEAD":  # Abrir mãos como se fosse um livro
        youtube_music.open_explore()
    elif message == "MOVEUPL":  # Mão em pinça para baixo
        youtube_music.scroll_up_categories()
    elif message == "MOVEDOWNL":  # Mão em pinça para cima
        youtube_music.scroll_down_categories()
    elif message == "MOVEUPR":  # Apontar para cima
        youtube_music.move_up_music_list()
    elif message == "MOVEDOWNR":  # Apontar para baixo
        youtube_music.move_down_music_list()
    elif message == "MOVELEFT":
        if is_exploring:
            youtube_music.move_left_category()
        else:
            youtube_music.previous_song()
    elif message == "MOVERIGHT":
        if is_exploring:
            youtube_music.move_right_category()
        else:
            youtube_music.next_song()
    elif message == "RANDOMMUSIC":  # Fazer gesto de shaka
        youtube_music.play_music_by_link()
    elif message == "PUSH":  # Mão aberta e movert para a frente
        if is_exploring:
            youtube_music.select_something_category()
        elif can_resume:
            youtube_music.resume()
        else:
            youtube_music.pause()
    elif message == "SEARCHMUSIC":
        youtube_music.search_music_list("crescer vai dar tempo fado")
    elif message == "TESTEDOWN":
        youtube_music.move_down_music_list()
    elif message == "TESTEUP":
        youtube_music.move_up_music_list()


def fusion_control(youtube_music, message):
    print(f"Fusion received: {message}")
    command = message[0][0]

    if command == "QUIT":
        global not_quit
        not_quit = False
        youtube_music.sendoToTTS("Até à próxima!")
    elif command == "HELP":
        youtube_music.help(message[0][1])
    elif command == "MOVEUP_RIGHT":
        youtube_music.move_up_music_list()
    elif command == "MOVEDOWN_RIGHT":
        youtube_music.move_down_music_list()
    elif command == "SELECT":
        youtube_music.select_something_category()
    elif command == "VOLUME_DOWN":
        youtube_music.decrease_volume_generic(30)
    elif command == "VOLUME_UP":
        for c in message[1]:
            command = json.loads(c.text)
            if command["recognized"][0] == "SPEECH":
                nlu = json.loads(command["nlu"])
                for entity in nlu["entities"]:
                    if entity["entity"] == "value":
                        youtube_music.increase_volume_generic(int(entity["value"]))
    elif command == "PAUSE":
        youtube_music.pause()
    elif command == "PLAY":
        youtube_music.resume()


async def main():
    tts = TTS(FusionAdd=f"https://{HOST}:8000/IM/USER1/APPSPEECH").sendToVoice
    youtube_music = YoutubeMusic(
        TTS=tts
    )  # Crie uma classe MusicPlayer para controlar a reprodução de músicas
    mmi_cli_out_add = f"wss://{HOST}:8005/IM/USER1/APP"

    # SSL config
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    # Connect to websocket
    async with websockets.connect(mmi_cli_out_add, ssl=ssl_context) as websocket:
        print("Connected to MMI CLI OUT")

        while not_quit:
            try:
                msg = await websocket.recv()
                await message_handler(youtube_music=youtube_music, message=msg)
            except Exception as e:
                tts("Ocorreu um erro, a fechar o aplicativo")
                print(f"Error: {e}")
                break

        youtube_music.close()
        exit(0)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
