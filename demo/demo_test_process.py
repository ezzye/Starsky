import io
import json
from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN

nlu_engine = SnipsNLUEngine(config=CONFIG_EN)


def train():
    with io.open('dataset.json') as f:
        dataset = json.load(f)
    print("training.......")
    nlu_engine.fit(dataset)
    nlu_engine.persist("demo")


train()
parsing = nlu_engine.parse("Hey, lights on in the lounge !")
print("parsing...")
print(json.dumps(parsing, indent=2))

# Use CLI to generate dataset, snips-nlu generate-dataset en dataset.yaml > dataset.json
