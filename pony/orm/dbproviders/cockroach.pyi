from pony.orm import core, dbapiprovider, ormtypes
from pony.orm.core import log_orm
from pony.orm.dbapiprovider import wrap_dbapi_exceptions
from pony.orm.dbproviders.postgres import (
    PGArrayConverter,
    PGBlobConverter,
    PGColumn,
    PGDatetimeConverter,
    PGIntConverter,
    PGJsonConverter,
    PGProvider,
    PGRealConverter,
    PGSQLBuilder,
    PGSchema,
    PGStrConverter,
    PGTimedeltaConverter,
    PGTranslator
)
from pony.py23compat import PY2, basestring, buffer, int_types, unicode
from typing import Any, Dict, List, Optional, Tuple, Union

NoneType: Any

class CRColumn(PGColumn):
    auto_template: str = ...

class CRSchema(PGSchema):
    column_class: CRColumn = ...

class CRTranslator(PGTranslator): ...
class CRSQLBuilder(PGSQLBuilder): ...

class CRIntConverter(PGIntConverter):
    signed_types: Any = ...  # TODO: Should be Dict[Optional[int], str]

    unsigned_types: Any = ...  # TODO: Should be Dict[Optional[int], str]

class CRBlobConverter(PGBlobConverter):
    def sql_type(converter: Any) -> str: ...

class CRTimedeltaConverter(PGTimedeltaConverter):
    sql_type_name: str = ...

class PGUuidConverter(dbapiprovider.UuidConverter):
    def py2sql(converter: Any, val: Any) -> Any: ...

class CRArrayConverter(PGArrayConverter):
    array_types: List[Any, Tuple[str, Any]] = ...

class CRProvider(PGProvider):
    dbapi_module: Any = ...
    dbschema_cls: Any = ...  # TODO: Should be CRSchema
    translator_cls: Any = ...  # TODO: Should be CRTranslator
    sqlbuilder_cls: Any = ...  # TODO: Should be CRSQLBuilder
    array_converter_cls: Any = ...  # TODO: Should be CRArrayConverter
    default_schema_name: str = ...
    fk_types: Dict[str, str] = ...
    def normalize_name(provider: Any, name: Any) -> str: ...
    def set_transaction_mode(provider: Any, connection: Any, cache: Any) -> None: ...
    converter_classes: Dict[Any, Any] = ...
provider_cls = CRProvider
