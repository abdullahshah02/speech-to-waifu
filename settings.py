import os
from os.path import join, dirname
from dotenv import load_dotenv
from enum import Enum

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

VOICEVOX_PORT = os.environ.get("VOICEVOX_PORT")
DEEPL_API_KEY = os.environ.get("DEEPL_API_KEY")


class Speaker(Enum):
    # Shikoku Metan
    SHIKOKU_NORMAL = 2
    SHIKOKU_SWEET = 0
    SHIKOKU_TSUNTSUN = 6
    SHIKOKU_SEXY = 4
    SHIKOKU_WHISPER = 36
    SHIKOKU_WHISPERING = 37

    # Zundamon
    ZUNDAMON_NORMAL = 3
    ZUNDAMON_SWEET = 1
    ZUNDAMON_TSUNTSUN = 7
    ZUNDAMON_SEXY = 5
    ZUNDAMON_WHISPER = 22
    ZUNDAMON_WHISPERING = 38

    # Tsumugi Kasukabe
    TSUMUGI_NORMAL = 8

    # Amehare Hau
    AMEHARE_NORMAL = 10

    # Namion Ritsu
    NAMION_NORMAL = 9

    # Himari
    HIMARI_NORMAL = 14

    # Kyushu Sky
    KYUSHU_NORMAL = 16
    KYUSHU_SWEET = 15
    KYUSHU_TSUNTSUN = 18
    KYUSHU_SEXY = 17
    KYUSHU_WHISPER = 19

    # Mochiko
    MOCHIKO_NORMAL = 20

    # White CUL
    WHITE_NORMAL = 23
    WHITE_FUN = 24
    WHITE_SAD = 25
    WHITE_BIEN = 26

    # Goki
    GOKI_NORMAL = 27
    GOKU_PLUSH = 28

    # No. 7
    SEVEN_NORMAL = 29
    SEVEN_ANNOUNCEMENT = 30
    SEVEN_STORYTELLING = 31

    # Nurse Robo_Type T
    NURSE_NORMAL = 47
    NURSE_EASILY = 48
    NURSE_SCARY = 49
    NURSE_SECRET_STORY = 50
