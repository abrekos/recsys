import os
from pathlib import Path
from typing import Any, Tuple

import cattr
import pandas as pd
from rectools import Columns
from rectools.dataset import Dataset, Interactions
from rectools.models import PopularModel

from service.api.types.model import BaseModel


class PopModel(BaseModel):
    def __init__(self, dataset_path: Path, backbone_model: Any):
        self._dataset, self._item_id_map = self._load_dataset(dataset_path)
        self._model: PopularModel = backbone_model

    @staticmethod
    def _load_dataset(dataset_path: Path) -> Tuple[Dataset, dict]:
        if not os.path.isfile(dataset_path):
            return None

        interactions_df = pd.read_csv(dataset_path)
        interactions_df.rename(columns={"last_watch_dt": Columns.Datetime, "total_dur": Columns.Weight}, inplace=True)

        interactions = Interactions(interactions_df)
        dataset = Dataset.construct(interactions.df)
        item_id_map = dict(enumerate(cattr.unstructure(dataset.item_id_map)["external_ids"].tolist()))
        return dataset, item_id_map

    def get_reco(self, user_id: int, num_reco: int) -> list[int]:
        return [self._item_id_map[p] for p in self._model.popularity_list[0][:num_reco]]
