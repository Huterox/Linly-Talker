from .SadTalker import SadTalker
from .Wav2Lip import Wav2Lip
try:
    from .ERNeRF import ERNeRF
except Exception as e:
    print("ERNeRF导入失败，原因：", e)
    print("使用ERNeRF前需要安装对应的环境")
try:
    from .MuseTalk import MuseTalk, MuseTalk_RealTime
except Exception as e:
    print("MuseTalk导入失败，原因：", e)
    print("使用MuseTalk前需要安装对应的环境")