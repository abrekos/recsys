from .simplelist import SimpleListModel
from .userknnreco import UserKnn
from helpers.unpickler import load


models = {
    "simple_list_model":  SimpleListModel(),
    "user_knn": UserKnn(
        backbone_model=load("userknn.pkl"),
    )
}
