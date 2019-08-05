class Solution:
    def shoppingOffers(self, price: 'List[int]', special: 'List[List[int]',
                       needs: 'List[int]') -> 'int':
        def shopping(price, special, needs, memo):
            needs_msg = str(needs)
            if needs_msg in memo:
                return memo[needs_msg]
            consume = sum([needs[i] * price[i] for i in range(len(needs))])
            for i in range(len(special)):
                new_needs = [
                    needs[j] - special[i][j] for j in range(len(needs))
                ]
                if min(new_needs) < 0:
                    continue
                special_consume = shopping(price, special, new_needs,
                                           memo) + special[i][-1]
                consume = min(consume, special_consume)

            memo[needs_msg] = consume

            return consume

        memo = {}
        consume = shopping(price, special, needs, memo)
        return consume
