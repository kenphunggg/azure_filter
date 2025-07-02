# azure_filter: Filter module for Azure Functions Trace

This work presents a summary of the tasks completed using the *[Azure Functions Trace](https://github.com/Azure/AzurePublicDataset/blob/master/AzureFunctionsDataset2019.md)*

# Configuration

## Install dependencies

```bash
$ pip install -r requirements.txt
```

## Running filter

```bash
$ python3 main.py <rps>
```

## Plotting filtered data

Filtered data is plotted within `./filtered_data/rps_200/invocations`