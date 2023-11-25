# this is prototype/rapidly developed code and is not indicative of refactored code :^)
# https://github.com/turbits/SEPM-A2-CostEstimator

import csv

# ================ INITIAL MENU
print("")
print("========================================")
print("SEPM A2 Cost Estimator")
print("University of Essex")
print("Group 1:\n- Nassar Al-Naimi\n- Charles Kuyayama\n- Abdulah Alihu Ngamjeh\n- Trevor Woodman")
print("November 2023")
print("https://github.com/turbits/SEPM-A2-CostEstimator")
print("========================================")
print("")


# ================ HARDWARE ESTIMATE COMPILATION FROM hw_spec.csv
hwHeader = []
hwItems = []
hwUnitCost = 0
hwMfgCost = 0
hwDesignWeeks = 0
hwDesignLabourCost = 0
hwRedesignWeeks = 0
hwRedesignLabourCost = 0

# opening the hw_spec file. 'r' means opening the file as reading mode,
# and it is the default, but I prefer to be explicit
with open('csv/hw_spec.csv', 'r') as hwSpecFile:
    hwCsvReader = csv.reader(hwSpecFile)
    hwHeader = next(hwCsvReader)

    # compiling an array of the rows(items) in the hw_spec file
    for row in hwCsvReader:
        hwItems.append(row)

    # looping over the items in the array
    for item in hwItems:
        itemUnitCost = float(item[1])
        itemQuantity = float(item[2])
        itemMfgCost = float(item[3])
        itemDesignLabourer = str(item[4])
        itemDesignWeeks = float(item[5])
        itemDesignLabourCost = float(item[6])
        itemRedesignWeeks = float(item[7])
        itemRedesignLabourCost = float(item[8])

        # compiling totals for each col where appropriate
        if itemQuantity > 1:
            hwUnitCost += (itemUnitCost * itemQuantity)
        else:
            hwUnitCost += itemUnitCost

        # manufacturing costs
        hwMfgCost += itemMfgCost

        # design costs
        hwDesignWeeks += itemDesignWeeks
        # only calc cost if there is work done
        if itemDesignLabourCost > 0:
            hwDesignLabourCost += (itemDesignWeeks * itemDesignLabourCost)

        # redesign costs
        hwRedesignWeeks += itemRedesignWeeks
        # only calc cost if there is work done
        if itemRedesignLabourCost > 0:
            hwRedesignLabourCost += (itemRedesignWeeks * itemRedesignLabourCost)


# ================ SOFTWARE ESTIMATE COMPILATION FROM sw_spec.csv
swHeader = []
swItems = []
swUnitCost = 0
swMfgCost = 0
swDesignWeeks = 0
swDesignLabourCost = 0
swRedesignWeeks = 0
swRedesignLabourCost = 0

# opening the sw_spec file, basically the same as the hw_spec file
# but this one has different columns
with open('csv/sw_spec.csv', 'r') as swSpecFile:
    swCsvReader = csv.reader(swSpecFile)
    swHeader = next(swCsvReader)

    # compiling an array of the rows(items) in the hw_spec file
    for row in swCsvReader:
        swItems.append(row)

    # looping over the items in the array
    for item in swItems:
        itemUnitCost = float(item[1])
        itemDesignLabourer = str(item[2])
        itemDesignWeeks = float(item[3])
        itemDesignLabourCost = float(item[4])
        itemRedesignWeeks = float(item[5])
        itemRedesignLabourCost = float(item[6])

        # compiling totals for each col where appropriate
        swUnitCost += itemUnitCost

        # design costs
        swDesignWeeks += itemDesignWeeks
        # only calc cost if there is work done
        if itemDesignLabourCost > 0:
            swDesignLabourCost += (itemDesignWeeks * itemDesignLabourCost)

        # redesign costs
        swRedesignWeeks += itemRedesignWeeks
        # only calc cost if there is work done
        if itemRedesignLabourCost > 0:
            swRedesignLabourCost += (itemRedesignWeeks * itemRedesignLabourCost)


# ================ TOTALS
totalUnitCost = hwUnitCost + swUnitCost
totalDesignCost = hwDesignLabourCost + hwRedesignLabourCost + swDesignLabourCost + swRedesignLabourCost


# ================ 3POINT GENERATION
# P = 2(M) // pessimistic
# M = at cost // most likely
# O = 0.5(M) // optimistic


# ================ GENERATE 3POINT FOR HARDWARE
# pessimistic (x2) - assumes being behind schedule, most delays, low efficiency
p_hardwareUnitCost = hwUnitCost * 2
p_hardwareDesignCost = hwDesignLabourCost + hwRedesignLabourCost * 2
# most likely (x1) - assumes being on schedule, average delays, average efficiency
m_hardwareUnitCost = hwUnitCost
m_hardwareDesignCost = hwDesignLabourCost + hwRedesignLabourCost
# optimistic (x0.5) - assumes being ahead of schedule, minimal delays, high efficiency
o_hardwareUnitCost = hwUnitCost * 0.5
o_hardwareDesignCost = hwDesignLabourCost + hwRedesignLabourCost * 0.5


# ================ GENERATE 3POINT FOR SOFTWARE
# pessimistic (x2) - assumes being behind schedule, most delays, low efficiency
p_softwareUnitCost = swUnitCost * 2
p_softwareDesignCost = swDesignLabourCost + swRedesignLabourCost * 2
# most likely (x1) - assumes being on schedule, average delays, average efficiency
m_softwareUnitCost = swUnitCost
m_softwareDesignCost = swDesignLabourCost + swRedesignLabourCost
# optimistic (x0.5) - assumes being ahead of schedule, minimal delays, high efficiency
o_softwareUnitCost = swUnitCost * 0.5
o_softwareDesignCost = swDesignLabourCost + swRedesignLabourCost * 0.5


# ================ GENERATE 3POINT FOR TOTAL
# pessimistic
p_totalUnitCost = '£{:,.2f}'.format(p_hardwareUnitCost + p_softwareUnitCost)
p_totalLabourCost = '£{:,.2f}'.format(p_hardwareDesignCost + p_softwareDesignCost)
# most likely
m_totalUnitCost = '£{:,.2f}'.format(m_hardwareUnitCost + m_softwareUnitCost)
m_totalLabourCost = '£{:,.2f}'.format(m_hardwareDesignCost + m_softwareDesignCost)
# optimistic
o_totalUnitCost = '£{:,.2f}'.format(o_hardwareUnitCost + o_softwareUnitCost)
o_totalLabourCost = '£{:,.2f}'.format(o_hardwareDesignCost + o_softwareDesignCost)


# ================ OUTPUT ESTIMATES
# pessimistic
print("")
print("========================================")
print("Estimation Results")
print("========================================")
print("These estimations are based on the 3-point technique:\n"
      "- Pessimistic {P = 2(M)}: assumes being behind schedule, has the most delays, and low efficiency\n"
      "- Most Likely {M}: 1:1 costs from provided BOMs, assumes being on schedule, average delays, and average efficiency\n"
      "- Optimistic {O = 0.5(M)}: assumes being ahead of schedule, minimal delays, and high efficiency")
print("")
print("========================================")
print(f"Pessimistic Estimation (P):\n- Unit Cost: {p_totalUnitCost}\n- Labour Cost: {p_totalLabourCost}\n")
print("========================================")
print(f"Most Likely Estimation (M):\n- Unit Cost: {m_totalUnitCost}\n- Labour Cost: {m_totalLabourCost}\n")
print("========================================")
print(f"Optimistic Estimation (O):\n- Unit Cost: {o_totalUnitCost}\n- Labour Cost: {o_totalLabourCost}\n")
