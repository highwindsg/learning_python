#!/usr/bin/env python3

"""
try:
    # Runs first
    < code >
except:
    # Runs if exception occurs in try block
    < code >
else:
    # Executes if try block *succeeds*
    < code >
finally:
    # This code *always* executes
    < code >
"""
import logging
import time

# Create logger. This would create the filename 'problems.log'.
logging.basicConfig(
    filename="///Users/cay1sgp/Documents/GitHub/learning_python/YouTube_Socratica/UnitTests/problems.log",
    level=logging.DEBUG)

logger = logging.getLogger()

def read_file_timed(path):
    """Return the contents of the file at 'path' and measure time required."""
    start_time = time.time()
    try:
        f = open(path, mode="rb")
        data = f.read()
        return data
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info("Time required for {file} = {time}".format(file=path, time=dt))

# The line below will write to the logger file 'problems.log'.
data = read_file_timed("///Users/cay1sgp/Documents/GitHub/learning_python/YouTube_Socratica/UnitTests/audio_file.wav")
# The line below will write to the logger file 'problems.log' of the file not found.
data = read_file_timed("///Users/cay1sgp/Documents/GitHub/learning_python/YouTube_Socratica/UnitTests/imaginary_file")
