import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from datafeeders import FeederProf, DataFeeder
from net import LstmEncoder

feeder_options = {
    "batch_size": 128,
    "input_fields": ["toa", "time_series"],
    "target_field": "outcome",
}

prof_alberto = FeederProf(
    "trained/albertino", "data_by_entry/train", difficulty_levels=5, **feeder_options
)

prof_alberto.teaching_level = 4
print(f"Prof has {len(prof_alberto)} lessons to give")

val_feeder = DataFeeder("data_by_entry/validation", **feeder_options)
mariuccio = LstmEncoder(path="trained/mariuccio")

mariuccio.train(
    x=prof_alberto,
    epochs=300,
    validation_data=val_feeder,
    batch_size=128,
    verbose=1,
    use_multiprocessing=False,
)
