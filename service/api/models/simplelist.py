from service.api.types.model import BaseModel


class SimpleListModel(BaseModel):
    MODEL_NAME: str = "simple_list_model"

    def get_reco(self, user_id: int, num_reco: int) -> list[int]:
        return list(range(1, num_reco + 1))