
import math

total_city_coverage_area = 1300
radius = 4
a = (2.591*(radius**2))
Nc = round(total_city_coverage_area/a)

allocated_spectrum = 40000
channel_width = 60
N = 7
C = round(allocated_spectrum/(channel_width*N))

A = 84
max_c_t = math.floor(Nc*A)

U = round(max_c_t/0.03)

no_of_channel = math.floor(allocated_spectrum/channel_width)
no_of_m_p_c = math.floor(U/no_of_channel)

g = C * Nc
print(f"Cells (Nc): {Nc}")
print(f"Channels per cell (C): {C}")
print(f"Total carried traffic (Erlangs): {max_c_t}")
print(f"Users supported (U): {U}")
print(f"Mobiles per channel: {no_of_m_p_c}")
print(f"Theoretical max simultaneous users: {g}")
