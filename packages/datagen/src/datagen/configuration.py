from dataclasses import dataclass, field
from typing import List, Dict, Any, Tuple, Optional

@dataclass
class Column:
    name: str
    dtype: type
    value_range: Optional[Tuple[float, float]] = None
    allowed_values: List[Any] = field(default_factory=list)
    nullable: bool = True

    def __post_init__(self):
        numeric_types = (int, float)

        # Check value_range is only for numeric types
        if self.value_range is not None and not issubclass(self.dtype, numeric_types):
            raise ValueError(f"value_range can only be used with numeric types (int, float), got {self.dtype}")

        # Validate value_range tuple
        if self.value_range:
            min_val, max_val = self.value_range
            if min_val > max_val:
                raise ValueError(f"value_range min cannot be greater than max: {self.value_range}")

    def validate(self, value: Any) -> bool:
        if value is None:
            return self.nullable
        if not isinstance(value, self.dtype):
            return False
        if self.value_range:
            min_val, max_val = self.value_range
            if not (min_val <= value <= max_val):
                return False
        if self.allowed_values:
            if value not in self.allowed_values:
                return False
        return True
      
@dataclass
class Entity:
    name: str
    columns: List[Column] = field(default_factory=list)

    def __post_init__(self):
        # Check for duplicate column names
        names = [col.name for col in self.columns]
        if len(names) != len(set(names)):
            duplicates = set([x for x in names if names.count(x) > 1])
            raise ValueError(f"Duplicate column names are not allowed: {duplicates}")

        # Store columns as a dictionary for quick access
        self._columns_dict: Dict[str, Column] = {col.name: col for col in self.columns}

    def add_column(self, column: Column):
        if column.name in self._columns_dict:
            raise ValueError(f"Column with name '{column.name}' already exists in entity '{self.name}'.")
        self.columns.append(column)
        self._columns_dict[column.name] = column

    def get_column(self, name: str) -> Column:
        return self._columns_dict.get(name)

    def validate_row(self, row: dict) -> bool:
        """
        Validate a dictionary representing a row against all column constraints.
        Returns True if all columns are valid.
        """
        for col in self.columns:
            if col.name not in row:
                if not col.nullable:
                    return False
                continue
            if not col.validate(row[col.name]):
                return False
        return True