import re
from typing import Dict, List, Tuple

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    result = text
    
    if casefold:
        result = result.casefold()    
    if yo2e:
        result = result.replace('ё', 'е').replace('Ё', 'е')
    
    for char in ['\t', '\r', '\n']:
        result = result.replace(char, ' ')
    
    result = re.sub(r'\s+', ' ', result).strip()
    return result

def tokenize(text: str) -> List[str]:
    pattern = r'\w+(?:-\w+)*'
    tokens = re.findall(pattern, text)
    return tokens

def count_freq(tokens: List[str]) -> Dict[str, int]:
    frequency_dict = {}
    for token in tokens:
        frequency_dict[token] = frequency_dict.get(token, 0) + 1
    return frequency_dict

def top_n(freq: Dict[str, int], n: int = 5) -> List[Tuple[str, int]]:
    items = list(freq.items())
    sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]

