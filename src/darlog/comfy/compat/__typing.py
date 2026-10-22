# encoding: utf-8
"""Type hints."""

import typing as _t
from typing import (
	Any as _A, Callable as _C, Optional as _O, Union as _U,
	TypeVar as _TypeVar
)

from comfy_api.latest import io as _io

T = _TypeVar('T')
T2 = _TypeVar('T2')
KT = _TypeVar('KT')
VT = _TypeVar('VT')

DictMap = _TypeVar('DictMap', bound=_U[_t.Dict, _t.Mapping])
T_ComfyNode = _TypeVar('T_ComfyNode', bound=_io.ComfyNode)
T_Input = _t.TypeVar('T_Input', bound=_io.Input)
T_Output = _t.TypeVar('T_Output', bound=_io.Output)
