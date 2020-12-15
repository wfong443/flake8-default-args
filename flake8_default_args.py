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
        self._debug = False
        self.tree = tree

    def get_default_values(self, defaults):
        return [default.value for default in defaults if default is not None and default.value is not None]

    def run(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                defvals = []
                if len(node.args.defaults) > 0:
                    if self._debug:
                        print(f"len(node.args.defaults)={len(node.args.defaults)}")
                        print(f"{node.name}.defaults={node.args.defaults}")
                        print(f"{node.name}.kwonlyargs={node.args.kwonlyargs}")
                        print(f"{node.name}.kw_defaults={node.args.kw_defaults}")
                    res = self.get_default_values(node.args.defaults)
                    if res != []:
                        defvals.append(res)
                if len(node.args.kwonlyargs) > 0:
                    if self._debug:
                        print(f"len(node.args.kwonlyargs)={len(node.args.kwonlyargs)}")
                        print(f"{node.name}.defaults={node.args.defaults}")
                        print(f"{node.name}.kwonlyargs={node.args.kwonlyargs}")
                        print(f"{node.name}.kw_defaults={node.args.kw_defaults}")
                    res = self.get_default_values(node.args.kw_defaults)
                    if res != []:
                        defvals.append(res)
                if len(defvals) > 0:
                    error_msg = f"Function {node.name} has keyword args with non-None default values {defvals}"
                    yield (node.lineno, node.col_offset, f"WFDA100 {error_msg}", type(self))
