from pathlib import Path

class FrameInfo(object):
    def __init__(self, filepath=None, landmarks_list=None, alpha_images_list=None):
        self.filepath = filepath
        self.landmarks_list = landmarks_list or []
        self.alpha_images_list = alpha_images_list or []
        self.motion_deg = 0
        self.motion_power = 0