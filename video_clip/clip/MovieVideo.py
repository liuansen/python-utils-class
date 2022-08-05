# -*- coding: utf-8 -*-
"""
@Time    : 2022/8/5 15:55
@Author  : Anson
@File    : MovieVideo.py
"""
from moviepy.editor import *
from moviepy.video.compositing import transitions


# 图片转场效果
CROSSFADEIN = transitions.crossfadein  # 渐进
CROSSFADEOUT = transitions.crossfadeout  # 渐消


class MovieVideo(object):
    """封装视频处理方法"""
    def __init__(self, video_path='', image_list_path='', save_path='', video_save_name='',
                 transition_second=1.0):
        """
        video_path: 视频地址
        image_list_path： 要生成视频的图片地址
        save_path： 生成视频的保存地址
        video_save_name： 保存的视频名称
        transition_second: 图片转场秒数
        """
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
            print(item)
            if item.endswith('.png') or item.endswith('.jpg') or item.endswith('.jpeg'):
                photo_path = self.image_list_path + '{}'.format(item)
                clips1 = ImageClip(photo_path).set_duration(self.transition_second).fx(CROSSFADEIN, 1)
                clips_list.append(clips1)
        if clips_list:
            video_clip = concatenate_videoclips(clips_list, method="compose")
            video_clip.write_videofile(self.save_path+self.video_save_name, fps=24, remove_temp=True)
            return True
        else:
            return False

    def add_audio(self):
        """
        添加音频
        """

    def run(self):
        print(self.image_to_video())
        pass


if __name__ == '__main__':
    MovieVideo(
        image_list_path='E:/anson/image/LeBron', save_path='E:/anson/data/video',
        video_save_name='test.mp4', transition_second=2.0).run()
