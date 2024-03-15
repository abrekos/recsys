from helpers.unpickler import load

from .ann import ANN
from .offlinereco import OfflineReco
from .pop import PopModel
from .simplelist import SimpleListModel
from .userknnreco import UserKnn

DATASET_PATH = "kion_train/interactions.csv"
ALS_MODEL_PATH = "weights/als.pkl"
ANN_MODEL_PATH = "weights/ann.pkl"
POP_MODEL_PATH = "weights/pop.pkl"

VAE_RECOS = "weights/vae_recos.json"
MULTIVAE_RECOS = "weights/multivae_recos.json"
DSSM_RECOS = "weights/dssm.json"
XGBOOST_RECOS = "weights/xgb.json"


models = {
    "simple_list_model": SimpleListModel(),
    "ranking_pop": UserKnn(
        backbone_model=load("weights/userknn.pkl"),
    ),
    "als_model": ANN(
        backbone_model=load(ANN_MODEL_PATH),
        popular_model=PopModel(dataset_path=DATASET_PATH, backbone_model=load(POP_MODEL_PATH)),
    ),
    "vae_reco_offline_model": OfflineReco(
        recos_path=VAE_RECOS,
        popular_model=PopModel(dataset_path=DATASET_PATH, backbone_model=load(POP_MODEL_PATH)),
    ),
    "multivae_model": OfflineReco(
        recos_path=MULTIVAE_RECOS,
        popular_model=PopModel(dataset_path=DATASET_PATH, backbone_model=load(POP_MODEL_PATH)),
    ),
    "dssm_model": OfflineReco(
        recos_path=DSSM_RECOS,
        popular_model=PopModel(dataset_path=DATASET_PATH, backbone_model=load(POP_MODEL_PATH)),
    ),
    "xgboost_model": OfflineReco(
        recos_path=XGBOOST_RECOS,
        popular_model=PopModel(dataset_path=DATASET_PATH, backbone_model=load(POP_MODEL_PATH)),
    ),
}
