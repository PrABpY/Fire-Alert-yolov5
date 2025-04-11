import torch
from pathlib import PurePosixPath, WindowsPath

def convert_path(obj):
    if isinstance(obj, dict):
        return {k: convert_path(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_path(v) for v in obj]
    elif isinstance(obj, tuple):
        return tuple(convert_path(v) for v in obj)
    elif isinstance(obj, WindowsPath):
        return PurePosixPath(str(obj))  # ✅ เปลี่ยนตรงนี้
    return obj

model = torch.load('best.pt', map_location='cpu')
fixed_model = convert_path(model)
torch.save(fixed_model, 'best_fixed.pt')
