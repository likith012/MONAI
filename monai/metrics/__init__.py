# Copyright (c) MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from .active_learning_metrics import LabelQualityScore, VarianceMetric, compute_variance, label_quality_score
from .confusion_matrix import ConfusionMatrixMetric, compute_confusion_matrix_metric, get_confusion_matrix
from .cumulative_average import CumulativeAverage
from .f_beta_score import FBetaScore
from .froc import compute_fp_tp_probs, compute_froc_curve_data, compute_froc_score
from .generalized_dice import GeneralizedDiceScore, compute_generalized_dice
from .hausdorff_distance import HausdorffDistanceMetric, compute_hausdorff_distance, compute_percent_hausdorff_distance
from .loss_metric import LossMetric
from .meandice import DiceHelper, DiceMetric, compute_dice
from .meaniou import MeanIoU, compute_iou, compute_meaniou
from .metric import Cumulative, CumulativeIterationMetric, IterationMetric, Metric
from .panoptic_quality import PanopticQualityMetric, compute_panoptic_quality
from .regression import MAEMetric, MSEMetric, PSNRMetric, RMSEMetric, SSIMMetric
from .rocauc import ROCAUCMetric, compute_roc_auc
from .surface_dice import SurfaceDiceMetric, compute_surface_dice
from .surface_distance import SurfaceDistanceMetric, compute_average_surface_distance
from .utils import do_metric_reduction, get_mask_edges, get_surface_distance, ignore_background, is_binary_tensor
from .wrapper import MetricsReloadedBinary, MetricsReloadedCategorical
