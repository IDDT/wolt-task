from xgboost import XGBRegressor
from .types import ModelInput


class Model:
    def __init__(self, fp_model_artifact:str):
        self.model = XGBRegressor()
        self.model.load_model(fp_model_artifact)

    def __call__(self, inp:ModelInput) -> float:
        return self.model.predict([inp])[0].item()
