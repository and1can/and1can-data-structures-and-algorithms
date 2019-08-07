def detect_and_order_chain_businesses(businesses, location): 
    valid = defaultdict(list)
    for business in businesses: 
        if business.location == location: 
            if business.id not in valid[business.name]: 
                valid[business.name].append(business.id)
    chains = []
    for key in valid.keys(): 
        chains.append(Chain(key, len(set(valid[key]))))
    chains.sort(key = lambda x: x.name)
    chains.sort(key = lambda x: -1*x.frequency)
    
    
    return chains