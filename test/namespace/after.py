import metomi.rose
import metomi.rose.config
from metomi.rose.config import ConfigNode

print(metomi.rose.__version__)
print(metomi.rose.config.__file__)

class MyNode(metomi.rose.config.ConfigNode):
    pass
