import logging

from digital_thought_commons import internet
from digital_thought_commons.cache import APICache


class EclecticIQDomain:

    def __init__(self, request_session, api_cache, api_url, lookup_method):
        self.request_session = request_session
        self.cache = api_cache
        self.api_url = api_url
        self.lookup_method = lookup_method

    def retrieve_domain_information(self, domain):
        query_payload = "extracts.kind:domain AND extracts.value: {}".format(domain)
        return self.cache.lookup(self.lookup_method, query_payload=query_payload)

class EclecticIQIPAddress:

    def __init__(self, request_session, api_cache, api_url, lookup_method):
        self.request_session = request_session
        self.cache = api_cache
        self.api_url = api_url
        self.lookup_method = lookup_method

    def retrieve_ip_information(self, ip_address):
        query_payload = "extracts.kind:ipv4 AND extracts.value: {}".format(ip_address)
        return self.cache.lookup(self.lookup_method, query_payload=query_payload)


# class VirusTotalURL:
#
#     def __init__(self, request_session, api_cache, api_url, lookup_method):
#         self.request_session = request_session
#         self.cache = api_cache
#         self.api_url = api_url
#         self.lookup_method = lookup_method
#
#     def __encode_url(self, url):
#         return base64.b64encode(url.encode("UTF-8")).decode("UTF-8")
#
#     def retrieve_url_information(self, url):
#         query_payload = 'urls/{}'.format(self.__encode_url(url))
#         return self.cache.lookup(self.lookup_method, query_payload=query_payload)
#
#     def retrieve_url_comments(self, url):
#         query_payload = 'urls/{}/comments'.format(self.__encode_url(url))
#         return self.cache.lookup(self.lookup_method, query_payload=query_payload)
#
#     def retrieve_url_relationships(self, url, relationship):
#         query_payload = 'urls/{}/{}'.format(self.__encode_url(url), relationship)
#         return self.cache.lookup(self.lookup_method, query_payload=query_payload)
#
#     def retrieve_url_relationship_objects(self, url, relationship):
#         query_payload = 'urls/{}/relationships/{}'.format(self.__encode_url(url), relationship)
#         return self.cache.lookup(self.lookup_method, query_payload=query_payload)
#
#     def retrieve_url_votes(self, url):
#         query_payload = 'urls/{}/votes'.format(self.__encode_url(url))
#         return self.cache.lookup(self.lookup_method, query_payload=query_payload)


class EclecticIQ:
    
    api_url = '"https://{}.eiq-platform.com/private/search-all/"'

    def __init__(self, api_key, eiq_instance="default"):
        self.api_key = api_key
        self.api_url = self.api_url.format(eiq_instance)
        self.request_session = internet.retry_request_session(headers={'Authorization': 'Bearer {}'.format(api_key), 'Content-Type': 'application/json'})

        self.cache = APICache('eclecticiq')

    def __lookup(self, query_payload):
        try:
            logging.debug('Performing EclecticIQ Lookup for: {}'.format(query_payload))
            post_query = {
                "query": {
                    "query_string": {
                        "query": query_payload
                    }
                }
            }
            response = self.request_session.post(self.api_url,json=post_query)
            if response.status_code != 200:
                raise Exception('Status code {} encountered while looking up IP address.  Error: {}'
                                .format(str(response.status_code), response.content))

            return response.json()
        except Exception as ex:
            logging.exception(ex)
            return {'error': str(ex)}

    def ip_lookups(self):
        return EclecticIQIPAddress(self.request_session, self.cache, self.api_url, self.__lookup)

    def domain_lookups(self):
        return EclecticIQDomain(self.request_session, self.cache, self.api_url, self.__lookup)

    # def url_lookups(self):
    #     return VirusTotalURL(self.request_session, self.cache, self.api_url, self.__lookup)

    def search(self, query):
        query_payload = 'search?query={}'.format(query)
        return self.cache.lookup(self.__lookup, query_payload=query_payload)

    def eclecticiq_metadata(self):
        query_payload = 'metadata'
        return self.cache.lookup(self.__lookup, query_payload=query_payload)
