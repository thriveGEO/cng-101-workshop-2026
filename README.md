<p align="center">
  <img src="./img/cng_thrivegeo_banner.png" alt="CNG 101 workshop banner" width="100%">
</p>

# Cloud-Native Geospatial 101: A Practical Introduction to Modern Geospatial Workflows
 
Hands-on notebooks that show you how to work with satellite and geospatial data in the cloud.

## About this repository
 
This repository contains the **final solution notebooks** from [Cloud-Native Geospatial 101](https://2026.cloudnativegeo.org/#/agenda?day=1&lang=en&sessionId=200860000000640064), an introductory workshop on Cloud-Native Geospatial. The course was run at the **Cloud Native Geospatial Forum 2026** in **Utah, USA**, on **6 October 2026**.
 
The notebooks include both the worked examples and the solutions to the exercises. You can use them to follow the course again at your own pace, or to learn the topics from scratch.
 
**Who is it for?** <br>
Anyone who knows a little Python and wants to understand how modern geospatial data formats work. You don't need to know STAC, COG, Zarr, Parquet, Dask or SQL beforehand. Every concept is explained as it appears.
 
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
| 1 | [`10_intro_stac.ipynb`](./10_intro_stac.ipynb) | Connect to a STAC catalogue, browse collections and search for satellite scenes by place, date and cloud cover | Earth Search by Element 84 (Sentinel-2), EOPF Sentinel Zarr Samples Service |
| 2 | [`21_intro_cog.ipynb`](./21_intro_cog.ipynb) | Open Cloud-Optimised GeoTIFFs and learn their structure including Tiles and Overviews | EarthSearch by Element 84 (Sentinel-2) | 
| 3 | [`22_intro_zarr.ipynb`](./22_intro_zarr.ipynb) | Open a Zarr store from the cloud, read and write pieces of it, and learn why chunk shape decides what a question costs | ERA5 weather data, Sentinel-2 (Douro valley, Portugal) |
| 4 | [`23_intro_parquet.ipynb`](./23_intro_parquet.ipynb) | Read the footer of a (Geo)Parquet file, skip folders, row groups and columns, and map the result | Overture Maps, EuroCrops dataset on Source Cooperative |
| 5 | [`31_intro_dask.ipynb`](./31_intro_dask.ipynb) | Start a Dask cluster, understand lazy calculations and chunk sizes, and scale from one year to decades of data | ERA5 (64 Novembers at Snowbird) |
| 6 | [`32_intro_duckdb.ipynb`](./32_intro_duckdb.ipynb) | Write your first SQL queries on cloud data, watch DuckDB skip data, and save results as GeoParquet | Overture Maps |
 
### Suggested order
 
Work through the notebooks in the order above. They build on each other:
 
- Start with **STAC**, because later notebooks use it to find data.
- **Zarr** builds on STAC and COG.
- **Parquet** builds on STAC. COG and Zarr help, but are not required.
- **Dask** builds on Zarr.
- **DuckDB** builds on Parquet.

## Getting started
 
### What you need
 
- Python 3.13.11
- A web connection, because the data is read directly from the cloud
- The main libraries used in the notebooks: `pystac-client`, `xarray`, `zarr`, `dask`, `geopandas`, `pyarrow`, `s3fs`, `duckdb`, `rasterio`, and `matplotlib`
 
### Run it on your own computer
 
1. Clone the repository:
```bash
   git clone https://github.com/thriveGEO/cng-101-workshop-2026
   cd cng-101-workshop-2026
```
 
2. Create the environment:
```bash
   conda env create -f env_cng_26.yml
   conda activate cng_workshop
```
 
3. Start JupyterLab and open the first notebook:
```bash
   jupyter lab
```

## Data sources and acknowledgements
 
We are grateful to the providers of the open data used in this course:
 
- **[Earth Search by Element 84](https://registry.opendata.aws/sentinel-2-l2a-cogs/)**: Sentinel-2 data on AWS
- **[EOPF Sentinel Zarr Samples Service](https://zarr.eopf.copernicus.eu/)**: Sentinel data in Zarr, from the European Space Agency (ESA) and Copernicus
- **[ERA5 Global Reanalysis - prepared by the WeatherBench 2 project](https://github.com/pangeo-data/WeatherBench)**: a copy of ECMWF's global climate reanalysis data ERA5, prepared by the WeatherBench project 
- **[Overture Maps Foundation](https://overturemaps.org/)**: open map data
- **[EuroCrops](https://github.com/maja601/EuroCrops)**: crop reporting dataset from European countries (accessed via [Source Cooperative](https://source.coop/cholmes/eurocrops))
 
## Authors and contributors
 
* [Gisela Romero Candanedo](https://github.com/gisromerocandanedo), [thriveGEO](https://github.com/thriveGEO)
* [Julia Wagemann](https://github.com/jwagemann), [thriveGEO](https://github.com/thriveGEO)
* [Guillaume Eynard-Bontemps](https://github.com/guillaumeeb), [CNES](https://github.com/CNES)

 
## Licence

<a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" />
</a>
<br />
This work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

## How to cite
 
> [thriveGEO](https://thrivegeo.com/) (2026). *Cloud-Native Geospatial 101 workshop notebooks.* Cloud Native Geospatial Forum, Utah, USA, 6 October 2026. [URL]
