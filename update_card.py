import re

file_path = '/Users/okgoogle13/Projects/Computer purchase/cards/laptops/GZ302EA-RU004W_rog_flow_z13.md'

with open(file_path, 'r') as f:
    content = f.read()

# Update frontmatter
content = re.sub(r'price_aud: \d+\.\d+', 'price_aud: 3499.00', content)
content = re.sub(r'effective_best_price_aud: \d+\.\d+', 'effective_best_price_aud: 3499.00', content)
content = re.sub(r'retailer: .*', 'retailer: PLE Computers', content)
content = re.sub(r'url: .*', 'url: https://www.ple.com.au/products/672657/asus-rog-flow-z13-gz302-134-180hz-ryzen-ai-max-395-32gb1tb-win-11-gaming-notebook', content)
content = re.sub(r'score: .*', 'score: 7.4', content)
content = re.sub(r'Performance_Headroom: .*', 'Performance_Headroom: 6', content)
content = re.sub(r'Price_Value: .*', 'Price_Value: 9', content)
content = re.sub(r'Future_Proof: .*', 'Future_Proof: 6', content)
content = re.sub(r'Portability: .*', 'Portability: 10', content)
content = re.sub(r'Track2_Avoidance: .*', 'Track2_Avoidance: 6', content)
content = re.sub(r'source_platform: .*', 'source_platform: MAJOR_RETAILER_AU', content)
content = re.sub(r'seller_class: .*', 'seller_class: MAJOR_RETAILER_AU', content)

# Update markdown text
content = re.sub(r'\$4,499\.00', '$3,499.00', content)
content = re.sub(r'\$4,499', '$3,499', content)
content = re.sub(r'Retailer:\*\* ASUS Australia', 'Retailer:** PLE Computers', content)
content = re.sub(r'\[ASUS Store Listing\]\(.*?\)', '[PLE Computers Listing](https://www.ple.com.au/products/672657/asus-rog-flow-z13-gz302-134-180hz-ryzen-ai-max-395-32gb1tb-win-11-gaming-notebook)', content)

content = re.sub(r'\*\*Price_Value:\*\* 6 \(Fair value at current verified AU pricing\)', '**Price_Value:** 9 (Bargain exception due to special price of $3,499)', content)
content = re.sub(r'\*\*MCDA_Total:\*\* 6\.8', '**MCDA_Total:** 7.4', content)

with open(file_path, 'w') as f:
    f.write(content)

