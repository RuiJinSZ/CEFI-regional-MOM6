"""
Add alkalinity to 15 regions with given value, unit mol m^-3

pH uses mol L-1, and 1 mol L^-1 = 1000 mol m^-3
"""


import numpy as np
import xarray as xr

import matplotlib.pyplot as plt

import cartopy
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.ticker as mticker
import pandas as pd


region_to_box_lat_lon = {
    "Salish Sea/Puget Sound": {
        "latmin": 47.0,
        "latmax": 49.0,
        "lonmin": -126.0,
        "lonmax": -122.0
    },
    "Gulf of Mexico, near Houston": {
        "latmin": 28.0,
        "latmax": 30.0,
        "lonmin": -96.0,
        "lonmax": -93.0
    },
    "Norfolk VA": {
        "latmin": 36.0,
        "latmax": 38.0,
        "lonmin": -78.0,
        "lonmax": -75.0
    },
    "Halifax Habour": {
        "latmin": 43.0,
        "latmax": 46.0,
        "lonmin": -65.0,
        "lonmax": -61.0
    },
    "At the Amazon": {
        "latmin": -3.0,
        "latmax": 2.0,
        "lonmin": -51.0,
        "lonmax": -47.0
    },
    "Sao Francisco River": {
        "latmin": -12.0,
        "latmax": -9.0,
        "lonmin": -38.0,
        "lonmax": -34.0
    },
    "Ortigueira estuary": {
        "latmin": 43.0,
        "latmax": 45.0,
        "lonmin": -9.0,
        "lonmax": -7.0
    },
    "Elbe Delta": {
        "latmin": 53.0,
        "latmax": 55.0,
        "lonmin": 8.0,
        "lonmax": 10.0
    },
    "Tana River Delta Kenya": {
        "latmin": -4.5,
        "latmax": -1.0,
        "lonmin": 39.0,
        "lonmax": 43.0
    },
    "Persian Gulf": {
        "latmin": 24.0,
        "latmax": 30.0,
        "lonmin": 48.0,
        "lonmax": 56.0
    },
    "Bay of Bengal": {
        "latmin": 19.0,
        "latmax": 23.0,
        "lonmin": 88.0,
        "lonmax": 92.0
    },
    "Singapore": {
        "latmin": 0.0,
        "latmax": 3.0,
        "lonmin": 101.0,
        "lonmax": 106.0
    },
    "Yellow Sea": {
        "latmin": 35.0,
        "latmax": 40.0,
        "lonmin": 124.0,
        "lonmax": 128.0
    },
    "West coast Australia, Indian Ocean": {
        "latmin": -33.0,
        "latmax": -28.0,
        "lonmin": 112.0,
        "lonmax": 117.0
    },
    "Timor-Arafura Sea": {
        "latmin": -14.0,
        "latmax": -9.0,
        "lonmin": 133.0,
        "lonmax": 138.0
    }
}


class RiverParser:
    def __init__(self, dataset):
        self.times = dataset.variables["time"]
        self.latitudes = dataset.variables["grid_y_T"]
        self.longitudes = dataset.variables["grid_x_T"]

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
            if longitude <= -180:
                longitude += 360
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
    cs = ax.contourf(lon_grid, lat_grid, data[0, :, :], transform=ccrs.PlateCarree(), cmap='viridis', levels=np.linspace(0, np.amax(data), 100))
    fig.colorbar(cs, ax=ax, shrink=0.5, label='Alkalinity')

    # Plot each region as a box
    for region, coordinate in region_to_box_lat_lon.items():
        lon_pts = [coordinate["lonmin"], coordinate["lonmax"], coordinate["lonmax"], coordinate["lonmin"], coordinate["lonmin"]]
        lat_pts = [coordinate["latmax"], coordinate["latmax"], coordinate["latmin"], coordinate["latmin"], coordinate["latmax"]]
        ax.plot(lon_pts, lat_pts, color="black", linewidth=1.5, transform=ccrs.PlateCarree())

    ax.set_title('15 Regions for OAE Alkalinity Addition', fontsize=10)
    plt.show()


def create_alk(input_nc, output_nc, concentration):
    input_dataset = xr.open_dataset(input_nc, engine="netcdf4")
    river_parser = RiverParser(input_dataset)

    alk = np.ones((river_parser.len_times, river_parser.len_latitudes, river_parser.len_longitudes), dtype=np.float64)
    for region, coordinate in region_to_box_lat_lon.items():
        indices_of_lat_lon = river_parser.map_coordinate_to_slice_indices(coordinate)
        index_latmin = indices_of_lat_lon["index_latmin"]
        index_latmax = indices_of_lat_lon["index_latmax"]
        index_lonmin = indices_of_lat_lon["index_lonmin"]
        index_lonmax = indices_of_lat_lon["index_lonmax"]
        alk[:, index_latmin : index_latmax, index_lonmin : index_lonmax] = concentration

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
    output_nc = "WithAlkalinity_RiverNutrients_GlobalNEWS2_DaiTren_012222_OM4p25.nc"
    concentration_in_mol_L = 1.0
    concentration_in_mol_m3 = 1000.0 * concentration_in_mol_L
    create_alk(input_nc, output_nc, concentration_in_mol_m3)
