from helpers.unpickler import load

from .ann import ANN
from .pop import PopModel
from .simplelist import SimpleListModel
from .userknnreco import UserKnn

ALS_MODEL_PATH = "weights/als.pkl"
ANN_MODEL_PATH = "weights/ann.pkl"
POP_MODEL_PATH = "weights/pop.pkl"
DATASET_PATH = "kion_train/interactions.csv"

try:
    models = {
        "simple_list_model": SimpleListModel(),
        "user_knn": UserKnn(
            backbone_model=load("weights/userknn.pkl"),
        ),
        "als_model": ANN(
            backbone_model=load(ANN_MODEL_PATH),
            popular_model=PopModel(dataset_path=DATASET_PATH, backbone_model=load(POP_MODEL_PATH)),
        ),
    }
except: