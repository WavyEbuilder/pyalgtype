"""
GPL-3.0 License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from typing import TypeVar, Generic, Optional
from .result import Err, Ok, Result

T = TypeVar('T')


class Some(Generic[T]):

    def __init__(self, value: T):
        self.value = value

    def __str__(self):
        return f"Some({self.value})"


class Option(Generic[T]):

    def __init__(self, value: Optional[Some[T]] = None):
        self.value = value

    def __str__(self):
        if self.value is not None:
            return str(self.value)
        else:
            return "None"

    def is_some(self) -> bool:
        return self.value is not None

    def is_none(self) -> bool:
        return self.value is None

    def unwrap(self) -> T:
        if self.value is not None:
            return self.value.value
        else:
            raise ValueError("Tried to unwrap a `None` value")

    def map(self, func) -> 'Option':
        if self.value is not None:
            return Option(Some(func(self.value.value)))
        else:
            return Option()

    def and_then(self, func) -> 'Option':
        if self.value is not None:
            return func(self.value.value)
        else:
            return Option()

    def or_else(self, func) -> 'Option':
        if self.value is not None:
            return Option(self.value)
        else:
            return func()

    def ok_or(self, err) -> Result:
        if self.value is not None:
            return Result(Ok(self.value.value))
        else:
            return Result(Err, error=err)
