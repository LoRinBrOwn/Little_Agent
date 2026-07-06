import subprocess
import sys
from pathlib import Path

import mini_leno


def test_mini_leno_module_and_public_exports():
    assert mini_leno.Leno is not None
    assert mini_leno.FakeModelClient is not None
    assert not hasattr(mini_leno, "MiniAgent")
    result = subprocess.run([sys.executable, "-m", "mini_leno", "--help"], capture_output=True, text=True, check=True)
    assert "Teaching-sized Leno agent harness" in result.stdout


def test_readme_main_mapping_points_to_existing_files():
    repo_root = Path(__file__).resolve().parents[3]
    main_files = [
        "leno/cli.py",
        "leno/runtime.py",
        "leno/agent_loop.py",
        "leno/context_manager.py",
        "leno/providers/clients.py",
        "leno/tool_executor.py",
        "leno/tools.py",
        "leno/task_state.py",
        "leno/run_store.py",
        "leno/workspace.py",
    ]
    for path in main_files:
        assert (repo_root / path).exists()
