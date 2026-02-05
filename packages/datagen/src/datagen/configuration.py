"""Placeholder docstring for datagen.configuration module."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class Column:
    """
    Placeholder docstring for Column class.

    Parameters
    ----------
    name : str
        Column name.
    dtype : type
        Data type of the column.
    value_range : Optional[Tuple[float, float]], optional
        Minimum and maximum allowed values (numeric types only), by default None.
    allowed_values : List[Any], optional
        Explicitly allowed values, by default empty list.
    nullable : bool, optional
        Whether None is allowed, by default True.
    """

    name: str
    dtype: type
    value_range: Optional[Tuple[float, float]] = None
    allowed_values: List[Any] = field(default_factory=list)
    nullable: bool = True

    def __post_init__(self) -> None:
        """
        Post-initialization checks for Column.

        Raises
        ------
        ValueError
            If value_range is set for non-numeric dtype or min > max.
        """
        numeric_types = (int, float)

        # Check value_range is only for numeric types
        if self.value_range is not None and not issubclass(self.dtype, numeric_types):
            raise ValueError(
                f"value_range can only be used with numeric types (int, float), got {self.dtype}"
            )

        # Validate value_range tuple
        if self.value_range:
            min_val, max_val = self.value_range
            if min_val > max_val:
                raise ValueError(f"value_range min cannot be greater than max: {self.value_range}")

    def validate(self, value: Any) -> bool:
        """
        Validate a value against this column's rules.

        Parameters
        ----------
        value : Any
            The value to validate.

        Returns
        -------
        bool
            True if value is valid, False otherwise.
        """
        if value is None:
            return self.nullable
        if not isinstance(value, self.dtype):
            return False
        if self.value_range:
            min_val, max_val = self.value_range
            if not isinstance(value, (int, float)):
                return False
            value_numeric = float(value)
            if not (min_val <= value_numeric <= max_val):
                return False
        if self.allowed_values:
            if value not in self.allowed_values:
                return False
        return True


@dataclass
class Entity:
    """
    Placeholder docstring for Entity class.

    Parameters
    ----------
    name : str
        Name of the entity.
    columns : List[Column], optional
        List of columns in the entity, by default empty list.
    """

    name: str
    columns: List[Column] = field(default_factory=list)

    def __post_init__(self) -> None:
        """
        Post-initialization checks for Entity.

        Raises
        ------
        ValueError
            If duplicate column names are found.
        """
        # Check for duplicate column names
        names = [col.name for col in self.columns]
        if len(names) != len(set(names)):
            duplicates = set([x for x in names if names.count(x) > 1])
            raise ValueError(f"Duplicate column names are not allowed: {duplicates}")

        # Store columns as a dictionary for quick access
        self._columns_dict: Dict[str, Column] = {col.name: col for col in self.columns}

    def add_column(self, column: Column) -> None:
        """
        Add a new column to the entity.

        Parameters
        ----------
        column : Column
            Column to add.

        Raises
        ------
        ValueError
            If a column with the same name already exists.
        """
        if column.name in self._columns_dict:
            raise ValueError(
                f"Column with name '{column.name}' already exists in entity '{self.name}'."
            )
        self.columns.append(column)
        self._columns_dict[column.name] = column

    def get_column(self, name: str) -> Column | None:
        """
        Retrieve a column by name.

        Parameters
        ----------
        name : str
            Name of the column.

        Returns
        -------
        Column or None
            The column object if found, otherwise None.
        """
        return self._columns_dict.get(name)

    def validate_row(self, row: dict) -> bool:
        """
        Validate a dictionary representing a row against all column constraints.

        Parameters
        ----------
        row : dict
            Dictionary mapping column names to values.

        Returns
        -------
        bool
            True if all columns in the row are valid, False otherwise.
        """
        for col in self.columns:
            if col.name not in row:
                if not col.nullable:
                    return False
                continue
            if not col.validate(row[col.name]):
                return False
        return True
