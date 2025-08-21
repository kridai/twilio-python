# Twilio Python Helper Library

[![Tests](https://github.com/twilio/twilio-python/actions/workflows/test-and-deploy.yml/badge.svg)](https://github.com/twilio/twilio-python/actions/workflows/test-and-deploy.yml)
[![PyPI](https://img.shields.io/pypi/v/twilio.svg)](https://pypi.python.org/pypi/twilio)
[![PyPI](https://img.shields.io/pypi/pyversions/twilio.svg)](https://pypi.python.org/pypi/twilio)
[![Learn OSS Contribution in TwilioQuest](https://img.shields.io/static/v1?label=TwilioQuest&message=Learn%20to%20contribute%21&color=F22F46&labelColor=1f243c&style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAMAAAD04JH5AAAASFBMVEUAAAAZGRkcHBwjIyMoKCgAAABgYGBoaGiAgICMjIyzs7PJycnMzMzNzc3UoBfd3d3m5ubqrhfrMEDu7u739/f4vSb/3AD///9tbdyEAAAABXRSTlMAAAAAAMJrBrEAAAKoSURBVHgB7ZrRcuI6EESdyxXGYoNFvMD//+l2bSszRgyUYpFAsXOeiJGmj4NkuWx1Qeh+Ekl9DgEXOBwOx+Px5xyQhDykfgq4wG63MxxaR4ddIkg6Ul3g84vCIcjPBA5gmUMeXESrlukuoK33+33uID8TWeLAdOWsKpJYzwVMB7bOzYSGOciyUlXSn0/ABXTosJ1M1SbypZ4O4MbZuIDMU02PMbauhhHMHXbmebmALIiEbbbbbUrpF1gwE9kFfRNAJaP+FQEXCCTGyJ4ngDrjOFo3jEL5JdqjF/pueR4cCeCGgAtwmuRS6gDwaRiGvu+DMFwSBLTE3+jF8JyuV1okPZ+AC4hDFhCHyHQjdjPHUKFDlHSJkHQXMB3KpSwXNGJPcwwTdZiXlRN0gSp0zpWxNtM0beYE0nRH6QIbO7rawwXaBYz0j78gxjokDuv12gVeUuBD0MDi0OQCLvDaAho4juP1Q/jkAncXqIcCfd+7gAu4QLMACCLxpRsSuQh0igu0C9Svhi7weAGZg50L3IE3cai4IfkNZAC8dfdhsUD3CgKBVC9JE5ABAFzg4QL/taYPAAWrHdYcgfLaIgAXWJ7OV38n1LEF8tt2TH29E+QAoDoO5Ve/LtCQDmKM9kPbvCEBApK+IXzbcSJ0cIGF6e8gpcRhUDogWZ8JnaWjPXc/fNnBBUKRngiHgTUSivSzDRDgHZQOLvBQgf8rRt+VdBUUhwkU6VpJ+xcOwQUqZr+mR0kvBUgv6cB4+37hQAkXqE8PwGisGhJtN4xAHMzrsgvI7rccXqSvKh6jltGlrOHA3Xk1At3LC4QiPdX9/0ndHpGVvTjR4bZA1ypAKgVcwE5vx74ulwIugDt8e/X7JgfkucBMIAr26ndnB4UCLnDOqvteQsHlgX9N4A+c4cW3DXSPbwAAAABJRU5ErkJggg==)](https://twil.io/learn-open-source)

The **Twilio Python Helper Library** is the official Python SDK for interacting with Twilio's APIs. This library simplifies the process of making calls, sending SMS messages, generating TwiML, and accessing all of Twilio's communication services from your Python applications.

Twilio is a cloud communications platform that enables developers to build, scale, and operate real-time communications within software applications via web service APIs for messaging, voice, video, and authentication.

## Table of Contents

- [Key Features](#key-features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Documentation](#documentation)
- [Supported Python Versions](#supported-python-versions)
- [Usage Examples](#usage-examples)
  - [API Credentials](#api-credentials)
  - [Specify Region and/or Edge](#specify-region-andor-edge)
  - [Make a Call](#make-a-call)
  - [Get data about an existing call](#get-data-about-an-existing-call)
  - [Iterate through records](#iterate-through-records)
  - [Asynchronous API Requests](#asynchronous-api-requests)
  - [Enable Debug Logging](#enable-debug-logging)
  - [Handling Exceptions](#handling-exceptions)
  - [Generating TwiML](#generating-twiml)
- [Advanced Examples](#advanced-examples)
- [Docker Support](#docker-support)
- [Getting Help](#getting-help)
- [Contributing](#contributing)

## Key Features

- 🔗 **Complete API Coverage**: Access all Twilio REST APIs including Voice, SMS, Video, Chat, and more
- 🚀 **Easy to Use**: Intuitive Python interface with comprehensive documentation and examples
- ⚡ **Async Support**: Built-in support for asynchronous operations using `asyncio`
- 🌍 **Global Infrastructure**: Support for Twilio's global regions and edge locations
- 🔒 **Secure Authentication**: Multiple authentication methods including API keys and tokens
- 📞 **TwiML Generation**: Create TwiML responses for handling voice calls and messaging
- 🛠️ **Error Handling**: Comprehensive exception handling for robust applications
- 🐍 **Modern Python**: Supports Python 3.7+ with type hints and modern Python features

## Prerequisites

Before using the Twilio Python Helper Library, you'll need:

1. **Python 3.7 or higher** installed on your system
2. **A Twilio account** - [Sign up for free](https://www.twilio.com/try-twilio)
3. **Twilio credentials** - Your Account SID and Auth Token from the [Twilio Console](https://console.twilio.com)

## Documentation

- **📚 [Twilio API Documentation][apidocs]** - Complete reference for all Twilio APIs
- **🐍 [Python Library Documentation][libdocs]** - Detailed documentation for this Python helper library
- **🎯 [Quick Start Guide](https://www.twilio.com/docs/libraries/python)** - Get up and running quickly
- **💡 [Code Examples](https://www.twilio.com/docs/libraries/python/usage-guide)** - Real-world usage examples

## Supported Python Versions

This library supports the following Python implementations:

- **Python 3.7** - Supported
- **Python 3.8** - Supported  
- **Python 3.9** - Supported
- **Python 3.10** - Supported
- **Python 3.11** - Supported

> **Note**: `twilio-python` uses a modified version of [Semantic Versioning](https://semver.org) for all changes. [See this document](VERSIONS.md) for details.

## Installation

The Twilio Python Helper Library is available on PyPI and can be installed using pip, the standard Python package manager.

### Install via pip (Recommended)

Install from PyPi using [pip](https://pip.pypa.io/en/latest/):

```shell
pip3 install twilio
```

### Alternative Installation Methods

#### Install using pip if not available

If pip install fails on Windows, check the path length of the directory. If it is greater 260 characters then enable [Long Paths](https://docs.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation) or choose other shorter location.

Don't have pip installed? Try installing it, by running this from the command line:

```shell
curl https://bootstrap.pypa.io/get-pip.py | python
```

#### Install from source

You can also [download the source code (ZIP)](https://github.com/twilio/twilio-python/zipball/main 'twilio-python source code') for `twilio-python`, and then run:

```shell
python3 setup.py install
```

> **Info**
> If the command line gives you an error message that says Permission Denied, try running the above commands with `sudo` (e.g., `sudo pip3 install twilio`).

## Quick Start

Get started with Twilio in just a few lines of code! This example shows how to send your first SMS message.

### Your First SMS

Follow these steps to send your first SMS message:

**Step 1:** Save the following code to a file named `send_sms.py`. Make sure to update the credentials and phone numbers:

```python
from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
# Find these values at https://console.twilio.com
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"

# Initialize the Twilio client
client = Client(account_sid, auth_token)

# Send an SMS message
message = client.messages.create(
    to="+15558675309",      # Replace with your phone number
    from_="+15017250604",   # Replace with your Twilio number
    body="Hello from Python!")

print(f"Message sent! SID: {message.sid}")
```

**Step 2:** Run the script from your terminal:

```shell
python3 send_sms.py
```

**Step 3:** Check your phone! You should receive the SMS message within a few seconds.

> **Security Note**
> It's okay to hardcode your credentials when testing locally, but you should use environment variables to keep them secret before committing any code or deploying to production. Check out [How to Set Environment Variables](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html) for more information.

## Usage Examples

### API Credentials

The Twilio client requires authentication using your Twilio credentials. You have several options for providing these credentials securely:

#### Option 1: Environment Variables (Recommended)

Set your credentials as environment variables for maximum security:

```bash
export TWILIO_ACCOUNT_SID="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
export TWILIO_AUTH_TOKEN="your_auth_token"
```

Then initialize the client without parameters:

```python
from twilio.rest import Client

# Automatically uses TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN environment variables
client = Client()
```

#### Option 2: Direct Authentication with Account SID and Auth Token

Pass your credentials directly to the constructor:

```python
from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"
client = Client(account_sid, auth_token)
```

#### Option 3: API Key Authentication (More Secure)

For enhanced security, use API keys instead of your main Auth Token:

```python
from twilio.rest import Client

api_key = "XXXXXXXXXXXXXXXXX"
api_secret = "YYYYYYYYYYYYYYYYYY"
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client = Client(api_key, api_secret, account_sid)
```

> **Best Practice**: API keys can be restricted to specific permissions and are safer than using your main Auth Token. Create API keys in the [Twilio Console](https://console.twilio.com/us1/develop/api-keys).

Alternatively, a `Client` constructor without these parameters will
look for `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` variables inside the
current environment.

We suggest storing your credentials as environment variables. Why? You'll never
have to worry about committing your credentials and accidentally posting them
somewhere public.

```python
from twilio.rest import Client
client = Client()
```

### Specify Region and/or Edge

Optimize your application's performance by specifying Twilio's [Global Infrastructure](https://www.twilio.com/docs/global-infrastructure) regions and edges closest to your users:

#### Set Region and Edge at Client Creation

```python
from twilio.rest import Client

# Connect to Twilio's Australia region with Sydney edge location
client = Client(region='au1', edge='sydney')
```

#### Using Environment Variables

```bash
export TWILIO_REGION=au1
export TWILIO_EDGE=sydney
```

A `Client` constructor without these parameters will also look for `TWILIO_REGION` and `TWILIO_EDGE` variables inside the current environment.

#### Set Region and Edge After Client Creation

You can also modify the region and edge after creating the client:

```python
from twilio.rest import Client

client = Client()
client.region = 'au1'
client.edge = 'sydney'
```

This will result in the `hostname` transforming from `api.twilio.com` to `api.sydney.au1.twilio.com`.

> **Performance Tip**: Choosing the right region and edge can significantly reduce latency for your applications.

### Make a Call

Initiate outbound voice calls programmatically:

```python
from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"
client = Client(account_sid, auth_token)

# Make a phone call and play a message from a URL
call = client.calls.create(
    to="+19991231234",      # The phone number to call
    from_="+15551234567",   # Your Twilio phone number
    url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient"  # TwiML instructions
)

print(f"Call initiated! SID: {call.sid}")
```

> **Note**: Replace the phone numbers with actual numbers. The `from_` number must be a phone number you've purchased from Twilio or a verified caller ID.

### Get Data About an Existing Call

Retrieve information about calls you've made:

```python
from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"
client = Client(account_sid, auth_token)

# Fetch call details using the call SID
call = client.calls.get("CA42ed11f93dc08b952027ffbc406d0868")

print(f"Call to: {call.to}")
print(f"Call from: {call.from_}")
print(f"Call status: {call.status}")
print(f"Call duration: {call.duration} seconds")
```

### Iterate Through Records

The library automatically handles pagination for you. Collections, such as `calls` and `messages`, have `list` and `stream` methods that page under the hood. With both `list` and `stream`, you can specify the number of records you want to receive (`limit`) and the maximum size you want each page fetch to be (`page_size`). The library will then handle the task for you.

`list` eagerly fetches all records and returns them as a list, whereas `stream` returns an iterator and lazily retrieves pages of records as you iterate over the collection. You can also page manually using the `page` method.

#### Use the `list` method

Fetch all messages at once (be careful with large datasets):

```python
from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)

# Get all messages (use with caution for large datasets)
all_messages = client.messages.list()
for message in all_messages:
    print(f"Message to {message.to}: {message.body}")
```

#### Use the `stream` method (Recommended for large datasets)

```python
from twilio.rest import Client

client = Client()

# Stream messages efficiently - fetches pages as needed
for message in client.messages.stream(limit=100):
    print(f"Message SID: {message.sid}")
    print(f"To: {message.to}")
    print(f"Body: {message.body}")
    print("---")
```

#### Filtering and Limiting Results

```python
from datetime import datetime, timedelta
from twilio.rest import Client

client = Client()

# Get messages from the last 7 days
week_ago = datetime.now() - timedelta(days=7)
recent_messages = client.messages.list(
    date_sent_after=week_ago,
    limit=50  # Only fetch 50 messages
)

for message in recent_messages:
    print(f"Recent message: {message.body}")
```

### Asynchronous API Requests

For high-performance applications, the Twilio client supports asynchronous operations using Python's `asyncio` library. This allows you to make multiple API calls concurrently without blocking your application.

#### Basic Async Usage

```python
import asyncio
from twilio.http.async_http_client import AsyncTwilioHttpClient
from twilio.rest import Client

async def send_messages():
    account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    auth_token  = "your_auth_token"
    
    # Create async HTTP client
    http_client = AsyncTwilioHttpClient()
    client = Client(account_sid, auth_token, http_client=http_client)

    # Send message asynchronously
    message = await client.messages.create_async(
        to="+12316851234", 
        from_="+15555555555",
        body="Hello from async Python!"
    )
    
    print(f"Async message sent! SID: {message.sid}")

# Run the async function
asyncio.run(send_messages())
```

#### Concurrent Operations

```python
import asyncio
from twilio.http.async_http_client import AsyncTwilioHttpClient
from twilio.rest import Client

async def send_multiple_messages():
    client = Client(http_client=AsyncTwilioHttpClient())
    
    # Send multiple messages concurrently
    tasks = []
    phone_numbers = ["+1234567890", "+1987654321", "+1555666777"]
    
    for number in phone_numbers:
        task = client.messages.create_async(
            to=number,
            from_="+15555555555",
            body=f"Hello {number}!"
        )
        tasks.append(task)
    
    # Wait for all messages to be sent
    messages = await asyncio.gather(*tasks)
    
    for message in messages:
        print(f"Sent message {message.sid}")

asyncio.run(send_multiple_messages())
```

### Enable Debug Logging

Debug logging helps you troubleshoot issues by showing the actual HTTP requests and responses between your application and Twilio's API.

#### Log to Console

```python
import logging
from twilio.rest import Client

# Set up logging to console
logging.basicConfig(level=logging.INFO)

client = Client(account_sid, auth_token)
client.http_client.logger.setLevel(logging.INFO)

# Now all API requests will be logged to console
message = client.messages.create(
    to="+1234567890",
    from_="+0987654321", 
    body="This request will be logged!"
)
```

#### Log to File

```python
import logging
from twilio.rest import Client

# Set up logging to file
logging.basicConfig(
    filename='./twilio_api.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

client = Client(account_sid, auth_token)
client.http_client.logger.setLevel(logging.INFO)

# API requests will be logged to ./twilio_api.log
```

#### Advanced Logging Configuration

```python
import logging
from twilio.rest import Client

# Create custom logger
logger = logging.getLogger('twilio_app')
logger.setLevel(logging.DEBUG)

# Create file handler
handler = logging.FileHandler('twilio_debug.log')
handler.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

client = Client()
client.http_client.logger = logger
```

### Handling Exceptions

The Twilio Python Helper Library provides comprehensive error handling to help you build robust applications. Version 8.x+ exports specific exception classes for different types of errors.

#### Basic Exception Handling

```python
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

client = Client()

try:
    message = client.messages.create(
        to="+12316851234", 
        from_="+15555555555",
        body="Hello there!"
    )
    print(f"Message sent successfully: {message.sid}")
    
except TwilioRestException as e:
    print(f"Twilio error occurred: {e}")
    print(f"Error code: {e.code}")
    print(f"Error message: {e.msg}")
    print(f"More info: {e.uri}")
```

#### Handling Specific Error Types

```python
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

client = Client()

try:
    call = client.calls.create(
        to="+1234567890",
        from_="+1invalid_number",  # This will cause an error
        url="http://demo.twilio.com/docs/voice.xml"
    )
except TwilioRestException as e:
    if e.code == 21212:
        print("Invalid 'From' phone number format")
    elif e.code == 21213:
        print("Invalid 'To' phone number format")
    elif e.code == 21214:
        print("'To' number cannot be reached")
    else:
        print(f"Unexpected error: {e.msg}")
```

#### Async Exception Handling

```python
import asyncio
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from twilio.http.async_http_client import AsyncTwilioHttpClient

async def send_message_with_error_handling():
    client = Client(http_client=AsyncTwilioHttpClient())
    
    try:
        message = await client.messages.create_async(
            to="+12316851234",
            from_="+15555555555", 
            body="Hello async world!"
        )
        print(f"Async message sent: {message.sid}")
        
    except TwilioRestException as e:
        print(f"Async Twilio error: {e.msg}")

asyncio.run(send_message_with_error_handling())
```

### Generating TwiML

TwiML (Twilio Markup Language) is used to control phone calls and respond to SMS messages. The helper library provides an easy way to generate TwiML responses.

#### Voice TwiML Example

```python
from twilio.twiml.voice_response import VoiceResponse

# Create a TwiML response for a voice call
response = VoiceResponse()

# Say a message to the caller
response.say('Welcome to Twilio! This is generated using Python.', voice='alice')

# Pause for 2 seconds
response.pause(length=2)

# Play an audio file
response.play('https://api.twilio.com/cowbell.mp3')

# Redirect to another TwiML URL
response.redirect('https://demo.twilio.com/docs/voice.xml')

print(str(response))
```

Output:
```xml
<?xml version="1.0" encoding="utf-8"?>
<Response>
    <Say voice="alice">Welcome to Twilio! This is generated using Python.</Say>
    <Pause length="2"/>
    <Play>https://api.twilio.com/cowbell.mp3</Play>
    <Redirect>https://demo.twilio.com/docs/voice.xml</Redirect>
</Response>
```

#### SMS TwiML Example

```python
from twilio.twiml.messaging_response import MessagingResponse

# Create a TwiML response for SMS
response = MessagingResponse()

# Reply with a message
response.message('Thank you for your message! We received: ')

# Add media to the response
response.message().media('https://demo.twilio.com/owl.png')

print(str(response))
```

#### Interactive Voice Response (IVR) Example

```python
from twilio.twiml.voice_response import VoiceResponse

response = VoiceResponse()

# Gather user input
gather = response.gather(
    num_digits=1,
    action='/handle-user-input',
    method='POST'
)

gather.say(
    'Press 1 for Sales, Press 2 for Support, or Press 0 to speak with an operator.',
    voice='alice'
)

# Fallback if no input received
response.say('Sorry, I didn\'t receive any input. Goodbye!')

print(str(response))
```

## Advanced Examples

### Custom HTTP Client Configuration

Learn how to customize the HTTP client for enterprise environments, proxy servers, and custom authentication:

- **[Custom HTTP Client Guide](./advanced-examples/custom-http-client.md)** - Detailed guide for enterprise proxy configuration

### Real-World Use Cases

#### Build a Customer Support Hotline

```python
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client

def handle_incoming_call():
    response = VoiceResponse()
    
    gather = response.gather(
        num_digits=1,
        action='/route-call',
        method='POST',
        timeout=10
    )
    
    gather.say(
        'Welcome to Acme Corp. Press 1 for Sales, 2 for Support, or 0 for an operator.',
        voice='alice'
    )
    
    # If no input, repeat the menu
    response.redirect('/voice-menu')
    
    return str(response)
```

#### Send Bulk SMS Notifications

```python
import asyncio
from twilio.rest import Client
from twilio.http.async_http_client import AsyncTwilioHttpClient

async def send_bulk_notifications(phone_numbers, message):
    client = Client(http_client=AsyncTwilioHttpClient())
    
    tasks = []
    for number in phone_numbers:
        task = client.messages.create_async(
            to=number,
            from_='+15555555555',  # Your Twilio number
            body=message
        )
        tasks.append(task)
    
    # Send all messages concurrently
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    success_count = 0
    for result in results:
        if isinstance(result, Exception):
            print(f"Failed to send message: {result}")
        else:
            success_count += 1
            print(f"Message sent: {result.sid}")
    
    print(f"Successfully sent {success_count}/{len(phone_numbers)} messages")

# Usage
phone_list = ['+1234567890', '+1987654321', '+1555666777']
asyncio.run(send_bulk_notifications(phone_list, "Important update from our system!"))
```

## Docker Support

The `Dockerfile` present in this repository and its respective `twilio/twilio-python` Docker image are currently used by Twilio for testing purposes only.

### Running Tests with Docker

```bash
# Build the Docker image
docker build -t twilio/twilio-python .

# Run tests in container
docker run twilio/twilio-python pytest tests --ignore=tests/cluster
```

## Getting Help

Need help with the Twilio Python Helper Library? Here are your best resources:

### 📚 Documentation and Resources

- **[Twilio Support Help Center](https://support.twilio.com)** - Search our comprehensive knowledge base
- **[Python Library Documentation](https://twilio.github.io/twilio-python)** - Complete API reference
- **[Twilio Docs](https://www.twilio.com/docs)** - Official Twilio documentation
- **[Code Examples](https://www.twilio.com/docs/libraries/python)** - Real-world usage examples

### 🎫 Official Support

- **[File a Support Ticket](https://twilio.com/help/contact)** - Get help from Twilio's support team
- **[Twilio Community](https://community.twilio.com)** - Connect with other developers

### 🐛 Issues and Feature Requests

Found a bug in the library or have a feature request?

- **Search existing issues** first in our [GitHub Issues](https://github.com/twilio/twilio-python/issues)
- **Open a new issue** if your problem hasn't been reported
- **Submit a pull request** if you'd like to contribute a fix or improvement

### 📧 Security Issues

For security-related issues, please email us directly at **security@twilio.com** instead of opening a public issue.

## Contributing

We love contributions from the community! Here's how you can help:

### Ways to Contribute

- 🐛 **Report bugs** - Help us identify and fix issues
- 💡 **Suggest features** - Share ideas for new functionality  
- 📖 **Improve documentation** - Help make our docs clearer
- 🔧 **Submit code** - Fix bugs or implement new features
- ⭐ **Star the repo** - Show your support

### Getting Started

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Run the test suite (`make test`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/twilio-python.git
cd twilio-python

# Create virtual environment
make venv

# Install dependencies
make develop

# Run tests
make test
```

### Code Style

This project uses:
- **Black** for code formatting
- **Flake8** for linting
- **pytest** for testing

Run formatting and linting:
```bash
make prettier      # Format code
make prettier-check # Check formatting
make analysis      # Run linting
```

For more details, see our [Contributing Guide](CONTRIBUTING.md).

If you've instead found a bug in the library or would like new features added, go ahead and open issues or pull requests against this repo!

[apidocs]: https://www.twilio.com/docs/api
[twiml]: https://www.twilio.com/docs/api/twiml
[libdocs]: https://twilio.github.io/twilio-python
