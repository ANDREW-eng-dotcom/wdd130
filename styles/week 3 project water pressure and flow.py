
# exceeding requirements:
import re


water_density = 998.2  # improves readability by defining a constant
GRAVITY = 9.81  # m/s^2

def water_column_height(tower_height, tank_height):
    h = tower_height + (3 * tank_height) / 4
    return h


def pressure_gain_from_water_height(height):
    p = water_density * GRAVITY * height / 1000  # converts to kPa
    return p


def pressure_loss_from_pipefittings(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    # pressure loss (kPa) from friction factor and pipe geometry; negative denotes loss
    p = -friction_factor * pipe_length * water_density * fluid_velocity**2 / (2000 * pipe_diameter)
    return p


def pressure_net(tower_height, tank_height, pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    Return the net pressure gain (kPa): water column gain minus pipe-fitting losses.
    """
    gain = pressure_gain_from_water_height(water_column_height(tower_height, tank_height))
    loss = pressure_loss_from_pipefittings(pipe_diameter, pipe_length, friction_factor, fluid_velocity)
    return re



def pressure_loss_from_pipe_reduction (larger_diameter,
    fluid_velocity,reynolds_number,smaller_diameter):

    k=(0.1+(50/reynolds_number)) * (((larger_diameter/smaller_diameter)**4)-1)
    p=-k*water_density*fluid_velocity**2/2000
    return p


PVC_SCHED80_INNER_DIAMETERS=0.28687 #(meters) 11.294 inches
PVC_SCHED80_FRICTION_FACTOR=0.013   #(no units) typical for turbulent flow in PVC pipes
SUPPLY_VELOCITY=1.65                #(meters/second)
        
HDPE_SDR11_INNER_DIAMETER=0.28687   #(meters) 11.294 inches
HDPE_SDR11_FRICTION_FACTOR=0.019    #(meters)
HOUSEHOLD_VELOCITY=1.75             #(meters/second)


def main():
    tower_height = float(input("height of water tower (m): "))
    tank_height = float(input("height of water tankwalls (m): "))
    length1 = float(input("length of supply PVC pipe from the tank to lot (m): "))        
    quantity_angles = int(input("number of 90-degree angles in supply pipe: "))
    length2 = float(input("length of pipe from lot to house (HDPE) (m): "))
    
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height ("water_height")
    
    diameter = PVC_SCHED80_INNER_DIAMETERS
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = "reynolds_number"(diameter, velocity)
    loss = pressure_loss_from_pipefittings(diameter, length1, friction, velocity)
    pressure += loss

    # Move the pipe reduction loss calculation inside main after diameter is defined
    loss = pressure_loss_from_pipe_reduction(
        diameter,
        velocity,
        reynolds,
        HDPE_SDR11_INNER_DIAMETER
    )
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER    
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipefittings(diameter, length2, friction, velocity) 
    pressure += loss

    print(f"Net pressure at house: {pressure:.1f} kPa")
    
    
if __name__ == "__main__":
    main()