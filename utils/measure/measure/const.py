import os
from enum import Enum
from pathlib import Path

QUESTION_GENERATE_MODEL_JSON = "generate_model_json"
QUESTION_DUMMY_LOAD = "dummy_load"
QUESTION_MODEL_NAME = "model_name"
QUESTION_MEASURE_DEVICE = "measure_device"
QUESTION_ENTITY_ID = "entity_id"
QUESTION_MODEL_ID = "model_id"

script_dir = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = Path(os.path.join(script_dir, "../")).resolve()


class MeasureType(str, Enum):
    """Type of devices to measure power of"""

    LIGHT = "Light bulb(s)"
    SPEAKER = "Smart speaker"
    RECORDER = "Recorder"
    AVERAGE = "Average"
    CHARGING = "Charging device"
