# OpenRTE

![openrte-logo](https://raw.githubusercontent.com/henriupton99/openrte/main/images/openrte.png)

Python wrapper for [RTE API](https://data.rte-france.com/) requests. 

## 1. Usage

#### 1.1. Get RTE API credentials

You need to follow these first steps in order to setup your wrapper :  

* [create an account](https://data.rte-france.com/create_account) on the RTE platform
* [create an application](https://data.rte-france.com/group/guest/apps) associated to your account (the name and description of the app is not relevant)
* collect your app IDs (**ID Client** and **ID Secret**) available in your application dashboard

#### 1.2. Generate a data retrieval

To retrieve data using the wrapper, follow this pipeline :

```python
from openrte import Client
client = Client(client_id="XXX", client_secret="XXX")
dfs = client.retrieve_data(start_date="2024-01-01 00:00:00", end_date="2024-01-02 23:59:00", data_type="actual_generations_per_unit", output_dir="./output")
```

where :
* **start_date** is the first date of the data retrieval (format *YYYY-MM-DD HH:MM:SS*)
* **end_date** is the last date of the data retrieval (format *YYYY-MM-DD HH:MM:SS*)
* **data_type** is the desired data to collect (a keyword list is given in the next section). It can be a single keyword *"XXX"* or a list of keyword separated by a comma *"XXX,YYY,ZZZ"*
* **output_dir** (*optionnal*): the output directory to store the results

The generic output format is a pandas dataframe / **.csv** file containing the data for all dates between **start_date** and **end_date**. It will generate one file per desired **data_type** and will store all of them in a **./results** folder with the generic name *"<data_type>_<start_date>_<end_date>.csv"*.

## 2. Available *data_type* options

It is possible to see the full options catalog using the client attribute **catalog** :

```python
from openrte import Client
client = Client(client_id="XXX", client_secret="XXX")
client.catalog
```

The following table is an exhaustive list of all possible (currently handled) options for the **data_type** argument for the retrieval, and the description of the associated data :

| *data_type* | Request URL (Base) |
|-------------------|-----|
| `actual_generations_per_production_type` | *https://digital.iservices.rte-france.com/open_api/actual_generation/v1/actual_generations_per_production_type* |
| `actual_generations_per_unit` | *https://digital.iservices.rte-france.com/open_api/actual_generation/v1/actual_generations_per_unit* |
| `volumes_per_energy_type` | *https://digital.iservices.rte-france.com/open_api/balancing_energy/v4/volumes_per_energy_type* |
| `prices` | *https://digital.iservices.rte-france.com/open_api/balancing_energy/v4/prices* |
| `imbalance_data` | *https://digital.iservices.rte-france.com/open_api/balancing_energy/v4/imbalance_data* |
| `standard_rr_data` | *https://digital.iservices.rte-france.com/open_api/balancing_energy/v4/standard_rr_data* |
| `lead_times` | *https://digital.iservices.rte-france.com/open_api/balancing_energy/v4/lead_times* |
| `afrr_marginal_price` | *https://digital.iservices.rte-france.com/open_api/balancing_energy/v4/afrr_marginal_price* |
| `volumes_per_entity_price` | *https://digital.iservices.rte-france.com/open_api/balancing_energy/v4/volumes_per_entity_price* |
| `tso_offers` | *https://digital.iservices.rte-france.com/open_api/balancing_energy/v4/tso_offers* |
| `standard_afrr_data` | *https://digital.iservices.rte-france.com/open_api/balancing_energy/v4/standard_afrr_data* |
| `volumes_per_reasons` | *https://digital.iservices.rte-france.com/open_api/balancing_energy/v4/volumes_per_reasons* |
