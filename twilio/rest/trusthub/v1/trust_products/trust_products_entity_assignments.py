# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class TrustProductsEntityAssignmentsList(ListResource):

    def __init__(self, version, trust_product_sid):
        """
        Initialize the TrustProductsEntityAssignmentsList

        :param Version version: Version that contains the resource
        :param trust_product_sid: The unique string that identifies the TrustProduct resource.

        :returns: twilio.rest.trusthub.v1.trust_products.trust_products_entity_assignments.TrustProductsEntityAssignmentsList
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_entity_assignments.TrustProductsEntityAssignmentsList
        """
        super(TrustProductsEntityAssignmentsList, self).__init__(version)

        # Path Solution
        self._solution = {'trust_product_sid': trust_product_sid, }
        self._uri = '/TrustProducts/{trust_product_sid}/EntityAssignments'.format(**self._solution)

    def create(self, object_sid):
        """
        Create the TrustProductsEntityAssignmentsInstance

        :param unicode object_sid: The sid of an object bag

        :returns: The created TrustProductsEntityAssignmentsInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_entity_assignments.TrustProductsEntityAssignmentsInstance
        """
        data = values.of({'ObjectSid': object_sid, })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return TrustProductsEntityAssignmentsInstance(
            self._version,
            payload,
            trust_product_sid=self._solution['trust_product_sid'],
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams TrustProductsEntityAssignmentsInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trusthub.v1.trust_products.trust_products_entity_assignments.TrustProductsEntityAssignmentsInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists TrustProductsEntityAssignmentsInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trusthub.v1.trust_products.trust_products_entity_assignments.TrustProductsEntityAssignmentsInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of TrustProductsEntityAssignmentsInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of TrustProductsEntityAssignmentsInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_entity_assignments.TrustProductsEntityAssignmentsPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return TrustProductsEntityAssignmentsPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of TrustProductsEntityAssignmentsInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of TrustProductsEntityAssignmentsInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_entity_assignments.TrustProductsEntityAssignmentsPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return TrustProductsEntityAssignmentsPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a TrustProductsEntityAssignmentsContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.trusthub.v1.trust_products.trust_products_entity_assignments.TrustProductsEntityAssignmentsContext
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_entity_assignments.TrustProductsEntityAssignmentsContext
        """
        return TrustProductsEntityAssignmentsContext(
            self._version,
            trust_product_sid=self._solution['trust_product_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a TrustProductsEntityAssignmentsContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.trusthub.v1.trust_products.trust_products_entity_assignments.TrustProductsEntityAssignmentsContext
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_entity_assignments.TrustProductsEntityAssignmentsContext
        """
        return TrustProductsEntityAssignmentsContext(
            self._version,
            trust_product_sid=self._solution['trust_product_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trusthub.V1.TrustProductsEntityAssignmentsList>'


class TrustProductsEntityAssignmentsPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the TrustProductsEntityAssignmentsPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param trust_product_sid: The unique string that identifies the TrustProduct resource.

        :returns: twilio.rest.trusthub.v1.trust_products.trust_products_entity_assignments.TrustProductsEntityAssignmentsPage
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_entity_assignments.TrustProductsEntityAssignmentsPage
        """
        super(TrustProductsEntityAssignmentsPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of TrustProductsEntityAssignmentsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.trusthub.v1.trust_products.trust_products_entity_assignments.TrustProductsEntityAssignmentsInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_entity_assignments.TrustProductsEntityAssignmentsInstance
        """
        return TrustProductsEntityAssignmentsInstance(
            self._version,
            payload,
            trust_product_sid=self._solution['trust_product_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trusthub.V1.TrustProductsEntityAssignmentsPage>'


class TrustProductsEntityAssignmentsContext(InstanceContext):

    def __init__(self, version, trust_product_sid, sid):
        """
        Initialize the TrustProductsEntityAssignmentsContext

        :param Version version: Version that contains the resource
        :param trust_product_sid: The unique string that identifies the resource.
        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.trusthub.v1.trust_products.trust_products_entity_assignments.TrustProductsEntityAssignmentsContext
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_entity_assignments.TrustProductsEntityAssignmentsContext
        """
        super(TrustProductsEntityAssignmentsContext, self).__init__(version)

        # Path Solution
        self._solution = {'trust_product_sid': trust_product_sid, 'sid': sid, }
        self._uri = '/TrustProducts/{trust_product_sid}/EntityAssignments/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch the TrustProductsEntityAssignmentsInstance

        :returns: The fetched TrustProductsEntityAssignmentsInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_entity_assignments.TrustProductsEntityAssignmentsInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return TrustProductsEntityAssignmentsInstance(
            self._version,
            payload,
            trust_product_sid=self._solution['trust_product_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the TrustProductsEntityAssignmentsInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trusthub.V1.TrustProductsEntityAssignmentsContext {}>'.format(context)


class TrustProductsEntityAssignmentsInstance(InstanceResource):

    def __init__(self, version, payload, trust_product_sid, sid=None):
        """
        Initialize the TrustProductsEntityAssignmentsInstance

        :returns: twilio.rest.trusthub.v1.trust_products.trust_products_entity_assignments.TrustProductsEntityAssignmentsInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_entity_assignments.TrustProductsEntityAssignmentsInstance
        """
        super(TrustProductsEntityAssignmentsInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'trust_product_sid': payload.get('trust_product_sid'),
            'account_sid': payload.get('account_sid'),
            'object_sid': payload.get('object_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'trust_product_sid': trust_product_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: TrustProductsEntityAssignmentsContext for this TrustProductsEntityAssignmentsInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_entity_assignments.TrustProductsEntityAssignmentsContext
        """
        if self._context is None:
            self._context = TrustProductsEntityAssignmentsContext(
                self._version,
                trust_product_sid=self._solution['trust_product_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def trust_product_sid(self):
        """
        :returns: The unique string that identifies the TrustProduct resource.
        :rtype: unicode
        """
        return self._properties['trust_product_sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def object_sid(self):
        """
        :returns: The sid of an object bag
        :rtype: unicode
        """
        return self._properties['object_sid']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def url(self):
        """
        :returns: The absolute URL of the Identity resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch the TrustProductsEntityAssignmentsInstance

        :returns: The fetched TrustProductsEntityAssignmentsInstance
        :rtype: twilio.rest.trusthub.v1.trust_products.trust_products_entity_assignments.TrustProductsEntityAssignmentsInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the TrustProductsEntityAssignmentsInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trusthub.V1.TrustProductsEntityAssignmentsInstance {}>'.format(context)