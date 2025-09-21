================
CODE SNIPPETS
================
TITLE: Add and execute custom Python examples in OpenAI library
DESCRIPTION: This snippet demonstrates how to create a new Python example file within the 'examples/' directory and then make it executable. It allows running custom examples against the API.

SOURCE: https://github.com/openai/openai-python/blob/main/CONTRIBUTING.md#_snippet_4

LANGUAGE: Python
CODE:
```
# add an example to examples/<your-example>.py

#!/usr/bin/env -S rye run python
…
```

LANGUAGE: Shell
CODE:
```
$ chmod +x examples/<your-example>.py
```

LANGUAGE: Shell
CODE:
```
# run the example against your api
$ ./examples/<your-example>.py
```

--------------------------------

TITLE: Install OpenAI Python library from local wheel file
DESCRIPTION: After building the package, this command installs the library from the generated wheel file (.whl) using pip. This provides an efficient way to install the locally built version.

SOURCE: https://github.com/openai/openai-python/blob/main/CONTRIBUTING.md#_snippet_7

LANGUAGE: Shell
CODE:
```
$ pip install ./path-to-wheel-file.whl
```

--------------------------------

TITLE: Install OpenAI Python library from Git via pip
DESCRIPTION: This command installs the OpenAI Python library directly from its GitHub repository using pip, leveraging SSH for authentication. This method is suitable for using the repository from source.

SOURCE: https://github.com/openai/openai-python/blob/main/CONTRIBUTING.md#_snippet_5

LANGUAGE: Shell
CODE:
```
$ pip install git+ssh://git@github.com/openai/openai-python.git
```

--------------------------------

TITLE: Run OpenAI Python library tests
DESCRIPTION: This command executes the test suite for the OpenAI Python library. Ensure a mock server is set up and running before initiating the tests.

SOURCE: https://github.com/openai/openai-python/blob/main/CONTRIBUTING.md#_snippet_9

LANGUAGE: Shell
CODE:
```
$ ./scripts/test
```

--------------------------------

TITLE: Build OpenAI Python distributable package
DESCRIPTION: These commands build the OpenAI Python library into distributable formats (.tar.gz and .whl files) located in the 'dist/' directory. This is necessary for creating installable versions of the package.

SOURCE: https://github.com/openai/openai-python/blob/main/CONTRIBUTING.md#_snippet_6

LANGUAGE: Shell
CODE:
```
$ rye build
```

LANGUAGE: Shell
CODE:
```
$ python -m build
```

--------------------------------

TITLE: Install OpenAI Python dependencies using pip without Rye
DESCRIPTION: For users not using Rye, this command installs all development dependencies listed in 'requirements-dev.lock' using pip. Ensure a virtual environment is activated and the correct Python version is used.

SOURCE: https://github.com/openai/openai-python/blob/main/CONTRIBUTING.md#_snippet_3

LANGUAGE: Shell
CODE:
```
$ pip install -r requirements-dev.lock
```

--------------------------------

TITLE: Install OpenAI Python SDK with AIOHTTP Support
DESCRIPTION: Instructions to install the OpenAI Python library from PyPI. The `[aiohttp]` extra is included to provide asynchronous HTTP client capabilities, which are essential for `AsyncOpenAI`.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_7

LANGUAGE: Shell
CODE:
```
pip install openai[aiohttp]
```

--------------------------------

TITLE: Synchronize OpenAI Python environment dependencies with Rye
DESCRIPTION: After manually installing Rye, this command synchronizes all project dependencies and features, ensuring the Python environment is correctly configured for development.

SOURCE: https://github.com/openai/openai-python/blob/main/CONTRIBUTING.md#_snippet_1

LANGUAGE: Shell
CODE:
```
$ rye sync --all-features
```

--------------------------------

TITLE: Set up mock server for OpenAI Python tests with npx prism
DESCRIPTION: This command uses npx prism to set up a mock server based on an OpenAPI specification. A mock server is required for running most tests in the OpenAI Python library.

SOURCE: https://github.com/openai/openai-python/blob/main/CONTRIBUTING.md#_snippet_8

LANGUAGE: Shell
CODE:
```
# you will need npm installed
$ npx prism mock path/to/your/openapi.yml
```

--------------------------------

TITLE: Bootstrap OpenAI Python environment with Rye
DESCRIPTION: This command runs a bootstrap script to set up the development environment using Rye, which automatically provisions a Python environment with the expected version and manages dependencies.

SOURCE: https://github.com/openai/openai-python/blob/main/CONTRIBUTING.md#_snippet_0

LANGUAGE: Shell
CODE:
```
$ ./scripts/bootstrap
```

--------------------------------

TITLE: Manually publish OpenAI Python package to PyPI
DESCRIPTION: This command allows for manual publication of the OpenAI Python package to PyPI. It requires the 'PYPI_TOKEN' environment variable to be set for authentication.

SOURCE: https://github.com/openai/openai-python/blob/main/CONTRIBUTING.md#_snippet_12

LANGUAGE: Shell
CODE:
```
bin/publish-pypi
```

--------------------------------

TITLE: Install aiohttp for Async OpenAI Client (Shell)
DESCRIPTION: This command installs the `aiohttp` library, which can be used as an alternative HTTP backend for the `AsyncOpenAI` client to potentially improve concurrency performance.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_6

LANGUAGE: sh
CODE:
```
pip install aiohttp
```

--------------------------------

TITLE: Lint OpenAI Python code with ruff
DESCRIPTION: This command runs the linting process using ruff to identify and report code style and quality issues in the OpenAI Python repository.

SOURCE: https://github.com/openai/openai-python/blob/main/CONTRIBUTING.md#_snippet_10

LANGUAGE: Shell
CODE:
```
$ ./scripts/lint
```

--------------------------------

TITLE: Activate Python virtual environment and run script
DESCRIPTION: These commands activate the project's Python virtual environment, allowing direct execution of Python scripts without the 'rye run' prefix. This is standard practice for managing Python dependencies.

SOURCE: https://github.com/openai/openai-python/blob/main/CONTRIBUTING.md#_snippet_2

LANGUAGE: Shell
CODE:
```
# Activate the virtual environment - https://docs.python.org/3/library/venv.html#how-venvs-work
$ source .venv/bin/activate
```

LANGUAGE: Shell
CODE:
```
# now you can omit the `rye run` prefix
$ python script.py
```

--------------------------------

TITLE: Install OpenAI Python Library
DESCRIPTION: This command installs the official OpenAI Python API library from PyPI, enabling access to OpenAI's REST API functionalities from Python 3.8+ applications.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_0

LANGUAGE: sh
CODE:
```
pip install openai
```

--------------------------------

TITLE: Format OpenAI Python code with ruff and black
DESCRIPTION: This command automatically formats the code and fixes ruff issues in the OpenAI Python repository, ensuring adherence to established coding style guidelines.

SOURCE: https://github.com/openai/openai-python/blob/main/CONTRIBUTING.md#_snippet_11

LANGUAGE: Shell
CODE:
```
$ ./scripts/format
```

--------------------------------

TITLE: Start and Stream an Existing OpenAI Assistant Run (Python)
DESCRIPTION: Explains how to initiate and stream responses from an already existing OpenAI Assistant run associated with a populated thread. This method is used when you have an active run and want to receive its output in real-time.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_8

LANGUAGE: python
CODE:
```
client.beta.threads.runs.stream()
```

--------------------------------

TITLE: Check Installed OpenAI Python Library Version
DESCRIPTION: Provides a simple Python code snippet to programmatically determine the currently installed version of the `openai` library. This is useful for debugging and verifying environment setup.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_37

LANGUAGE: python
CODE:
```
import openai
print(openai.__version__)
```

--------------------------------

TITLE: Create Thread, Run, and Stream OpenAI Assistant Response (Python)
DESCRIPTION: Describes a helper method that combines adding a message to a thread, starting a new run, and then streaming its response. This is a convenient way to kick off a new interaction and immediately receive streaming updates.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_9

LANGUAGE: python
CODE:
```
client.beta.threads.create_and_run_stream()
```

--------------------------------

TITLE: Generate Text Asynchronously with OpenAI Responses API (Python)
DESCRIPTION: This Python example demonstrates asynchronous text generation using the `AsyncOpenAI` client. It shows how to initialize the asynchronous client, use `await` for API calls, and run the asynchronous function using `asyncio.run()`.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_5

LANGUAGE: python
CODE:
```
import os
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


async def main() -> None:
    response = await client.responses.create(
        model="gpt-4o", input="Explain disestablishmentarianism to a smart five year old."
    )
    print(response.output_text)


asyncio.run(main())
```

--------------------------------

TITLE: Connect to OpenAI Realtime API for Basic Text Conversation
DESCRIPTION: Shows how to establish a WebSocket connection to the OpenAI Realtime API using `AsyncOpenAI`. This example demonstrates sending a text message and processing incoming text delta events for a low-latency conversational experience.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_11

LANGUAGE: Python
CODE:
```
import asyncio
from openai import AsyncOpenAI

async def main():
    client = AsyncOpenAI()

    async with client.beta.realtime.connect(model="gpt-4o-realtime-preview") as connection:
        await connection.session.update(session={'modalities': ['text']})

        await connection.conversation.item.create(
            item={
                "type": "message",
                "role": "user",
                "content": [{"type": "input_text", "text": "Say hello!"}],
            }
        )
        await connection.response.create()

        async for event in connection:
            if event.type == 'response.text.delta':
                print(event.delta, flush=True, end="")

            elif event.type == 'response.text.done':
                print()

            elif event.type == "response.done":
                break

asyncio.run(main())
```

--------------------------------

TITLE: Generate Text with OpenAI Responses API (Python)
DESCRIPTION: This Python example demonstrates how to use the OpenAI Python library's Responses API to generate text from a specified model (e.g., gpt-4o). It shows how to initialize the client, set an API key, and make a text generation request with instructions and input.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_1

LANGUAGE: python
CODE:
```
import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

response = client.responses.create(
    model="gpt-4o",
    instructions="You are a coding assistant that talks like a pirate.",
    input="How do I check if a Python object is an instance of a class?",
)

print(response.output_text)
```

--------------------------------

TITLE: Generate Text with OpenAI Chat Completions API (Python)
DESCRIPTION: This Python example illustrates how to use the OpenAI Python library's Chat Completions API for text generation. It demonstrates initializing the client and sending a request with a list of messages, including role-based content, to a specified model.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_2

LANGUAGE: python
CODE:
```
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": "Talk like a pirate."},
        {
            "role": "user",
            "content": "How do I check if a Python object is an instance of a class?",
        },
    ],
)

print(completion.choices[0].message.content)
```

--------------------------------

TITLE: Asynchronous Automatic Pagination with OpenAI Python Client
DESCRIPTION: This example shows how to asynchronously iterate through paginated results using `AsyncOpenAI`. It uses `async for` to automatically fetch subsequent pages of fine-tuning jobs, suitable for non-blocking I/O operations in asynchronous applications.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_15

LANGUAGE: python
CODE:
```
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI()


async def main() -> None:
    all_jobs = []
    # Iterate through items across all pages, issuing requests as needed.
    async for job in client.fine_tuning.jobs.list(
        limit=20,
    ):
        all_jobs.append(job)
    print(all_jobs)


asyncio.run(main())
```

--------------------------------

TITLE: Uploading Files using PathLike with OpenAI Python Client
DESCRIPTION: This example demonstrates uploading a file to the OpenAI API using a `PathLike` object (specifically `pathlib.Path`). The client automatically handles reading the file contents for the upload, simplifying file management for purposes like fine-tuning.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_19

LANGUAGE: python
CODE:
```
from pathlib import Path
from openai import OpenAI

client = OpenAI()

client.files.create(
    file=Path("input.jsonl"),
    purpose="fine-tune",
)
```

--------------------------------

TITLE: List all available OpenAI Models
DESCRIPTION: Lists all available OpenAI models that can be used with the API. This method corresponds to the `GET /models` API endpoint and returns a paginated list of models.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_36

LANGUAGE: python
CODE:
```
client.models.list()
```

--------------------------------

TITLE: List Containers in OpenAI Python Client
DESCRIPTION: Lists containers using the OpenAI Python client. This method sends a GET request to the `/containers` endpoint, allowing pagination and filtering through optional parameters. It returns a `SyncCursorPage[ContainerListResponse]` object.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_151

LANGUAGE: python
CODE:
```
client.containers.list(**params) -> SyncCursorPage[ContainerListResponse]
```

--------------------------------

TITLE: List Fine-Tuning Jobs
DESCRIPTION: Lists all fine-tuning jobs associated with the account, with optional filtering parameters. This method corresponds to the `GET /fine_tuning/jobs` API endpoint and returns a paginated list.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_42

LANGUAGE: python
CODE:
```
client.fine_tuning.jobs.list(**params)
```

--------------------------------

TITLE: Perform Vision Task with OpenAI Responses API (Image URL, Python)
DESCRIPTION: This Python example shows how to use the OpenAI Responses API for vision tasks by providing an image via a URL. It demonstrates constructing a user input with both text and an image URL to query a vision-capable model like 'gpt-4o-mini'.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_3

LANGUAGE: python
CODE:
```
prompt = "What is in this image?"
img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/2023_06_08_Raccoon1.jpg/1599px-2023_06_08_Raccoon1.jpg"

response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": prompt},
                {"type": "input_image", "image_url": f"{img_url}"},
            ],
        }
    ],
)
```

--------------------------------

TITLE: Verifying and Parsing OpenAI Webhooks with Flask
DESCRIPTION: This comprehensive example shows how to set up a Flask endpoint to receive and verify OpenAI webhooks. It uses `client.webhooks.unwrap()` to parse the raw request body and headers, ensuring the webhook's authenticity before processing different event types. It also includes error handling for invalid signatures.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_20

LANGUAGE: python
CODE:
```
from openai import OpenAI
from flask import Flask, request

app = Flask(__name__)
client = OpenAI()  # OPENAI_WEBHOOK_SECRET environment variable is used by default


@app.route("/webhook", methods=["POST"])
def webhook():
    request_body = request.get_data(as_text=True)

    try:
        event = client.webhooks.unwrap(request_body, request.headers)

        if event.type == "response.completed":
            print("Response completed:", event.data)
        elif event.type == "response.failed":
            print("Response failed:", event.data)
        else:
            print("Unhandled event type:", event.type)

        return "ok"
    except Exception as e:
        print("Invalid signature:", e)
        return "Invalid signature", 400


if __name__ == "__main__":
    app.run(port=8000)
```

--------------------------------

TITLE: List Fine-Tuning Job Checkpoints
DESCRIPTION: Lists all available checkpoints for a specific fine-tuning job, allowing access to intermediate training states. This method corresponds to the `GET /fine_tuning/jobs/{fine_tuning_job_id}/checkpoints` API endpoint.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_48

LANGUAGE: python
CODE:
```
client.fine_tuning.jobs.checkpoints.list(fine_tuning_job_id, **params)
```

--------------------------------

TITLE: OpenAI Files API: Get File Content (Binary)
DESCRIPTION: Retrieves the raw binary content of a file by its ID. Returns an HttpxBinaryResponseContent object.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_18

LANGUAGE: python
CODE:
```
client.files.content(file_id)
```

--------------------------------

TITLE: Stream OpenAI API Responses Synchronously
DESCRIPTION: Illustrates how to use the synchronous `OpenAI` client to stream responses from the API. The example shows iterating over the `stream` object to process events as they are received, suitable for long-running text generation.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_9

LANGUAGE: Python
CODE:
```
from openai import OpenAI

client = OpenAI()

stream = client.responses.create(
    model="gpt-4o",
    input="Write a one-sentence bedtime story about a unicorn.",
    stream=True,
)

for event in stream:
    print(event)
```

--------------------------------

TITLE: Auto-parse OpenAI Function Tool Calls with Pydantic and Strict Mode in Python
DESCRIPTION: This example illustrates how to automatically parse function tool calls using the `client.chat.completions.parse()` method in the OpenAI Python SDK. It defines several Pydantic models (`Table`, `Column`, `Operator`, `Condition`, `Query`) to structure a database query tool. The snippet highlights the use of `openai.pydantic_function_tool()` and the requirement for strict tool schema for automatic parsing.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_1

LANGUAGE: Python
CODE:
```
from enum import Enum
from typing import List, Union
from pydantic import BaseModel
import openai

class Table(str, Enum):
    orders = "orders"
    customers = "customers"
    products = "products"

class Column(str, Enum):
    id = "id"
    status = "status"
    expected_delivery_date = "expected_delivery_date"
    delivered_at = "delivered_at"
    shipped_at = "shipped_at"
    ordered_at = "ordered_at"
    canceled_at = "canceled_at"

class Operator(str, Enum):
    eq = "="
    gt = ">"
    lt = "<"
    le = "<="
    ge = ">="
    ne = "!="

class OrderBy(str, Enum):
    asc = "asc"
    desc = "desc"

class DynamicValue(BaseModel):
    column_name: str

class Condition(BaseModel):
    column: str
    operator: Operator
    value: Union[str, int, DynamicValue]

class Query(BaseModel):
    table_name: Table
    columns: List[Column]
    conditions: List[Condition]
    order_by: OrderBy

client = openai.OpenAI()
completion = client.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant. The current date is August 6, 2024. You help users query for the data they are looking for by calling the query function.",
        },
        {
            "role": "user",
            "content": "look up all my orders in may of last year that were fulfilled but not delivered on time",
        },
    ],
    tools=[
        openai.pydantic_function_tool(Query),
    ],
)

tool_call = (completion.choices[0].message.tool_calls or [])[0]
print(tool_call.function)
assert isinstance(tool_call.function.parsed_arguments, Query)
print(tool_call.function.parsed_arguments.table_name)
```

--------------------------------

TITLE: Retrieve a specific OpenAI Model
DESCRIPTION: Retrieves detailed information for a specific OpenAI model by its unique identifier. This method corresponds to the `GET /models/{model}` API endpoint.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_35

LANGUAGE: python
CODE:
```
client.models.retrieve(model)
```

--------------------------------

TITLE: Retrieve a Fine-Tuning Job
DESCRIPTION: Retrieves detailed information about a specific fine-tuning job using its unique ID. This method corresponds to the `GET /fine_tuning/jobs/{fine_tuning_job_id}` API endpoint.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_41

LANGUAGE: python
CODE:
```
client.fine_tuning.jobs.retrieve(fine_tuning_job_id)
```

--------------------------------

TITLE: List Fine-Tuning Job Events
DESCRIPTION: Retrieves a list of events associated with a specific fine-tuning job, providing insights into its progress and status. This method corresponds to the `GET /fine_tuning/jobs/{fine_tuning_job_id}/events` API endpoint.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_44

LANGUAGE: python
CODE:
```
client.fine_tuning.jobs.list_events(fine_tuning_job_id, **params)
```

--------------------------------

TITLE: Access raw HTTP response data from OpenAI client (Python)
DESCRIPTION: This example demonstrates how to access the raw HTTP response object, including headers, by prefixing `.with_raw_response.` to any HTTP method call. After accessing raw data, the response can be parsed back into the expected object using `.parse()`.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_30

LANGUAGE: python
CODE:
```
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.with_raw_response.create(
    messages=[{
        "role": "user",
        "content": "Say this is a test",
    }],
    model="gpt-4o",
)
print(response.headers.get('X-My-Header'))

completion = response.parse()  # get the object that `chat.completions.create()` would have returned
print(completion)
```

--------------------------------

TITLE: Accessing Paginated Response Data Directly with OpenAI Python Client
DESCRIPTION: This example demonstrates how to access the raw data and pagination cursor (`.after`) directly from a paginated response object. It shows iterating through the `data` attribute of the response to process items from a single page.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_17

LANGUAGE: python
CODE:
```
first_page = await client.fine_tuning.jobs.list(
    limit=20,
)

print(f"next page cursor: {first_page.after}")
for job in first_page.data:
    print(job.id)
```

--------------------------------

TITLE: Get Final Completion from OpenAI Chat Stream (Python)
DESCRIPTION: Demonstrates how to retrieve the complete `ParsedChatCompletion` object after a chat completion stream has finished using the `get_final_completion()` helper method. This is useful for accessing the full response once all chunks have been received.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_3

LANGUAGE: python
CODE:
```
async with client.chat.completions.stream(...) as stream:
    ...

completion = await stream.get_final_completion()
print(completion.choices[0].message)
```

--------------------------------

TITLE: Handle OpenAI API Errors in Python
DESCRIPTION: This example illustrates how to catch and handle different types of errors that can occur when interacting with the OpenAI API, including `APIConnectionError` for network issues, `RateLimitError` for 429 responses, and `APIStatusError` for other non-success HTTP status codes. It shows how to access error details like status code and response.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_22

LANGUAGE: python
CODE:
```
import openai
from openai import OpenAI

client = OpenAI()

try:
    client.fine_tuning.jobs.create(
        model="gpt-4o",
        training_file="file-abc123",
    )
except openai.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except openai.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except openai.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

--------------------------------

TITLE: Perform Vision Task with OpenAI Responses API (Base64 Image, Python)
DESCRIPTION: This Python example demonstrates how to use the OpenAI Responses API for vision tasks by encoding an image as a base64 string. It shows reading an image file, encoding it, and then including the base64 string in the API request for a vision-capable model.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_4

LANGUAGE: python
CODE:
```
import base64
from openai import OpenAI

client = OpenAI()

prompt = "What is in this image?"
with open("path/to/image.png", "rb") as image_file:
    b64_image = base64.b64encode(image_file.read()).decode("utf-8")

response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": prompt},
                {"type": "input_image", "image_url": f"data:image/png;base64,{b64_image}"},
            ],
        }
    ],
)
```

--------------------------------

TITLE: Get Vector Store File Content using OpenAI Python Client
DESCRIPTION: This method retrieves the content of a specific file from a vector store. It requires the `file_id` and `vector_store_id`. It returns a `SyncPage` containing `FileContentResponse` objects, representing the file's content.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_63

LANGUAGE: python
CODE:
```
client.vector_stores.files.content(file_id, *, vector_store_id) -> SyncPage[FileContentResponse]
```

--------------------------------

TITLE: List Container Files in OpenAI Python Client
DESCRIPTION: Lists files within a specified container using the OpenAI Python client. This method sends a GET request to the `/containers/{container_id}/files` endpoint, allowing pagination and filtering. It returns a `SyncCursorPage[FileListResponse]` object.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_156

LANGUAGE: python
CODE:
```
client.containers.files.list(container_id, **params) -> SyncCursorPage[FileListResponse]
```

--------------------------------

TITLE: Access OpenAI API Request ID from Failed Response in Python
DESCRIPTION: This example demonstrates how to access the `request_id` property from an `openai.APIStatusError` exception when an API call fails. This is crucial for debugging and reporting issues related to unsuccessful API requests.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_24

LANGUAGE: python
CODE:
```
import openai

try:
    completion = await client.chat.completions.create(
        messages=[{"role": "user", "content": "Say this is a test"}], model="gpt-4"
    )
except openai.APIStatusError as exc:
    print(exc.request_id)  # req_123
    raise exc
```

--------------------------------

TITLE: Set OpenAI API Request Timeouts in Python
DESCRIPTION: This example demonstrates how to configure the timeout duration for OpenAI API requests. It shows how to set a default timeout for the entire client or specify a custom timeout for individual requests, accepting either a float for seconds or an `httpx.Timeout` object for fine-grained control.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_26

LANGUAGE: python
CODE:
```
from openai import OpenAI

# Configure the default for all requests:
client = OpenAI(
    # 20 seconds (default is 10 minutes)
    timeout=20.0,
)
```

--------------------------------

TITLE: Retrieve a Container in OpenAI Python Client
DESCRIPTION: Retrieves a specific container by its ID using the OpenAI Python client. This method performs a GET request to the `/containers/{container_id}` endpoint. It returns a `ContainerRetrieveResponse` object containing the container's details.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_150

LANGUAGE: python
CODE:
```
client.containers.retrieve(container_id) -> ContainerRetrieveResponse
```

--------------------------------

TITLE: List Eval Runs in OpenAI Python Client
DESCRIPTION: Lists evaluation runs for a given evaluation ID using the OpenAI Python client. This method sends a GET request to the `/evals/{eval_id}/runs` endpoint, allowing pagination and filtering through optional parameters. It returns a `SyncCursorPage[RunListResponse]` object.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_142

LANGUAGE: python
CODE:
```
client.evals.runs.list(eval_id, **params) -> SyncCursorPage[RunListResponse]
```

--------------------------------

TITLE: List Eval Run Output Items in OpenAI Python Client
DESCRIPTION: Lists output items for a specific evaluation run by its run ID and evaluation ID using the OpenAI Python client. This method sends a GET request to the `/evals/{eval_id}/runs/{run_id}/output_items` endpoint, allowing pagination and filtering. It returns a `SyncCursorPage[OutputItemListResponse]` object.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_147

LANGUAGE: python
CODE:
```
client.evals.runs.output_items.list(run_id, *, eval_id, **params) -> SyncCursorPage[OutputItemListResponse]
```

--------------------------------

TITLE: Retrieve a Container File in OpenAI Python Client
DESCRIPTION: Retrieves a specific file by its ID and associated container ID using the OpenAI Python client. This method performs a GET request to the `/containers/{container_id}/files/{file_id}` endpoint. It returns a `FileRetrieveResponse` object containing the file's details.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_155

LANGUAGE: python
CODE:
```
client.containers.files.retrieve(file_id, *, container_id) -> FileRetrieveResponse
```

--------------------------------

TITLE: Initialize Async OpenAI Client and Create Chat Completion
DESCRIPTION: Demonstrates how to set up the `AsyncOpenAI` client using `DefaultAioHttpClient` for asynchronous operations. It then shows a basic chat completion request to the `gpt-4o` model, awaiting the response.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_8

LANGUAGE: Python
CODE:
```
import asyncio
from openai import DefaultAioHttpClient
from openai import AsyncOpenAI


async def main() -> None:
    async with AsyncOpenAI(
        api_key="My API Key",
        http_client=DefaultAioHttpClient(),
    ) as client:
        chat_completion = await client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Say this is a test",
                }
            ],
            model="gpt-4o",
        )


asyncio.run(main())
```

--------------------------------

TITLE: Retrieve an Eval Run Output Item in OpenAI Python Client
DESCRIPTION: Retrieves a specific output item by its ID, associated run ID, and evaluation ID using the OpenAI Python client. This method performs a GET request to the `/evals/{eval_id}/runs/{run_id}/output_items/{output_item_id}` endpoint. It returns an `OutputItemRetrieveResponse` object.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_146

LANGUAGE: python
CODE:
```
client.evals.runs.output_items.retrieve(output_item_id, *, eval_id, run_id) -> OutputItemRetrieveResponse
```

--------------------------------

TITLE: Retrieve an Eval Run in OpenAI Python Client
DESCRIPTION: Retrieves a specific evaluation run by its run ID and associated evaluation ID using the OpenAI Python client. This method performs a GET request to the `/evals/{eval_id}/runs/{run_id}` endpoint. It returns a `RunRetrieveResponse` object containing the run's details.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_141

LANGUAGE: python
CODE:
```
client.evals.runs.retrieve(run_id, *, eval_id) -> RunRetrieveResponse
```

--------------------------------

TITLE: Create OpenAI Beta Realtime Sessions in Python
DESCRIPTION: This section describes the Python client method for creating new sessions within OpenAI's Beta Realtime API. The `create` method allows applications to initiate a real-time interaction session, returning a `SessionCreateResponse` object upon successful creation.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_79

LANGUAGE: python
CODE:
```
client.beta.realtime.sessions.create(**params) -> SessionCreateResponse
```

--------------------------------

TITLE: Customize HTTP Client per Request in OpenAI Python
DESCRIPTION: Shows how to apply HTTP client customizations on a per-request basis using the `with_options()` method. This is useful for dynamic network configurations without reinitializing the main client.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_34

LANGUAGE: python
CODE:
```
client.with_options(http_client=DefaultHttpxClient(...))
```

--------------------------------

TITLE: Create OpenAI Beta Realtime Transcription Sessions in Python
DESCRIPTION: This section describes the Python client method for creating new transcription sessions within OpenAI's Beta Realtime API. The `create` method allows applications to initiate a real-time audio transcription session, returning a `TranscriptionSession` object upon successful creation.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_81

LANGUAGE: python
CODE:
```
client.beta.realtime.transcription_sessions.create(**params) -> TranscriptionSession
```

--------------------------------

TITLE: Configure HTTP Client for OpenAI Python Library
DESCRIPTION: Demonstrates how to customize the `httpx` client used by the OpenAI Python library, including setting a base URL, proxy, and transport options. This allows for advanced network configurations like proxy support and custom local addresses.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_33

LANGUAGE: python
CODE:
```
import httpx
from openai import OpenAI, DefaultHttpxClient

client = OpenAI(
    # Or use the `OPENAI_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083/v1",
    http_client=DefaultHttpxClient(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

--------------------------------

TITLE: List all Run Steps for a Run in OpenAI Python SDK
DESCRIPTION: This method retrieves a paginated list of all run steps associated with a specific run and thread. It supports various parameters for filtering and pagination, allowing developers to traverse the sequence of actions taken by the Assistant during a run. The method returns a `SyncCursorPage` containing `RunStep` objects.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_101

LANGUAGE: python
CODE:
```
client.beta.threads.runs.steps.list(run_id, *, thread_id, **params) -> SyncCursorPage[RunStep]
```

--------------------------------

TITLE: Create Vector Store File Batch using OpenAI Python Client
DESCRIPTION: This method initiates the creation of a batch of files within a specified vector store. It requires the `vector_store_id` and parameters for the batch creation. It returns a `VectorStoreFileBatch` object.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_68

LANGUAGE: python
CODE:
```
client.vector_stores.file_batches.create(vector_store_id, **params) -> VectorStoreFileBatch
```

--------------------------------

TITLE: Create a Fine-Tuning Job
DESCRIPTION: Initiates a new fine-tuning job with specified parameters. This method corresponds to the `POST /fine_tuning/jobs` API endpoint and returns the newly created job object.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_40

LANGUAGE: python
CODE:
```
client.fine_tuning.jobs.create(**params)
```

--------------------------------

TITLE: Submit Tool Outputs and Stream OpenAI Assistant Run (Python)
DESCRIPTION: Details the method for submitting tool outputs to an OpenAI Assistant run that is currently waiting for them, and then continuing to stream the run's response. This is crucial for interactive tool use scenarios.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_10

LANGUAGE: python
CODE:
```
client.beta.threads.runs.submit_tool_outputs_stream()
```

--------------------------------

TITLE: Interact with OpenAI Assistants API using Python Client Methods
DESCRIPTION: This section lists the core methods available in the `client.beta.assistants` module for managing Assistants. It includes operations for creating new assistants, retrieving existing ones by ID, updating their properties, listing all assistants, and deleting an assistant. Each method corresponds to a specific REST API endpoint, providing a programmatic interface.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_83

LANGUAGE: python
CODE:
```
client.beta.assistants.create(**params) -> Assistant
```

LANGUAGE: python
CODE:
```
client.beta.assistants.retrieve(assistant_id) -> Assistant
```

LANGUAGE: python
CODE:
```
client.beta.assistants.update(assistant_id, **params) -> Assistant
```

LANGUAGE: python
CODE:
```
client.beta.assistants.list(**params) -> SyncCursorPage[Assistant]
```

LANGUAGE: python
CODE:
```
client.beta.assistants.delete(assistant_id) -> AssistantDeleted
```

--------------------------------

TITLE: Import OpenAI Fine-Tuning Configuration Types
DESCRIPTION: Imports various hyperparameter and method types related to fine-tuning configurations, such as DPO, Reinforcement, and Supervised learning parameters, from the OpenAI Python client.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_38

LANGUAGE: python
CODE:
```
from openai.types.fine_tuning import (
    DpoHyperparameters,
    DpoMethod,
    ReinforcementHyperparameters,
    ReinforcementMethod,
    SupervisedHyperparameters,
    SupervisedMethod,
)
```

--------------------------------

TITLE: Integrate Azure OpenAI with Python Library
DESCRIPTION: Explains how to use the `AzureOpenAI` class to interact with Azure OpenAI services. It demonstrates setting the API version and Azure endpoint, and making a chat completion request, highlighting the differences from the standard OpenAI API.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_36

LANGUAGE: python
CODE:
```
from openai import AzureOpenAI

# gets the API Key from environment variable AZURE_OPENAI_API_KEY
client = AzureOpenAI(
    # https://learn.microsoft.com/azure/ai-services/openai/reference#rest-api-versioning
    api_version="2023-07-01-preview",
    # https://learn.microsoft.com/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal#create-a-resource
    azure_endpoint="https://example-endpoint.openai.azure.com",
)

completion = client.chat.completions.create(
    model="deployment-name",  # e.g. gpt-35-instant
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
)
print(completion.to_json())
```

--------------------------------

TITLE: Import OpenAI Audio Types
DESCRIPTION: Imports core type definitions for OpenAI's audio APIs, including AudioModel and AudioResponseFormat.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_25

LANGUAGE: python
CODE:
```
from openai.types import AudioModel, AudioResponseFormat
```

--------------------------------

TITLE: Create OpenAI Batch (Python)
DESCRIPTION: Initiates a new batch operation using the OpenAI Python client. This allows processing multiple API requests asynchronously.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_109

LANGUAGE: python
CODE:
```
client.batches.create(**params) -> Batch
```

--------------------------------

TITLE: Handle Assistant ToolCall lifecycle events (Python)
DESCRIPTION: These methods allow subscribing to events for the creation, incremental updates (delta), and completion of ToolCalls. They are essential for tracking the execution and status of tool invocations within an assistant's run.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_16

LANGUAGE: python
CODE:
```
def on_tool_call_created(self, tool_call: ToolCall)
def on_tool_call_delta(self, delta: ToolCallDelta, snapshot: ToolCall)
def on_tool_call_done(self, tool_call: ToolCall)
```

--------------------------------

TITLE: Handle Assistant RunStep lifecycle events (Python)
DESCRIPTION: These methods enable subscription to events related to the creation, incremental updates (delta), and completion of a RunStep within the Assistant API. They are useful for tracking the detailed progress and state changes of an assistant's execution run.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_12

LANGUAGE: python
CODE:
```
def on_run_step_created(self, run_step: RunStep)
def on_run_step_delta(self, delta: RunStepDelta, snapshot: RunStep)
def on_run_step_done(self, run_step: RunStep)
```

--------------------------------

TITLE: Enable OpenAI client logging via environment variable
DESCRIPTION: This section explains how to enable logging for the OpenAI Python client using the standard `logging` module. Logging can be activated by setting the `OPENAI_LOG` environment variable to `info` for general information or `debug` for more verbose output.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_28

LANGUAGE: shell
CODE:
```
$ export OPENAI_LOG=info
```

--------------------------------

TITLE: Subscribe to all raw Assistant API streaming events (Python)
DESCRIPTION: This method allows subscribing to all possible raw events sent by the OpenAI streaming API. It provides a general-purpose event handler for comprehensive event processing, offering flexibility for various use cases.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_11

LANGUAGE: python
CODE:
```
def on_event(self, event: AssistantStreamEvent)
```

--------------------------------

TITLE: Stream Chat Completions with AsyncOpenAI in Python
DESCRIPTION: This code snippet demonstrates how to use the `AsyncOpenAI` client's `chat.completions.stream()` method to receive chat completion deltas asynchronously. It showcases the required usage within an `async with` context manager for proper resource handling and iterates through the stream's events, specifically printing `content.delta` events as they are received.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_2

LANGUAGE: python
CODE:
```
from openai import AsyncOpenAI

client = AsyncOpenAI()

async with client.chat.completions.stream(
    model='gpt-4o-2024-08-06',
    messages=[...],
) as stream:
    async for event in stream:
        if event.type == 'content.delta':
            print(event.content, flush=True, end='')
```

--------------------------------

TITLE: Create and Poll Vector Store File Batch in Python
DESCRIPTION: This method creates a batch of vector store files and then polls its status until it's ready. It simplifies the process of adding multiple files and ensuring their availability. It returns a `VectorStoreFileBatch` object.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_72

LANGUAGE: python
CODE:
```
client.vector_stores.file_batches.create_and_poll(*args) -> VectorStoreFileBatch
```

--------------------------------

TITLE: Create OpenAI Upload (Python)
DESCRIPTION: Initiates a new file upload operation using the OpenAI Python client. This prepares for uploading large files to the API.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_114

LANGUAGE: python
CODE:
```
client.uploads.create(**params) -> Upload
```

--------------------------------

TITLE: Manage Fine-Tuning Checkpoint Permissions with OpenAI Python Client
DESCRIPTION: These methods provide functionality to interact with permissions for fine-tuned model checkpoints. They allow creating new permissions, retrieving existing ones, and deleting specific permissions using the OpenAI Python client.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_50

LANGUAGE: python
CODE:
```
client.fine_tuning.checkpoints.permissions.create(fine_tuned_model_checkpoint, **params) -> SyncPage[PermissionCreateResponse]
```

LANGUAGE: python
CODE:
```
client.fine_tuning.checkpoints.permissions.retrieve(fine_tuned_model_checkpoint, **params) -> PermissionRetrieveResponse
```

LANGUAGE: python
CODE:
```
client.fine_tuning.checkpoints.permissions.delete(permission_id, *, fine_tuned_model_checkpoint) -> PermissionDeleteResponse
```

--------------------------------

TITLE: Handle Assistant Message lifecycle events (Python)
DESCRIPTION: These methods allow subscribing to events for the creation, incremental updates (delta), and completion of messages. The delta event conveniently includes both the incremental update and an accumulated snapshot of the content, simplifying message reconstruction.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_13

LANGUAGE: python
CODE:
```
def on_message_created(self, message: Message)
def on_message_delta(self, delta: MessageDelta, snapshot: Message)
def on_message_done(self, message: Message)
```

--------------------------------

TITLE: Create Vector Store File using OpenAI Python Client
DESCRIPTION: This method allows you to create a new file within a specified vector store. It requires the `vector_store_id` and additional parameters for file creation. The method returns a `VectorStoreFile` object upon successful creation.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_58

LANGUAGE: python
CODE:
```
client.vector_stores.files.create(vector_store_id, **params) -> VectorStoreFile
```

--------------------------------

TITLE: Create a new Evaluation in Python
DESCRIPTION: This method allows you to create a new evaluation resource using the OpenAI API. It typically accepts parameters to define the evaluation's configuration, including data sources and metrics. It returns an `EvalCreateResponse` object upon successful creation, providing details about the newly initiated evaluation.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_134

LANGUAGE: python
CODE:
```
client.evals.create(**params) -> EvalCreateResponse
```

--------------------------------

TITLE: Create OpenAI Python Completion
DESCRIPTION: Creates a text completion using the OpenAI API. This method sends parameters to the `/completions` endpoint and returns a `Completion` object, which contains the generated text and other relevant information.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_2

LANGUAGE: python
CODE:
```
client.completions.create(**params) -> Completion
```

--------------------------------

TITLE: Create a Container in OpenAI Python Client
DESCRIPTION: Creates a new container using the OpenAI Python client. This method sends a POST request to the `/containers` endpoint, accepting various parameters to define the container. It returns a `ContainerCreateResponse` object upon successful creation.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_149

LANGUAGE: python
CODE:
```
client.containers.create(**params) -> ContainerCreateResponse
```

--------------------------------

TITLE: Create and Poll Vector Store File in Python
DESCRIPTION: This method creates a vector store file and then polls its status until it's ready. It simplifies the process of uploading and ensuring file availability. It returns a `VectorStoreFile` object.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_64

LANGUAGE: python
CODE:
```
client.vector_stores.files.create_and_poll(*args) -> VectorStoreFile
```

--------------------------------

TITLE: Upload Vector Store File using OpenAI Python Client
DESCRIPTION: This method uploads a file to a vector store. It handles the underlying API call for file submission. It returns a `VectorStoreFile` object representing the uploaded file.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_66

LANGUAGE: python
CODE:
```
client.vector_stores.files.upload(*args) -> VectorStoreFile
```

--------------------------------

TITLE: Synchronous Automatic Pagination with OpenAI Python Client
DESCRIPTION: This snippet demonstrates how to automatically iterate through paginated results from the OpenAI API using the synchronous client. It fetches fine-tuning jobs, appending each job to a list until all pages are retrieved. This simplifies handling large datasets without manual page management.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_14

LANGUAGE: python
CODE:
```
for job in client.fine_tuning.jobs.list(
    limit=20,
):
    # Do something with job here
    all_jobs.append(job)
print(all_jobs)
```

--------------------------------

TITLE: Handle Assistant Image File completion event (Python)
DESCRIPTION: This method provides an event handler for when an image file is fully available. Since image files are not sent incrementally, this event signifies their complete reception and readiness for use.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_15

LANGUAGE: python
CODE:
```
def on_image_file_done(self, image_file: ImageFile)
```

--------------------------------

TITLE: Create and Stream a Run in OpenAI Python SDK
DESCRIPTION: This method creates a new run and immediately begins streaming events related to its progress. It's particularly useful for building real-time user interfaces or applications that need immediate updates on the run's status, messages, and tool calls. It returns an `AssistantStreamManager` for handling the event stream.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_94

LANGUAGE: python
CODE:
```
client.beta.threads.runs.create_and_stream(*args) -> AssistantStreamManager[AssistantEventHandler] | AssistantStreamManager[AssistantEventHandlerT]
```

--------------------------------

TITLE: Submit Tool Outputs and Stream Run in OpenAI Python SDK
DESCRIPTION: This method submits tool outputs for a run and then streams events related to its subsequent progress. It combines the action of providing tool results with real-time updates on how the run proceeds. It returns an `AssistantStreamManager` for handling the event stream.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_98

LANGUAGE: python
CODE:
```
client.beta.threads.runs.submit_tool_outputs_stream(*args) -> AssistantStreamManager[AssistantEventHandler] | AssistantStreamManager[AssistantEventHandlerT]
```

--------------------------------

TITLE: Import Fine-Tuning Checkpoint Permission Types in Python
DESCRIPTION: This snippet imports various response types related to permissions for fine-tuning model checkpoints, including creation, retrieval, and deletion responses, from the `openai.types.fine_tuning.checkpoints` module.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_49

LANGUAGE: python
CODE:
```
from openai.types.fine_tuning.checkpoints import (
    PermissionCreateResponse,
    PermissionRetrieveResponse,
    PermissionDeleteResponse,
)
```

--------------------------------

TITLE: OpenAI Files API: List Files
DESCRIPTION: Lists all files associated with the account, optionally filtered by parameters. Returns a paginated list of FileObject instances.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_16

LANGUAGE: python
CODE:
```
client.files.list(**params)
```

--------------------------------

TITLE: List Vector Store Files using OpenAI Python Client
DESCRIPTION: This method retrieves a paginated list of files associated with a given vector store. It takes the `vector_store_id` and optional parameters for filtering or pagination. It returns a `SyncCursorPage` containing `VectorStoreFile` objects.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_61

LANGUAGE: python
CODE:
```
client.vector_stores.files.list(vector_store_id, **params) -> SyncCursorPage[VectorStoreFile]
```