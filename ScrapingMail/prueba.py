import requests

cookies = {
    'CFID': '1450434',
    'CFTOKEN': 'f39ce55f3e1ec6b9-5EB05EC0-9B60-DD21-635E3406C1063B83',
    'JSESSIONID': '7BCFB0F07A291BAD89EE85B1451F9D82.cfusion',
    'DEFAULTLOCALE': 'en_GB',
    'feathr_session_id': '658372ba42fa177a3ca8def8',
    '_pk_id.385.bc0c': 'e8f2e5c15c323524.1703113403.1.1703115158.1703113403.',
    '_pk_ses.385.bc0c': '1',
    '_gcl_au': '1.1.319893802.1703113403',
    '_ga_MSEQLQ3X1J': 'GS1.1.1703113403.1.1.1703115157.42.0.0',
    '_ga': 'GA1.1.578715590.1703113404',
    '__q_state_gbxv6GGmbygPpVDq': 'eyJ1dWlkIjoiYzkxZDNmNzctOTFlYS00NGYwLWFjODYtNTBjOTUwNjQ0OTgwIiwiY29va2llRG9tYWluIjoiaWNlZ2FtaW5nLmNvbSIsIm1lc3NlbmdlckV4cGFuZGVkIjpmYWxzZSwicHJvbXB0RGlzbWlzc2VkIjp0cnVlLCJjb252ZXJzYXRpb25JZCI6IjEyOTMxMDIzOTQ5NjkyMTE4ODIifQ==',
    '_fbp': 'fb.1.1703113405433.1500183674',
    '_hjSessionUser_3289664': 'eyJpZCI6ImZiYmY5MjkxLWZlYmYtNWNhMC1hYWFlLTgxYWRlZWJmYzEyMiIsImNyZWF0ZWQiOjE3MDMxMTM0MDU3MDIsImV4aXN0aW5nIjp0cnVlfQ==',
    '_hjFirstSeen': '1',
    '_hjIncludedInSessionSample_3289664': '0',
    '_hjSession_3289664': 'eyJpZCI6Ijg1NTQ3ZTgwLTM3NjMtNDE1OC05NTM3LTVmNmE4ZDBhODFlMyIsImMiOjE3MDMxMTM0MDU3MDUsInMiOjAsInIiOjAsInNiIjoxfQ==',
    '_hjAbsoluteSessionInProgress': '0',
    'sa-user-id': 's%253A0-e120020b-4873-5c9e-49d9-90c2039e9a4a.OjkKkLHHp8PVKwNiCDDhCCYuX81tboIfWrKZL5puOlc',
    'sa-user-id-v2': 's%253A4SACC0hzXJ5J2ZDCA56aSrXHLGU.ANVwm3qcGckD3ELwiQUfIAHttVV3B2qLjrw4TXeFn8U',
    'sa-user-id-v3': 's%253AAQAKIItZDDJRIrt1iWncaRY1My-jPEg9e8WPssD_B6kOJ7KTEAEYAyC95Y2sBjABOgTmUr0yQgTqdEXD.8J3dWoq7nnIaTvRB%252F5uKvA%252BPhUoERox72wMalXuQYJU',
    '__gads': 'ID=168bf52d2313188f:T=1703113408:RT=1703115137:S=ALNI_MZMw1xuD7qrmSkicnFkxRoCqAFOYw',
    '__gpi': 'UID=00000dabea81ca44:T=1703113408:RT=1703115137:S=ALNI_MYXlqdhG0A_DV5J_kPmzhTlTuj0hQ',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Dec+20+2023+18%3A32%3A20+GMT-0500+(hora+de+Ecuador)&version=202310.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=b771b896-9c33-4847-a058-879be39ca446&interactionCount=1&landingPath=NotLandingPage&groups=C0004%3A1%2CC0003%3A1%2CC0002%3A1%2CC0001%3A1%2CC0007%3A1%2CC0008%3A1&geolocation=EC%3BG&AwaitingReconsent=false',
    'visitor_id339401': '566507506',
    'visitor_id339401-hash': '935f6157036ea37e283995c80fabbc0d49a7d6d642b546743a96b2224b4e2a581ca5e1b8e857f9449363b5a499d6e806bd36ba54',
    'OptanonAlertBoxClosed': '2023-12-20T23:32:20.155Z',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Accept': '*/*',
    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://www.icegaming.com/exhibitor-list?&sortby=customfield_12158%20desc%2Ccustomfield_11984%20desc&page=2&searchgroup=D48EE8B1-exhibitors',
    # 'Cookie': 'CFID=1450434; CFTOKEN=f39ce55f3e1ec6b9-5EB05EC0-9B60-DD21-635E3406C1063B83; JSESSIONID=7BCFB0F07A291BAD89EE85B1451F9D82.cfusion; DEFAULTLOCALE=en_GB; feathr_session_id=658372ba42fa177a3ca8def8; _pk_id.385.bc0c=e8f2e5c15c323524.1703113403.1.1703115158.1703113403.; _pk_ses.385.bc0c=1; _gcl_au=1.1.319893802.1703113403; _ga_MSEQLQ3X1J=GS1.1.1703113403.1.1.1703115157.42.0.0; _ga=GA1.1.578715590.1703113404; __q_state_gbxv6GGmbygPpVDq=eyJ1dWlkIjoiYzkxZDNmNzctOTFlYS00NGYwLWFjODYtNTBjOTUwNjQ0OTgwIiwiY29va2llRG9tYWluIjoiaWNlZ2FtaW5nLmNvbSIsIm1lc3NlbmdlckV4cGFuZGVkIjpmYWxzZSwicHJvbXB0RGlzbWlzc2VkIjp0cnVlLCJjb252ZXJzYXRpb25JZCI6IjEyOTMxMDIzOTQ5NjkyMTE4ODIifQ==; _fbp=fb.1.1703113405433.1500183674; _hjSessionUser_3289664=eyJpZCI6ImZiYmY5MjkxLWZlYmYtNWNhMC1hYWFlLTgxYWRlZWJmYzEyMiIsImNyZWF0ZWQiOjE3MDMxMTM0MDU3MDIsImV4aXN0aW5nIjp0cnVlfQ==; _hjFirstSeen=1; _hjIncludedInSessionSample_3289664=0; _hjSession_3289664=eyJpZCI6Ijg1NTQ3ZTgwLTM3NjMtNDE1OC05NTM3LTVmNmE4ZDBhODFlMyIsImMiOjE3MDMxMTM0MDU3MDUsInMiOjAsInIiOjAsInNiIjoxfQ==; _hjAbsoluteSessionInProgress=0; sa-user-id=s%253A0-e120020b-4873-5c9e-49d9-90c2039e9a4a.OjkKkLHHp8PVKwNiCDDhCCYuX81tboIfWrKZL5puOlc; sa-user-id-v2=s%253A4SACC0hzXJ5J2ZDCA56aSrXHLGU.ANVwm3qcGckD3ELwiQUfIAHttVV3B2qLjrw4TXeFn8U; sa-user-id-v3=s%253AAQAKIItZDDJRIrt1iWncaRY1My-jPEg9e8WPssD_B6kOJ7KTEAEYAyC95Y2sBjABOgTmUr0yQgTqdEXD.8J3dWoq7nnIaTvRB%252F5uKvA%252BPhUoERox72wMalXuQYJU; __gads=ID=168bf52d2313188f:T=1703113408:RT=1703115137:S=ALNI_MZMw1xuD7qrmSkicnFkxRoCqAFOYw; __gpi=UID=00000dabea81ca44:T=1703113408:RT=1703115137:S=ALNI_MYXlqdhG0A_DV5J_kPmzhTlTuj0hQ; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Dec+20+2023+18%3A32%3A20+GMT-0500+(hora+de+Ecuador)&version=202310.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=b771b896-9c33-4847-a058-879be39ca446&interactionCount=1&landingPath=NotLandingPage&groups=C0004%3A1%2CC0003%3A1%2CC0002%3A1%2CC0001%3A1%2CC0007%3A1%2CC0008%3A1&geolocation=EC%3BG&AwaitingReconsent=false; visitor_id339401=566507506; visitor_id339401-hash=935f6157036ea37e283995c80fabbc0d49a7d6d642b546743a96b2224b4e2a581ca5e1b8e857f9449363b5a499d6e806bd36ba54; OptanonAlertBoxClosed=2023-12-20T23:32:20.155Z',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

response = requests.get(
    'https://www.icegaming.com/exhibitors/b2binpay?&sortby=customfield_12158%20desc%2Ccustomfield_11984%20desc&page=2&searchgroup=libraryentry-exhibitors',
    cookies=cookies,
    headers=headers,
)

print(response.json())