import os
import pytest

@pytest.mark.skipif(os.uname().sysname != "Linux" and os.uname().release != "Ubuntu", reason="Test only executed on Linux Ubuntu")
def test_minimum_memory_requirement():
    # Getting all memory using os.popen()
    total_memory, used_memory, free_memory = map(
        int, os.popen('free -t -m').readlines()[-1].split()[1:])

    # Check minimum memory requirement
    minimum_memory_requirement = 0  # Minimum memory requirement in MB
    assert free_memory >= minimum_memory_requirement, f"Insufficient memory. Free memory: {free_memory} MB < Minimum memory requirement: {minimum_memory_requirement} MB"

    print(total_memory)
    print(used_memory)
    print(free_memory)
