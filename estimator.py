# this is prototype/rapidly developed code and is not indicative of finalized/refactored code :^)
# https://github.com/turbits/SEPM-A2-CostEstimator

import csv

salesPrice = 399.99

# ================ INITIAL MENU
print("\n========================================")
print("SEPM A2 Cost Estimator")
print("University of Essex")
print("Group 1:\n- Nassar Al-Naimi\n- Charles Kuyayama\n- Abdulah Alihu Ngamjeh\n- Trevor Woodman")
print("November 2023")
print("https://github.com/turbits/SEPM-A2-CostEstimator")
print("========================================\n")


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

    # looping over the items (rows) in the array and
    # temp storing each col item in a var to use them to compile cost vars
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
p_hardwareDesignWeeks = hwDesignWeeks + hwRedesignWeeks * 2
# most likely (x1) - assumes being on schedule, average delays, average efficiency
m_hardwareUnitCost = hwUnitCost
m_hardwareDesignCost = hwDesignLabourCost + hwRedesignLabourCost
m_hardwareDesignWeeks = hwDesignWeeks + hwRedesignWeeks
# optimistic (x0.5) - assumes being ahead of schedule, minimal delays, high efficiency
o_hardwareUnitCost = hwUnitCost * 0.5
o_hardwareDesignCost = hwDesignLabourCost + hwRedesignLabourCost * 0.5
o_hardwareDesignWeeks = hwDesignWeeks + hwRedesignWeeks * 0.5


# ================ GENERATE 3POINT FOR SOFTWARE
# pessimistic (x2) - assumes being behind schedule, most delays, low efficiency
p_softwareUnitCost = swUnitCost * 2
p_softwareDesignCost = swDesignLabourCost + swRedesignLabourCost * 2
p_softwareDesignWeeks = swDesignWeeks + swRedesignWeeks * 2
# most likely (x1) - assumes being on schedule, average delays, average efficiency
m_softwareUnitCost = swUnitCost
m_softwareDesignCost = swDesignLabourCost + swRedesignLabourCost
m_softwareDesignWeeks = swDesignWeeks + swRedesignWeeks
# optimistic (x0.5) - assumes being ahead of schedule, minimal delays, high efficiency
o_softwareUnitCost = swUnitCost * 0.5
o_softwareDesignCost = swDesignLabourCost + swRedesignLabourCost * 0.5
o_softwareDesignWeeks = swDesignWeeks + swRedesignWeeks * 0.5


# ================ GENERATE 3POINT FOR TOTAL
# pessimistic
p_totalUnitCost = p_hardwareUnitCost + p_softwareUnitCost
p_totalProfitPerUnit = salesPrice - p_totalUnitCost
p_totalLabourCost = p_hardwareDesignCost + p_softwareDesignCost
p_totalLabourWeeks = p_hardwareDesignWeeks + p_softwareDesignWeeks
# most likely
m_totalUnitCost = m_hardwareUnitCost + m_softwareUnitCost
m_totalProfitPerUnit = salesPrice - m_totalUnitCost
m_totalLabourCost = m_hardwareDesignCost + m_softwareDesignCost
m_totalLabourWeeks = m_hardwareDesignWeeks + m_softwareDesignWeeks
# optimistic
o_totalUnitCost = o_hardwareUnitCost + o_softwareUnitCost
o_totalProfitPerUnit = salesPrice - o_totalUnitCost
o_totalLabourCost = o_hardwareDesignCost + o_softwareDesignCost
o_totalLabourWeeks = o_hardwareDesignWeeks + o_softwareDesignWeeks


# ================ GENERATE PERT ESTIMATES
pert_Unit = (o_totalUnitCost + (4 * m_totalUnitCost) + p_totalUnitCost) / 6
pert_LabourCost = (o_totalLabourCost + (4 * m_totalLabourCost) + p_totalLabourCost) / 6
pert_LabourWeeks = (o_totalLabourWeeks + (4 * m_totalLabourWeeks) + p_totalLabourWeeks) / 6


# ================ OUTPUT ESTIMATES
# pessimistic
print("\n========================================")
print("Estimation Results")
print("========================================")
print("These estimations are based on the 3-point technique:\n"
      "- Pessimistic {P = 2(M)}: assumes being behind schedule, has the most delays, and low efficiency\n"
      "- Most Likely {M}: 1:1 costs from provided BOMs, assumes being on schedule, average delays, and average efficiency\n"
      "- Optimistic {O = 0.5(M)}: assumes being ahead of schedule, minimal delays, and high efficiency")
print("Following these points is a PERT estimation, which is based on the following formula: Mean = O + 4M + P / 6")
print("We have included the PERT estimations for unit cost and labour costs.")
print("========================================")
print(f"Pessimistic Estimation (P):\n"
      f"- Unit Cost: {'£{:,.2f}'.format(p_totalUnitCost)}\n"
      f"- Profit/unit: {'£{:,.2f}'.format(p_totalProfitPerUnit)}\n"
      f"- Labour Cost: {'£{:,.2f}'.format(p_totalLabourCost)}\n"
      f"- Labour Weeks: {p_totalLabourWeeks} wks")
print("========================================")
print(f"Most Likely Estimation (M):\n"
      f"- Unit Cost: {'£{:,.2f}'.format(m_totalUnitCost)}\n"
      f"- Profit/unit: {'£{:,.2f}'.format(m_totalProfitPerUnit)}\n"
      f"- Labour Cost: {'£{:,.2f}'.format(m_totalLabourCost)}\n"
      f"- Labour Weeks: {m_totalLabourWeeks} wks")
print("========================================")
print(f"Optimistic Estimation (O):\n"
      f"- Unit Cost: {'£{:,.2f}'.format(o_totalUnitCost)}\n"
      f"- Profit/unit: {'£{:,.2f}'.format(o_totalProfitPerUnit)}\n"
      f"- Labour Cost: {'£{:,.2f}'.format(o_totalLabourCost)}\n"
      f"- Labour Weeks: {o_totalLabourWeeks} wks")

print("========================================")
print("PERT Estimations (Mean)")
print(f"- Unit Cost: {'£{:,.2f}'.format(pert_Unit)}")
print(f"- Labour Cost: {'£{:,.2f}'.format(pert_LabourCost)}")
print(f"- Labour Weeks: {pert_LabourWeeks} weeks")
print("========================================\n")
