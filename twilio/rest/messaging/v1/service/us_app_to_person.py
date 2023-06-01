r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Messaging
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class UsAppToPersonInstance(InstanceResource):

    """
    :ivar sid: The unique string that identifies a US A2P Compliance resource `QE2c6890da8086d771620e9b13fadeba0b`.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that the Campaign belongs to.
    :ivar brand_registration_sid: The unique string to identify the A2P brand.
    :ivar messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) that the resource is associated with.
    :ivar description: A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096 characters.
    :ivar message_samples: Message samples, at least 1 and up to 5 sample messages (at least 2 for starter/sole proprietor), >=20 chars, <=1024 chars each.
    :ivar us_app_to_person_usecase: A2P Campaign Use Case. Examples: [ 2FA, EMERGENCY, MARKETING, SOLE_PROPRIETOR...]. SOLE_PROPRIETOR campaign use cases can only be created by SOLE_PROPRIETOR Brands, and there can only be one SOLE_PROPRIETOR campaign created per SOLE_PROPRIETOR Brand.
    :ivar has_embedded_links: Indicate that this SMS campaign will send messages that contain links.
    :ivar has_embedded_phone: Indicates that this SMS campaign will send messages that contain phone numbers.
    :ivar campaign_status: Campaign status. Examples: IN_PROGRESS, VERIFIED, FAILED.
    :ivar campaign_id: The Campaign Registry (TCR) Campaign ID.
    :ivar is_externally_registered: Indicates whether the campaign was registered externally or not.
    :ivar rate_limits: Rate limit and/or classification set by each carrier, Ex. AT&T or T-Mobile.
    :ivar message_flow: Details around how a consumer opts-in to their campaign, therefore giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign, they must all be listed. 40 character minimum. 2048 character maximum.
    :ivar opt_in_message: If end users can text in a keyword to start receiving messages from this campaign, the auto-reply messages sent to the end users must be provided. The opt-in response should include the Brand name, confirmation of opt-in enrollment to a recurring message campaign, how to get help, and clear description of how to opt-out. This field is required if end users can text in a keyword to start receiving messages from this campaign. 20 character minimum. 320 character maximum.
    :ivar opt_out_message: Upon receiving the opt-out keywords from the end users, Twilio customers are expected to send back an auto-generated response, which must provide acknowledgment of the opt-out request and confirmation that no further messages will be sent. It is also recommended that these opt-out messages include the brand name. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.
    :ivar help_message: When customers receive the help keywords from their end users, Twilio customers are expected to send back an auto-generated response; this may include the brand name and additional support contact information. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.
    :ivar opt_in_keywords: If end users can text in a keyword to start receiving messages from this campaign, those keywords must be provided. This field is required if end users can text in a keyword to start receiving messages from this campaign. Values must be alphanumeric. 255 character maximum.
    :ivar opt_out_keywords: End users should be able to text in a keyword to stop receiving messages from this campaign. Those keywords must be provided. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.
    :ivar help_keywords: End users should be able to text in a keyword to receive help. Those keywords must be provided as part of the campaign registration request. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: The absolute URL of the US App to Person resource.
    :ivar mock: A boolean that specifies whether campaign is a mock or not. Mock campaigns will be automatically created if using a mock brand. Mock campaigns should only be used for testing purposes.
    :ivar errors: Details indicating why a campaign registration failed. These errors can indicate one or more fields that were incorrect or did not meet review requirements.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        messaging_service_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.brand_registration_sid: Optional[str] = payload.get(
            "brand_registration_sid"
        )
        self.messaging_service_sid: Optional[str] = payload.get("messaging_service_sid")
        self.description: Optional[str] = payload.get("description")
        self.message_samples: Optional[List[str]] = payload.get("message_samples")
        self.us_app_to_person_usecase: Optional[str] = payload.get(
            "us_app_to_person_usecase"
        )
        self.has_embedded_links: Optional[bool] = payload.get("has_embedded_links")
        self.has_embedded_phone: Optional[bool] = payload.get("has_embedded_phone")
        self.campaign_status: Optional[str] = payload.get("campaign_status")
        self.campaign_id: Optional[str] = payload.get("campaign_id")
        self.is_externally_registered: Optional[bool] = payload.get(
            "is_externally_registered"
        )
        self.rate_limits: Optional[Dict[str, object]] = payload.get("rate_limits")
        self.message_flow: Optional[str] = payload.get("message_flow")
        self.opt_in_message: Optional[str] = payload.get("opt_in_message")
        self.opt_out_message: Optional[str] = payload.get("opt_out_message")
        self.help_message: Optional[str] = payload.get("help_message")
        self.opt_in_keywords: Optional[List[str]] = payload.get("opt_in_keywords")
        self.opt_out_keywords: Optional[List[str]] = payload.get("opt_out_keywords")
        self.help_keywords: Optional[List[str]] = payload.get("help_keywords")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")
        self.mock: Optional[bool] = payload.get("mock")
        self.errors: Optional[List[object]] = payload.get("errors")

        self._solution = {
            "messaging_service_sid": messaging_service_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[UsAppToPersonContext] = None

    @property
    def _proxy(self) -> "UsAppToPersonContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: UsAppToPersonContext for this UsAppToPersonInstance
        """
        if self._context is None:
            self._context = UsAppToPersonContext(
                self._version,
                messaging_service_sid=self._solution["messaging_service_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the UsAppToPersonInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the UsAppToPersonInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "UsAppToPersonInstance":
        """
        Fetch the UsAppToPersonInstance


        :returns: The fetched UsAppToPersonInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "UsAppToPersonInstance":
        """
        Asynchronous coroutine to fetch the UsAppToPersonInstance


        :returns: The fetched UsAppToPersonInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Messaging.V1.UsAppToPersonInstance {}>".format(context)


class UsAppToPersonContext(InstanceContext):
    def __init__(self, version: Version, messaging_service_sid: str, sid: str):
        """
        Initialize the UsAppToPersonContext

        :param version: Version that contains the resource
        :param messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) to fetch the resource from.
        :param sid: The SID of the US A2P Compliance resource to fetch `QE2c6890da8086d771620e9b13fadeba0b`.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "messaging_service_sid": messaging_service_sid,
            "sid": sid,
        }
        self._uri = "/Services/{messaging_service_sid}/Compliance/Usa2p/{sid}".format(
            **self._solution
        )

    def delete(self) -> bool:
        """
        Deletes the UsAppToPersonInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the UsAppToPersonInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> UsAppToPersonInstance:
        """
        Fetch the UsAppToPersonInstance


        :returns: The fetched UsAppToPersonInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return UsAppToPersonInstance(
            self._version,
            payload,
            messaging_service_sid=self._solution["messaging_service_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> UsAppToPersonInstance:
        """
        Asynchronous coroutine to fetch the UsAppToPersonInstance


        :returns: The fetched UsAppToPersonInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return UsAppToPersonInstance(
            self._version,
            payload,
            messaging_service_sid=self._solution["messaging_service_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Messaging.V1.UsAppToPersonContext {}>".format(context)


class UsAppToPersonPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> UsAppToPersonInstance:
        """
        Build an instance of UsAppToPersonInstance

        :param payload: Payload response from the API
        """
        return UsAppToPersonInstance(
            self._version,
            payload,
            messaging_service_sid=self._solution["messaging_service_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Messaging.V1.UsAppToPersonPage>"


class UsAppToPersonList(ListResource):
    def __init__(self, version: Version, messaging_service_sid: str):
        """
        Initialize the UsAppToPersonList

        :param version: Version that contains the resource
        :param messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) to fetch the resource from.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "messaging_service_sid": messaging_service_sid,
        }
        self._uri = "/Services/{messaging_service_sid}/Compliance/Usa2p".format(
            **self._solution
        )

    def create(
        self,
        brand_registration_sid: str,
        description: str,
        message_flow: str,
        message_samples: List[str],
        us_app_to_person_usecase: str,
        has_embedded_links: bool,
        has_embedded_phone: bool,
        opt_in_message: Union[str, object] = values.unset,
        opt_out_message: Union[str, object] = values.unset,
        help_message: Union[str, object] = values.unset,
        opt_in_keywords: Union[List[str], object] = values.unset,
        opt_out_keywords: Union[List[str], object] = values.unset,
        help_keywords: Union[List[str], object] = values.unset,
    ) -> UsAppToPersonInstance:
        """
        Create the UsAppToPersonInstance

        :param brand_registration_sid: A2P Brand Registration SID
        :param description: A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096 characters.
        :param message_flow: Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign, they must all be listed. 40 character minimum. 2048 character maximum.
        :param message_samples: Message samples, at least 1 and up to 5 sample messages (at least 2 for sole proprietor), >=20 chars, <=1024 chars each.
        :param us_app_to_person_usecase: A2P Campaign Use Case. Examples: [ 2FA, EMERGENCY, MARKETING..]
        :param has_embedded_links: Indicates that this SMS campaign will send messages that contain links.
        :param has_embedded_phone: Indicates that this SMS campaign will send messages that contain phone numbers.
        :param opt_in_message: If end users can text in a keyword to start receiving messages from this campaign, the auto-reply messages sent to the end users must be provided. The opt-in response should include the Brand name, confirmation of opt-in enrollment to a recurring message campaign, how to get help, and clear description of how to opt-out. This field is required if end users can text in a keyword to start receiving messages from this campaign. 20 character minimum. 320 character maximum.
        :param opt_out_message: Upon receiving the opt-out keywords from the end users, Twilio customers are expected to send back an auto-generated response, which must provide acknowledgment of the opt-out request and confirmation that no further messages will be sent. It is also recommended that these opt-out messages include the brand name. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.
        :param help_message: When customers receive the help keywords from their end users, Twilio customers are expected to send back an auto-generated response; this may include the brand name and additional support contact information. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.
        :param opt_in_keywords: If end users can text in a keyword to start receiving messages from this campaign, those keywords must be provided. This field is required if end users can text in a keyword to start receiving messages from this campaign. Values must be alphanumeric. 255 character maximum.
        :param opt_out_keywords: End users should be able to text in a keyword to stop receiving messages from this campaign. Those keywords must be provided. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.
        :param help_keywords: End users should be able to text in a keyword to receive help. Those keywords must be provided as part of the campaign registration request. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.

        :returns: The created UsAppToPersonInstance
        """
        data = values.of(
            {
                "BrandRegistrationSid": brand_registration_sid,
                "Description": description,
                "MessageFlow": message_flow,
                "MessageSamples": serialize.map(message_samples, lambda e: e),
                "UsAppToPersonUsecase": us_app_to_person_usecase,
                "HasEmbeddedLinks": has_embedded_links,
                "HasEmbeddedPhone": has_embedded_phone,
                "OptInMessage": opt_in_message,
                "OptOutMessage": opt_out_message,
                "HelpMessage": help_message,
                "OptInKeywords": serialize.map(opt_in_keywords, lambda e: e),
                "OptOutKeywords": serialize.map(opt_out_keywords, lambda e: e),
                "HelpKeywords": serialize.map(help_keywords, lambda e: e),
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return UsAppToPersonInstance(
            self._version,
            payload,
            messaging_service_sid=self._solution["messaging_service_sid"],
        )

    async def create_async(
        self,
        brand_registration_sid: str,
        description: str,
        message_flow: str,
        message_samples: List[str],
        us_app_to_person_usecase: str,
        has_embedded_links: bool,
        has_embedded_phone: bool,
        opt_in_message: Union[str, object] = values.unset,
        opt_out_message: Union[str, object] = values.unset,
        help_message: Union[str, object] = values.unset,
        opt_in_keywords: Union[List[str], object] = values.unset,
        opt_out_keywords: Union[List[str], object] = values.unset,
        help_keywords: Union[List[str], object] = values.unset,
    ) -> UsAppToPersonInstance:
        """
        Asynchronously create the UsAppToPersonInstance

        :param brand_registration_sid: A2P Brand Registration SID
        :param description: A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096 characters.
        :param message_flow: Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign, they must all be listed. 40 character minimum. 2048 character maximum.
        :param message_samples: Message samples, at least 1 and up to 5 sample messages (at least 2 for sole proprietor), >=20 chars, <=1024 chars each.
        :param us_app_to_person_usecase: A2P Campaign Use Case. Examples: [ 2FA, EMERGENCY, MARKETING..]
        :param has_embedded_links: Indicates that this SMS campaign will send messages that contain links.
        :param has_embedded_phone: Indicates that this SMS campaign will send messages that contain phone numbers.
        :param opt_in_message: If end users can text in a keyword to start receiving messages from this campaign, the auto-reply messages sent to the end users must be provided. The opt-in response should include the Brand name, confirmation of opt-in enrollment to a recurring message campaign, how to get help, and clear description of how to opt-out. This field is required if end users can text in a keyword to start receiving messages from this campaign. 20 character minimum. 320 character maximum.
        :param opt_out_message: Upon receiving the opt-out keywords from the end users, Twilio customers are expected to send back an auto-generated response, which must provide acknowledgment of the opt-out request and confirmation that no further messages will be sent. It is also recommended that these opt-out messages include the brand name. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.
        :param help_message: When customers receive the help keywords from their end users, Twilio customers are expected to send back an auto-generated response; this may include the brand name and additional support contact information. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.
        :param opt_in_keywords: If end users can text in a keyword to start receiving messages from this campaign, those keywords must be provided. This field is required if end users can text in a keyword to start receiving messages from this campaign. Values must be alphanumeric. 255 character maximum.
        :param opt_out_keywords: End users should be able to text in a keyword to stop receiving messages from this campaign. Those keywords must be provided. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.
        :param help_keywords: End users should be able to text in a keyword to receive help. Those keywords must be provided as part of the campaign registration request. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.

        :returns: The created UsAppToPersonInstance
        """
        data = values.of(
            {
                "BrandRegistrationSid": brand_registration_sid,
                "Description": description,
                "MessageFlow": message_flow,
                "MessageSamples": serialize.map(message_samples, lambda e: e),
                "UsAppToPersonUsecase": us_app_to_person_usecase,
                "HasEmbeddedLinks": has_embedded_links,
                "HasEmbeddedPhone": has_embedded_phone,
                "OptInMessage": opt_in_message,
                "OptOutMessage": opt_out_message,
                "HelpMessage": help_message,
                "OptInKeywords": serialize.map(opt_in_keywords, lambda e: e),
                "OptOutKeywords": serialize.map(opt_out_keywords, lambda e: e),
                "HelpKeywords": serialize.map(help_keywords, lambda e: e),
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return UsAppToPersonInstance(
            self._version,
            payload,
            messaging_service_sid=self._solution["messaging_service_sid"],
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[UsAppToPersonInstance]:
        """
        Streams UsAppToPersonInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[UsAppToPersonInstance]:
        """
        Asynchronously streams UsAppToPersonInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[UsAppToPersonInstance]:
        """
        Lists UsAppToPersonInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[UsAppToPersonInstance]:
        """
        Asynchronously lists UsAppToPersonInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> UsAppToPersonPage:
        """
        Retrieve a single page of UsAppToPersonInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of UsAppToPersonInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return UsAppToPersonPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> UsAppToPersonPage:
        """
        Asynchronously retrieve a single page of UsAppToPersonInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of UsAppToPersonInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return UsAppToPersonPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> UsAppToPersonPage:
        """
        Retrieve a specific page of UsAppToPersonInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of UsAppToPersonInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return UsAppToPersonPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> UsAppToPersonPage:
        """
        Asynchronously retrieve a specific page of UsAppToPersonInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of UsAppToPersonInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return UsAppToPersonPage(self._version, response, self._solution)

    def get(self, sid: str) -> UsAppToPersonContext:
        """
        Constructs a UsAppToPersonContext

        :param sid: The SID of the US A2P Compliance resource to fetch `QE2c6890da8086d771620e9b13fadeba0b`.
        """
        return UsAppToPersonContext(
            self._version,
            messaging_service_sid=self._solution["messaging_service_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> UsAppToPersonContext:
        """
        Constructs a UsAppToPersonContext

        :param sid: The SID of the US A2P Compliance resource to fetch `QE2c6890da8086d771620e9b13fadeba0b`.
        """
        return UsAppToPersonContext(
            self._version,
            messaging_service_sid=self._solution["messaging_service_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Messaging.V1.UsAppToPersonList>"
