import importlib.util
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def test_background_runner_imports():
    spec = importlib.util.spec_from_file_location("background_runner", ROOT / "background_runner.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    assert hasattr(module, "run_in_background")
    assert hasattr(module, "run_on_startup")
