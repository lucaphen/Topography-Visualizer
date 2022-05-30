import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
import pandas as pd

# Go to this website: https://topex.ucsd.edu/cgi-bin/get_data.cgi
# Find latitude and longitude of area you want to visualize and box it
# Generate Results and copy into a .txt file

# Load data
data = np.loadtxt('Madagascar_Elevation.txt')

# Check data for NaN values
# pdata = pd.read_csv('Madagascar_Elevation.txt', header=None)
# pdata.isnull().any()

# Structure the data into Latitude and Longitude
long = data[:,0]    # Longitude
lat = data[:,1]     # Latitude
elev = data[:,2]    # Elevation

# Specify number of points for accuracy
points = 1000000    # Number of desired points

# Create the Grid
[x,y]=np.meshgrid(
    np.linspace(np.min(long),np.max(long),int(np.sqrt(points))),
    np.linspace(np.min(lat),np.max(lat),int(np.sqrt(points)))
);

# Interpolate data
z = griddata((long, lat), elev, (x,y), method='linear')
x = np.matrix.flatten(x)    # Gridded Longitude
y = np.matrix.flatten(y)    # Gridded Latitude
z = np.matrix.flatten(z)    # Gridded Elevation

# Data Visualization
plt.scatter(x,y,1,z,cmap='terrain')
plt.colorbar(label='Elevation above sea level [m]')
plt.xlabel('Longitude [°]')
plt.ylabel('Latitude [°]')

# Further visualization tweaks
plt.gca().set_aspect('equal')

plt.show()