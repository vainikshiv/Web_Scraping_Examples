# Scrapy settings for scrapy_demo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_demo'

SPIDER_MODULES = ['scrapy_demo.spiders']
NEWSPIDER_MODULE = 'scrapy_demo.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_demo (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
#   'Cookie':'PF_USERLOC_CC=IN; PF_DTM_USER_VISIT=%7B%22visitNum%22%3A1%2C%22initialTime%22%3A%222021-10-30T15%3A04%3A45.602Z%22%2C%22pageLoadTime%22%3A%222021-10-30T15%3A05%3A19.630Z%22%7D; PF_USERLOC_CC=IN; PF_DTM_USER_VISIT=%7B%22visitNum%22%3A1%2C%22initialTime%22%3A%222021-10-30T15%3A04%3A45.602Z%22%2C%22pageLoadTime%22%3A%222021-10-30T15%3A05%3A11.618Z%22%7D; PF_USERLOC_CC=IN; PF_USERLOC_CC=IN; AKA_A2=A; bm_sz=9C3A6C0E468A4DAC3EB283413941BD9C~YAAQkugyF3CNoMx8AQAA8Dy70Q3US2G0xJn3vcntCQJ3+kW5y/gSidJeNNG1ObvT6ghQCI1sx/aTTeKfnqf/q+vpHOZKrVh7qk1GBq3YE0ns5+pWg4id9AgbaYAzyTeyhcpurjnZr/Wcvpsyi2WW1uHHEnKj8wA/9Cj/4qw1w6ABSPwppAuIqT8gXU52WOit2FmkDec9POi0MGsEjs5RdGFJrI8CDxDWA6m/Qxc4tH5dn7FRlwCgv6Ukuzl535W+fXvFA2/wE1+0y4+gnTLKiypbK/i7xOwL1+yV4XBPdd7C3WhTX/k=~4340023~3420993; rxVisitor=163560628106905FHB25DUQ6727MH3VEJ5IR4GPLBM31I; dtCookie=v_4_srv_4_sn_CCT8PGO4RTSSI64JO2927H3JIHBS76KK_perc_100000_ol_0_mul_1_app-3A2aad253ffd9f7288_1; JSESSIONID=000067v2aCxhNy-VFhiOOceHDm7:1ctdehfua; PF_HEADER_INFO=N; WC_SESSION_ESTABLISHED=true; WC_PERSISTENT=Oe0bMzoyG5v5jACWRC1PhYGBk5cdXSE6PBOFbTdNre4%3D%3B2021-10-30+23%3A04%3A42.006_1635606282003-114682_10186_-1002%2C91%2CINR_10186; WC_AUTHENTICATION_-1002=-1002%2C4nhPDM2%2BSo599mBFV6S38uJ2%2BxDFbZOgY9M9emtUQ1A%3D; WC_ACTIVEPOINTER=91%2C10186; WC_USERACTIVITY_-1002=-1002%2C10186%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C849998103%2CXBCReQDGwzXpmNoyy8uy%2F4qxXdYqH2K7YXlzRTvzyBxqeyWPIqUWZsWgZB4h1%2B5WPRczzH4AEXK6r9RzKipIX%2BW5g2sNF49KPT357TBm0rb2AplOEkheWgBORbQKYbR5WgpWXe2WEm75QPoiiS4%2BwMmOYL9A%2BKf12xTeIYFDNDR3TwQwfh2QT3x59LdsJJwetJMA%2BuLfNukVpqw5y4ON2ixkhrdK7uH8Eq0TSwPLdPS%2BWE14V1u29i6H6DtLLgQA; WC_GENERIC_ACTIVITYDATA=[315732767897%3Atrue%3Afalse%3A0%3AYNBwxrTQavlqKNfXxLOsz6BqIxCn2l7uwSbeQXx6%2BwI%3D][com.ibm.commerce.context.entitlement.EntitlementContext|10644%2610644%26null%26-2000%26null%26null%26null][com.ibm.commerce.context.audit.AuditContext|1635606282003-114682][com.pf.commerce.context.generic.PFGenericContext|null][com.ibm.commerce.context.globalization.GlobalizationContext|91%26INR%2691%26INR][com.ibm.commerce.store.facade.server.context.StoreGeoCodeContext|null%26null%26null%26null%26null%26null][com.pf.commerce.context.entitlement.PFEntitlementContext|10644%2610644%26null%26null%26null%26null%26true%26false%26true%26null%26null%26null][com.pf.commerce.punchout.businesscontext.PunchoutContext|null%26false%26false%26false%26false%26null][com.ibm.commerce.context.experiment.ExperimentContext|null][com.ibm.commerce.giftcenter.context.GiftCenterContext|null%26null%26null][com.pf.commerce.checkout.context.PFCheckoutStubContext|null][com.ibm.commerce.catalog.businesscontext.CatalogContext|15001%26null%26false%26false%26false][CTXSETNAME|Store][com.pf.commerce.cms.preview.context.CMSPreviewContext|contentStoreKey%253Dlocal][com.ibm.commerce.context.base.BaseContext|10186%26-1002%26-1002%26-1][com.pf.commerce.ibuy.businesscontext.IBuyContext|null%26null%26false%26null%26null%26null%26null%26null%26false%26null]; f5avraaaaaaaaaaaaaaaa_session_=CLOGCCIDNGFPONMHEGFJCBJKKPCFDCODILKPLOLFABMNJLJCOPIKPBCLFJHDGENFHAKDCOABOOGNCLDDDAMALBHELFBJCHDPFIPNNDJPGKAKIJIBCKEFIEIMHDIBFEHH; TS01764c4c=018f8ed7b596c315dc0350043ce59535d6173b4f7cf94d04217a90bf1a7d153ce4daa86e5195631f572a4075a0ef96fb398bdb69ff55d443b6088f7c46fdfd7049da362722; TS01db1002=018f8ed7b5ea76c6f91872cdae503ccc8bae7e2252f94d04217a90bf1a7d153ce4daa86e51664fd2898dc97af118124ce27a82886b; TS01764c4c028=018b310b55c5f8df1ecb2a9853860414e633a7f6d8539487df75e1d3ba51910fcde223cfe61d918e07ded9754b63092445fe728cce; at_check=true; AMCVS_106315F354E6D5430A4C98A4%40AdobeOrg=1; s_ecid=MCMID%7C32443930504099262293458302218357562926; AMCV_106315F354E6D5430A4C98A4%40AdobeOrg=2121618341%7CMCIDTS%7C18931%7CMCMID%7C32443930504099262293458302218357562926%7CMCAAMLH-1636211081%7C12%7CMCAAMB-1636211081%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1635613481s%7CNONE%7CMCAID%7CNONE; ak_bmsc=ECA2E39CD8B3D3A4354D86E58E068A16~000000000000000000000000000000~YAAQkugyF42NoMx8AQAAiU270Q3ABbWZjIiNHvkpToi+c25gH2eWjGS0+UwdnPiAPZ/HyN7EiUu1l+AKGMcfenOcfC7GeeZKoKWI8vBNsNC7BFdIHTwUA1iIxqqtI5kxdPbPnBP66vSwfPRURVEW+LgtOPETsmCgLZrDLChNJfaaHmzh+M+UK/GjnvJOXCsAd8N7stQApJ42R1hTVl+uM8GkpeSecyMMwVk7Pyo/wEaUwe5l2UKWOYfFkye6ksVRhSb0HYM4w7vy3ekQ6kYgyCqVHQuHWC6CPyhGp7KDxpNRqDePQ407JimXri73GX+/tshzH6E6Nv2EL0+9U5fT3s7SO79mkMhSjGkIgp6Eo3zVGRN254iPRsOffqib63S/XCdQ6AS6M2gXC4mMeocsLxmFo1iwbUcr5KRSKQLY0vvsPmB8zg0UcSHnN41UahgVINuRmJ/V1G3rpb1on+UoL5wlKW8itxJ89NHcePNlC4GLYauso+iQ3QEfz16/KXo=; PF_LOOKAHEAD_10186=true; PF_DTM_USER_VISIT=%7B%22visitNum%22%3A1%2C%22initialTime%22%3A%222021-10-30T15%3A04%3A45.602Z%22%2C%22pageLoadTime%22%3A%222021-10-30T15%3A04%3A45.602Z%22%7D; _abck=E830858417253D1D2519384F85BB0BE7~0~YAAQkugyF5ONoMx8AQAA+0+70QbHchOlcNslxutFs7n9wH3zGrBlopM3QjXn9FUdqO1x43bUxe2QeZ+RPfUWAw1byofaBm8X+2Udi9EdSUz961MIM4fKyFwysn3urVni/lsIJI38Z+8ZZFJ4uluuBeMBAwW6PRl959A+ebnByLYWTDBNIEBxpctAPjZR69DrJQQIe5WdcFJCBjZMYUAGH55akSSUthbUoLVxU2E0P9Tyb1R3jIdN/wd8dOHDhQDnvcsW9n4Nt9m7zZevY0AoaFF+tIeN9TVwhbGOv0A43RfocLLCxrT1ltzX+q3rtQEQbW1Opys954c9L5hxPY9kYgF+ClgG0iv8ta67fbUD10niQxSl2fpv/YlD7TKF9+97z30gkrEwsev6MnM0OPYNFi5Llp3Q1TXcNhe4~-1~||-1||~-1; TLTSID=24398752739830704155084454912244; s_cc=true; _gcl_aw=GCL.1635606287.EAIaIQobChMIkam8mbTy8wIVix0rCh3qgApYEAAYASAAEgI-x_D_BwE; _gcl_au=1.1.2077439376.1635606287; _mkto_trk=id:059-JXI-597&token:_mch-element14.com-1635606288922-65340; _ga=GA1.2.217469629.1635606290; _gid=GA1.2.1138116875.1635606290; _gac_UA-26026183-7=1.1635606290.EAIaIQobChMIkam8mbTy8wIVix0rCh3qgApYEAAYASAAEgI-x_D_BwE; _gac_UA-26026183-15=1.1635606290.EAIaIQobChMIkam8mbTy8wIVix0rCh3qgApYEAAYASAAEgI-x_D_BwE; PF_OMN_TAG_10186=%22%7B%7D%22; dtSa=-; s_sq=%5B%5BB%5D%5D; rxvt=1635608120465|1635606281075; da_sid=2EBC23818E33AE85ABDFAA134887C35215|3|0|3; da_lid=1D8F10B29A73EA1E3E8EBB990A858959A6|0|0|0; da_intState=; dtPC=4$6317379_958h-vHBWGMDTPFMADHACHWUHBKHKCRMFETQPH-0e0; _uetsid=b8beb570399211ecadb3cf1a1db8bf1b; _uetvid=b8bf1d00399211ec8a14c32676bbb19c; bm_sv=7CE9BB8C92976E71CD4AA25A34F77192~8jGy59o1FQrJPGAtnlYhoY15ZL/pGw4pdFHX0K3MmagGUbqJRU4kulldL++nF2ZfOvwynH8uKFbvQMJc6UhOCbmMPYdpGeDI1dS8ZWQGD3/8WMA6xNVUbwwfYjik/dPo7Zy0c7TkuthZwSp6XXu5/jYymJwUkE8ymsNMPUx99TM=; dtLatC=2; mbox=session#5a160378cc4749caa138843f87ed9dbc#1635608201|PC#5a160378cc4749caa138843f87ed9dbc.31_0#1698851082'
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrapy_demo.middlewares.ScrapyDemoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'scrapy_demo.middlewares.ScrapyDemoDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'scrapy_demo.pipelines.ScrapyDemoPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
