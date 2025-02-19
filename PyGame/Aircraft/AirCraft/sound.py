# 定义声音类Sound， 控制音乐与音效的播放
import pygame


class Sound:
    def __init__(self):
        # background
        pygame.mixer.music.load("res/sound/game_music.wav")
        self.music = pygame.mixer.music

        # sound effect
        self.sounds = {}

        sounds_name = ["bullet", "enemy1_down", "enemy2_down", "enemy3_down", "game_over"]

        for sound in sounds_name:
            self.sounds[sound] = pygame.mixer.Sound(sound.join(["res/sound]", ".wav"]))

    def play(self, name):
        if name == "bg":
            self.music.play(-1)
        else:
            self.sounds[name].play()

    def pause(self, name):
        if name == "bg":
            self.music.pause()

    def unpause(self, name):
        if name == "bg":
            self.music.unpause()

    def fadeout(self, name):
        if name == "bg":
            self.music.fadeout(1000)
