# Argent Blockchain Engineer Assessment

In this repository there are solutions for the Argent Blockchain Engineer Technical interview.

## Assessment A: Algorithm & Data Structure problem

The solution is coded in Python. Find it in `assessment_a/solution.py`.

## Assessment B: Smart-contract problem

### Point 1

```
function draw():

    # check if time limit is done
    if actual block > block number limit:
        # check everyone has submitted the secret
        if submitted_secrets equal tickets_bought:
            winner_address = XOR tickets
            winner_address.send(balance)
        # revert transactions for fairness
        else:
            for ticket in tickets_bought:
                ticket.send(balance / tickets_bought.length)
        # reset all
        del tickets_bought
        del balance
        del submitted_secrets

        return winner_address
```

The strategy is secure because it is needed that participants send a hash computed locally with the chosen number. The sender and the linked hash is stored so we can assure only one number per participant to make the process fair. There is a time limit of confirmed block to be able to start the lottery to avoid exploits from miners. Also, if all the ticket buyers don't commit their submission when this function is called the lottery reverts as the last committer may have advantage to previous commiters.

### Point 2

Array `secrets` for mapping addresses to secrets
Array `balances` for mapping addresses to eth sent
Array `accounts` for participant index to address
Array `tickets` for commited participants

The random number would be generated from: `rand = n1 XOR n2 XOR n3 .. XOR nn` where n is the commit number by the participant. Then we would apply a module operation to the commiters length. `tickets[rand%tickets.length]` to choose the winner.

### Point 3

Having a constructor in the contract where `owner = msg.sender()` and require that `msg.sender() == owner` when calling the `draw` method.
            
## Assessment 3: DeFi problem

### Point a

Following the Aave [documentation of Health Risk](https://docs.aave.com/risk/asset-risk/risk-parameters#health-factor) definition:

`((100 + (100,000 / 2,000)) * ((0.8) / 3)) / (150,000 / 2,000) = 1.6`

### Point b

When ETH price is < 880$ the Health Factor would be below 1 which is not recommended. When ETH price < 500$ the position would be liquidated.

HF below 1:

`((100 + (100,000 / 880)) * ((0.8) / 3)) / (150,000 / 880) = 1`

Liquidation HF:

`((100 + (100,000 / 500)) * ((0.8) / 3)) / (150,000 / 500) = 0.8`

### Point c

For keeping the HF above 1.2 the borrowed USDC must be below 200k USDC. So, 50k more USDC could be borrowed while keeping HF above 1.2.

`((100 + (100,000 / 500)) * ((0.8) / 3)) / (150,000 / 500) = 0.8`

### Point d

If ~280,000 USDC are borrowed the HF would be 0.85 and the position would be liquidated
