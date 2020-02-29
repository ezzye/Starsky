import io
import json
from snips_nlu import SnipsNLUEngine

nlu_engine = SnipsNLUEngine()


def train():
    with io.open('sample_dataset.json') as f:
        sample_dataset = json.load(f)
    print("training.......")
    nlu_engine.fit(sample_dataset)


train()
parsing = nlu_engine.parse("What will be the weather in San Francisco next week?")
print(parsing)
print(json.dumps(parsing, indent=2))
