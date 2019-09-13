import collections
def knapsack(items, capacity):

    def knapsack_helper(k, avail_capacity):
        
        if k < 0:
            return 0

        if V[k][avail_capacity] == -1:
            without_item = knapsack_helper(k-1, avail_capacity)
            with_item = (0 if items[k].weight > avail_capacity else items[k].value + knapsack_helper(k-1, avail_capacity - items[k].weight))
            V[k][avail_capacity] = max(with_item, without_item)
            print(k, avail_capacity)
        return V[k][avail_capacity]

    V = [[-1] * (capacity + 1) for _ in items]
    return knapsack_helper(len(items) - 1, capacity)

Item = collections.namedtuple('Item', ('weight', 'value'))
items = [Item(4,100), Item(3, 90), Item(2, 65), Item(5, 110), Item(6, 125)]
print(knapsack(items, 10))
