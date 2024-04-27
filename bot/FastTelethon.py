import asyncio
import hashlib
import logging
import math
import os
from collections import defaultdict
from typing import (
    AsyncGenerator,
    Awaitable,
    BinaryIO,
    DefaultDict,
    List,
    Optional,
    Tuple,
    Union,
)

from telethon import TelegramClient, helpers, utils
from telethon.crypto import AuthKey
from telethon.network import MTProtoSender
from telethon.tl.alltlobjects import LAYER
from telethon.tl.functions import InvokeWithLayerRequest
from telethon.tl.functions.auth import (
    ExportAuthorizationRequest,
    ImportAuthorizationRequest,
)
from telethon.tl.functions.upload import (
    GetFileRequest,
    SaveBigFilePartRequest,
    SaveFilePartRequest,
)
from telethon.tl.types import (
    Document,
    InputDocumentFileLocation,
    InputFile,
    InputFileBig,
    InputFileLocation,
    InputPeerPhotoFileLocation,
    InputPhotoFileLocation,
    TypeInputFile,
)

filename = ""

log: logging.Logger = logging.getLogger("FastTelethon")

TypeLocation = Union[
    Document,
    InputDocumentFileLocation,
    InputPeerPhotoFileLocation,
    InputFileLocation,
    InputPhotoFileLocation,
]

class DownloadSender:
    # Class definition goes here...

class UploadSender:
    # Class definition goes here...

class ParallelTransferrer:
    # Class definition goes here...

parallel_transfer_locks: DefaultDict[int, asyncio.Lock] = defaultdict(
    lambda: asyncio.Lock()
)

def stream_file(file_to_stream: BinaryIO, chunk_size=1024):
    # Function definition goes here...

async def _internal_transfer_to_telegram(
    client: TelegramClient, response: BinaryIO, progress_callback: callable
) -> Tuple[TypeInputFile, int]:
    # Function definition goes here...

async def download_file(
    client: TelegramClient,
    location: TypeLocation,
    out: BinaryIO,
    progress_callback: callable = None,
) -> BinaryIO:
    # Function definition goes here...

async def upload_file(
    client: TelegramClient,
    file: BinaryIO,
    name,
    progress_callback: callable = None,
) -> TypeInputFile:
    # Function definition goes here...
