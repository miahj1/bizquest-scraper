# BizQuest Scraper
<div align="center">
    <picture><img width="200px" alt="bizquest logo" src="https://github.com/miahj1/bizquest-scraper/assets/84815985/d165661c-b45e-41b4-b16a-d0d3b664913f"></picture>
    <div align="center"><a href="https://www.bizquest.com">Homepage</a> | <a href="https://www.bizquest.com/businesses-for-sale/">Businesses for Sale</a></div>
</div>
<br>

Founded in 1994, BizQuest is the original business-for-sale website connecting business brokers, sellers, and buyers, boasting a vast inventory of businesses for sale, a comprehensive directory of business brokers, and a leading franchise opportunities directory, with millions of annual visits to their desktop and mobile sites, providing easy access for buyers, optimal exposure for brokers through the BrokerWorks Network, efficient marketing solutions for sellers, and a franchise directory for franchisors to connect with qualified entrepreneurs.

## Python Modules
- beautiful soup 4
- requests
- re
- types
- threading
- pandas

# Summary
The data scraped from the website consists of information regarding the listing of businesses that are up for sale where the client specified these elements to be extracted:
- The `title` of the listing.
- Sidebar information such as the `asking price`, `gross revenue`, `cash flow`, `ebitdta`, `inventory`, and `ff&e`.
- The content in the body of the listing: `business description` as well as all the fields in `about the business`  and `about the sale`.

The client requested each piece of the data circled in red below.

![image](https://github.com/miahj1/bizquest-scraper/assets/84815985/96adc9a2-fcfa-43a6-a264-5492bd1bcf8b)
![image](https://github.com/miahj1/bizquest-scraper/assets/84815985/8f7cd8e1-a978-40e3-aa17-e0b29d2f34a2)
![image](https://github.com/miahj1/bizquest-scraper/assets/84815985/3d653821-b07f-4f88-8470-c36e27e66185)

