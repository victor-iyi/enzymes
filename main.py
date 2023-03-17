import fire

from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.metrics import CategoricalAccuracy

from spektra.models import GeneralGNN

from enzymes.data import load_data
from enzymes.data import data_loader


def main(
    name: str = 'ENZYMES',
    hidden_layers: int = 256,
    batch_size: int = 32,
    epochs: int = 100,
    lr: float = 0.001,
    dropout: float = 0.5,
    loader: str = 'disjoint',
    test_split: float = 0.8,
    val_split: float = 0.9,
) -> None:
    """Graph Neural  Network.

    Args:
        name (str, optional): Name of the dataset.
        hidden_layers (int, optional): Number of hidden layers.
        batch_size (int, optioinal): Batch size.
        epochs (int, optional): Number of epochs.
        lr (float, optional): Learning rate.
        dropout (float, optional): Dropout rate.
        loader (str, optional): Loader type.
        test_split (float, optional): Test split.
        val_split (float, optional): Validation split.
    """

    # Load the dataset.
    train_ds, val_ds, test_ds = load_data(
        name=name,
        test_split=test_split,
        val_split=val_split,
    )
    print(f'Train dataset: {train_ds}')
    print(f'Validation dataset: {val_ds}')
    print(f'Test dataset: {test_ds}')

    # Create the data loaders.
    train_loader = data_loader(
        dataset=train_ds,
        batch_size=batch_size,
        loader=loader,
        epochs=epochs,
        shuffle=True,
    )
    val_loader = data_loader(
        dataset=val_ds,
        batch_size=batch_size,
        loader=loader,
        epochs=None,
        shuffle=False,
    )
    test_loader = data_loader(
        dataset=test_ds,
        batch_size=batch_size,
        loader=loader,
        epochs=None,
        shuffle=False,
    )

    # Create the model.
    model = GeneralGNN(
        train_ds.n_labels,
        hidden=hidden_layers,
        dropout=dropout,
        activation='softmax',
    )

    # Compile the model.
    optimizer = Adam(learning_rate=lr)
    loss_fn = CategoricalCrossentropy()
    acc_fn = CategoricalAccuracy()

    model.compile(
        optimizer=optimizer,
        loss=loss_fn,
        metrics=[acc_fn],
    )

    # Train the model.
    model.fit(
        train_loader.load(),
        steps_per_epoch=train_loader.steps_per_epoch,
        epochs=epochs,
        validation_data=val_loader.load(),
        validation_steps=val_loader.steps_per_epoch,
    )

    # Print the model summary.
    model.summary()

    # Evaluate the model on the test set.
    print('Evaluating model.')
    loss, acc = model.evaluate(
        test_loader.load(),
        steps=test_loader.steps_per_epoch,
    )
    print(f'Test loss: {loss:.4f} - Test accuracy: {acc:.02%}')



if __name__ == '__main__':
    fire.Fire(main, name='enzymes')

