from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, Type

from jsonlogic._compat import Self, TypedDict
from jsonlogic.json_schema.types import DatetimeType, DateType, JSONSchemaType
from jsonlogic.resolving import PointerReferenceParser, ReferenceParser

from .diagnostics import DiagnosticType


def _d_variable_casts() -> Dict[str, Type[JSONSchemaType]]:
    return {
        "date": DateType,
        "date-time": DatetimeType,
    }


@dataclass
class DiagnosticsConfig:
    general: DiagnosticType | None = "error"
    """A general diagnostic.

    Default: :python:`"error"`.
    """

    argument_type: DiagnosticType | None = "error"
    """An argument has the wrong type.

    Default: :python:`"error"`.
    """

    operator: DiagnosticType | None = "error"
    """Operator not supported for type(s).

    Default: :python:`"error"`.
    """

    unresolvable_variable: DiagnosticType | None = "error"
    """Variable in unresolvable.

    Default: :python:`"error"`.
    """


@dataclass
class TypecheckSettings:
    """Settings used when typechecking an :class:`~jsonlogic.core.Operator`."""

    # fail_fast: bool
    # """Whether to stop typechecking on the first error.

    # Default: ``False``.
    # """

    reference_parser: ReferenceParser = field(default_factory=PointerReferenceParser)
    """A reference parser instance to use when resolving variables.

    Default: :class:`~jsonlogic.resolving.PointerReferenceParser`.
    """

    variable_casts: Dict[str, Type[JSONSchemaType]] = field(default_factory=_d_variable_casts)
    """A mapping between `JSON Schema formats`_ and their corresponding
    :class:`~jsonlogic.json_schema.types.JSONSchemaType`.

    When an operator makes use of the provided data JSON Schema to read variables
    (such as the ``"var"`` operator), such variables with a type of `"string"`
    might have a format provided. To allow for features specific to these formats,
    such strings can be inferred as a specific JSON :class:`~jsonlogic.json_schema.types.JSONSchemaType`.

    This setting is analogous to the :attr:`~jsonlogic.evaluation.EvaluationSettings.variable_casts`
    configuration of the :class:`~jsonlogic.evaluation.EvaluationSettings` class.

    Default: :python:`{"date": DateType, "date-time": DatetimeType}`.

    .. _JSON Schema formats: https://json-schema.org/understanding-json-schema/reference/string#built-in-formats
    """

    literal_casts: Dict[Callable[[str], Any], Type[JSONSchemaType]] = field(default_factory=dict)
    """A mapping between conversion callables and their corresponding
    :class:`~jsonlogic.json_schema.types.JSONSchemaType`.

    When a literal string value is encountered in a JSON Logic expression, it might be
    beneficial to infer the :class:`~jsonlogic.json_schema.types.JSONSchemaType` from
    the format of the string. The callable must take a single string argument and raise
    any exception if the format is invalid.

    This setting is analogous to the :attr:`~jsonlogic.evaluation.EvaluationSettings.literal_casts`
    configuration of the :class:`~jsonlogic.evaluation.EvaluationSettings` class.

    Default: :python:`{}` (no cast).

    .. warning::

        The order in which the conversion callables are defined matters. Each
        callable will be applied one after the other until no exception is raised.
    """

    diagnostics: DiagnosticsConfig = field(default_factory=DiagnosticsConfig)
    """Configuration of type for diagnostics.

    This is a mapping between the emitted diagnostic categories and the
    corresponding type (e.g. :python:`"error"` or  :python:`"warning"`).

    Default: see :class:`DiagnosticsConfig`.
    """

    @classmethod
    def from_dict(cls, dct: TypecheckSettingsDict) -> Self:
        init_dct: Dict[str, Any] = {}
        if (reference_parser := dct.get("reference_parser")) is not None:
            init_dct["reference_parser"] = reference_parser

        if (variable_casts := dct.get("variable_casts")) is not None:
            init_dct["variable_casts"] = variable_casts

        if (literal_casts := dct.get("literal_casts")) is not None:
            init_dct["literal_casts"] = literal_casts

        diagnostics_dct = dct.get("diagnostics", {})
        init_dct["diagnostics"] = DiagnosticsConfig(**diagnostics_dct)

        return cls(**init_dct)


class DiagnosticsConfigDict(TypedDict, total=False):
    general: DiagnosticType | None
    """A general diagnostic.

    Default: :python:`"error"`.
    """

    argument_type: DiagnosticType | None
    """An argument has the wrong type.

    Default: :python:`"error"`.
    """

    operator: DiagnosticType | None
    """Operator not supported for type(s).

    Default: :python:`"error"`.
    """

    unresolvable_variable: DiagnosticType | None
    """Variable in unresolvable.

    Default: :python:`"error"`.
    """


class TypecheckSettingsDict(TypedDict, total=False):
    """Settings used when typechecking an :class:`~jsonlogic.core.Operator`."""

    # fail_fast: bool
    # """Whether to stop typechecking on the first error.

    # Default: ``False``.
    # """

    reference_parser: ReferenceParser
    """A reference parser instance to use when resolving variables.

    Default: :class:`~jsonlogic.resolving.PointerReferenceParser`.
    """

    variable_casts: Dict[str, Type[JSONSchemaType]]
    """A mapping between `JSON Schema formats`_ and their corresponding
    :class:`~jsonlogic.json_schema.types.JSONSchemaType`.

    When an operator makes use of the provided data JSON Schema to read variables
    (such as the ``"var"`` operator), such variables with a type of `"string"`
    might have a format provided. To allow for features specific to these formats,
    such strings can be inferred as a specific JSON :class:`~jsonlogic.json_schema.types.JSONSchemaType`.

    This setting is analogous to the :attr:`~jsonlogic.evaluation.EvaluationSettings.variable_casts`
    configuration of the :class:`~jsonlogic.evaluation.EvaluationSettings` class.

    Default: :python:`{"date": DateType, "date-time": DatetimeType}`.

    .. _JSON Schema formats: https://json-schema.org/understanding-json-schema/reference/string#built-in-formats
    """

    literal_casts: Dict[Callable[[str], Any], Type[JSONSchemaType]]
    """A mapping between conversion callables and their corresponding
    :class:`~jsonlogic.json_schema.types.JSONSchemaType`.

    When a literal string value is encountered in a JSON Logic expression, it might be
    beneficial to infer the :class:`~jsonlogic.json_schema.types.JSONSchemaType` from
    the format of the string. The callable must take a single string argument and raise
    any exception if the format is invalid.

    This setting is analogous to the :attr:`~jsonlogic.evaluation.EvaluationSettings.literal_casts`
    configuration of the :class:`~jsonlogic.evaluation.EvaluationSettings` class.

    Default: :python:`{}` (no cast).

    .. warning::

        The order in which the conversion callables are defined matters. Each
        callable will be applied one after the other until no exception is raised.
    """

    diagnostics: DiagnosticsConfigDict
    """Configuration of type for diagnostics.

    This is a mapping between the emitted diagnostic categories and the
    corresponding type (e.g. :python:`"error"` or  :python:`"warning"`).

    Default: see :class:`DiagnosticsConfigDict`.
    """
