# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class PoliciesTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trusthub.v1.policies.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://trusthub.twilio.com/v1/Policies',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "results": [],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://trusthub.twilio.com/v1/Policies?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://trusthub.twilio.com/v1/Policies?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "results"
                }
            }
            '''
        ))

        actual = self.client.trusthub.v1.policies.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://trusthub.twilio.com/v1/Policies?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://trusthub.twilio.com/v1/Policies?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "results"
                },
                "results": [
                    {
                        "url": "https://trusthub.twilio.com/v1/Policies/RNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "requirements": {
                            "end_user": [
                                {
                                    "url": "/EndUserTypes/customer_profile_business_information",
                                    "fields": [
                                        "business_type",
                                        "business_registration_number",
                                        "business_name",
                                        "business_registration_identifier",
                                        "business_identity",
                                        "business_industry",
                                        "website_url",
                                        "business_regions_of_operation",
                                        "social_media_profile_urls"
                                    ],
                                    "type": "customer_profile_business_information",
                                    "name": "Business Information",
                                    "requirement_name": "customer_profile_business_information"
                                },
                                {
                                    "url": "/EndUserTypes/authorized_representative_1",
                                    "fields": [
                                        "first_name",
                                        "last_name",
                                        "email",
                                        "phone_number",
                                        "business_title",
                                        "job_position"
                                    ],
                                    "type": "authorized_representative_1",
                                    "name": "Authorized Representative 1",
                                    "requirement_name": "authorized_representative_1"
                                },
                                {
                                    "url": "/EndUserTypes/authorized_representative_2",
                                    "fields": [
                                        "first_name",
                                        "last_name",
                                        "email",
                                        "phone_number",
                                        "business_title",
                                        "job_position"
                                    ],
                                    "type": "authorized_representative_2",
                                    "name": "Authorized Representative 2",
                                    "requirement_name": "authorized_representative_2"
                                }
                            ],
                            "supporting_trust_products": [],
                            "supporting_document": [
                                [
                                    {
                                        "description": "Customer Profile HQ Physical Address",
                                        "type": "document",
                                        "name": "Physical Business Address",
                                        "accepted_documents": [
                                            {
                                                "url": "/SupportingDocumentTypes/customer_profile_address",
                                                "fields": [
                                                    "address_sids"
                                                ],
                                                "type": "customer_profile_address",
                                                "name": "Physical Business Address"
                                            }
                                        ],
                                        "requirement_name": "customer_profile_address"
                                    }
                                ]
                            ],
                            "supporting_customer_profiles": []
                        },
                        "friendly_name": "Primary Customer Profile of type Business",
                        "sid": "RNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ]
            }
            '''
        ))

        actual = self.client.trusthub.v1.policies.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trusthub.v1.policies("RNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://trusthub.twilio.com/v1/Policies/RNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "url": "https://trusthub.twilio.com/v1/Policies/RNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "requirements": {
                    "end_user": [
                        {
                            "url": "/EndUserTypes/customer_profile_business_information",
                            "fields": [
                                "business_type",
                                "business_registration_number",
                                "business_name",
                                "business_registration_identifier",
                                "business_identity",
                                "business_industry",
                                "website_url",
                                "business_regions_of_operation",
                                "social_media_profile_urls"
                            ],
                            "type": "customer_profile_business_information",
                            "name": "Business Information",
                            "requirement_name": "customer_profile_business_information"
                        },
                        {
                            "url": "/EndUserTypes/authorized_representative_1",
                            "fields": [
                                "first_name",
                                "last_name",
                                "email",
                                "phone_number",
                                "business_title",
                                "job_position"
                            ],
                            "type": "authorized_representative_1",
                            "name": "Authorized Representative 1",
                            "requirement_name": "authorized_representative_1"
                        },
                        {
                            "url": "/EndUserTypes/authorized_representative_2",
                            "fields": [
                                "first_name",
                                "last_name",
                                "email",
                                "phone_number",
                                "business_title",
                                "job_position"
                            ],
                            "type": "authorized_representative_2",
                            "name": "Authorized Representative 2",
                            "requirement_name": "authorized_representative_2"
                        }
                    ],
                    "supporting_trust_products": [],
                    "supporting_document": [
                        [
                            {
                                "description": "Customer Profile HQ Physical Address",
                                "type": "document",
                                "name": "Physical Business Address",
                                "accepted_documents": [
                                    {
                                        "url": "/SupportingDocumentTypes/customer_profile_address",
                                        "fields": [
                                            "address_sids"
                                        ],
                                        "type": "customer_profile_address",
                                        "name": "Physical Business Address"
                                    }
                                ],
                                "requirement_name": "customer_profile_address"
                            }
                        ]
                    ],
                    "supporting_customer_profiles": []
                },
                "friendly_name": "Primary Customer Profile of type Business",
                "sid": "RNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.trusthub.v1.policies("RNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)