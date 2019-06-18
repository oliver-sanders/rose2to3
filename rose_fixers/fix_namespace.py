from lib2to3.fixer_base import BaseFix
from lib2to3.pgen2 import token


class FixNamespace(BaseFix):

    _accept_type = token.NAME

    def match(self, node):
        if (
            node.value == 'rose'
            and node.type == token.NAME
        ):
            return True
        return False

    def transform(self, node, results):
        node.value = 'metomi.rose'
        return node
