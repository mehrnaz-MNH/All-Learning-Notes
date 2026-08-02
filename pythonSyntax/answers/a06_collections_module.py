"""Reference answers for 06_collections_module.py.

Kept out of the topic file so solving a question doesn't spoil it.
Shown only by `--answers` mode via ANSWERS[func_name]."""

import os, sys
from collections import Counter, defaultdict, OrderedDict, namedtuple, deque, ChainMap


ANSWERS = {
    "word_frequency": lambda sentence: Counter(sentence.lower().split()),
    "top_n_common": lambda items, n: Counter(items).most_common(n),
    "remaining_stock": lambda stock, sold: Counter(stock) - Counter(sold),
    "group_by_first_letter": lambda words: (lambda g: [g[w[0].lower()].append(w) for w in words] and g or g)(defaultdict(list)),
    "adjacency_list": lambda edges: (lambda g: [g[s].append(d) for s, d in edges] and g or g)(defaultdict(list)),
    "reverse_keys": lambda pairs: list(reversed(OrderedDict(pairs))),
    "product_to_dict": lambda name, category, price, in_stock: dict(
        namedtuple('Product', ['name', 'category', 'price', 'in_stock'])(
            name, category, price, in_stock)._asdict()),
    "replace_price": lambda title, price, available, rating, new_price: tuple(
        namedtuple('Listing', ['title', 'price', 'available', 'rating'])(
            title, price, available, rating)._replace(price=new_price)),
    "rotate_deque": lambda items, n: (lambda dq: (dq.rotate(n), list(dq))[1])(deque(items)),
    "chainmap_lookup": lambda first, second, key: ChainMap(first, second)[key],
}
