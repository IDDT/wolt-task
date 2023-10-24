import unittest
from unittest.mock import Mock
import numpy as np
from src.config import FILEPATHS
from src.model import Model
from src.types import ModelInput


class TestModel(unittest.TestCase):
    def test_model_instantiation(self):
        model = Model(FILEPATHS['model_artifact'])
        self.assertIsInstance(model, Model)

    def test_model_runs(self):
        model = Model(FILEPATHS['model_artifact'])
        model(ModelInput(is_retail=1, avg_prep_time=30.0, hour_of_day=15))

    def test_model_prediction(self):
        model = Model(FILEPATHS['model_artifact'])
        mock_xgboost_model = Mock()
        mock_xgboost_model.predict.return_value = [np.float32(42.0)]
        model.model = mock_xgboost_model
        out = model(ModelInput(is_retail=1, avg_prep_time=30.0, hour_of_day=15))
        self.assertEqual(out, 42.0)
