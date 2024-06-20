'''
Gülnur Uzun, Alper Tanrıkulu

Q3

(50 points) A scientist is growing two types of bacteria in a flask. Each type of bacteria produces a chemical that is toxic to the other one. Their features are as follows:
One mole of Bacteria X produces 0.41 mole of Bacteria X and 0.5 mole of Toxin X every hour.
One mole of Bacteria Y produces 0.55 mole of Bacteria Y and one mole of Toxin Y every hour.
One mole of Toxin X kills 0.5% of Bacteria Y every hour.
One mole of Toxin Y kills 1% of Bacteria X every hour.
5% of Toxin Y degrades every hour.
Initial conditions: @ Time = 0 hours : Bacteria X = Bacteria Y = 10 moles, Toxin X = Toxin Y = 0 moles.
Write a Python script that calculates concentrations of Bacteria X, Bacteria Y, Toxin X and Toxin Y in the flask every hour and report it as:
(e.g. Hour 5: x moles of Bacteria X, y moles of Bacteria Y, z moles of Toxin X, w moles of Toxin Y.)
The simulation should stop when the change in concentrations are less than 0.1% (steady state conditions) in an hour or when a maximum of 1000 iterations are done.


'''

bx = 10
by = 10
tx = 0
ty = 0

max_iteration = 1000

for i in range(0,max_iteration):

    # calculations of concentrations in according to given information
    bx1 = (bx+(bx*0.41)) - ((bx*ty*1)/100)
    by1 = (by+(by*0.55)) - ((by*tx*0.5)/100)
    tx1 = tx + bx*0.5
    ty1 = (ty + (by*1)) - ((ty*5)/100)
    
    # concentrations can't be minus. 
    if (bx1 <= 0):
        bx1 = 0
    if (by1 <= 0):
        by1 = 0
    if (tx1 <= 0):
        tx1 = 0
    if (ty1 <= 0):
        ty1 = 0
        
    print(f"Hour {i}:\nmoles of bacteria X: {bx}\nmoles of bacteria Y: {by}\nmoles of toxin X: {tx}\nmoles of toxin Y: {ty}\n")
    if ( i == 0 ): # to exclude first hour. Because toxins are having 0 which makes the denominator 0.
        change_bx = ((bx1-bx)/bx) * 100
        change_by = ((by1-by)/by) * 100
        change_tx = "First iteration"
        change_ty = "First iteration"

        
    else:
        # if the concentration is not 0, it calculates the change percentage of the concentration.
        # if the concentration of bacteria or toxin is 0, it assigns 0 to change percentage. 
        # in the other hand we can't make calculation when 0 be in denominator.
        change_bx = ((bx1 - bx) / bx) * 100 if bx != 0 else 0 # it is simple if else statement in one line.
        change_by = ((by1 - by) / by) * 100 if by != 0 else 0
        change_tx = ((tx1 - tx) / tx) * 100 if tx != 0 else 0
        change_ty = ((ty1 - ty) / ty) * 100 if ty != 0 else 0

    # to stop the iteration when the change percentage is less than 0.1 for booth bacteria concentration.
    #We didn't understand very well if the one of the concentrations are enough to stop the iteration. 
    #if it is please use the code below with "or" statement.
    #if (change_bx < 0.1 and change_bx > -0.1) or (change_by < 0.1 and change_by > -0.1): 
    if (change_bx < 0.1 and change_bx > -0.1) and (change_by < 0.1 and change_by > -0.1): # change of bacteria X stopped    
        print("there is no difference among concentrations. Iteration have been stopped\nIteration number:", i)
        break

    print(f"Change in bacteria X: {change_bx}\nChange in bacteria Y: {change_by}\nChange in toxin X: {change_tx}\nChange in toxin Y: {change_ty}\n")
    
    # to assign new concentrations to old concentrations
    bx = bx1 
    by = by1
    tx = tx1
    ty = ty1
    print("--------------------------------------------------")
    
'''
Summary:

The change in toxins is not calculated in the first round because there are initially 0 moles of toxins present. 
When the percentage change formula is applied, the denominator becomes 0, making it uncalculable.

Between the 3rd and 4th hours, the bacterial population peaks.

Between the 6th and 7th hours, the X bacterial population is completely wiped out. 
Since there is no production of toxin X, toxin X stabilizes at 48 moles.

The changes in the concentrations of Bacteria X and Toxin X remain constant, and are found to be 0.

The bacteria continue to multiply, leading to the continued increase in Toxin Y.

'''