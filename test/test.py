from utils.detection import detection
import torch

# 설정 파라미터
model_path = r'models\best.pt'               # 모델 경로
input_video = 'data\sample1.mp4'             # 디텍션을 수행할 비디오 경로
output_video = 'results\sample1_result'      # 디텍션 결과를 저장할 경로

# 모델 임포팅
model = torch.hub.load('ultralytics/yolov5', 'custom', model_path)

# 디텍션 수행, 결과는 output_video로 저장됩니다
detection(model = model,
          input_video = input_video,
          output_video = output_video)