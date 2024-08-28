cap = 5000
daily_profit = cap*0.05
days = 101
for i in range(1,days):
    daily_profit = daily_profit + daily_profit*0.10
    cap+=daily_profit
    print(f"Day {i}, Profit: {round(daily_profit)},  Capital: {round(cap)}")
