import numpy as np

from spektral.datasets import TUDataset
from spektral.data import Dataset
from spektra.loader import BatchLoader, DisjointLoader, Loader

from typing import Literal


def load_data(
    name: str = 'ENZYMES',
    test_split: float = 0.9,
    val_split: float = 0.8,
) -> tuple[Dataset, ...]:
    """Load a dataset from the TUDataset collection.

    Args:
        name (str): Name of the dataset to load.
            Defaults to 'ENZYMES'.
        test_split (float, optional): Fraction of the dataset to use for testing.
            Defaults to 0.9.
        val_split (float, optional): Fraction of the dataset to use for validation.
            Defaults to 0.8.

    Returns:
        tuple[Dataset]: The training, validation and test datasets.
    """
    # Load the dataset.
    dataset = TUDataset(name=name)

    # Split the dataset.
    idxs = np.random.permutation(len(dataset))

    # Split indices.
    split_va = int(len(dataset) * val_split)
    split_te = int(len(dataset) * test_split)

    idx_tr, idx_va, idx_te = np.split(idxs, [split_va, split_te])

    dataset_tr = dataset[idx_tr]
    dataset_va = dataset[idx_va]
    dataset_te = dataset[idx_te]

    return dataset_tr, dataset_va, dataset_te

def data_loader(
    dataset: Dataset,
    batch_size: int = 32,
    loader: Literal['batch', 'disjoint'] = 'disjoint',
    epochs: int | None = None,
    shuffle: bool = True,
) -> tuple[Loader, ...]:
    """Load the dataset and create the data loaders.

    Args:
        dataset (Dataset): Dataset to load.
        batch_size (int, optional): Batch size.
            Defaults to 32.
        loader (str, optional): Loader to use. Can be 'batch' or 'disjoint'.
            Defaults to 'disjoint'.
        epochs (int, optional): Number of epochs to train for.
            Defaults to None.
        shuffle (bool, optional): Whether to shuffle the dataset.
            Defaults to True.
    Returns:
        Loader: Dataset loader.
    """

    if loader == 'batch':
        loader = BatchLoader(
            dataset,
            batch_size=batch_size,
            epochs=epochs,
            mask=True,
            shuffle=shuffle,
        )
    elif loader == 'disjoint':
        loader = DisjointLoader(
            dataset,
            batch_size=batch_size,
            epochs=epochs,
            shuffle=shuffle,
        )
    else:
        raise ValueError(f'Invalid loader: {loader}')

    return loader
