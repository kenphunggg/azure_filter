from module.filter_rps import filter_rps
from module.libs import Logger
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        Logger.error('Please provide an RPS threshold as an argument.')
        Logger.normal('Usage: python main.py <rps_value>')
        sys.exit(1)  # Exit with an error code

    try:
        # Convert the argument from a string to an integer
        rps = int(sys.argv[1])
        filter_rps(rps)

    except ValueError:
        # Handle cases where the argument is not a valid number
        Logger.error(f'[{sys.argv[1]}] is not a valid integer.')
        sys.exit(1)
