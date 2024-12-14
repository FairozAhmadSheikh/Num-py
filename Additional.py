
investment_in_bitcoin = 1.9
bitcoin_to_usd = 40000

# 1) write a function to calculate bitcoin to usd
def bitcoinToUSD(investment_in_bitcoin, bitcoin_to_usd):
  usd_value =investment_in_bitcoin*bitcoin_to_usd
  return usd_value

investment_in_usd = bitcoinToUSD(investment_in_bitcoin, bitcoin_to_usd)

if investment_in_usd <=30000:
  print("Investment below $30,000! SELL!")
else:
  print("Investment above $30,000")

"""#  """
investment_in_bitcoin = 1.2
bitcoin_to_usd = 40000

# 1) Write a function to calculate bitcoin to USD
def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
    usd_value = bitcoin_amount * bitcoin_value_usd
    return usd_value

# 2) Use the function to calculate if the value is below $30,000
investment_in_usd = bitcoinToUSD(investment_in_bitcoin, bitcoin_to_usd)

if investment_in_usd <= 30000:  # Check if the investment value is below $30,000
    print("Investment below $30,000! SELL!")
else:
    print("Investment above $30,000")
