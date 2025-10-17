'''Business Profit CalculatorCalculates profit and margin percentagefrom revenue and cost data’’’

# Get revenue from user

revenue = float(input("Enter total revenue: $"))
# Get costs from user  

costs = float(input("Enter total costs: $"))

# Calculate profit

profit = revenue – costs

# Calculate profit margin percentage

margin = (profit / revenue) * 100

# Display results

print("\n--- Financial Summary ---")
print(f"Revenue: ${revenue:,.2f}")
print(f"Costs: ${costs:,.2f}")
print(f"Profit: ${profit:,.2f}")
print(f"Profit Margin: {margin:.1f}%")

class BuisnessCalculator():
    
    revenue = float(input("Enter total revenue: $"))
    costs = float(input("Enter total costs: $"))
    
    def __init__(self):
        pass
    
    def calculate_profit(revenue, costs):
        profit = revenue - costs 
        return profit
    
    def calculate_margin(revenue, costs):
        margin = (profit / revenue) * 100
        return margin
    


revenue = float(input("Enter total revenue: $"))
costs = float(input("Enter total costs: $"))

def calculate_profit(revenue, costs):
    profit = revenue - costs 
    return profit
def calculate_margin(revenue, costs):
    margin = (profit / revenue) * 100
    return margin
