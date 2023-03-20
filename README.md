# YOLO_object_detection

```
│  README.md
│  requirements.txt
├─models
│      best.pt
├─results
|
├─sample_video_data
│      sample4.mp4
├─test
│      test.py
│      train_process.ipynb
└─utils
        __init__.py
        detection.py
        utils.py
```

- **model** : object detection에 사용될 모델의 가중치 파일(best.pt)가 저장된 디렉토리입니다.  
- **sample_video_data** : object detection의 입력값으로 사용할 샘플 영상 파일들이 저장된 디렉토리입니다.  
- **result** : object detection의 결과 영상들이 저장된 디렉토리입니다.  
- **test** : object detection의 예시가 구현되어 있는 코드(test.py)와,  
전처리 및 훈련 과정이 기록된 노트북(train_process.ipynb)이 저장된 디렉토리입니다.  
- **utils** : detection이 구현된 코드(detection.py)와, helper function이 정의된 코드(utils.py)가 저장된 디렉토리입니다.
  
  
  
### 다음은 test.py에서 object detection 실행의 예시입니다.
```python
import sys
sys.path.append('./utils')
import detection
import torch

# 설정 파라미터
model_path = './models/best.pt'                # 모델 경로
input_video = 'sample_video_data\sample1.mp4'  # 디텍션을 수행할 비디오 경로
output_video = './results/sample1_result.mp4'  # 디텍션 결과를 저장할 경로

# 모델 임포팅
model = torch.hub.load('ultralytics/yolov5', 'custom', model_path)

#디텍션 수행, 결과는 output_video로 저장됩니다
import sys
sys.path.append('./utils')
import detection
import torch
import torchvision

# 설정 파라미터
model_path = './models/best.pt'                # 모델 경로
input_video = './sample_video_data/sample1.mp4'  # 디텍션을 수행할 비디오 경로
output_video = './results/sample1_result.mp4'  # 디텍션 결과를 저장할 경로

# 모델 임포팅
model = torch.hub.load('ultralytics/yolov5', 'custom', model_path)

#디텍션 수행, 결과는 output_video로 저장됩니다
detection.detection(model = model,
                    input_video = input_video,
                    output_video = output_video)
```
