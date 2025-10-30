import numpy as np
import xarray as xr
import sys


def print_nc(nc_path, champion_name=None):
    """
    Print comprehensive NetCDF file information including units
    
    Parameters:
    nc_path (str): Path to NetCDF file
    champion_name (str): Optional variable name to analyze in detail
    """
    try:
        dataset = xr.open_dataset(nc_path, engine="netcdf4")
        
        print("🔬 NETCDF FILE ANALYSIS")
        print("=" * 80)
        print(f"File: {nc_path}")
        print()
        
        # Print basic dataset info
        print("📋 DATASET OVERVIEW:")
        print("-" * 40)
        print(dataset)
        print()
        
        # Print dimensions
        print("📏 DIMENSIONS:")
        print("-" * 40)
        for dim_name, dim_size in dataset.dims.items():
            print(f"  {dim_name}: {dim_size}")
        print()
        
        # Print global attributes
        print("🌐 GLOBAL ATTRIBUTES:")
        print("-" * 40)
        for attr_name, attr_value in dataset.attrs.items():
            if len(str(attr_value)) > 100:
                attr_value = str(attr_value)[:97] + "..."
            print(f"  {attr_name}: {attr_value}")
        print()
        
        # Print variables with units and descriptions
        print("📊 VARIABLES WITH UNITS:")
        print("-" * 80)
        print(f"{'Variable':<20} {'Shape':<20} {'Units':<20} {'Description':<30}")
        print("-" * 80)
        
        for var_name, var_data in dataset.variables.items():
            # Get units
            units = var_data.attrs.get('units', 
                   var_data.attrs.get('unit', 
                   var_data.attrs.get('Units', 'N/A')))
            
            # Get description
            description = var_data.attrs.get('long_name', 
                         var_data.attrs.get('description', 
                         var_data.attrs.get('standard_name', 'N/A')))
            
            # Truncate long strings
            if len(str(units)) > 18:
                units = str(units)[:15] + "..."
            if len(str(description)) > 28:
                description = str(description)[:25] + "..."
            
            shape_str = str(var_data.shape)
            print(f"{var_name:<20} {shape_str:<20} {units:<20} {description:<30}")
        
        print()
        
        # Detailed variable information
        print("🔍 DETAILED VARIABLE INFORMATION:")
        print("=" * 80)
        
        for var_name, var_data in dataset.variables.items():
            print(f"\n📈 Variable: {var_name}")
            print(f"   Shape: {var_data.shape}")
            print(f"   Dimensions: {var_data.dims}")
            print(f"   Data type: {var_data.dtype}")
            
            # Print all attributes
            if var_data.attrs:
                print("   Attributes:")
                for attr_name, attr_value in var_data.attrs.items():
                    if attr_name.lower() in ['units', 'unit']:
                        print(f"     🏷️  {attr_name}: {attr_value}")
                    elif attr_name.lower() in ['long_name', 'description', 'standard_name']:
                        print(f"     📝 {attr_name}: {attr_value}")
                    else:
                        print(f"      {attr_name}: {attr_value}")

            # Print basic statistics for numeric variables
            if np.issubdtype(var_data.dtype, np.number) and var_data.size > 0:
                try:
                    # Use xarray's built-in methods which handle large datasets efficiently
                    print("   Statistics:")
                    print(f"     Min:  {float(var_data.min().values)}")
                    print(f"     Max:  {float(var_data.max().values)}")
                    print(f"     Mean: {float(var_data.mean().values):.6f}")
                    print(f"     Std:  {float(var_data.std().values):.6f}")
                except Exception as e:
                    print(f"   Statistics: Error computing - {e}")
            
            print("-" * 60)
        
        # Analyze champion variable if specified
        if champion_name:
            print(f"\n🏆 CHAMPION VARIABLE ANALYSIS: {champion_name}")
            print("=" * 60)
            
            if champion_name in dataset.variables:
                champion = dataset.variables[champion_name]
                
                print(f"Variable: {champion_name}")
                print(f"Shape: {champion.shape}")
                print(f"Dimensions: {champion.dims}")
                print(f"Data type: {champion.dtype}")
                
                # Print units and description
                units = champion.attrs.get('units', 'N/A')
                description = champion.attrs.get('long_name', 
                            champion.attrs.get('description', 'N/A'))
                print(f"Units: {units}")
                print(f"Description: {description}")
                
                # Print min/max as in original code
                try:
                    min_val = float(champion.min().values)
                    max_val = float(champion.max().values)
                    print(f"Minimum value: {min_val}")
                    print(f"Maximum value: {max_val}")
                    print(f"Range: {max_val - min_val}")
                    
                    # Additional statistics
                    mean_val = float(champion.mean().values)
                    std_val = float(champion.std().values)
                    print(f"Mean: {mean_val:.6f}")
                    print(f"Standard deviation: {std_val:.6f}")
                    
                except Exception as e:
                    print(f"Error computing statistics: {e}")
                
                # Print all attributes for champion variable
                print("\nAll attributes:")
                for attr_name, attr_value in champion.attrs.items():
                    print(f"  {attr_name}: {attr_value}")
                    
            else:
                print(f"❌ Variable '{champion_name}' not found in dataset!")
                print("Available variables:")
                for var_name in dataset.variables.keys():
                    print(f"  - {var_name}")
        
        # Close dataset
        dataset.close()
        print("\n✅ Analysis completed successfully!")
        
    except Exception as e:
        print(f"❌ Error reading NetCDF file: {e}")
        return False
    
    return True


def main():
    """Main entry point with command line support"""
    if len(sys.argv) < 2:
        print("Usage: python script.py <netcdf_file> [champion_variable]")
        print("Example: python script.py data.nc temperature")
        nc_path = input("Enter NetCDF file path: ").strip()
        if not nc_path:
            print("No file path provided. Exiting.")
            return
        champion_name = input("Enter champion variable name (optional): ").strip()
        champion_name = champion_name if champion_name else None
    else:
        nc_path = sys.argv[1]
        champion_name = sys.argv[2] if len(sys.argv) > 2 else None
    
    print_nc(nc_path, champion_name)


if __name__ == "__main__":
    main()
