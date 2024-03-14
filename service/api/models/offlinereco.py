import json
import os
from pathlib import Path

from service.api.models.pop import PopModel
from service.api.types.model import BaseModel


class OfflineReco(BaseModel):
    def __init__(self, recos_path: Path, popular_model: PopModel):
        if os.path.isfile(recos_path):
            self._recos = self._load_recos(recos_path)
            self._pop_model = popular_model

    def _load_recos(self, recos_path: Path):
        with open(recos_path, encoding="utf-8") as jf:
            return json.load(jf)

    def get_reco(self, user_id: int, num_reco: int) -> list[int]:
        if str(user_id) in self._recos:
            return self._recos[str(user_id)][:num_reco]
        return self._pop_model.get_reco(user_id, num_reco)
