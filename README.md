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

> Solution

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution

