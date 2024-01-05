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

from typing import TypeVar, Generic, Optional, Union, Type

T = TypeVar('T')
E = TypeVar('E', bound=BaseException)


class Ok(Generic[T]):

    def __init__(self, value: T):
        self.value = value


class Err(Generic[E]):

    def __init__(self, error: E):
        self.error = error


class Result(Generic[T, E]):

    def __init__(self,
                 result_type: Union[Type[Ok[T]], Type[Err[E]]],
                 value: Optional[T] = None,
                 error: Optional[E] = None):
        self.result_type = result_type
        if result_type == Ok:
            self.value = Ok(value)
        else:
            self.error = Err(error)

    def __str__(self):
        if self.result_type == Ok:
            return f"Ok({self.value.value})"
        else:
            return f"Err({self.error.error})"

    def is_Ok(self) -> bool:
        return self.result_type == Ok

    def is_err(self) -> bool:
        return self.result_type == Err

    def Ok(self) -> Optional[Ok[T]]:
        if self.result_type == Ok:
            return self.value
        else:
            return None

    def err(self) -> Optional[Err[E]]:
        if self.result_type == Err:
            return self.error
        else:
            return None

    def unwrap(self) -> T:
        if self.result_type == Ok:
            return self.value.value
        else:
            raise ValueError(f"Result is Error: {self.error.error}")

    def unwrap_err(self) -> E:
        if self.result_type == Err:
            return self.error.error
        else:
            raise ValueError(f"Result is Ok: {self.value.value}")
