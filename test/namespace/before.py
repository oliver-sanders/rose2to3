import rose
import rose.config
from rose.config import ConfigNode

print(rose.__version__)
print(rose.config.__file__)

class MyNode(rose.config.ConfigNode):
    pass
