# Zybo 7020 petalinux

## Goal : Zynq SoC 기반 조난자 탐색 및 구출 UAV 미션 컴퓨터 개발

본 프로젝트는 Zynq SoC를 활용하여 조난자 탐색 및 구출 임무를 수행하는 무인 항공기(UAV)용 미션 컴퓨터를 개발하는 것을 목표로 합니다. 주요 개발 내용은 다음과 같습니다.

- MIPI CSI-2 인터페이스 카메라 입력
- YOLO 기반 객체 인식
- 영상 압축 및 전송
- (Optical) 제어기 행렬 연산 가속

### 구현 사항
1. (PL) CSI Interface로 영상 입력
2. (PL) YOLO
3. (PL) Side Video compression (ex. H.254, H.265, VP9, **AV1**)
4. (PS) USB Wi-Fi 동글을 통한 영상 전송
5. (PL, Optical) 제어기 행렬 연산 가속

## 프로젝트 구조

```bash
├─hw                # vivado
├─petalinux_build   # petalinux
│  └─petalinux      # petalinux hw에 관한 파일
└─yolo              # yolo on petalinux
```

## Setting & installation

### SW
- Ubuntu 20.04 LTS
- Petalinux 24.02
- Vivado 24.02
- yolov5
- tera term
  
### HW
- zybo z7-20
- Pcam5c camera
- micro SD 카드 (FAT32, 128GB 미만 권장)
- USB port
- HDMI (모니터 송출 테스트 시에만 필요)
  
## Steps

1. vivado에서 hardware export (.xsa파일)
   -> digilent pcam5c demo 홈페이지 실습 <https://digilent.com/reference/programmable-logic/zybo-z7/demos/pcam-5c>
2. petalinux 설치 및 패키지 생성
3. .xsa 파일 하드웨어 연동
4. petalinux build
5. sd카드에 아래 4가지 파일 복사
  - BOOT.BIN
  - image.ub
6. zybo 보드에 SD Card로 부팅
7. tera term 환경에서 pytorch를 사용할 수 없으므로, 우분투에서 yolov5n.pt 파일을 .onnx 파일로 변환 후 복사(이더넷 문제로 그냥 sd카드로 복사..)
8. 딥러닝을 위한 환경 설정 (현재 이 단계 진행 중)

## 참고 래퍼런스

- vivado 파일은 digilent 홈페이지에 올라와있는 pcam5c demo 파일을 그대로 사용했습니다.

   <https://digilent.com/reference/programmable-logic/zybo-z7/demos/pcam-5c>

- yolov5 모델은 아래 깃허브에서 사용했습니다.

   <https://github.com/ultralytics/yolov5>
