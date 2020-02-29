from snips_nlu import SnipsNLUEngine
import json

engine = SnipsNLUEngine.from_path("demo")
parsing = engine.parse("Turn lights on in the bathroom please")
print("parsing...")
print(json.dumps(parsing, indent=2))