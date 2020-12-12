import ast
import sys

if sys.version_info < (3, 8):
    import importlib_metadata
else:
    import importlib.metadata as importlib_metadata


__version__ = '0.1.0'


class FcnDefaultArgsChecker(object):
    """Mutable default argument checker.
    Flake8 extension that alerts when a mutable type is used
    as an argument's default value.
    """
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree, filename):
        self.tree = tree

    def run(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                if node.args.defaults is not [] :
                    error_msg = f"Function {node.name} has keyword argument(s) assigned"
                    yield (node.lineno, node.col_offset, f"WFDA100 {error_msg}", type(self))
