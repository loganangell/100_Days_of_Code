# Define the Hotel Name
hotel_name = str(input('What is the name of the hotel: '))

# Define inputs
total_rooms = float(input('How many rooms does the hotel have: '))
rooms_sold = float(input('How many hotel rooms were sold: '))
hotel_revenue = float(input('Enter the total room revenue generated ($): '))

# Calcuate KPIs with room information inputs
occupancy = (rooms_sold / total_rooms) * 100
adr = hotel_revenue / rooms_sold
revpar = adr * (occupancy / 100)

# Display KPI results

print(f"\n --- {hotel_name} KPI --- ")
print(f'Occupancy Rate: {occupancy:.2f}%')
print(f'Average Daily Rate (ADR): ${adr:.2f}')
print(f'Revenue per Available Room (RevPAR): ${revpar:.2f}')