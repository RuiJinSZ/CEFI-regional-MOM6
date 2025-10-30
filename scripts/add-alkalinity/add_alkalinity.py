"""
Add alkalinity to 15 regions with given value, unit mol m^-3

pH uses mol L-1, and 1 mol L^-1 = 1000 mol m^-3

--------------------------------------------------------------------------------
Variable             Shape                Units                Description                   
--------------------------------------------------------------------------------
time                 (1,)                 N/A                  N/A                           
grid_x_T             (1440,)              degree_east          Nominal Longitude of T-ce...  
grid_y_T             (1080,)              degree_north         Nominal Latitude of T-cel...  
NO3_CONC             (1, 1080, 1440)      mol m-3              DIN_CONC                      
LDON_CONC            (1, 1080, 1440)      mol m-3              0.3*DON_CONC                  
SLDON_CONC           (1, 1080, 1440)      mol m-3              0.35*DON_CONC                 
SRDON_CONC           (1, 1080, 1440)      mol m-3              0.35*DON_CONC                 
NDET_CONC            (1, 1080, 1440)      mol m-3              1.0*PN_CONC                   
PO4_CONC             (1, 1080, 1440)      mol m-3              PO4_CONC                      
LDOP_CONC            (1, 1080, 1440)      mol m-3              0.3*DOP_CONC                  
SLDOP_CONC           (1, 1080, 1440)      mol m-3              0.35*DOP_CONC                 
SRDOP_CONC           (1, 1080, 1440)      mol m-3              0.35*DOP_CONC                 
PDET_CONC            (1, 1080, 1440)      mol m-3              0.3*PP_CONC                   
FED_CONC             (1, 1080, 1440)      mol m-3              FED_CONC                      
FEDET_CONC           (1, 1080, 1440)      mol m-3              FEDET_CONC                    
ALK_CONC             (1, 1080, 1440)      N/A                  N/A
"""


import numpy as np
import xarray as xr

import matplotlib.pyplot as plt

import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.ticker as mticker
import pandas as pd

from utils import region_to_box_lat_lon


original_river_alk_concentration = 0.42e-3


class RiverParser:
    def __init__(self, dataset):
        self.times = dataset.variables["time"]
        self.latitudes = dataset.variables["grid_y_T"]
        self.longitudes = np.array(dataset.variables["grid_x_T"])
        # region_to_box_lat_lon is using -180 <= longitude <= 180
        # but nc is using -300 <= longitude <= 60, so move it
        self.longitudes[self.longitudes < -180] += 360

    @property
    def len_times(self) -> int:
        return len(self.times)

    @property
    def len_latitudes(self) -> int:
        return len(self.latitudes)

    @property
    def len_longitudes(self) -> int:
        return len(self.longitudes)

    def map_coordinate_to_slice_indices(self, coordinate: dict[str, float]) -> dict[str, int]:
        indices_within_lat = []
        for index in range(self.len_latitudes):
            latitude = self.latitudes[index]
            if coordinate["latmin"] <= latitude and latitude <= coordinate["latmax"]:
                indices_within_lat.append(index)
        index_latmin = indices_within_lat[0]
        index_latmax = indices_within_lat[-1]

        indices_within_lon = []
        for index in range(self.len_longitudes):
            longitude = self.longitudes[index]
            if coordinate["lonmin"] <= longitude and longitude <= coordinate["lonmax"]:
                indices_within_lon.append(index)
        index_lonmin = indices_within_lon[0]
        index_lonmax = indices_within_lon[-1]

        return {
            "index_latmin": index_latmin,
            "index_latmax": index_latmax,
            "index_lonmin": index_lonmin,
            "index_lonmax": index_lonmax,
        }


def plot_regions(data: np.ndarray, latitudes: np.ndarray, longitudes: np.ndarray) -> None:
    # Plot the regions following the notebook style
    fig = plt.figure(figsize=(18,9))
    ax = fig.add_subplot(1,1,1, projection=ccrs.PlateCarree())
    ax.set_extent([-180, 180, -90, 90], ccrs.PlateCarree())
    ax.coastlines('10m', linewidth=0.5)

    # Plot the alkalinity data
    lon_grid, lat_grid = np.meshgrid(longitudes, latitudes)
    cs = ax.contourf(
        lon_grid, lat_grid, data[0, :, :],
        transform=ccrs.PlateCarree(),
        cmap='viridis',
        levels=np.linspace(np.min(data), np.amax(data), 100),
    )
    fig.colorbar(cs, ax=ax, label='Alkalinity')

    # Plot each region as a box
    for region, coordinate in region_to_box_lat_lon.items():
        lon_pts = [coordinate["lonmin"], coordinate["lonmax"], coordinate["lonmax"], coordinate["lonmin"], coordinate["lonmin"]]
        lat_pts = [coordinate["latmax"], coordinate["latmax"], coordinate["latmin"], coordinate["latmin"], coordinate["latmax"]]
        ax.plot(lon_pts, lat_pts, color="black", linewidth=1.5, transform=ccrs.PlateCarree())

    ax.set_title('15 Regions for OAE Alkalinity Addition', fontsize=10)
    plt.show()


def create_alk(input_nc, output_nc, extra_concentration):
    input_dataset = xr.open_dataset(input_nc, engine="netcdf4")
    river_parser = RiverParser(input_dataset)

    alk = np.full(
        (river_parser.len_times, river_parser.len_latitudes, river_parser.len_longitudes),
        original_river_alk_concentration,
        dtype=np.float64,
    )
    for region, coordinate in region_to_box_lat_lon.items():
        indices_of_lat_lon = river_parser.map_coordinate_to_slice_indices(coordinate)
        index_latmin = indices_of_lat_lon["index_latmin"]
        index_latmax = indices_of_lat_lon["index_latmax"]
        index_lonmin = indices_of_lat_lon["index_lonmin"]
        index_lonmax = indices_of_lat_lon["index_lonmax"]
        alk[:, index_latmin : index_latmax, index_lonmin : index_lonmax] += extra_concentration

    alk_data_array = xr.DataArray(
        alk,
        dims=("time", "grid_y_T", "grid_x_T"),
        coords={"time": input_dataset["time"], "grid_y_T": input_dataset["grid_y_T"], "grid_x_T": input_dataset["grid_x_T"]},
        name="ALK_CONC",
    )

    output_dataset = input_dataset.copy()
    output_dataset["ALK_CONC"] = alk_data_array
    output_dataset.to_netcdf(output_nc, engine="netcdf4")

    plot_regions(alk, river_parser.latitudes, river_parser.longitudes)


if __name__ == "__main__":
    input_nc = "RiverNutrients_GlobalNEWS2_DaiTren_012222_OM4p25.nc"
    output_nc = f"WithAlkalinity_{input_nc}"
    # annually
    #     alkalinity (NaOH) mass 109.08 mega ton
    #     alkalinity (NaOH) mol 2.727 Tmol
    # after 20 years, same to Kristen 54.54 Tmol
    extra_concentration = 0.00097038
    create_alk(input_nc, output_nc, extra_concentration)
