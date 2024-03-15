from helpers.unpickler import load

from .simplelist import SimpleListModel
from .userknnreco import UserKnn

models = {
    "simple_list_model": SimpleListModel(),
    "user_knn": UserKnn(
        backbone_model=load("weights/userknn.pkl"),
    ),
}
