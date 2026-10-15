<p align="center">
  <img src="./eodata/img/cng_thrivegeo_banner.png" alt="CNG 101 workshop banner" width="95%">
</p>
# Cloud-Native Geospatial 101: A Practical Introduction to Modern Geospatial Workflows
 
Hands-on notebooks that show you how to find, read and analyse geospatial data directly in the cloud.
<hr>

## About this repository
 
This repository contains the **final solution notebooks** from **Cloud-Native Geospatial 101**, an introductory workshop on Cloud-Native Geospatial. The course was run at the **Cloud Native Geospatial Forum 2026** in **Utah, USA**, on **6 October 2026**.
 
The notebooks include both the worked examples and the solutions to the exercises. You can use them to follow the course again at your own pace, or to learn the topics from scratch.
 
**Who is it for?** Anyone who knows a little Python and wants to understand how modern geospatial data formats work. You don't need to know STAC, COG, Zarr, Parquet, Dask or SQL beforehand. Every concept is explained as it appears.
 
## What is Cloud-Native Geospatial?
 
Geospatial datasets are now very large. Downloading a whole dataset just to look at one small area is slow and wasteful. Cloud-native formats solve this problem. They store data so that you can **read the description first, and then fetch only the pieces you need**, straight from the cloud.
 
This one idea appears again and again in the notebooks. Each format applies it in its own way:
 
- **STAC** helps you *find* the right data.
- **COG** lets you read part of an *image*.
- **Zarr** lets you read part of a large *multi-dimensional array*, such as weather data over time.
- **GeoParquet** lets you read part of a large *table of vector features*, such as buildings or fields.
- **Dask** and **DuckDB** are tools that help you work with these formats at scale.

## What you will learn
 
| # | Notebook | What you do | Data used |
|---|----------|-------------|-----------|
| 1 | [`10_intro_stac.ipynb`](10_intro_stac.ipynb) | Connect to a STAC catalogue, browse collections and search for satellite scenes by place, date and cloud cover | Earth Search by Element 84 (Sentinel-2), EOPF Sentinel Zarr Samples Service |
| 2 | [`21_intro_cog.ipynb`](21_intro_cog.ipynb) |  |  |
| 3 | [`22_intro_zarr.ipynb`](22_intro_zarr.ipynb) | Open a Zarr store from the cloud, read and write pieces of it, and learn why chunk shape decides what a question costs | ERA5 weather data, Sentinel-2 (Douro valley, Portugal) |
| 4 | [`23_intro_parquet.ipynb`](23_intro_parquet.ipynb) | Read the footer of a (Geo)Parquet file, skip folders, row groups and columns, and map the result | Overture Maps, EuroCrops dataset on Source Cooperative |
| 5 | [`31_intro_dask.ipynb`](31_intro_dask.ipynb) | Start a Dask cluster, understand lazy calculations and chunk sizes, and scale from one year to decades of data | ERA5 (64 Novembers at Snowbird) |
| 6 | [`32_intro_duckdb.ipynb`](32_intro_duckdb.ipynb) | Write your first SQL queries on cloud data, watch DuckDB skip data, and save results as GeoParquet | Overture Maps |
 
### Suggested order
 
Work through the notebooks in the order above. They build on each other:
 
- Start with **STAC**, because later notebooks use it to find data.
- **Zarr** builds on STAC and COG.
- **Parquet** builds on STAC. COG and Zarr help, but are not required.
- **Dask** builds on Zarr.
- **DuckDB** builds on Parquet.

## Getting started
 
### What you need
 
- Python [VERSION]
- A web connection, because the data is read directly from the cloud
- The main libraries used in the notebooks: `pystac-client`, `xarray`, `zarr`, `dask`, `geopandas`, `pyarrow`, `s3fs`, `duckdb`, `rasterio`, and `matplotlib`
 
### Run it on your own computer
 
1. Clone the repository:
```bash
   git clone [REPOSITORY URL]
   cd [REPOSITORY NAME]
```
 
2. Create the environment:
```bash
   [COMMAND, for example: conda env create -f environment.yml]
   [COMMAND, for example: conda activate cng101]
```
 
3. Start JupyterLab and open the first notebook:
```bash
   jupyter lab
```

## Data sources and acknowledgements
 
We are grateful to the providers of the open data used in this course:
 
- **Earth Search by Element 84**: Sentinel-2 data on AWS
- **EOPF Sentinel Zarr Samples Service**: Sentinel data in Zarr, from the European Space Agency (ESA) and Copernicus
- **ERA5**: global weather reanalysis from the European Centre for Medium-Range Weather Forecasts (ECMWF)
- **Overture Maps Foundation**: open map data
- **EuroCrops**: field boundaries of European farms
 
## Authors and contributors
 
* Gisela Romero Candanedo, thriveGEO GmbH
* @jwagemann, thriveGEO GmbH
* Guillaume Eynard-Bontemps, CNES

 
## Licence
 
- **Code:** [LICENCE, for example MIT]
- **Text and images in the notebooks:** CC BY 4.0
- **Data:** each dataset keeps its own licence. Please check the providers listed above.

## How to cite
 
> [thriveGEO](https://thrivegeo.com/) (2026). *Cloud-Native Geospatial 101 workshop notebooks.* Cloud Native Geospatial Forum, Utah, USA, 6 October 2026. [URL]