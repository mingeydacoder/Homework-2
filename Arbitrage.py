liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

for pair, data in liquidity.items():
    token_pair = pair[0], pair[1]
    liquidity_amount = data[0]
    tokenB_amount = data[1]
    print(f"交易對: {token_pair}, ", data[1]/data[0], data[0]/data[1])

tokens = ["tokenA", "tokenB", "tokenC", "tokenD", "tokenE"]
liquidity_matrix = [[0 for _ in range(5)] for _ in range(5)]

# Populate the matrix based on the liquidity data
for i, token1 in enumerate(tokens):
    for j, token2 in enumerate(tokens):
        if (token1, token2) in liquidity:
            liquidity_matrix[i][j] = (liquidity[(token1, token2)][1],liquidity[(token1, token2)][0])
        elif (token2, token1) in liquidity:
            liquidity_matrix[i][j] = (liquidity[(token2, token1)][0],liquidity[(token2, token1)][1])

liquidity_matrixa = [[(0, 0) if element == 0 else element for element in row] for row in liquidity_matrix]


result = [0,0,0,0,0]
path = []
for i in range(5):
    result[i] = (997 * 5 * liquidity_matrixa[1][i][0]) / (1000 * liquidity_matrixa[1][i][1] + 997 * 5)
max_value = max(result)
max_index = result.index(max_value)
path.append(max_index)

for j in range(5):
    result[j] = (997 * max_value * liquidity_matrixa[max_index][j][0]) / (1000 * liquidity_matrixa[max_index][j][1] + 997 * max_value)
max_value = max(result)
max_index = result.index(max_value)
if max_index == 1: #跑回B
    result[max_index] = 0
    max_value = max(result)
    max_index = result.index(max_value)
path.append(max_index)

for k in range(5):
    result[k] = (997 * max_value * liquidity_matrixa[max_index][k][0]) / (1000 * liquidity_matrixa[max_index][k][1] + 997 * max_value)
max_value = max(result)
max_index = result.index(max_value)
if max_index == 1: #跑回B
    result[max_index] = 0
    max_value = max(result)
    max_index = result.index(max_value)
path.append(max_index)

for l in range(5):
    result[l] = (997 * max_value * liquidity_matrixa[max_index][1][0]) / (1000 * liquidity_matrixa[max_index][1][1] + 997 * max_value)
max_value = max(result)
max_index = result.index(max_value)
if max_index == 1: #跑回B
    result[max_index] = 0
    max_value = max(result)
    max_index = result.index(max_value)

#print(path)
#print(result)
# Mapping integers 0, 1, 2, 3, 4, 5 to strings 'a', 'b', 'c', 'd', 'e', 'f'
mapping = {0: 'tokenA', 1: 'tokenB', 2: 'tokenC', 3: 'tokenD', 4: 'tokenE'}

# Applying the mapping to the example list
mapped_list = [mapping[number] for number in path]
print(mapped_list)
print('path: tokenB ->',mapped_list[0],'->',mapped_list[1],'->',mapped_list[2],'-> tokenB, tokenB balance =',result[0])

'''
[5.655321988655322, 2.372138936383089, 13.376356555351348, 9.715189286516857, 3.2776835896101484, 16.18671418317894]
#form = [original[i:i+5] for i in range(0, len(original), 5)]

token = [0,0,0,0,0,0]
path = []
path.append(liquidity_matrix[1][0]) 
path.append(liquidity_matrix[0][2]) 
path.append(liquidity_matrix[2][1])
path.append(liquidity_matrix[1][0]) 
path.append(liquidity_matrix[0][2]) 
path.append(liquidity_matrix[2][1]) 

print(path)

def arbitrage():
    token[0] = (997 * 5 * path[0][0]) / (1000 * path[0][1] + 997 * 5)
    for i in range(5):
        token[i+1] = (997 * token[i] * path[i+1][0]) / (1000 * path[i+1][1] + 997 * token[i])

    return(token)

print(arbitrage())

'''
