
# dollar store discount - cost and display using functions

# calculate pre-tax cost with conditional discount
def calcCost(count):
    """
    Parameters
    ----------
    count : number of items bought

    Returns
    -------
    cost : cost with or without discount

    """
    if count >= 5:
       discount = .05 * count
    
    discount = 0
    cost = count - discount
    return cost

# function to display lines with a consistent format
def displayLine(label,amount):
    print(format(label, "10s"), format(amount,".2f"))

# display results
def display(cost, tax):
    """
    Parameters
    ----------
    cost : calculated cost - discount
    tax : tax amount

    Returns
    -------
    None.

    """
    
    print("\nResults:")
    
    
    #example
    #cost = 5
    #tax = 0.075
    displayLine("Net Cost:", cost)
    displayLine("Tax:", tax)
    displayLine("After tax:", cost+tax)



