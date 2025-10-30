"""
Compute total water flux at 15 regions, then
given total mega ton of CaO determine OH- concentration

--------------------------------------------------------------------------------
Variable             Shape                Units                Description                   
--------------------------------------------------------------------------------
i                    (1440,)              N/A                  Grid position along first...  
j                    (1080,)              N/A                  Grid position along secon...  
IQ                   (1441,)              N/A                  Grid position along first...  
JQ                   (1081,)              N/A                  Grid position along secon...  
time                 (12,)                N/A                  Time                          
lon                  (1080, 1440)         degrees_east         Longitude of cell centers     
lat                  (1080, 1440)         degrees_north        Latitude of cell centers      
lon_crnr             (1081, 1441)         degrees_east         Longitude of mesh nodes       
lat_crnr             (1081, 1441)         degrees_north        Latitude of mesh nodes        
area                 (1080, 1440)         m2                   Cell area                     
runoff               (12, 1080, 1440)     kg m-2 s-1           Dai_Trenberth River Runoff 
"""


import numpy as np
import xarray as xr

from utils import region_to_box_lat_lon


class RiverParser:
    def __init__(self, dataset):
        self.times = dataset.variables["time"]
        self.latitudes = dataset.variables["lat"]
        self.longitudes = np.array(dataset.variables["lon"])
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

    def map_coordinate_to_indices(self, coordinate: dict[str, float]) -> tuple[tuple[int, int]]:
        ge_latmin = np.greater_equal(self.latitudes, coordinate["latmin"])
        le_latmax = np.less_equal(self.latitudes, coordinate["latmax"])
        ge_lonmin = np.greater_equal(self.longitudes, coordinate["lonmin"])
        le_lonmax = np.less_equal(self.longitudes, coordinate["lonmax"])
        in_lat = np.logical_and(ge_latmin, le_latmax)
        in_lon = np.logical_and(ge_lonmin, le_lonmax)
        return np.logical_and(in_lat, in_lon)


def compute_total_water_flux(input_nc) -> float:
    input_dataset = xr.open_dataset(input_nc, engine="netcdf4")
    time = input_dataset.variables["time"]
    area = input_dataset.variables["area"]
    runoff = input_dataset.variables["runoff"]
    river_parser = RiverParser(input_dataset)

    total_water_mass = 0
    for region, coordinate in region_to_box_lat_lon.items():
        indices = river_parser.map_coordinate_to_indices(coordinate)
        area_region = area[np.where(indices)]
        mass = 0
        for month_index in range(12):
            runoff_month = runoff[month_index, :, :]
            runoff_month_region = runoff_month[np.where(indices)]
            # kg s-1
            discharge = np.sum(area_region * runoff_month_region, axis=(-2, -1))
            # kg = kg s-1 * 1 month
            mass += discharge * 30 * 24 * 60 * 60
        total_water_mass += mass

    return total_water_mass


if __name__ == "__main__":
    alkalinity_name = "NaOH"
    molar_mass = 40
    # mega ton
    alkalinity_mass = 40 * 54.54 / 20
    # mol
    alkalinity_mol = alkalinity_mass * 1e6 * 1e3 * 1e3 / molar_mass

    # kg
    total_water_mass = compute_total_water_flux("runoff.daitren.clim.1440x1080.v20180328.nc")
    # m3
    total_water_volume = total_water_mass / 1e3

    # Tmol = 1e12 mol
    alkalinity_Tmol = alkalinity_mol / 1e12
    # mol m-3
    concentration = alkalinity_mol / total_water_volume
    # mol L-1
    concentration_mol_L = concentration / 1e3
    pH = 14 + np.log(concentration_mol_L) / np.log(10)

    print(f"alkalinity ({alkalinity_name}) mass {alkalinity_mass} mega ton")
    print(f"alkalinity ({alkalinity_name}) mol {alkalinity_Tmol} Tmol")
    print(f"concentration {concentration} mol m-3")
    print(f"pH {pH}")
