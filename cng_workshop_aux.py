import math
from pystac_client import Client, CollectionClient
from pystac import Collection, MediaType
import xarray as xr
import matplotlib.pyplot as plt
import matplotlib
import rioxarray
import planetary_computer as pc
import numpy as np
import rasterio
from matplotlib.patches import Rectangle
from rio_cogeo.cogeo import cog_validate
from rasterio.crs import CRS
from rasterio.warp import transform_bounds



# Helper function to collect the found scenes

def list_found_elements(search_result):
    """
    Returns the number of found elements from a STAC .search()
    Parameters
    ----------
    search_result : pystac_client.item_search.ItemSearch

    Returns
    -------
    list
        A list of lists with Item ID and the dicts containing the hrefs for each contained asset

    """
    the_list = [] # will store the id of the retrieved items.
    for item in search_result.items(): #retrieves the result inside the catalog.
        the_list.append([item.id,item.assets]) # appeds the id plus the assets paths
    return the_list

## For COGS

# To explore the metadata:

def metadata_cog(raterio_cog: rasterio.io.DatasetReader):
    """
    Description of the metadata contained within the IFD of a COG hosted in the cloud
    
    Parameters
    ----------
    raterio_cog : rasterio.io.DatasetReader

    Returns
    -------
    str
        A description of the geographical information and the overviews layout.

    """
    # Calculate overview factors and resolutions once to keep things clean
    overviews = raterio_cog.overviews(1)
    res_per_level = [i * int(raterio_cog.res[0]) for i in overviews]

    print(
        f"Size:          {raterio_cog.width} x {raterio_cog.height} pixels"
        f"Resolution:    {raterio_cog.res[0]:.0f} m\n"
        f"CRS:           {raterio_cog.crs}\n"
        f"Tile size:     {raterio_cog.block_shapes[0][1]} x {raterio_cog.block_shapes[0][0]} pixels\n"
        f"Overviews:     {raterio_cog.overviews(1)}\n"
        f"The Resolution\n"
        f"per overview is: {res_per_level} m"
    )


# To create COG tiling layout based on selected overviews

def cog_tiles_overview(band_data_array , metadata , aoi_bbox , overview_lev):

    # reprojecting the AOI bbox:
    proj_bbox = transform_bounds(CRS.from_epsg(4326), metadata.crs, *aoi_bbox)

    aoi = Rectangle(
        (proj_bbox[0],proj_bbox[1]),
        abs(proj_bbox[0]-proj_bbox[2]),abs(proj_bbox[1]-proj_bbox[3]),
        linewidth=4,
        edgecolor="yellow",
        facecolor="none",
    )

    if overview_lev == None:
        overview = 1
    else:
        overview = metadata.overviews(1)[overview_lev]

    #generating our resolutions grid coordinates:
    x_coords = list(range(int(metadata.bounds.left), int(metadata.bounds.right), int((metadata.block_shapes[0][0]*metadata.res[0]*overview))))
    y_coords = list(range(int(metadata.bounds.top), int(metadata.bounds.bottom), -int((metadata.block_shapes[0][1]*metadata.res[1]*overview))))

    # Highlighting the first tile (top-left)
    first_tile_xmin = metadata.bounds.left
    first_tile_xmax = metadata.bounds.left + (metadata.block_shapes[0][0]*metadata.res[0]*overview)
    first_tile_ymax = metadata.bounds.top
    first_tile_ymin = metadata.bounds.top - ((metadata.block_shapes[0][1]*metadata.res[1])*overview)

    rect = Rectangle(
        (first_tile_xmin, first_tile_ymin),
        (metadata.block_shapes[0][0]*metadata.res[0]*overview),
        (metadata.block_shapes[0][1]*metadata.res[1]*overview),
        linewidth=4,
        edgecolor="blue",
        facecolor="none",
    )

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.imshow(band_data_array.isel(band=0).values, cmap="gray", extent=[metadata.bounds.left, metadata.bounds.right, metadata.bounds.bottom, metadata.bounds.top])
    
    if overview_lev == None:
        ax.set_title(f"COG Tile Grid @ Full Resolution ({metadata.res[0]}m resolution)")
    else:
        ax.set_title(f"COG Tile Grid @ Overview Level = {overview_lev} ({metadata.res[0]*overview}m resolution)")
    ax.set_xlabel("Easting (m)")
    ax.set_ylabel("Northing (m)")
    # Add grid lines
    for x in x_coords:
        ax.axvline(x=x, color="red", linewidth=0.5)
    for y in y_coords:
        ax.axhline(y=y, color="red", linewidth=0.5)

    ax.add_patch(rect)
    ax.add_patch(aoi)

    return plt.show()
