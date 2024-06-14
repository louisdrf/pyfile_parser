def displayNumberStatistics(numberList):
    numberList = [float(num) for num in numberList if num.strip().replace('.', '', 1).isdigit()]
    average = float(sum(numberList) / len(numberList))
    print(f"max : {max(numberList)} / min : {min(numberList)} / moyenne : {average:.2f}")
    
def displayBoolStatistics(bool_list):
    total = len(bool_list)
    
    if bool_list[0] in {'0', '1'}:
        count_falses = bool_list.count('0')
        count_trues = bool_list.count('1')
    else:
        count_falses = bool_list.count("false")
        count_trues = bool_list.count("true")

    falses = (count_falses / total) * 100
    trues = (count_trues / total) * 100
    
    print(f"faux : {falses:.1f} % | vrais : {trues:.1f} %")