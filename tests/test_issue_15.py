import os
from tensorflow import keras
from keras.utils.vis_utils import plot_model

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from context import FeederProf, DataFeeder
from context import LstmEncoder, ToaEncoder, TimeSeriesLSTM

from matplotlib import pyplot as plt

# constants
EPOCHS = 50
BATCH_SIZE = 128

# options
feeder_options = {
    "shuffle": True,
    "batch_size": BATCH_SIZE,
    "input_fields": "time_series",
    "target_field": "outcome",
}

train_feeder = DataFeeder("data_by_entry/train", **feeder_options)
val_feeder = DataFeeder("data_by_entry/validation", **feeder_options)
test_feeder = DataFeeder("data_by_entry/test", **feeder_options)

# initializing TimeSeries class
lstm = TimeSeriesLSTM()


# TensorBoard callbacks, # Write TensorBoard logs to `./logs` directory
tb_callbacks = keras.callbacks.TensorBoard(
    log_dir=f"{lstm.path}/logs", histogram_freq=1
)

lstm.train(
    x=train_feeder,
    epochs=EPOCHS,
    validation_data=val_feeder,
    batch_size=BATCH_SIZE,
    callbacks=[tb_callbacks],
    verbose=1,
    use_multiprocessing=False,
)