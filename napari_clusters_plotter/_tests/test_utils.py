import sys

import numpy as np
import pandas as pd

from napari_clusters_plotter._utilities import (
    add_column_to_layer_tabular_data,
    get_layer_tabular_data,
    set_features,
)

sys.path.append("../")


def test_feature_setting(make_napari_viewer):

    viewer = make_napari_viewer()
    label = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 2, 2],
            [0, 0, 0, 0, 2, 2, 2],
            [3, 3, 0, 0, 0, 0, 0],
            [0, 0, 4, 4, 0, 5, 5],
            [6, 6, 6, 6, 0, 5, 0],
            [0, 7, 7, 0, 0, 0, 0],
        ]
    )
    label_layer = viewer.add_labels(label)

    some_features = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    set_features(label_layer, some_features)

    features = get_layer_tabular_data(label_layer)

    assert isinstance(features, pd.DataFrame)
    assert features.equals(some_features)

    some_features = get_layer_tabular_data(label_layer)
    assert isinstance(some_features, pd.DataFrame)

    new_data = pd.DataFrame(columns=['A', 'C'])
    new_data['A'] = some_features['A']
    new_data['C'] = [3, 4, 7]
    add_column_to_layer_tabular_data(label_layer, new_data, on='A')
    some_features = get_layer_tabular_data(label_layer)
    assert "C" in some_features.columns


if __name__ == "__main__":
    import napari
    test_feature_setting(napari.Viewer)
