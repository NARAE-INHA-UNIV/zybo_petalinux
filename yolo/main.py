#!/usr/bin/env python3
"""
Zybo Z7‑20 + Pcam 5C 실시간 사람 탐지 데모
1) 모델: yolov5n.pt  (default)   2) 입력: V4L2 카메라
"""

import cv2
import torch
import argparse
from pathlib import Path
import time

def get_args():
    p = argparse.ArgumentParser()
    p.add_argument('--model',  default='yolov5n.pt', help='weight file')
    p.add_argument('--imgsz',  type=int, default=320, help='square inference size')
    p.add_argument('--source', default='/dev/video0', help='camera or video file')
    p.add_argument('--view',   action='store_true', help='show HDMI window')
    p.add_argument('--save',   default='', help='folder to save annotated frames')
    return p.parse_args()

def main(opt):
    print('[INFO] load model…')
    model = torch.hub.load('ultralytics/yolov5', 'custom',
                           path=opt.model, device='cpu')
    model.conf = 0.4         # confidence threshold
    model.classes = [0]      # 0 = person

    print(f'[INFO] open camera {opt.source}')
    cap = cv2.VideoCapture(opt.source, cv2.CAP_V4L2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,  opt.imgsz)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, opt.imgsz)
    if not cap.isOpened():
        raise RuntimeError(f'cannot open {opt.source}')

    if opt.save:
        Path(opt.save).mkdir(parents=True, exist_ok=True)

    n, t0 = 0, time.time()
    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                print('[WARN] no frame'); break
            res = model(frame, size=opt.imgsz)
            show = res.render()[0]        # BGR ndarray
            if opt.view:
                cv2.imshow('YOLOv5', show)
                if cv2.waitKey(1) & 0xFF == 27:  # ESC
                    break
            if opt.save:
                cv2.imwrite(f'{opt.save}/f{n:06d}.jpg', show)
            n += 1
    finally:
        cap.release(); cv2.destroyAllWindows()
        dt = time.time() - t0
        if dt:
            print(f'[INFO] avg FPS {n/dt:.2f}')

if __name__ == '__main__':
    main(get_args())
