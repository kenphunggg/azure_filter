# azure_filter: Filter module for Azure Functions Trace

This work presents a summary of the tasks completed using the *[Azure Functions Trace](https://github.com/Azure/AzurePublicDataset/blob/master/AzureFunctionsDataset2019.md)*

# Configuration

## Install dependencies

To get started, let's install the packages the code needs to run.

```bash
$ pip install -r requirements.txt
```

Once the dependencies are set up, you'll need to download the dataset.

```bash
$ wget https://azurepublicdatasettraces.blob.core.windows.net/azurepublicdatasetv2/azurefunctions_dataset2019/azurefunctions-dataset2019.tar.xz

$ tar -xf azurefunctions-dataset2019.tar.xz
```

After having dataset installed, move extracted files to `./data`

## Running filter

```bash
$ python3 main.py <rps>
```

## Plotting filtered data

Filtered data is plotted within `./filtered_data/rps_200/invocations`