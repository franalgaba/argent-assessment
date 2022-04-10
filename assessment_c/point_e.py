def calculate_apy(amount, interest, years, borrowed=False):
    return amount * ((1 + (interest/100.0)) ** years)


liquidation_limit = 0.8

# ETH position
eth_amount = 100
eth_interest = 2

# DAI position
dai_amount = 100000
dai_interest = 10

# USDC position
usdc_amount = -150000
usdc_interest = 15

risk_after_years = None
liquidation_after_years = None

risk_hf = None
liquidation_hf = None

for years in range(1, 10):
    eth_apy = calculate_apy(eth_amount, eth_interest, years)
    dai_apy = calculate_apy(dai_amount, dai_interest, years)
    usdc_apy = - calculate_apy(usdc_amount, usdc_interest, years)
    result = ((eth_apy + (dai_apy / 2000)) * 0.8) / (usdc_apy / 2000)
    if result < 1 and not risk_after_years:
        risk_after_years = years
        risk_hf = result
    if result < liquidation_limit and not liquidation_after_years:
        liquidation_after_years = years
        liquidation_hf = result
    if liquidation_after_years and risk_after_years:
        break

print(f"Number of years to be in risk of liquidation: {risk_after_years} with HF: {risk_hf:.2f}")
print(f"Number of years to be liquidated: {liquidation_after_years} with HF: {liquidation_hf:.2f}")
