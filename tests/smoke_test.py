import pytest
import sys
import os

sys.path.append(os.path.abspath('../src'))
## import {{MODULES}}

@pytest.mark.filterwarnings("ignore::FutureWarning")
def test_smoke():
##    {{COMMANDS}}
