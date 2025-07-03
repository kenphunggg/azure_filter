from module.filter_rps import filter_rps
from module.libs import Logger
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        Logger.error('Please provide an RPS threshold as an argument.')
        Logger.normal('Usage: python main.py <lower_bound> <upper_bound>')
        sys.exit(1)  # Exit with an error code

    try:
        low_bound = int(sys.argv[1])
    except ValueError:
        Logger.error(f'Lower bound [{sys.argv[1]}] is not a valid integer.')
        sys.exit(1)

    # 3. Handle the upper bound conversion
    try:
        up_bound = int(sys.argv[2])
    except ValueError:
        Logger.error(f'Upper bound [{sys.argv[2]}] is not a valid integer.')
        sys.exit(1)

    filter_rps(low_bound, up_bound)
