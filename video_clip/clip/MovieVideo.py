# -*- coding: utf-8 -*-
"""
@Time    : 2022/8/5 15:55
@Author  : Anson
@File    : MovieVideo.py
"""
from pathlib import Path
from sys import path

from moviepy.editor import *
from moviepy.video.compositing import transitions


path.append(os.path.abspath('..'))
file_name = Path(__file__).stem
# 图片转场效果
CROSSFADEIN = transitions.crossfadein  # 渐进
CROSSFADEOUT = transitions.crossfadeout  # 渐消


class MovieVideo(object):
    """封装视频处理方法"""
    def __init__(self, video_path='', image_list_path='', save_path='', video_save_name='', audio_path='',
                 transition_second=1.0):
        """
        video_path: 视频地址
        image_list_path： 要生成视频的图片地址
        save_path： 生成视频的保存地址
        audio_path:  要给视频添加的音频地址
        video_save_name： 保存的视频名称
        transition_second: 图片转场秒数
        """
        self.audio_default = False  # 是否添加默认音乐
        if video_path:
            if video_path[-1] != '/':
                self.video_path = video_path + '/'
        else:
            self.video_path = video_path
        if image_list_path:
            if image_list_path[-1] != '/':
                self.image_list_path = image_list_path + '/'
        else:
            self.image_list_path = image_list_path
        if save_path:
            if save_path[-1] != '/':
                self.save_path = save_path + '/'
        else:
            self.save_path = save_path
        if audio_path:
            self.audio_path = audio_path
        else:
            self.audio_default = True
            if sys.platform == 'win32':
                self.audio_path = os.path.abspath(os.path.dirname(__file__)) + '\\intro.mp3'
            else:
                self.audio_path = os.path.abspath(os.path.dirname(__file__)) + '/intro.mp3'
        self.video_save_name = video_save_name
        self.transition_second = transition_second
        pass

    def image_to_video(self):
        """
        多张图片转视频
        """
        file_list = os.listdir(self.image_list_path)
        clips_list = []
        for item in file_list:
            if item.endswith('.png') or item.endswith('.jpg') or item.endswith('.jpeg'):
                photo_path = self.image_list_path + '{}'.format(item)
                clips1 = ImageClip(photo_path).set_duration(self.transition_second).fx(CROSSFADEIN, 1)
                clips_list.append(clips1)
        if clips_list:
            video_clip = concatenate_videoclips(clips_list, method="compose")
            video_clip.write_videofile(self.save_path+self.video_save_name, fps=24, remove_temp=True)
            if self.audio_default:
                self.add_audio()
            return True
        else:
            return False

    def add_audio(self):
        """
        添加音频
        """
        video = self.save_path + self.video_save_name
        video_clip = VideoFileClip(video)
        audio_clip = AudioFileClip(self.audio_path)
        final_clip = video_clip.set_audio(audio_clip)
        final_clip.write_videofile(self.save_path+'output.mp4', fps=60, remove_temp=True, codec="libx264")

    def run(self):
        print(self.image_to_video())
        pass


if __name__ == '__main__':
    MovieVideo(
        image_list_path='E:/anson/image/LeBron',
        save_path='E:/anson/data/video',
        video_save_name='test.mp4',
        # audio_path='E:/anson/data/music/Intro.mp3',
        transition_second=2.0).run()
