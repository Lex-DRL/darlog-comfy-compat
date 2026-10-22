# encoding: utf-8
"""
"""

import typing as _t

from .__typing import (
	_A, _C,
	T as _T, DictMap as _DictMap
)

# noinspection PyShadowingBuiltins
def _validate_type_factory(
	_type: _t.Type[_T], type_name: str = None, what: str = 'Value', a='a'
) -> _C[[_A], _T]:
	"""Build a function to type-check an input against a specific type."""
	if not what:
		what = 'Value'
	what = str(what)
	what = what[0].upper() + what[1:]  # Make the first letter uppercase

	if not a:
		a = 'a'
	a = str(a)

	if not type_name:
		type_name = _type.__name__
	type_name = str(type_name)

	error_template = f"{what} isn't {a} <{type_name}> instance: {{}}"

	def validate_type(value: _A) -> _T:
		"""Type-check an input."""
		if not isinstance(value, _type):
			raise TypeError(error_template.format(repr(value)))
		return value

	return validate_type


_validate_str = _validate_type_factory(str, type_name='string')
_validate_int = _validate_type_factory(int, type_name='int', a='an')
_validate_float = _validate_type_factory(float, type_name='float')


def _validate_dict(value: _A) -> _DictMap:
	if value is None:
		raise ValueError("No Dict provided.")
	if not isinstance(value, (_t.Dict, _t.Mapping)):
		raise TypeError(f"Not a Dict: {value!r}")
	if not value:
		raise ValueError("Dict is empty.")
	return value


def _validate_str_key(key: _A, strip: bool = False) -> str:
	if key is None:
		raise ValueError("No key provided.")
	key = str(key)

	if not strip:
		return key

	key_raw = key
	key = ''
	for line in key_raw.split():
		line = line.strip()  # just in case \r is left
		if line:
			key = line
			break
	return key
