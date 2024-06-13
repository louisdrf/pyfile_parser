def displayNumberStatistics(numberList):
    numberList = [float(num) for num in numberList if num.strip().replace('.', '', 1).isdigit()]
    average = float(sum(numberList) / len(numberList))
    print(f"max : {max(numberList)} / min : {min(numberList)} / moyenne : {average:.2f}")
    
def displayBoolStatistics(boolList):
        print(boolList)
    