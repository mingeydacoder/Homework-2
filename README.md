# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

Slippage in Automated Market Makers (AMMs) refers to the difference between the expected price of a trade and the actual price at which the trade is executed. This occurs because as trades are made, the pool's reserves change, affecting the price. In other words, slippage is the cost incurred due to the lack of liquidity in the pool.
Uniswap V2 addresses or mitigates the issue of slippage through its unique constant product formula x*y=k, where x and y represent the quantities of the two tokens in the trading pair, and k is a constant value. This formula ensures that the value of the asset pool remains unchanged before and after the trade, thereby enhancing the liquidity and stability of the market.
Assume the asset pool contains 1000 units of token A and 1000 units of token B, i.e., x=1000, y=1000, thus k=x*y=1000000. Now, suppose someone wants to exchange 100 units of token A for token B, we can calculate the new quantities after the trade and the actual amount of token B received.
x*y=k, we can calculate the situation after the trade as follows:

* The quantity of token A after the exchange becomes 1100 units.
* The quantity of token B after the exchange is approximately 909.09 units.
* Therefore, the actual amount of token B received is approximately 90.91 units.

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

To prevent users from adding extremely small amounts of liquidity that could potentially cause disproportionate slippage for subsequent trades.
When liquidity is initially added to a Uniswap V2 pair, the liquidity provider (LP) is essentially depositing an equivalent value of both tokens into the liquidity pool. However, if there were no minimum liquidity requirement, LPs could theoretically add extremely small amounts of liquidity, which might not have a significant impact on the overall liquidity pool but could still affect the price of the tokens significantly due to the automated market maker mechanism.
By subtracting a minimum liquidity requirement, Uniswap V2 ensures that LPs are providing a minimum threshold of liquidity, which helps maintain a more stable price for trades within the pool. This minimum liquidity requirement acts as a deterrent for LPs to add insignificant amounts of liquidity, thereby improving the overall efficiency and stability of the automated market maker system.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

The specific formula used to determine the amount of liquidity tokens minted is based on the constant product invariant formula employed by Uniswap V2. This formula ensures that the product of the reserve amounts of the two tokens in the pool remains constant before and after the liquidity addition. The intention behind this formula is to maintain the integrity of the automated market maker mechanism and prevent arbitrage opportunities.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

A sandwich attack is a form of market manipulation where an attacker exploits a victim's high slippage tolerance, often found in large transactions on decentralized exchanges (DEXes).
First Transaction (Front-Running): The attacker places a large buy order just before the victim's transaction. In AMM platforms like Uniswap V2, this buy order increases the token price due to the way prices are adjusted based on the token ratios in the liquidity pool.
Victim's Transaction: As a result of the increased price, the victim's transaction executes at a less favorable rate. They end up receiving fewer tokens than anticipated, exacerbated by their high slippage setting.
Second Transaction (Back-Running): Finally, the attacker sells the tokens they initially purchased. This sale often reduces the token price back to its original level or lower, enabling the attacker to profit from the price discrepancies between these transactions. Eventually, the victim suffers a financial loss by buying high and/or selling low, while the attacker benefits from the price difference created by this sequence of transactions.



