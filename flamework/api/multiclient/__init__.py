# https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
__import__('pkg_resources').declare_namespace(__name__)

import flamework.api.client
import grequests

class OAuth2(flamework.api.client.OAuth2):

    def execute_methods(self, multi, size=10):

        req = []

        for details in multi:
            url, args = self.prepare_request(*details)
            req.append(grequests.post(url, **args))

        rsp = grequests.map(req)

        for r in rsp:
            yield self.parse_response(r)
