cap = 5000
daily_profit = cap*0.05
days = 83
with open("trade.txt", "r+") as file:
    for i in range(1,days):
        daily_profit = daily_profit + daily_profit*0.10
        cap+=daily_profit
        file.write(f"Day {i}, Profit: {round(daily_profit)},  Capital: {round(cap)}\n")
    
