# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

Slippage in Automated Market Makers (AMMs) refers to the difference between the expected price of a trade and the actual price at which the trade is executed. This occurs because as trades are made, the pool's reserves change, affecting the price. In other words, slippage is the cost incurred due to the lack of liquidity in the pool.
Uniswap V2 addresses this issue through the implementation of a mathematical formula that adjusts the price based on the size of the trade relative to the liquidity available in the pool. This formula ensures that larger trades experience more slippage compared to smaller trades, which discourages large trades that could potentially cause significant price fluctuations.

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



