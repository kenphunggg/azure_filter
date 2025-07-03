import csv
from typing import Dict, List, Tuple

from module.libs import getFile, Logger, Const


def filter_rps(rps: int, up_bound: int):
    invocation_file_list = getFile(Const.INVOCATIONS_FOLDER)

    result: Dict[Tuple[str, str, str], Dict[str, float]] = {}
    # app1: {day1: 300rps, day2: 200rps}

    for invocation_file in invocation_file_list:
        file = f'{Const.INVOCATIONS_FOLDER}/{invocation_file}'
        Logger.critical(f'Opening {file}')

        with open(file) as invocationFile:
            iReader = csv.reader(invocationFile, delimiter=',')

            next(iReader)

            for row in iReader:
                values = row[4:]
                numeric_values = [float(v) for v in values]

                avg = sum(numeric_values)/len(numeric_values)/60

                if avg > rps and avg < up_bound:
                    metadata: Tuple[str] = (row[0], row[1], row[2])
                    Logger.info(f"Found {metadata} with {avg}rps")

                    if metadata not in result:
                        result[metadata] = {}

                    result[metadata][invocation_file] = avg

    Logger.succeed('Finished loading 14 days')

    Logger.critical('Loading filterd data')

    for invocation_file in invocation_file_list:
        file = f'./filtered_data/rps_{rps}/invocations/{invocation_file}'
        with open(file, 'w') as resetFile:
            resetFile.truncate()

    for function in result:
        if len(result[function]) == Const.total_day:
            Logger.succeed(
                f'Function [{function}] have 14 days with >= {rps}rps')

            Logger.info(
                f'Import new invocation data to ./filtered_data/rps_{rps}')
            for invocation_file in invocation_file_list:
                file = f'{Const.INVOCATIONS_FOLDER}/{invocation_file}'
                with open(file) as invocationFile:
                    iReader = csv.reader(invocationFile, delimiter=',')
                    next(iReader)
                    for row in iReader:
                        if row[0] == function[0] and row[1] == function[1] and row[2] == function[2]:
                            Logger.info(
                                f'Import data for {function} at {invocation_file}')
                            newfile = f'./filtered_data/rps_{rps}/invocations/{invocation_file}'
                            with open(newfile, mode='a', newline='') as newInvocationFile:
                                iWriter = csv.writer(
                                    newInvocationFile, delimiter=',')
                                iWriter.writerow(row)

            # Logger.critical(
            #     f'Import new function_durations data to ./filtered_data/rps_{rps}')
            # Logger.critical(
            #     f'Import new app_memory data to ./filtered_data/rps_{rps}')
        else:
            Logger.warning(
                f'Function {function} have {len(result[function])} days with >= {rps}rps')

    Logger.succeed('Finished loading filterd data')

    Logger.critical('Merge data for 14 days')
