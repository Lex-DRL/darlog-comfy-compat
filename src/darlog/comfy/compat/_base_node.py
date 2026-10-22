# encoding: utf-8
"""
"""

import typing as _t
from typing import TypeVar as _TypeVar

from comfy_api.latest import io as _io


# noinspection PyAbstractClass
class CachedSchemaNodeABC(_io.ComfyNode):
	"""Shared base class for all the nodes in pack.
	Stores schema in internal class attribute.
	"""
	_schema: _io.Schema = None

	@classmethod
	def define_schema(cls) -> _io.Schema:
		return cls._schema


T_CachedSchemaNode = _TypeVar('T_CachedSchemaNode', bound=CachedSchemaNodeABC)
